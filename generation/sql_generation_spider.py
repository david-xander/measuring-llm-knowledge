import sys
sys.path.append('../')
import os
import json
import pandas as pd
from core.llm_factory import PromptingServiceFactory
from pydantic import BaseModel


class CodeGenerationResponse(BaseModel):
    code: str


class PromptingDataBuilder():
    def __init__(self):
        pass

    def get_code_generation_prompt(self, database, question):
        res = f"""
You are an expert in SQL. Based on the following database:
{database}

Create a SQL statement in response that replies to the following question:
{question}

Requirements:
1. Write MYSQL compatible statements.
2. Write a complete SQL select statement that shows the content from the dataset that satisfy the question.
3. Write clean, efficient, and well-structured code.
4. Do NOT include test cases or example usage.

Provide ONLY the code implementation without any explanation, comments, or markdown formatting.
"""
        
        res += """
        Format the output as a JSON object with the following structure:
        {
            "code": "generated code for the constraint"
        }


        Do not include explanations, examples, or usage demonstrations. Only provide the JSON array.
        """        
        return res


class SpiderSQLCodeGeneration():
    def __init__(self, models, target_path):
        self.target_path = target_path
        self.models = models
        self.data = PromptingDataBuilder()
        self.dataset = []

    def generate_code_for_task(self, model, db_id, database, question):
        prompting = PromptingServiceFactory.get_instance(model)
        prompting.clear_context()
        prompt = self.data.get_code_generation_prompt(
            database=database, 
            question=question
        )
        prompting.add_to_context(prompt)
        response = prompting.run_and_get_result(response_format=CodeGenerationResponse.model_json_schema())
        prompt_context = json.dumps(prompting.get_context(), indent=2)
        
        res = self.process_llm_response(response, prompt_context)
        
        if res["result"] > 0:
            res["db_id"] = db_id
            res["question"] = question
            res["model"] = model
        
        return res

    def process_llm_response(self, raw_response, cprompt):
        try:
            cleaned_response = raw_response.strip().strip('```').strip('json').strip()
            parsed_response = json.loads(cleaned_response)
            
            if "code" in parsed_response:
                return {
                    "result": 1, 
                    "code": parsed_response["code"],
                    "cprompt": cprompt, 
                    "crawresp": raw_response
                }
            else:
                return {"result": -1, "error": "Missing required key 'code'"}
        except json.JSONDecodeError:
            return {
                "result": -1, 
                "error": "ERROR PROCESSING LLM OUTPUT: Invalid JSON FORMAT", 
                "cprompt": cprompt, 
                "crawresp": raw_response
            }

    def run(self):
        spider = SpiderLoad()

        ds = spider.load_questions_in_df()
        
        self.dataset = []
        for model in self.models:
            print(f"\n{'='*60}")
            print(ds.shape)
            for i, row in ds.iterrows():
                db_id = row["db_id"]
                db = spider.pretty_print_dataset(db_id)
                question = row["question"]

                res = self.generate_code_for_task(
                    model=model,
                    db_id=db_id,
                    database=db,
                    question=question,
                )
                
                if res["result"] > 0:
                    print(i, "[OK]")
                    self.dataset.append(res)
                else:
                    print(i, f"[ERROR] {res.get('error', 'Unknown error')}")
                    res["db_id"] = db_id
                    res["question"] = question
                    res["model"] = model
                    self.dataset.append(res)
            
            self.save_to_disk(model)
            self.dataset = []
    
    def save_to_disk(self, model):
        fp = os.path.join(self.target_path, model.replace("/", "")+"_spider.csv")
        print(f"\nSaving results to '{fp}'")
        
        ds = pd.DataFrame(self.dataset)
        # Drop internal result flag but keep error information
        if 'result' in ds.columns:
            ds = ds.drop(columns=['result'])
        
        ds.to_csv(fp, index=False)


class SpiderLoad():
    def __init__(self):
        self.tables_path = os.path.join(os.getcwd(), "..", 'datasets', 'spider', 'tables.json')
        self.questions_path = os.path.join(os.getcwd(), "..", 'datasets', 'spider', 'dev.json')
        self.datasets = {}
        self.load_datasets()
    
    def process_column_name(self, name: str):
        return name.replace(" ", "_")

    def load_datasets(self):
        db = pd.read_json(self.tables_path)
        for _, row in db.iterrows():
            db_id = row['db_id']
            tables = row['table_names']
            columns = row['column_names']
            types = row['column_types']
            fks = row['foreign_keys']

            # Initialize the database structure
            db_structure = {
                "tables": [],
                "foreign_keys": []
            }
            
            # Process each table
            for table_idx in range(len(tables)):
                table_name = tables[table_idx]
                table_columns = []
                
                # Find columns that belong to this table
                for col_idx in range(len(columns)):
                    column = columns[col_idx]
                    # column[0] is the table index, column[1] is the column name
                    if column[0] == table_idx:
                        table_columns.append({
                            "name": self.process_column_name(column[1]),
                            "type": types[col_idx]
                        })
                
                # Add table with its columns
                db_structure["tables"].append({
                    "name": table_name,
                    "columns": table_columns
                })
            
            # Process foreign keys - convert column indices to table names
            for fk in fks:
                left_col_idx = fk[0]
                right_col_idx = fk[1]
                
                # Get table indices from column definitions
                left_table_idx = columns[left_col_idx][0]
                right_table_idx = columns[right_col_idx][0]
                
                # Get column names
                left_col_name = columns[left_col_idx][1]
                right_col_name = columns[right_col_idx][1]
                
                # Get table names
                left_table_name = tables[left_table_idx]
                right_table_name = tables[right_table_idx]
                
                db_structure["foreign_keys"].append({
                    "from": {
                        "table": left_table_name,
                        "column": self.process_column_name(left_col_name)
                    },
                    "to": {
                        "table": right_table_name,
                        "column": self.process_column_name(right_col_name)
                    }
                })
            
            # Store in the datasets dictionary with the db_id as key
            self.datasets[f"{db_id}"] = db_structure
    
    def pretty_print_dataset(self, db_id):
        if db_id not in self.datasets:
            raise Exception(f"Error: Database '{db_id}' not found.")
        
        db = self.datasets[db_id]
        output = []
        # output.append(f"Consider the following database '{db_id}' schema:")
        # output.append("")
        
        # Print tables and columns in a clear format
        for table in db["tables"]:
            output.append(f"Table: {table['name']}")
            for col in table["columns"]:
                output.append(f"  - {col['name']} ({col['type']})")
            output.append("")
        
        # Print foreign keys if they exist
        if db["foreign_keys"]:
            output.append("Foreign Keys:")
            for fk in db["foreign_keys"]:
                output.append(f"  - {fk['from']['table']}.{fk['from']['column']} -> {fk['to']['table']}.{fk['to']['column']}")
            output.append("")
        
        return "\n".join(output)
            
    def load_questions_in_df(self):
        return pd.read_json(self.questions_path)
            

if __name__ == "__main__":
    results_path = os.path.join(os.getcwd(), 'results', 'sql_spider')
    os.makedirs(results_path, exist_ok=True)
    # models = ["gpt-5", "gpt-5-nano", "gpt-4o-mini"]
    # models = [ "gpt-4o"]
    # models = ["deepseek-coder:6.7b","llama3.1:latest","granite-code:8b"]
    # models = ["deepseek-coder:6.7b"]
    models = ["DeepSeek-V3.1", "Llama-3.3-70B-Instruct"]
    
    test = SpiderSQLCodeGeneration(
        models=models,
        target_path=os.path.join(results_path)
    )
    test.run()