import sys
sys.path.append('../')
import os
import json
import pandas as pd
from datasets import load_dataset
from core.llm_factory import PromptingServiceFactory
from pydantic import BaseModel


class CodeGenerationResponse(BaseModel):
    code: str


class PromptingDataBuilder():
    def __init__(self, language):
        self.language = language
    
    def set_language(self, language):
        self.language = language

    def get_code_generation_prompt(self, text):
        res = f"""
You are an expert {self.language} programmer. You need to write a function based on the following specification.

Task description:
{text}

Requirements:
1. Write a complete function implementation that satisfies the task description
2. Write clean, efficient, and well-structured code
3. Include necessary imports if needed
4. Ensure the implementation handles edge cases
5. Include the complete function definition with signature
6. Do NOT include test cases or example usage

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


class MBPPCodeGeneration():
    def __init__(self, language, models, target_path):
        self.target_path = target_path
        self.models = models
        self.language = language
        self.data = PromptingDataBuilder(language)
        self.dataset = []

    def generate_code_for_task(self, model, task_id, prompt):
        prompting = PromptingServiceFactory.get_instance(model)
        prompting.clear_context()
        prompting.add_to_context(self.data.get_code_generation_prompt(prompt))
        
        response = prompting.run_and_get_result(response_format=CodeGenerationResponse.model_json_schema())
        prompt_context = json.dumps(prompting.get_context(), indent=2)
        
        res = self.process_llm_response(response, prompt_context)
        
        if res["result"] > 0:
            res["task_id"] = task_id
            res["text"] = prompt
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
        print(f"Generating code completions for MBPP (sanitized) in {self.language}...")
        
        # Load the MBPP sanitized dataset
        dataset_sanitized = load_dataset("mbpp", "sanitized")
        
        self.dataset = []
        
        for model in self.models:
            print(f"\n{'='*60}")
            print(f"Testing model: {model}")
            print(f"{'='*60}\n")
            
            for idx, example in enumerate(dataset_sanitized["test"]):
                task_id = example['task_id']
                prompt = example['prompt']
                
                print(f"[{idx+1}/{len(dataset_sanitized['test'])}] Task {task_id} with {model}... ", end="")
                
                res = self.generate_code_for_task(
                    model=model,
                    task_id=task_id,
                    prompt=prompt,
                )
                
                if res["result"] > 0:
                    print("[OK]")
                    self.dataset.append(res)
                else:
                    print(f"[ERROR] {res.get('error', 'Unknown error')}")
                    # Still append failed attempts for analysis
                    res["model"] = model
                    res["task_id"] = task_id
                    res["prompt"] = prompt
                    self.dataset.append(res)
        
            self.save_to_disk(model)
            self.dataset = []
    
    def save_to_disk(self, model):
        fp = os.path.join(self.target_path, model.replace("/", "")+"_MBPP.csv")
        print(f"\nSaving results to '{fp}'")
        
        ds = pd.DataFrame(self.dataset)
        # Drop internal result flag but keep error information
        if 'result' in ds.columns:
            ds = ds.drop(columns=['result'])
        
        ds.to_csv(fp, index=False)


if __name__ == "__main__":
    results_path = os.path.join(os.getcwd(), 'results', 'python_mbpp')
    os.makedirs(results_path, exist_ok=True)
    
    language = "Python"
    models = ["gpt-4o-mini", "gpt-4o", "DeepSeek-V3.1", "Llama-3.3-70B-Instruct", "deepseek-coder:6.7b","llama3.1:latest"]
    
    test = MBPPCodeGeneration(
        language=language,
        models=models,
        target_path=os.path.join(results_path)
    )
    test.run()