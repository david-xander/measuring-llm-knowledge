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
from languages.plantuml.analyzer import KeywordFrequencyAnalyzer
from generation.plantuml_modelset import GoldemUMLMOdelsetSpecs


class ExtractKeywordsPlantUML(ExtractKeywords):
    def filter_literals(self, literals):
        # Allow every alphabetic and non-alphabetic keywords to co-exist in the list
        keywords = sorted(
            {kw for kw in literals}
        )     

        return keywords 

class RunAnalysisPlantUML(RunAnalysis):
    def __init__(self):
        super().__init__()
        self.analyzer = KeywordFrequencyAnalyzer(self.keywords)

    def extract_data_from_grammar(self):
        lexer_path = os.path.join(self.local_dir_path(), 'languages', 'plantuml', 'parser', 'PlantUMLLexer.g4')
        extractor = ExtractKeywordsPlantUML()
        extractor.extract(lexer_path)
        self.keywords = extractor.keywords
        self.lexer_rules = extractor.lexer_rules

        parser_path = os.path.join(self.local_dir_path(), 'languages', 'plantuml', 'parser', 'PlantUML.g4')
        extractor = ExtractKeywordsPlantUML()
        extractor.extract(parser_path)
        self.parser_rules = extractor.parser_rules  
    
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)    

class RunAnalysisForPlantUMLExamples(RunAnalysisPlantUML):    
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        dataset_path = os.path.join(self.local_dir_path(), 'datasets', 'GoldenUMLmodelset')
        ds_dic_list = GoldemUMLMOdelsetSpecs(dataset_path, "plantuml.txt")

        for i, row in enumerate(ds_dic_list):
            code = row["content"]
            print(f"\nFreq. Generating {(i+1)} of {len(ds_dic_list)}")
            self.compute_frequency_add_result(code)

        for i, row in enumerate(ds_dic_list):
            code = row["content"]
            print(f"\nSyntanctic. Generating {(i+1)} of {len(ds_dic_list)}")
            self.compute_syntactic_usage_add_result(code)         

        for i, row in enumerate(ds_dic_list):
            code = row["content"]
            print(f"\nSequences. Generating {(i+1)} of {len(ds_dic_list)}")
            self.extract_valid_rule_sequences_add_result(code)

        self.save_results(dataset_name=ds_name, language="plantuml")

class RunAnalysisForPlantUMLGeneratedExamples(RunAnalysisPlantUML):
    def load_results(self, ds_name):
        res = []
        results_f = os.path.join(self.local_dir_path(), 'datasets', 'PlantUML_GoldenUMLmodelset_gentest', ds_name)
        csv = [file for file in os.listdir(results_f) if file.endswith('.csv')]
        for filename in csv:
            res.append(pd.read_csv( os.path.join(results_f, filename) ))
        return res
            
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        # Load dataset
        files = self.load_results(ds_name)
        df = pd.concat(files)

        for _, row in df.iterrows():
            self.compute_frequency_add_result(code=row["code"])

        for _, row in df.iterrows():
            self.compute_syntactic_usage_add_result(code=row["code"])

        for _, row in df.iterrows():
            self.extract_valid_rule_sequences_add_result(code=row["code"])

        self.save_results(dataset_name=ds_name, language="plantuml")


if __name__ == "__main__":
    
    test = RunAnalysisForPlantUMLExamples()
    test.run_analysis("BaseLine")

    test = RunAnalysisForPlantUMLGeneratedExamples()
    test.run_analysis("gpt-4o")
    test.run_analysis("gpt-4o-mini")
    test.run_analysis("deepseek")
    test.run_analysis("llama")
    test.run_analysis("deepseek-sm")
    test.run_analysis("llama-sm")

    kwgenerator = KeywordGroupingGenerator(
        language="plantuml",
        keywords=test.keywords,
    )
    result = KeywordResultWriter()
    # EXCLUDE keywords
    result.excluded_keywords = [
        '/*', '*/', '\\u2211', '\\u222B', '\\\\', '\\\'', '"', ',', '.', '_', 'u',
    ]
    kwgenerator.save_excluded_keywords_to_cache(result.excluded_keywords, "MANUAL")

    # GROUP keywords
    result.grouped_keywords = {
        'other_uml_type': ['Sequence', 'Set', 'Bag', 'OrderedSet', 'SortedSet', 'Map', 'SortedMap', 'Function'],

        'leftAncestorSymbol': ['<|--', '<|-', '<|---', '<|..', '^--'],

        'visibility': ['+','-','#','~'],

        'modifier': ['static','classifier','abstract'],

        'rightAncestorSymbol': ['--|>','-|>','---|>','..|>','--^'],

        'associationSymbol': ['-','--','---','-->','->','<--','<-'],

        'aggregationSymbol': ['o--','--o','o-->','<--o'],

        'compositionSymbol': ['*--','*-','--*','-*','*-->','*->','<--*','<-*'],

        'dependencySymbol': ['..','..>','<..','...','...>','<...'],

        'direction': ['>','<'],

        'stereotype': ['<<','>>'],
    } 
    kwgenerator.save_groups_to_cache(result.grouped_keywords, result.excluded_keywords, "MANUAL")

    result.datasets = ["BaseLine","gpt-4o","gpt-4o-mini","deepseek","llama","deepseek-sm","llama-sm"]
    result.ds_groups = {"GoldenUMLmodelset": ["BaseLine","gpt-4o","gpt-4o-mini","deepseek","deepseek-sm","llama","llama-sm"]}
    result.write_result_to_file("plantuml")

