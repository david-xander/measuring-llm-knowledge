import sys
sys.path.append('../')
import json
import os
import pandas as pd
from core.analysis_lib import RunAnalysis
from core.keyword_extractor import ExtractKeywords
from core.jupyter_writer import KeywordResultWriter
from core.generate_keyword_features import KeywordGroupingGenerator
from languages.ocl.analyzer import KeywordFrequencyAnalyzer
import re

class ExtractKeywordsOCL(ExtractKeywords):
    def filter_literals(self, literals):
        # Allow every alphabetic and non-alphabetic keywords to co-exist in the list
        res = []
        for kw in literals:
            if len(kw)> 2 and kw[0:2] == "->":
                kw = re.sub('[^a-zA-Z]+', '', kw)
                # kw = kw.replace('->', '')
            res.append(kw)
        
        keywords = sorted(res)     

        return keywords 

class RunAnalysisOCL(RunAnalysis):
    def __init__(self):
        super().__init__()
        self.analyzer = KeywordFrequencyAnalyzer(self.keywords)

    def extract_data_from_grammar(self):
        grammar_path = os.path.join(self.local_dir_path(), 'languages', 'ocl', 'parser', 'OCL.g4')
        extractor = ExtractKeywordsOCL()
        extractor.extract(grammar_path)
        self.keywords = extractor.keywords
        self.lexer_rules = extractor.lexer_rules
        self.parser_rules = extractor.parser_rules

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)           

class BaseLineAnalysis(RunAnalysisOCL):
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        # Load dataset
        dataset_path = os.path.join(self.local_dir_path(), 'datasets', 'OCL_Abukhalaf', ds_name)
        df = pd.read_json(dataset_path, encoding="utf-8")

        # Frequency
        for _, row in df.iterrows():
            ocl_code_list = [item["ocl"] for item in row["constraints"]]
            for _, ocl_code in enumerate(ocl_code_list):
                self.compute_frequency_add_result(ocl_code)
        
        # Syntactic
        for _, row in df.iterrows():
            ocl_code_list = [item["ocl"] for item in row["constraints"]]
            for _, ocl_code in enumerate(ocl_code_list):
                self.compute_syntactic_usage_add_result(ocl_code)

        # Sequences
        for _, row in df.iterrows():
            ocl_code_list = [item["ocl"] for item in row["constraints"]]
            for _, ocl_code in enumerate(ocl_code_list):
                self.extract_valid_rule_sequences_add_result(ocl_code)

        ds_name, _ = os.path.splitext(ds_name)
        self.save_results(dataset_name=ds_name, language="ocl")

class GeneratedOCL(RunAnalysisOCL):   
    def load_results(self, ds_name):
        res = []
        results_f = os.path.join(self.local_dir_path(), 'datasets', 'OCL_Abukhalaf_generated', ds_name+".csv")
        res = pd.read_csv(results_f)
        return res

    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        df = self.load_results(ds_name)
        df = df[df["LANGUAGE"]=="OCL"]
        df = df[df["TASK"]!=-1]

        # Frequency
        for _, row in df.iterrows():
            task = row["TASK"]
            ocl_code = row["RESULT"]
            print(f"\Frequency.{task}")
            self.compute_frequency_add_result(ocl_code)
        
        # Syntactic
        for _, row in df.iterrows():
            task = row["TASK"]
            ocl_code = row["RESULT"]
            print(f"\Syntactic.{task}")
            self.compute_syntactic_usage_add_result(ocl_code)        

        # Sequences
        for _, row in df.iterrows():
            task = row["TASK"]
            ocl_code = row["RESULT"]
            print(f"\Sequences.{task}")
            self.extract_valid_rule_sequences_add_result(ocl_code)

        self.save_results(dataset_name=ds_name, language="ocl")


class OCLKeywordsGenerated(RunAnalysisOCL):
    def load_results(self, ds_name):
        res = []
        results_f = os.path.join(self.local_dir_path(), 'datasets', "OCL_kw_generation_test", ds_name)
        csv = [file for file in os.listdir(results_f) if file.endswith('.csv')]
        for filename in csv:
            res.append(pd.read_csv( os.path.join(results_f, filename) ))
        return res
        
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        files = self.load_results(ds_name)
        df = pd.concat(files)

        # Frequency
        for _, row in df.iterrows():
            self.compute_frequency_add_result(code=row["code"])

        # Syntactic
        for _, row in df.iterrows():
            self.compute_syntactic_usage_add_result(code=row["code"])

        # Sequences
        for _, row in df.iterrows():
            self.extract_valid_rule_sequences_add_result(code=row["code"])


        self.save_results(dataset_name=ds_name+"_kwGENtest", language="ocl")


class PanOCLDataset(RunAnalysisOCL):
    def run_analysis(self, ds_name):
        super().run_analysis(ds_name)

        # Load dataset
        dataset_path = os.path.join(self.local_dir_path(), 'datasets', 'OCL_Pan', ds_name)
        df = pd.read_json(dataset_path, encoding="utf-8")

        # Frequency
        for _, row in df.iterrows():
            self.compute_frequency_add_result(row["ocl"])
        
        # Syntactic
        for _, row in df.iterrows():
            self.compute_syntactic_usage_add_result(row["ocl"])

        # Sequences
        for _, row in df.iterrows():
            self.extract_valid_rule_sequences_add_result(row["ocl"])

        ds_name, _ = os.path.splitext(ds_name)
        self.save_results(dataset_name=ds_name, language="ocl")


