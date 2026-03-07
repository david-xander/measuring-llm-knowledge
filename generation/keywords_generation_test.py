import sys
sys.path.append('../')
import os
import json
import pandas as pd
from core.llm_factory import PromptingServiceFactory
from pydantic import BaseModel


class KeyWordTestResponse(BaseModel):
    code: str

class PromptingDataBuilder():
    def __init__(self, language):
        self.language = language
    
    def set_language(self, language):
        self.language = language

    def get_explained_task(self, code_task):
        res = f"""
Code in {self.language} the following task: {code_task}

Do not include explanations, examples, usage demonstrations or any commentaries in the code.
                """
        return res


class KeywordCodeGeneration():
    def __init__(self, testing_ds, language, model, target_path):
        self.target_path = target_path
        self.model = model
        self.testing_ds = testing_ds
        self.language = language
        self.data = PromptingDataBuilder(language)
        self.prompting = PromptingServiceFactory.get_instance(self.model)
        self.dataset = []

    def generate_code_for_keyword(self, code_task):
        self.prompting.clear_context()
        self.prompting.add_to_context( self.data.get_explained_task(code_task) )
        response = self.prompting.run_and_get_result(response_format=KeyWordTestResponse.model_json_schema())
        prompt_context = json.dumps( self.prompting.get_context(), indent=2 )
        res = self.process_llm_response(response, prompt_context)

        return res

    def process_llm_response(self, raw_response, cprompt):
        try:
            cleaned_response = raw_response.strip().strip('```').strip('json').strip()
            parsed_response = json.loads(cleaned_response)
            
            # Validate that the necessary keys exist
            if "code" in parsed_response:
                return {"result": 1, "code": parsed_response["code"], "cprompt":cprompt, "crawresp": raw_response}
            else:
                return {"error": "Missing required keys 'result' or 'desc'"}
        except json.JSONDecodeError:
            return {"result": -1, "desc": "ERROR PROCESSING LLM OUTPUT: Invalid JSON FORMAT", "cprompt": cprompt, "crawresp": raw_response}


    def run(self):
        print(f"\n\nGenerating code in {self.language} for the following keywords... ")

        self.dataset = []

        for _, row in self.testing_ds.iterrows():
            keyword = row["keyword"]
            task = row["spec"]

            print(f"{keyword}")
            res = self.generate_code_for_keyword(task)
            if res["result"] > 0:
                print("[OK]")
                res["keyword"] = keyword
                res["task"] = task
                self.dataset.append(res)
            else:
                print("[ERROR]", res)
        
        self.save_to_disk()
        
    def save_to_disk(self):
        fp = os.path.join(self.target_path)
        print("Saving file '"+fp+"' to disk")
        ds = pd.DataFrame(self.dataset)
        ds = ds.drop(columns=['result'])
        ds.to_csv(fp, index=False)  

if __name__ == "__main__":
    language = "OCL"
    results_path = os.path.join(os.getcwd(), 'results', f"{language}_kw_generation_test")
    models = ["gpt-4o","gpt-4o-mini"]
    # models = ["deepseek-coder:6.7b","llama3.1:latest","granite-code:8b"]
    # models = ["granite-code:8b"]

    # With the automatic .csv generated keywords
    # dataset_path = os.path.join(os.getcwd(), 'results', 'kw_spec_OCL_gpt-4o-mini.csv')
    # df = pd.read_csv(dataset_path, encoding="utf-8")    
    

    for ds in range(1,3):
        # With the GEMINI json
        dataset_path = os.path.join(os.getcwd(), 'results', 'kw_spec_OCL', f"kw_spec_OCL_gemini{ds+1}.json")
        df = pd.read_json(dataset_path, encoding="utf-8")
        print("dataset", dataset_path)

        for model in models:
            for attempt in range(0,3):
                model_str = model.replace("/", "")
                file_name = f"{language}_{attempt+(ds*3)}.csv"
                os.makedirs(os.path.join(results_path, model_str), exist_ok=True)
                test = KeywordCodeGeneration(
                    testing_ds=df,
                    language=language, 
                    model=model,
                    target_path=os.path.join(results_path, model_str, file_name)
                )
                test.run()
