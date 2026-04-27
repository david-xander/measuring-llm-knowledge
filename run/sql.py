import sys
sys.path.append('../')
import json
import os
import pandas as pd
from pathlib import Path
from core.analysis_lib import RunAnalysis
from core.keyword_extractor import ExtractKeywords
from core.jupyter_writer import KeywordResultWriter
from languages.sql.analyzer import KeywordFrequencyAnalyzer
from generation.sql_generation_spider import SpiderLoad
from core.generate_keyword_features import KeywordGroupingGenerator


class ExtractKeywordsSQL(ExtractKeywords):
    def filter_literals(self, literals):
        # Allow every alphabetic and non-alphabetic keywords to co-exist in the list
        keywords = sorted(
            {kw for kw in literals}
        )     
        return keywords 

class RunAnalysisSQL(RunAnalysis):
    def __init__(self):
        super().__init__()
        self.analyzer = KeywordFrequencyAnalyzer(self.keywords)

    def extract_data_from_grammar(self):
        lexer_path = os.path.join(self.local_dir_path(), 'languages', 'sql', 'parser', 'MariaDBLexer.g4')
        extractor = ExtractKeywordsSQL()
        extractor.extract(lexer_path)
        self.keywords = extractor.keywords
        self.lexer_rules = extractor.lexer_rules

        parser_path = os.path.join(self.local_dir_path(), 'languages', 'sql', 'parser', 'MariaDBParser.g4')
        extractor = ExtractKeywordsSQL()
        extractor.extract(parser_path)
        self.parser_rules = extractor.parser_rules  
    
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)
        print(f"Starting analysis for {ds_name}...")


class RunAnalysisForSQLExamples(RunAnalysisSQL):    
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        spider = SpiderLoad()
        ds = spider.load_questions_in_df()

        for i, row in ds.iterrows():
            code = row["query"]
            print(f"\nFreq. Generating {(i+1)}/{len(ds)}")
            self.compute_frequency_add_result(code)

        for i, row in ds.iterrows():
            code = row["query"]
            print(f"\nSyntanctic. Generating {(i+1)} of {len(ds)}")
            self.compute_syntactic_usage_add_result(code)         

        for i, row in ds.iterrows():
            code = row["query"]
            print(f"\nSequences. Generating {(i+1)} of {len(ds)}")
            self.extract_valid_rule_sequences_add_result(code)

        self.save_results(dataset_name=ds_name, language="sql")

class GeneratedSQL(RunAnalysisSQL):
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
        for i, row in df.iterrows():
            if not pd.isna(row["code"]):
                print(f"Frequency. {i+1} of {len(df)}")
                code = row["code"]
                self.compute_frequency_add_result(code)
        
        # Syntactic
        for i, row in df.iterrows():
            if not pd.isna(row["code"]):
                print(f"Syntactic. {i+1} of {len(df)}")
                code = row["code"]
                self.compute_syntactic_usage_add_result(code)        

        # # Sequences
        # for i, row in df.iterrows():
        #     print(f"Sequences. {i+1} of {len(df)}")
        #     code = row["code"]
        #     self.extract_valid_rule_sequences_add_result(code)

        self.save_results(dataset_name=ds_name, language="sql")


if __name__ == "__main__":
    
    test = RunAnalysisForSQLExamples()
    test.run_analysis("BaseLine")

    test = GeneratedSQL()
    test.folder = "sql_spider_generated"
    test.run_analysis("gpt-4o")
    test.run_analysis("gpt-4o-mini")
    test.run_analysis("deepseek")
    test.run_analysis("deepseek-sm")
    test.run_analysis("llama")
    test.run_analysis("llama-sm")


    result = KeywordResultWriter()
    kwgenerator = KeywordGroupingGenerator(
        language="sql",
        keywords=test.keywords,
    )
    result.excluded_keywords = kwgenerator.get_excluded_keywords()
    result.grouped_keywords = kwgenerator.get_semantic_groups()

    result.datasets = ['BaseLine','deepseek', 'gpt-4o', 'gpt-4o-mini', 'llama', 'deepseek-sm', 'llama-sm']

    result.ds_groups = {
        "LLM Generation - Spider": ['BaseLine','deepseek', 'gpt-4o', 'gpt-4o-mini', 'llama', 'deepseek-sm', 'llama-sm'],
    }

    result.write_result_to_file("sql")

