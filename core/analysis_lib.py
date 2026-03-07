import os
import pandas as pd
import traceback
from abc import ABC, abstractmethod
from collections import Counter

class RunAnalysis():
    def __init__(self):
        self.methods = ["regex", "lexer", "parser"]
        self.keywords = None
        self.analyzer = None
        self.parser_rules = None
        self.lexer_rules = None        
        self.initialize_features()
        self.extract_data_from_grammar()

        if self.keywords == None or self.parser_rules == None:
            raise Exception("Keywords or Parser rules not initailized")

    def initialize_features(self):
        self.results = {} # keyword frequency   
        self.errors = {} # only lexer and parsing errors of kw freq computation
        for method in self.methods:
            self.results[method] = []
            self.errors[method] = []
        self.syntactically_correct_keywords = []
        self.total_keywords = []
        self.rule_usage_accuracy = []
        self.rule_usage_vectors = []
        self.rule_correct_vectors = []
        self.rule_errors = []
        self.parser_lexer_errors = []
        self.tree_depth = []
        self.tree_size = []
        self.syntactically_valid_sequences_of_rules = []

    def local_dir_path(self):
        return os.path.dirname(os.getcwd())

    @abstractmethod
    def run_analysis(self, ds_name):
        self.initialize_features() 

    @abstractmethod
    def extract_data_from_grammar(self):
        pass

    def compute_frequency_add_result(self, code):
        for method in self.methods:
            freq_vector = [0] * len(self.keywords)
            try:
                freq_vector = self.analyzer.analyze(code, method)
            except Exception as e:
                self.errors[method].append({
                    "code": code,
                    "error": str(e),
                    "traceback": traceback.format_exc()
                })
            self.results[method].append({
                "code": code,
                **{kw: freq for kw, freq in zip(self.keywords, freq_vector)}
            })
    
    def extract_valid_rule_sequences_add_result(self, code):
        try:
            sequence = self.analyzer.extract_syntatically_valid_sequence_of_rules(code)
            self.syntactically_valid_sequences_of_rules.append(sequence)
        except Exception as e:
            print(e)
    
    def compute_syntactic_usage_add_result(self, code):
        # Collect all per-rule stats from the analyzer
        kw_correct, kw_used, rules_with_errors, rule_usage, rule_correct_usage, parser_lexer_errors, tree_depth, tree_size = self.analyzer.compute_usage_with_error_tolerant_parser(code)

        # Vector for correct keywords
        kw_vector = [kw_correct.get(kw, 0) for kw in self.keywords]
        kw_vector_data = {key: value for key, value in zip(self.keywords, kw_vector)}
        self.syntactically_correct_keywords.append(kw_vector_data)

        # Vector for any used keywords
        kw_vector2 = [kw_used.get(kw, 0) for kw in self.keywords]
        kw_vector_data2 = {key: value for key, value in zip(self.keywords, kw_vector2)}
        self.total_keywords.append(kw_vector_data2)

        # Rule usage vectors ---
        # For each rule in the grammar, get counts or default to 0
        rule_usage_vector = [rule_usage.get(rule, 0) for rule in self.parser_rules]
        rule_correct_vector = [rule_correct_usage.get(rule, 0) for rule in self.parser_rules]
        ruv_data ={key: value for key, value in zip(self.parser_rules,rule_usage_vector)}
        rcv_data ={key: value for key, value in zip(self.parser_rules,rule_correct_vector)}
        self.rule_usage_vectors.append(ruv_data)
        self.rule_correct_vectors.append(rcv_data)        

        # Global accuracy metric ---
        total_rule_correct = sum(rule_correct_usage.values())
        total_rule_usage = sum(rule_usage.values())
        accuracy = total_rule_correct / total_rule_usage if total_rule_usage > 0 else 0.0
        # accuracy_data = {key: value for key, value in zip(self.parser_rules, accuracy)}
        self.rule_usage_accuracy.append({"accuracy": accuracy})

        # Storing error messages for later generalization
        for rule_name, rule_entries in rules_with_errors.items():
            for entry in rule_entries:
                for err in entry.get("errors", []):
                    self.rule_errors.append({
                        "rule": rule_name,
                        "error": err["msg"]
                    })
        
        for error in parser_lexer_errors:
            self.parser_lexer_errors.append(error)

        # Storing depth and size of trees
        self.tree_depth.append(tree_depth)
        self.tree_size.append(tree_size)


    def get_results_path(self, language, method, file_name):
        # Build the path to the file
        results_path = os.path.join(
            self.local_dir_path(),
            'results',
            language,
            method,
            file_name
        )
        
        # Ensure all directories in the path exist (except the file)
        os.makedirs(os.path.dirname(results_path), exist_ok=True)
        
        # Return the full file path (you can then check or write to it)
        return results_path

    def save_results(self, language, dataset_name):
        for method in self.methods:
            
            # Save results
            self.save_csv(
                language=language,
                dataset_name=dataset_name,
                content=self.results[method],
                folder=method,
                file_name="_kw_freq.csv",
                message="✅ Keyword frequency results saved to"
            )

            # Save errors if any
            if self.errors[method]:
                self.save_csv(
                    language=language,
                    dataset_name=dataset_name,
                    content=self.errors[method],
                    folder=method,
                    file_name="_parsing_errors.csv",
                    message="⚠️ Some parsing errors occurred — details saved to"
                )  

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.syntactically_correct_keywords,
            folder="SyntacticalAnalysis",
            file_name="_syntactically_correct_kw.csv",
            message="✅ Syntactically correct keywords observed to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.total_keywords,
            folder="SyntacticalAnalysis",
            file_name="_total_kw.csv",
            message="✅ Total keywords observed to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.rule_usage_vectors,
            folder="SyntacticalAnalysis",
            file_name="_rule_usage_vectors.csv",
            message="✅ Rules usage vectors saved to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.rule_correct_vectors,
            folder="SyntacticalAnalysis",
            file_name="_rule_correct_vectors.csv",
            message="✅ Rules correct vectors saved to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.rule_usage_accuracy,
            folder="SyntacticalAnalysis",
            file_name="_rule_usage_accuracy.csv",
            message="✅ Rules usage accuracy saved to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.rule_errors,
            folder="SyntacticalAnalysis",
            file_name="_rule_errors.csv",
            message="✅ Rules errors saved to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.parser_lexer_errors,
            folder="SyntacticalAnalysis",
            file_name="_parser_lexer_errors.csv",
            message="✅ Parser and Lexer errors saved to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content=self.parser_lexer_errors,
            folder="SyntacticalAnalysis",
            file_name="_parser_lexer_errors.csv",
            message="✅ Parser and Lexer errors saved to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content={"tree_depth": self.tree_depth, "tree_size": self.tree_size},
            folder="SyntacticalAnalysis",
            file_name="_tree_depth_and_size.csv",
            message="✅ Tree depth and size saved to"
        )

        self.save_csv(
            language=language,
            dataset_name=dataset_name,
            content={"sequence": self.syntactically_valid_sequences_of_rules},
            folder="SyntacticalAnalysis",
            file_name="_sequences.csv",
            message="✅ Syntactically valid sequences of rules saved to"
        )
    
    def save_csv(self, language, dataset_name, content, folder, file_name, message):
        target_path = self.get_results_path(language, folder, dataset_name + file_name)
        results_df = pd.DataFrame(content)
        results_df["ds"] = dataset_name
        results_df.to_csv(target_path, index=False, encoding="utf-8")
        print(f"\n{message}: {target_path}")  