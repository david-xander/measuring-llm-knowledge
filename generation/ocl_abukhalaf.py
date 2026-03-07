import sys
sys.path.append('../')
import os
import json
import pandas as pd
from core.llm_factory import PromptingServiceFactory
from pydantic import BaseModel


class ExperimentCodingTaskResponse(BaseModel):
    code: str


class PromptingDataBuilder():
    def __init__(self, language):
        self.language = language
    
    def set_language(self, language):
        self.language = language


    def get_domain_model(self, domain_description):
        res = f"Below is the domain model described in PlantUML::\n{domain_description}"
        return res
    
    def get_code_generation_prompt(self, coding_task):
        res = f"Code this constraint in {self.language}:\n{coding_task}"

        res += """
        Format the output as a JSON object with the following structure:
        {
            "code": "generated code for the constraint"
        }


        Do not include explanations, examples, or usage demonstrations. Only provide the JSON array.
        """

        return res


class OCLCodeGeneration():
    def __init__(self, language, models, target_path):
        self.target_path = target_path
        self.models = models
        self.language = language
        self.data = PromptingDataBuilder(language)
        self.dataset = []

    def generate_code_for_domain(self, model, task_id, coding_task, puml, domain_name):
        prompting = PromptingServiceFactory.get_instance(model)
        prompting.clear_context()
        prompting.add_to_context(self.data.get_domain_model(puml))
        prompting.add_to_context(self.data.get_code_generation_prompt(coding_task))
        
        response = prompting.run_and_get_result(response_format=ExperimentCodingTaskResponse.model_json_schema())
        prompt_context = json.dumps(prompting.get_context(), indent=2)
        
        res = self.process_llm_response(response, prompt_context)

        res["TASK"] = task_id
        res["DOMAIN_NAME"] = domain_name
        res["MODEL"] = model
        res["LANGUAGE"] = "OCL"
        
        return res

    def process_llm_response(self, raw_response, cprompt):
        try:
            cleaned_response = raw_response.strip().strip('```').strip('json').strip()
            parsed_response = json.loads(cleaned_response)
            
            if "code" in parsed_response:
                return {
                    "STATUS": 1, 
                    "RESULT": parsed_response["code"],
                    "ERROR":"",
                    "PROMPT": cprompt, 
                    "RAW_RESULT": raw_response
                }
            else:
                return {
                    "STATUS": -1, 
                    "RESULT": "",
                    "ERROR": "Missing required keys 'code'",
                    "PROMPT": cprompt, 
                    "RAW_RESULT": raw_response                    
                }
        except json.JSONDecodeError:
            return {
                "STATUS": -1,
                "RESULT": "", 
                "ERROR": "ERROR PROCESSING LLM OUTPUT: Invalid JSON FORMAT", 
                "PROMPT": cprompt, 
                "RAW_RESULT": raw_response
            }


    def run(self):        
        dataset_path = os.path.join(os.getcwd(), "..", 'datasets', 'OCL_Abukhalaf', 'BaseLine.json')
        df = pd.read_json(dataset_path, encoding="utf-8")
        
        self.dataset = []
        
        for model in self.models:
            print(f"\n{'='*60}")
            print(f"Testing model: {model}")
            print(f"{'='*60}\n")

            # Frequency
            for _, row in df.iterrows():
                domain_name = row["domain_name"]
                puml = row["plantuml_model"]
                task_list = [item["specification"] for item in row["constraints"]]
                for task_number, coding_task in enumerate(task_list):
                    print(f"Task: {domain_name}.{task_number} with {model}... ", end="")
                
                    res = self.generate_code_for_domain(
                        model=model,
                        task_id=task_number,
                        coding_task=coding_task,
                        puml=puml,
                        domain_name=domain_name
                    )
                
                    if res["STATUS"] > 0:
                        print("[OK]")
                        self.dataset.append(res)
                    else:
                        print(f"[ERROR] {res.get('error', 'Unknown error')}")
                        # Still append failed attempts for analysis
                        res["TASK"] = -1
                        self.dataset.append(res)
            
            self.save_to_disk(model)
            self.dataset = []
    
    def save_to_disk(self, model):
        fp = os.path.join(self.target_path, model.replace("/", "")+".csv")
        print(f"\nSaving results to '{fp}'")
        
        ds = pd.DataFrame(self.dataset)
        # Drop internal result flag but keep error information
        if 'STATUS' in ds.columns:
            ds = ds.drop(columns=['STATUS'])
        
        ds.to_csv(fp, index=False)


if __name__ == "__main__":
    results_path = os.path.join(os.getcwd(), 'results', 'OCL_Abukhalaf_generated')
    os.makedirs(results_path, exist_ok=True)
    
    language = "OCL"
    # models = ["gpt-4o-mini"]
    # models = ["gpt-4o-mini", "gpt-4o"]
    # models = ["DeepSeek-V3.1", "Llama-3.3-70B-Instruct"]
    # models = ["deepseek-coder:6.7b","llama3.1:latest","granite-code:8b"]
    # models = ["llama3.1:latest","granite-code:8b"]      
    # models = ["llama3.1:latest", "deepseek-coder:6.7b"]
    models = ["deepseek-coder:6.7b"]

    
    test = OCLCodeGeneration(
        language=language,
        models=models,
        target_path=os.path.join(results_path)
    )

    test.run()