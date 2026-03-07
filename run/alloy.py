import sys
sys.path.append('../')
import json
import os
import pandas as pd
from pathlib import Path
from core.analysis_lib import RunAnalysis
from core.keyword_extractor import ExtractKeywords
from core.jupyter_writer import KeywordResultWriter
from languages.alloy.analyzer import KeywordFrequencyAnalyzer


class RunAnalysisAlloy(RunAnalysis):
    def __init__(self):
        super().__init__()
        self.analyzer = KeywordFrequencyAnalyzer(self.keywords)

    def extract_keywords_from_grammar(self):
        grammar_path = os.path.join(self.local_dir_path(), 'languages', 'alloy', 'alloy.g4')
        extractor = ExtractKeywords()
        extractor.extract(grammar_path)
        self.keywords = extractor.keywords
        self.lexer_rules = extractor.lexer_rules
        self.parser_rules = extractor.parser_rules
    
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)    

class RunAnalysisForAlloy(RunAnalysisAlloy):
    def load_results(self, ds_name):
        res = []
        results_f = os.path.join(self.local_dir_path(), 'datasets', ds_name)
        csv = [file for file in os.listdir(results_f) if file.endswith('.csv')]
        for filename in csv:
            res.append(pd.read_csv( os.path.join(results_f, filename) ))
        return res

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        files = self.load_results(ds_name)
        df = pd.concat(files)

        # df = df.rename(columns={"PS": "PT"})
        df = df.rename(columns={"INSTANCE": "ATTEMPT"})
        df = df[df["ATTEMPT"] < 4]
        df = df[df["LANGUAGE"]=="ALLOY"]
        # df = df[df["W.F."]!=0]
        df = df[df["TASK"]!=-1]

        for _, row in df.iterrows():
            domain_name = row["DOMAIN_NAME"]
            ps = row["PS"]
            instance = row["ATTEMPT"]
            task = row["TASK"]
            alloy_code = row["RESULT"]
            print(f"\nGenerating {instance}.{ps}.{task}: {domain_name}")
            self.compute_frequency_add_result(domain_name, alloy_code)

        self.save_results(dataset_name=ds_name, language="alloy")



class RunAnalysisForAlloyExamples(RunAnalysisAlloy):
    def iter_als_files(self, ds_name):
        results_f = os.path.join(self.local_dir_path(), 'datasets', ds_name)

        for path in Path(results_f).rglob('*.als'):
            parent_folder = str(path.parent)
            file_name = path.name            
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            yield parent_folder, file_name, content

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        for parent_folder, file_name, alloy_code in self.iter_als_files(ds_name): 
            # print("Processing: ", parent_folder+"/"+file_name)
            self.compute_frequency_add_result(parent_folder+"/"+file_name, alloy_code)

        self.save_results(dataset_name=ds_name, language="alloy")



if __name__ == "__main__":

    # test = RunAnalysisForAlloy()
    # ds_names = ["deepseek-DS1","deepseek-DS2","gpt-4o-DS1","gpt-4o-mini-DS1","gpt-4o-DS2","gpt-4o-mini-DS2","llama-DS1","llama-DS2"]
    # for ds_name in ds_names:
    #     test.run_analysis(ds_name)
    
    # test = RunAnalysisForAlloyExamples()
    # ds_names = ["alloy_examples"]
    # for ds_name in ds_names:
    #     test.run_analysis(ds_name)

    KeywordResultWriter().write_result_to_file("alloy")