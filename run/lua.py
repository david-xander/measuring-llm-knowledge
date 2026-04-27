import sys
sys.path.append('../')
import json
import os
import pandas as pd
from core.analysis_lib import RunAnalysis
from core.keyword_extractor import ExtractKeywords
from core.jupyter_writer import KeywordResultWriter
from core.generate_keyword_features import KeywordGroupingGenerator
from languages.lua.analyzer import KeywordFrequencyAnalyzer
import re

class ExtractKeywordsLua(ExtractKeywords):
    def filter_literals(self, literals):
        # Allow every alphabetic and non-alphabetic keywords to co-exist in the list
        keywords = sorted(
            {kw for kw in literals}
        )     

        return keywords 

class RunAnalysisLua(RunAnalysis):
    def __init__(self):
        super().__init__()
        self.analyzer = KeywordFrequencyAnalyzer(self.keywords)

    def extract_data_from_grammar(self):
        lexer_path = os.path.join(self.local_dir_path(), 'languages', 'lua', 'parser', 'LuaLexer.g4')
        extractor = ExtractKeywordsLua()
        extractor.extract(lexer_path)
        self.keywords = extractor.keywords
        self.lexer_rules = extractor.lexer_rules

        parser_path = os.path.join(self.local_dir_path(), 'languages', 'lua', 'parser', 'LuaParser.g4')
        extractor = ExtractKeywordsLua()
        extractor.extract(parser_path)
        self.parser_rules = extractor.parser_rules  


    def strip_code_fences(self, text: str) -> str:
        text = text.replace("```lua", "")
        text = text.replace("```", "")
        return text
    

    def normalize_lua_for_antlr(self, code: str):
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

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)     
        print(f"Starting analysis for {ds_name}...")      

class BaseLineAnalysisMultiplT(RunAnalysisLua):
        
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        # Load dataset
        dataset_path = os.path.join(self.local_dir_path(), 'datasets', 'multipl-t', ds_name)
        df = pd.read_parquet(dataset_path)


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
        # for i, row in df.iterrows():
        #     print(f"Sequences. DS {ds_name}, Task {i}")
        #     code = row["content"]
        #     self.extract_valid_rule_sequences_add_result(code)

        ds_name, _ = os.path.splitext(ds_name)
        self.save_results(dataset_name='multipl-t', language="lua")


class GeneratedLuaMultiplE(RunAnalysisLua):
    def __init__(self):
        super().__init__()
        self.folder = None
    
    def load_results(self, ds_name):
        if self.folder is None:
            raise Exception("The 'folder' attribute of the class must be defined!!!")
        results_f = os.path.join(self.local_dir_path(), 'datasets', 'lua_multipl-e_generated', self.folder)
        filename = ds_name + ".csv"
        return pd.read_csv( os.path.join(results_f, filename) )

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        df = self.load_results(ds_name)
        
        # Frequency
        for _, row in df.iterrows():
            print(f"Frequency. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_lua_for_antlr(str(row["code"]))
            self.compute_frequency_add_result(code)
        
        # Syntactic
        for _, row in df.iterrows():
            print(f"Syntactic. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_lua_for_antlr(str(row["code"]))
            self.compute_syntactic_usage_add_result(code)        

        # Sequences
        for _, row in df.iterrows():
            print(f"Sequences. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_lua_for_antlr(str(row["code"]))
            self.extract_valid_rule_sequences_add_result(code)

        self.save_results(dataset_name=ds_name, language="lua")


if __name__ == "__main__":

    test = BaseLineAnalysisMultiplT()
    # test.run_analysis("lua-00000-of-00001.parquet")

    test = GeneratedLuaMultiplE()
    test.folder = 'humanEval'
    ds_names = ['deepseek-he', 'deepseek-sm-he', 'gpt-4o-he', 'gpt-4o-mini-he', 'llama-he', 'llama-sm-he']
    for ds_name in ds_names:
        test.run_analysis(ds_name)  

    test = GeneratedLuaMultiplE()
    test.folder = 'mbpp'
    ds_names = ['deepseek-mbpp', 'deepseek-sm-mbpp', 'gpt-4o-mbpp', 'gpt-4o-mini-mbpp', 'llama-mbpp', 'llama-sm-mbpp']
    for ds_name in ds_names:
        test.run_analysis(ds_name)

    result = KeywordResultWriter()
    kwgenerator = KeywordGroupingGenerator(
        language="lua",
        keywords=test.keywords,
    )
    result.excluded_keywords = kwgenerator.get_excluded_keywords()
    result.grouped_keywords = kwgenerator.get_semantic_groups()

    result.datasets = ['multipl-t', 'deepseek-he', 'gpt-4o-he', 'gpt-4o-mini-he', 'llama-he', 'llama-sm-he', 'deepseek-mbpp', 'gpt-4o-mbpp', 'gpt-4o-mini-mbpp', 'llama-mbpp', 'deepseek-sm-he', 'llama-sm-he', 'deepseek-sm-mbpp', 'llama-sm-mbpp']

    result.ds_groups = {
        "LLM Generation - Multipl-E (HumanEval)": ['deepseek-he', 'gpt-4o-he', 'gpt-4o-mini-he', 'llama-he', 'deepseek-sm-he', 'llama-sm-he'],

        "LLM Generation - Multipl-E (MBPP)": ['deepseek-mbpp', 'gpt-4o-mbpp', 'gpt-4o-mini-mbpp', 'llama-mbpp', 'deepseek-sm-mbpp', 'llama-sm-mbpp'], 

        "Dataset test - Multipl-T": ["multipl-t"]
    }

    result.write_result_to_file("lua")
