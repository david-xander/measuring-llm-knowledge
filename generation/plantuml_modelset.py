import sys
sys.path.append('../')
import os
import json
import pandas as pd
from core.llm_factory import PromptingServiceFactory
from core.keyword_extractor import ExtractKeywords
from pydantic import BaseModel
from pathlib import Path


class CodeGenerationResponse(BaseModel):
    code: str

class PromptingDataBuilder():
    def __init__(self, language):
        self.language = language
    
    def set_language(self, language):
        self.language = language

    def get_explained_task(self, code_task):
        res = f"""
Code in {self.language} the following task: {code_task}

It is only a plain domain model definition, therefore follow these instructions carefully:
1. Only use the UML valid data types: String, Integer, Date, Boolean, Decimal.
2. There are no private or public attributes. 
3. Usually there are no methods defined, because it is just a domain model definition.

Do not include explanations, examples, usage demonstrations or any commentaries in the code.
                """
        

        res += """
        Format the output as a JSON object with the following structure:
        {
            "code": "generated code for the constraint"
        }


        Do not include explanations, examples, or usage demonstrations. Only provide the JSON array.
        """        
        return res


class Task2CodeGeneration():
    def __init__(self, testing_ds, language, model, target_path):
        self.target_path = target_path
        self.model = model
        self.testing_ds = testing_ds
        self.language = language
        self.data = PromptingDataBuilder(language)
        self.prompting = PromptingServiceFactory.get_instance(self.model)
        self.dataset = []

    def generate_code_for_specification(self, code_task):
        self.prompting.clear_context()
        self.prompting.add_to_context( self.data.get_explained_task(code_task) )
        response = self.prompting.run_and_get_result(response_format=CodeGenerationResponse.model_json_schema())
        prompt_context = json.dumps( self.prompting.get_context(), indent=2 )
        res = self.process_llm_response(response, prompt_context)

        return res

    def process_llm_response(self, raw_response, cprompt):
        try:
            cleaned_response = raw_response.strip().strip('```').strip('json').strip()
            parsed_response = json.loads(cleaned_response)
            
            # Validate that the necessary keys exist
            if "code" in parsed_response:
                code = parsed_response["code"].strip().strip('```').strip('plantuml').strip()
                return {"result": 1, "code": code, "cprompt":cprompt, "crawresp": raw_response}
            else:
                return {"error": "Missing required keys 'result' or 'desc'"}
        except json.JSONDecodeError:
            return {"result": -1, "desc": "ERROR PROCESSING LLM OUTPUT: Invalid JSON FORMAT", "cprompt": cprompt, "crawresp": raw_response}


    def run(self):
        print(f"\n\nGenerating code in {self.language}... ")

        self.dataset = []

        for i, row in self.testing_ds.iterrows():
            folder = row["parent_folder"]
            task = row["content"]

            print(f"\n\n{i}...", end="")
            res = self.generate_code_for_specification(task)
            if res["result"] > 0:
                print("[OK]")
                res["folder"] = folder
                res["task"] = task
                self.dataset.append(res)
            else:
                print("[ERROR]\n", res)
        
        self.save_to_disk()
        
    def save_to_disk(self):
        fp = os.path.join(self.target_path)
        print("Saving file '"+fp+"' to disk")
        ds = pd.DataFrame(self.dataset)
        ds = ds.drop(columns=['result'])
        ds.to_csv(fp, index=False)  


def GoldemUMLMOdelsetSpecs(target_path, ext=".md"):
    res = []
    for path in Path(target_path).rglob('*'+ext):
        
        # We don't want any extramaterial content, just the dataset specs
        if 'extramaterial' in path.parts:
            continue

        parent_folder = str(path.parent)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        res.append({"parent_folder": parent_folder, "content": content})

    return res

if __name__ == "__main__":
    language = "PlantUML"
    models = ["gpt-4o-mini", "gpt-4o", "DeepSeek-V3.1", "Llama-3.3-70B-Instruct", "deepseek-coder:6.7b","llama3.1:latest"]    
    results_path = os.path.join(os.getcwd(), 'results', f"{language}_GoldenUMLmodelset_gentest")
    
    dataset_path = os.path.join(os.getcwd(), "..", 'datasets', 'GoldenUMLmodelset')
    ds_dic_list = GoldemUMLMOdelsetSpecs(dataset_path)
    df = pd.DataFrame(ds_dic_list)

    os.makedirs(results_path, exist_ok=True)

    for model in models:
        model_str = model.replace("/", "")
        file_name = f"{language}_0.csv"
        os.makedirs(os.path.join(results_path, model_str), exist_ok=True)
        test = Task2CodeGeneration(
            testing_ds=df,
            language=language, 
            model=model,
            target_path=os.path.join(results_path, model_str, file_name)
        )
        test.run()