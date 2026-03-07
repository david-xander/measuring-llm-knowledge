import sys
sys.path.append('../')
import os
import json
import pandas as pd
from core.llm_factory import PromptingServiceFactory
from core.keyword_extractor import ExtractKeywords
from pydantic import BaseModel


class NLSpecificationResponse(BaseModel):
    spec: str

class PromptingDataBuilder():
    def __init__(self, language):
        self.language = language
    
    def set_language(self, language):
        self.language = language

    def get_task_introduction(self, keyword):
        res = f"""
You are a technical writer generating realistic software requirements.
Your goal is to produce a natural-language specification that describes a small, coherent programming task in {self.language}, where the implementation must involve the keyword {keyword} in a meaningful way.

Follow these guidelines:
1. Write the specification in clear, professional natural language, as if it were part of a software requirements document.
2. Describe what should be implemented, not how.
3. The task should be self-contained and small enough for a single function, class, or script.
4. Make sure the keyword {keyword} would naturally be required to solve the task in {self.language}.
5. Avoid explicitly mentioning the keyword in the text of the specification. The keyword should be implied by the requirements.
6. The specification should be between 3 to 6 sentences.
                """
        return res


class KeywordNLSpecificationGeneration():
    def __init__(self, keywords, language, model, target_path):
        self.target_path = target_path
        self.model = model
        self.keywords = keywords
        self.language = language
        self.data = PromptingDataBuilder(language)
        self.prompting = PromptingServiceFactory.get_instance(self.model)
        self.dataset = []

    def generate_specifications_with_keywords(self, keyword):
        self.prompting.clear_context()
        self.prompting.add_to_context( self.data.get_task_introduction(keyword) )
        response = self.prompting.run_and_get_result(response_format=NLSpecificationResponse.model_json_schema())
        prompt_context = json.dumps( self.prompting.get_context(), indent=2 )
        res = self.process_llm_response(response, prompt_context)

        return res

    def process_llm_response(self, raw_response, cprompt):
        try:
            cleaned_response = raw_response.strip().strip('```').strip('json').strip()
            parsed_response = json.loads(cleaned_response)
            
            # Validate that the necessary keys exist
            if "spec" in parsed_response:
                return {"result": 1, "spec": parsed_response["spec"], "cprompt":cprompt, "crawresp": raw_response}
            else:
                return {"error": "Missing required keys 'result' or 'desc'"}
        except json.JSONDecodeError:
            return {"result": -1, "desc": "ERROR PROCESSING LLM OUTPUT: Invalid JSON FORMAT", "cprompt":cprompt, "crawresp": raw_response}


    def run(self):
        print(f"Generating NL specifications to be coded in {self.language}... ")

        self.dataset = []
        for keyword in self.keywords:
            print(f"{keyword}")
            res = self.generate_specifications_with_keywords(keyword)
            if res["result"] > 0:
                print("[OK]")
                res["keyword"] = keyword
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
    grammar_path = os.path.join(os.getcwd(), '..', 'languages', 'ocl', 'OCL.g4')
    extractor = ExtractKeywords()
    extractor.extract(grammar_path)
    keywords = extractor.keywords
    results_path = os.path.join(os.getcwd(), 'results', 'kw_spec_OCL')
    language = "OCL"
    model = "gpt-4o-mini"

    test = KeywordNLSpecificationGeneration(
        keywords=keywords, 
        language=language, 
        model=model,
        target_path=os.path.join(results_path, f"kw_spec_{language}_{model}.csv"))
    test.run()

    