if __name__ == "__main__":

    test = BaseLineAnalysis()
    test.run_analysis("BaseLine.json")

    test = GeneratedOCL()
    ds_names = ["gpt-4o","gpt-4o-mini","deepseek","llama","llama-sm","deepseek-sm"] 
    for ds_name in ds_names:
        test.run_analysis(ds_name)

    test = OCLKeywordsGenerated()
    test.run_analysis("gpt-4o")
    test.run_analysis("gpt-4o-mini")
    test.run_analysis("granite-code8b")
    test.run_analysis("llama3.1latest")

    test = PanOCLDataset()
    test.run_analysis("Pan_et_al.json") 

    result = KeywordResultWriter()
    kwgenerator = KeywordGroupingGenerator(
        language="ocl",
        keywords=test.keywords,
    )
    result.excluded_keywords = [
    '!','--', '/:', '/=','<:','?','/*', '*/', ' ', '"', '\'', '\\', '//', ',', '..', '\\\'', '\\\\', ';', 'derive', 'body', 'def', 'init','_','u','lambda','Function','Ref','derive:', 'init:','|->','undefinedLiteral','#','~','{','}']
    kwgenerator.save_excluded_keywords_to_cache(result.excluded_keywords, "MANUAL")    

    result.grouped_keywords = {
        'additiveOperators': ['+', '-'],
        'multiplicativeOperators': ['*', '/', 'div','mod'],
        'logicalOperators': ['or', 'xor', 'and', 'not','implies'],
        'logicalSymbols': ['=>','&'],
        'relationalOperators': ['<', '>', '>=', '<='],
        'equalityOperators': ['=', '<>'],

        'types': [
            'date', 'Date', 'String', 'Real', 'real', 'Str', 'str', 'string', 'Boolean', 'boolean', 'Integer', 'integer', 'int'
        ],
        'valueTypes': ['true', 'false'],
        'undefinedLiteral': ['null', 'oclUndefined', 'Undefined'],

        'conditionals': ['if', 'then', 'else', 'endif'],
        'namespaceOperators': ['::'],
        'prePostConditions': ['pre', 'post', '@pre'],
        'constraintDefinition': ['context', 'inv'],
        'variableBinding': ['let', 'in'],

        'typeOperations': [
            'oclAsType', 'oclIsKindOf', 'oclIsTypeOf', 'oclAsSet', 'selectByType', 'selectByKind'
        ],
        'collectionType': [
            'Collection', 'Set', 'set', 'Sequence', 'Bag', 'OrderedSet', 'Map',
            'Bag{', 'Set{', 'Sequence{', 'OrderedSet{', 'Map{'
        ],
        'collectionIterators': [
            'collect', 'forAll', 'exists', 'iterate', 'select', 'reject', 'one',
            'isUnique', 'any', 'collectNested', 'sortedBy'
        ],
        'collectionOperations': [
            'includes', 'excludes', 'count', 'size', 'includesAll', 'excludesAll',
            'isEmpty', 'notEmpty', 'sum', 'union'
        ],

        'typeFunctions': [
            'oclType', 'allInstances', 'oclIsUndefined', 'oclIsInvalid', 'oclIsNew'
        ],

        'numericFunctions': [
            'abs', 'floor', 'ceil', 'round',
            'log', 'exp', 'log10', 'pow', 'gcd',
            'sqrt', 'cbrt', 'sqr',
            'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
            'tanh', 'sinh', 'cosh',
            'max', 'min', 'prd'
        ],

        'conversionFunctions': [
            'toInteger', 'toReal', 'toBoolean',
            'toUpperCase', 'toLowerCase', 'asSet', 'asBag',
            'asOrderedSet', 'asSequence', 'characters'
        ],

        'collectionFunctions': [
            'copy', 'sort', 'unionAll', 'intersectAll', 'concatenateAll',
            'intersection', 'including', 'excluding', 'symmetricDifference',
            'prepend', 'append', 'apply', 'closure', 'subrange'
        ],

        'stringFunctions': [
            'split', 'hasPrefix', 'hasSuffix', 'equalsIgnoreCase',
            'replace', 'replaceAll', 'replaceAllMatches', 'replaceFirstMatch',
            'insertAt', 'insertInto', 'setAt', 'indexOf', 'lastIndexOf',
            'firstMatch', 'isMatch', 'hasMatch', 'display'
        ],

        'navigationFunctions': [
                'first', 'last', 'front', 'tail', 'reverse', 'at'
        ],

        'syntaxSymbols': [
            '(', ')', ':', '[', ']', '|'
        ],

        'navigation': ['.'],


    }
    kwgenerator.save_groups_to_cache(result.grouped_keywords, result.excluded_keywords, "MANUAL")

    result.datasets = ["BaseLine","deepseek","gpt-4o","gpt-4o-mini","llama","llama-sm","deepseek-sm","gpt-4o_kwGENtest","gpt-4o-mini_kwGENtest","granite-code8b_kwGENtest","llama3.1latest_kwGENtest","Pan_et_al"]
    result.ds_groups = {
        "LLM Generation - Abukhalaf et al., 2023": ["BaseLine","deepseek","llama","gpt-4o","gpt-4o-mini","llama-sm","deepseek-sm"], 

        "Dataset test - Pan et al., 2024": ["Pan_et_al"], 
        
        "LLM Keyword Generation Test": ["gpt-4o_kwGENtest","gpt-4o-mini_kwGENtest","granite-code8b_kwGENtest","llama3.1latest_kwGENtest"]}

    result.write_result_to_file("ocl")
