import sys
sys.path.append('../')
import json
import os
import pandas as pd
from pathlib import Path
from core.analysis_lib import RunAnalysis
from core.keyword_extractor import ExtractKeywords
from core.jupyter_writer import KeywordResultWriter
from core.generate_keyword_features import KeywordGroupingGenerator
from languages.python3.analyzer import KeywordFrequencyAnalyzer

from datasets import load_dataset



class ExtractKeywordsPython3(ExtractKeywords):
    def filter_literals(self, literals):
        # Allow every alphabetic and non-alphabetic keywords to co-exist in the list
        keywords = sorted(
            {kw for kw in literals}
        )     

        return keywords 

class RunAnalysisPython3(RunAnalysis):
    def __init__(self):
        super().__init__()
        self.analyzer = KeywordFrequencyAnalyzer(self.keywords)

    def strip_code_fences(self, text: str) -> str:
        text = text.replace("```python", "")
        text = text.replace("```", "")
        return text
    

    def normalize_python_for_antlr(self, code: str):
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
        lexer_path = os.path.join(self.local_dir_path(), 'languages', 'python3', 'parser', 'Python3Lexer.g4')
        extractor = ExtractKeywordsPython3()
        extractor.extract(lexer_path)
        self.keywords = extractor.keywords
        self.lexer_rules = extractor.lexer_rules

        parser_path = os.path.join(self.local_dir_path(), 'languages', 'python3', 'parser', 'Python3Parser.g4')
        extractor = ExtractKeywordsPython3()
        extractor.extract(parser_path)
        self.parser_rules = extractor.parser_rules  
    
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)    

class RunAnalysisForPython3HumanEval(RunAnalysisPython3):     
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        dataset = load_dataset("openai_humaneval", cache_dir=os.path.join(self.local_dir_path(), 'datasets', 'hf_cache'))


        for example in dataset["test"]:
            print(f"Freq. Task ID: {example['task_id']}")
            # print(f"Prompt:\n{example['prompt']}")
            # print(f"Canonical solution:\n{example['canonical_solution']}")
            # print(f"Entry point: {example['entry_point']}")
            # print("===")
            complete_code = example["prompt"] + example["canonical_solution"]
            code = self.normalize_python_for_antlr(complete_code)
            self.compute_frequency_add_result(code)

        for example in dataset["test"]:
            print(f"Syntactic. Task ID: {example['task_id']}")
            complete_code = example["prompt"] + example["canonical_solution"]
            code = self.normalize_python_for_antlr(complete_code)
            self.compute_syntactic_usage_add_result(code)

        for example in dataset["test"]:
            print(f"Sequences. Task ID: {example['task_id']}")
            complete_code = example["prompt"] + example["canonical_solution"]
            code = self.normalize_python_for_antlr(complete_code)
            self.extract_valid_rule_sequences_add_result(code)


        self.save_results(dataset_name="BaseLine-"+ds_name, language="python3")

class RunAnalysisForPython3MBPP(RunAnalysisPython3):
            
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        # Load dataset
        dataset = load_dataset("mbpp", "sanitized", cache_dir=os.path.join(self.local_dir_path(), 'datasets', 'hf_cache'))

        for example in dataset["test"]:
            print(f"Freq. Task {example['task_id']}")
            # print("Problem description:")
            # print(example["text"])
            # print("\nReference solution:\n")
            # print(example["code"])
            # print("="*80)
            code = self.normalize_python_for_antlr(example["code"])
            self.compute_frequency_add_result(code)
        
        for example in dataset["test"]:
            print(f"Syntactic. Task {example['task_id']}")
            code = self.normalize_python_for_antlr(example["code"])
            self.compute_syntactic_usage_add_result(code)

        for example in dataset["test"]:
            print(f"Sequences. Task {example['task_id']}")
            code = self.normalize_python_for_antlr(example['code'])
            self.extract_valid_rule_sequences_add_result(code)

        self.save_results(dataset_name="BaseLine-"+ds_name, language="python3")


