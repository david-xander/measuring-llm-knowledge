import sys
sys.path.append('../')
import json
import os
import pandas as pd
from core.analysis_lib import RunAnalysis
from core.keyword_extractor import ExtractKeywords
from core.jupyter_writer import KeywordResultWriter
from core.generate_keyword_features import KeywordGroupingGenerator
from languages.r.analyzer import KeywordFrequencyAnalyzer
import re

class ExtractKeywordsR(ExtractKeywords):
    def filter_literals(self, literals):
        # Allow every alphabetic and non-alphabetic keywords to co-exist in the list
        keywords = sorted(
            {kw for kw in literals}
        )     

        return keywords 

class RunAnalysisR(RunAnalysis):
    def __init__(self):
        super().__init__()
        self.analyzer = KeywordFrequencyAnalyzer(self.keywords)

    def strip_code_fences(self, text: str) -> str:
        text = text.replace("```r", "")
        text = text.replace("```", "")
        return text
    

    def normalize_r_for_antlr(self, code: str):
        if code == "" or code == None:
            return ""
        else:
            code = self.strip_code_fences(str(code))
            lines = code.splitlines(True)
            stripped = [("" if l.strip() == "" else l) for l in lines]
            normalized = []
            seen_code = False
            for l in stripped:
                if not seen_code:
                    if l.strip() == "":
                        normalized.append(l)
                    else:
                        normalized.append(l.lstrip())
                        seen_code = True
                else:
                    normalized.append(l)

            return "".join(normalized)        

    def extract_data_from_grammar(self):
        grammar_path = os.path.join(self.local_dir_path(), 'languages', 'r', 'parser', 'R.g4')
        extractor = ExtractKeywordsR()
        extractor.extract(grammar_path)
        self.keywords = extractor.keywords
        self.lexer_rules = extractor.lexer_rules
        self.parser_rules = extractor.parser_rules
    
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)      
        print(f"Starting analysis for {ds_name}...")     

class BaseLineAnalysis(RunAnalysisR):
        
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        # Load dataset
        dataset_path = os.path.join(self.local_dir_path(), 'datasets', 'multipl-t', ds_name)
        df = pd.read_parquet(dataset_path)

        # for _, row in df.iterrows():
        #     print(_)
        #     code = row["content"]
        #     print("="*30)
        #     print(code)
        #     print("-"*30)
        #     issues_found = [5712, 9768, 12060, 14817]
        #     if not _ in issues_found :
        #         self.analyzer.compute_with_lexer(code)  
            
                      

        # Frequency
        for i, row in df.iterrows():
            print(f"Frequency. DS {ds_name}, Task {i}")
            code = row["content"]
            self.compute_frequency_add_result(code)
        
        # Syntactic
        for i, row in df.iterrows():
            print(f"Syntactic. DS {ds_name}, Task {i}")
            code = row["content"]
            self.compute_syntactic_usage_add_result(code)

        # Sequences
        for i, row in df.iterrows():
            print(f"Sequences. DS {ds_name}, Task {i}")
            code = row["content"]
            self.extract_valid_rule_sequences_add_result(code)

        ds_name, _ = os.path.splitext(ds_name)
        self.save_results(dataset_name='multipl-t', language="r")


class GeneratedRMultiplE(RunAnalysisR):
    def __init__(self):
        super().__init__()
        self.folder = None
    
    def load_results(self, ds_name):
        if self.folder is None:
            raise Exception("The 'folder' attribute of the class must be defined!!!")
        results_f = os.path.join(self.local_dir_path(), 'datasets', 'r_multipl-e_generated', self.folder)
        filename = ds_name + ".csv"
        return pd.read_csv( os.path.join(results_f, filename) )

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        df = self.load_results(ds_name)
        
        # Frequency
        for _, row in df.iterrows():
            print(f"Frequency. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_r_for_antlr(str(row["code"]))
            self.compute_frequency_add_result(code)
        
        # Syntactic
        for _, row in df.iterrows():
            print(f"Syntactic. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_r_for_antlr(str(row["code"]))
            self.compute_syntactic_usage_add_result(code)        

        # Sequences
        for _, row in df.iterrows():
            print(f"Sequences. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_r_for_antlr(str(row["code"]))
            self.extract_valid_rule_sequences_add_result(code)

        self.save_results(dataset_name=ds_name, language="r")

if __name__ == "__main__":

    test = BaseLineAnalysis()
    test.run_analysis("r-00000-of-00001.parquet")

    test = GeneratedRMultiplE()
    test.folder = 'humanEval'
    ds_names = ['deepseek-he', 'deepseek-sm-he', 'gpt-4o-he', 'gpt-4o-mini-he', 'llama-he', 'llama-sm-he']
    for ds_name in ds_names:
        test.run_analysis(ds_name)  

    test = GeneratedRMultiplE()
    test.folder = 'mbpp'
    ds_names = ['deepseek-mbpp', 'deepseek-sm-mbpp', 'gpt-4o-mbpp', 'gpt-4o-mini-mbpp', 'llama-mbpp', 'llama-sm-mbpp']
    for ds_name in ds_names:
        test.run_analysis(ds_name)    

    result = KeywordResultWriter()
    kwgenerator = KeywordGroupingGenerator(
        language="r",
        keywords=test.keywords,
    )
    result.excluded_keywords = kwgenerator.get_excluded_keywords()
    result.grouped_keywords = kwgenerator.get_semantic_groups()

    result.datasets = ['multipl-t', 'deepseek-he', 'deepseek-sm-he', 'gpt-4o-he', 'gpt-4o-mini-he', 'llama-he', 'llama-sm-he', 'deepseek-mbpp', 'gpt-4o-mbpp', 'gpt-4o-mini-mbpp', 'llama-mbpp', 'llama-sm-mbpp']

    result.ds_groups = {
        "LLM Generation - Multipl-E (HumanEval)": ['deepseek-he','deepseek-sm-he', 'gpt-4o-he', 'gpt-4o-mini-he', 'llama-he', 'llama-sm-he'],

        "LLM Generation - Multipl-E (MBPP)": ['deepseek-mbpp', 'deepseek-sm-mbpp', 'gpt-4o-mbpp', 'gpt-4o-mini-mbpp', 'llama-mbpp', 'llama-sm-mbpp'], 

        "Dataset test - Multipl-T": ["multipl-t"]
    }

    result.write_result_to_file("r")

    # code = """
    # """
    # test.analyzer.compute_with_lexer(code)