class GeneratedPython3(RunAnalysisPython3):
    def __init__(self):
        super().__init__()
        self.folder = None
    
    def load_results(self, ds_name):
        if self.folder is None:
            raise Exception("The 'folder' attribute of the class must be defined!!!")
        results_f = os.path.join(self.local_dir_path(), 'datasets', self.folder)
        filename = ds_name + ".csv"
        return pd.read_csv( os.path.join(results_f, filename) )

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        df = self.load_results(ds_name)
        
        # Frequency
        for _, row in df.iterrows():
            print(f"Frequency. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_python_for_antlr(str(row["code"]))
            self.compute_frequency_add_result(code)
        
        # Syntactic
        for _, row in df.iterrows():
            print(f"Syntactic. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_python_for_antlr(str(row["code"]))
            self.compute_syntactic_usage_add_result(code)        

        # Sequences
        for _, row in df.iterrows():
            print(f"Sequences. DS {ds_name}, Task {row['task_id']}")
            code = self.normalize_python_for_antlr(str(row["code"]))
            self.extract_valid_rule_sequences_add_result(code)

        self.save_results(dataset_name=ds_name, language="python3")



if __name__ == "__main__":
    
    test = RunAnalysisForPython3HumanEval()
    test.run_analysis("HumanEval")

    test = RunAnalysisForPython3MBPP()
    test.run_analysis("MBPP")

    test = GeneratedPython3()
    test.folder = 'python_humanEval'
    ds_names = ['deepseek-sm-he', 'deepseek-he', 'gpt-4o-he', 'gpt-4o-mini-he', 'llama-sm-he', 'llama-he']
    for ds_name in ds_names:
        test.run_analysis(ds_name)    

    test = GeneratedPython3()
    test.folder = 'python_mbpp'
    ds_names = ['deepseek-sm-mbpp', 'deepseek-mbpp', 'gpt-4o-mbpp', 'gpt-4o-mini-mbpp', 'llama-sm-mbpp', 'llama-mbpp']
    for ds_name in ds_names:
        test.run_analysis(ds_name)


    # ANOTHER DATASET :::      neulab/conala

    kwgenerator = KeywordGroupingGenerator(
        language="python3",
        keywords=test.keywords,
    )
    result = KeywordResultWriter()
    result.excluded_keywords = ["\\", "\f", "\n", "\r", "\u00b7", "\u0387", "\u1369", "\u1371", "\u1885", "\u1886", "\u19da", "\u2118", "\u212e", "\u309b", "\u309c"]
    kwgenerator.save_excluded_keywords_to_cache(result.excluded_keywords, "MANUAL")    
    
    result.grouped_keywords = {

        "literalKeywords": [
            "True", "False", "None", "0"
        ],

        "controlFlow": [
            "if", "elif", "else",
            "for", "while",
            "break", "continue",
            "match", "case"
        ],

        "exceptionHandling": [
            "try", "except", "finally", "raise"
        ],

        "definitions": [
            "def", "class", "lambda"
        ],

        "asyncProgramming": [
            "async", "await"
        ],

        "namespacesAndBinding": [
            "import", "from",
            "global", "nonlocal"
        ],

        "miscKeywords": [
            "and", "or", "not", "is", "in",
            "as", "pass", "yield",
            "assert", "del"
        ],

        "arithmeticOperators": [
            "+", "-", "*", "**", "/", "//", "%"
        ],

        "comparisonOperators": [
            "==", "!=", "<", ">", "<=", ">=", "<>"
        ],

        "bitwiseOperators": [
            "&", "|", "^", "~", "<<", ">>"
        ],

        "assignmentOperators": [
            "=", "+=", "-=", "*=", "**=", "/=", "//=",
            "%=", "&=", "|=", "^=", "<<=", ">>=", "@="
        ],

        "typeAndAnnotationSyntax": [
            "@",
            "->",
            ":"
        ],

        "delimiters": [
            "(", ")", "[", "]", "{", "}"
        ],

        "separators": [
            ",", ";", ".", "..."
        ],
    }
    kwgenerator.save_groups_to_cache(result.grouped_keywords, result.excluded_keywords, "MANUAL")


    result.datasets = ['BaseLine-HumanEval', 'BaseLine-MBPP', 'deepseek-sm-he', 'deepseek-he', 'deepseek-sm-mbpp', 'deepseek-mbpp', 'gpt-4o-mini-he', 'gpt-4o-mini-mbpp', 'gpt-4o-he', 'gpt-4o-mbpp', 'llama-sm-he', 'llama-he', 'llama-sm-mbpp', 'llama-mbpp']
    result.ds_groups = {
        "HumanEval": ['BaseLine-HumanEval', 'deepseek-sm-he', 'deepseek-he', 'gpt-4o-mini-he', 'gpt-4o-he', 'llama-sm-he', 'llama-he'], 
        
        "MBPP": ['BaseLine-MBPP','deepseek-sm-mbpp', 'deepseek-mbpp', 'gpt-4o-mini-mbpp', 'gpt-4o-mbpp', 'llama-sm-mbpp', 'llama-mbpp']
    }
    result.write_result_to_file("python3") 
