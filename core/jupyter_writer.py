import nbformat as nbf
import os

class JupyterNotebookWriter():
    def __init__(self):
        self.cells = []
    
    def append_text(self, text):
        self.cells.append( nbf.v4.new_markdown_cell(text) )

    def append_code(self, code):
        self.cells.append( nbf.v4.new_code_cell(code) )

    def write_to_file(self, target_path):
        nb = nbf.v4.new_notebook()
        nb["cells"] = self.cells
        with open(target_path, 'w') as f:
            nbf.write(nb, f)
        print("Jupyter File saved!")


class KeywordResultWriter():
    def __init__(self):
        self.excluded_keywords = []
        self.grouped_keywords = {}
        self.datasets = []
        self.ds_groups = None

    def write_result_to_file(self, language):
        exclude_keywords_code = f"# EXCLUDE keywords\nexcluded_keywords = {self.excluded_keywords}"
        group_keywords_code = f"# GROUP keywords\ngrouped_keywords = {self.grouped_keywords}"

        results = JupyterNotebookWriter()

########################################################

        results.append_text(f"# Keyword Analysis Results for {language.upper()}")
        results.append_text("## Results Dataset")
        results.append_code(f""" 
import sys
sys.path.append('../')                            
from core.results_analysis import ResultsDataset     
from core.results_analysis import ResultsGraph
df = ResultsDataset().load_dataset_for_language("{language}")
df.head()
        """)
        results.append_text("### List of **RAW** Keywords (including metadata)")
        results.append_code(""" 
df.columns
        """)

########################################################

        results.append_text("## Keyword groups and filters")


        temp = []
        temp.append(exclude_keywords_code)
        temp.append(f"""   
{group_keywords_code}
df = ResultsDataset().filter_and_group_keywords(df, excluded_keywords, None)
df.head()                    
        """)
        results.append_code("\n".join(temp))
        results.append_text("### List of **CLEANED** Keywords (including metadata)")
        results.append_code(""" 
df.columns
        """)

########################################################

        results.append_text("## Keyword Coverage per dataset by Extractor")

        if self.ds_groups is None:
            results.append_code(""" 
ResultsGraph(df).keyword_coverage_per_dataset_by_extractor()
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f""" 
ResultsGraph(df).keyword_coverage_per_dataset_by_extractor({self.ds_groups[key]})
                """)                

########################################################

        results.append_text("## Uncovered Keywords by Extractor")
        results.append_code(""" 
from core.results_analysis import ResultsCoverage

test = ResultsCoverage(df)
print("Uncovered keywords REGEX", test.get_uncovered_keywords( test.compute_coverage(test.filter_kw_extractor_to_regex())) )
print("Uncovered keywords LEXER", test.get_uncovered_keywords( test.compute_coverage(test.filter_kw_extractor_to_lexer()) ))
print("Uncovered keywords PARSER", test.get_uncovered_keywords( test.compute_coverage(test.filter_kw_extractor_to_parser()) ))
        """)

########################################################

        results.append_text("## Keyword groups Frequency by dataset")
        results.append_text("""Considerations:
- Frequencies of keywords are extracted with a Lexer only.
- Frequency are normalized by dataset (the counts between datasets can be comparable now).
- Keywords are grouped to improve understanding.
        """)        

        results.append_code(f""" 
df = ResultsDataset().load_dataset_for_language("{language}")
df = ResultsDataset().filter_and_group_keywords(df, excluded_keywords, grouped_keywords)                            
        """)

        if self.ds_groups is None:
            results.append_code(""" 
ResultsGraph(df).keyword_frequency_by_dataset_heatmap()
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f""" 
ResultsGraph(df).keyword_frequency_by_dataset_heatmap(7, {self.ds_groups[key]})
                """)
        
########################################################        

        results.append_text("## Detail of individual Keywords Frequency by dataset")
        results.append_text("""Considerations:
- Frequencies of keywords are extracted with a Lexer only.
- Frequency are normalized by dataset (the counts between datasets can be comparable now).
        """)                
        results.append_code(f""" 
df = ResultsDataset().load_dataset_for_language("{language}")
df = ResultsDataset().filter_and_group_keywords(df, excluded_keywords, None)                            
ResultsGraph(df).keyword_frequency_by_dataset_heatmap()
        """)

########################################################

        results.append_text("## Keyword variance")
        results.append_text("""Considerations:
- Frequencies of keywords are extracted with a Lexer only.
        """)              
        results.append_code(f""" 
df = ResultsDataset().load_dataset_for_language("{language}")
df = ResultsDataset().filter_and_group_keywords(df, excluded_keywords, grouped_keywords)                            
        """)

        if self.ds_groups is None:
            results.append_code(""" 
ResultsGraph(df).plot_variance_analysis()   
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f""" 
ResultsGraph(df).plot_variance_analysis({self.ds_groups[key]})
                """)

########################################################
########################################################
########################################################

        results.append_text("# Syntactical Analysis")

        if not len(self.grouped_keywords.keys()) > 0:
            results.append_text("⚠️ **Warning:** Please create groups of keywords (`grouped_keywords`) according to the target language to be able to analyze properly its syntactical coverage.")

        results.append_code(f"""
# If there are no groups, the gruoup is the set of keywords - exclused_keywords
grouped_keywords = ResultsDataset().check_for_group_consistency(df, grouped_keywords, excluded_keywords)

# Load datasets
df = ResultsDataset().load_dataset_for_language("{language}")
syntactically_correct_kw_ds, total_kw_ds, rule_usage_vectors_ds, rule_correct_vectors_ds, rule_usage_accuracy_ds, rule_errors_ds, parser_lexer_errors, tree_depth_and_size, sequences_ds = ResultsDataset().load_syntactic_analysis_dataset_for_language("{language}")

# Exclude columns not relevant for analysis, but NO GROUPING
df = ResultsDataset().filter_and_group_keywords(df, excluded_keywords, None)
syntactically_correct_kw_ds = ResultsDataset().filter_and_group_keywords(syntactically_correct_kw_ds, excluded_keywords, None)
total_kw_ds = ResultsDataset().filter_and_group_keywords(total_kw_ds, excluded_keywords, None)


grouped_tables = ResultsCoverage(df).get_grouped_tables(df, syntactically_correct_kw_ds, total_kw_ds, grouped_keywords)

        """)
        results.append_text("""
## Questions:
- 1. Which language keywords does the LLM recognize and use appropriately? 
- 2. Which language keywords does the LLM fail to recognize or use correctly?
        """)

        if self.ds_groups is None:
            results.append_code(""" 
ResultsGraph(df).plot_heatmap_keyword_usage(grouped_tables)
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f"""
ResultsCoverage(df).get_keyword_coverage_and_correctness_table_v2(df, syntactically_correct_kw_ds, total_kw_ds, rule_usage_vectors_ds, rule_correct_vectors_ds, tree_depth_and_size, {self.ds_groups[key]})
                """)
                results.append_code(f""" 
ResultsGraph(df).plot_heatmap_keyword_usage(grouped_tables, {self.ds_groups[key]})
                """)                   

########################################################

        results.append_text(f"## Detail Table for each dataset")
        for ds in self.datasets:
            results.append_code(f""" 
grouped_tables["{ds}"]
            """)

########################################################
        
        results.append_text("""
## Syntactically Correct Rule Usage
        """)
        if self.ds_groups is None:
            results.append_code(""" 
ResultsGraph(df).syntactically_correct_rule_usage_distribution(rule_usage_accuracy_ds)
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f""" 
ResultsGraph(df).syntactically_correct_rule_usage_distribution(rule_usage_accuracy_ds, {self.ds_groups[key]})
                """)                 

########################################################

        results.append_text("""
## Rule usage ratio by dataset
        """)
        results.append_code("""
rules_usage_summary = ResultsCoverage(df).get_rule_usage_summary(rule_usage_vectors_ds, rule_correct_vectors_ds)
rule_usage_avg_accuracy = ResultsCoverage(df).get_rule_usage_avg_accuracy(rules_usage_summary)
        """)

        if self.ds_groups is None:
            results.append_code(f""" 
ResultsGraph(df).plot_heatmap_rule_usage_summary(rules_usage_summary)
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f""" 
ResultsGraph(df).plot_heatmap_rule_usage_summary(rules_usage_summary, {self.ds_groups[key]})
                """)

########################################################

        results.append_text("## Rule usage variance")       

        if self.ds_groups is None:
            results.append_code(""" 
ResultsGraph(df).plot_rule_variance_analysis(rule_usage_vectors_ds)   
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f""" 
ResultsGraph(df).plot_rule_variance_analysis(rule_usage_vectors_ds, {self.ds_groups[key]})
                """)

########################################################

        results.append_text("## Tree size and depth")       
        results.append_text("""
                            
- Do LLMs generate simple flat constructs? Are the LLM-generated programs reaching the same complexity region as human-written ones?
- Can LLMs use deeply nested or recursive syntax? How does the "shape" of complexity differ across datasets (LLMs)?
        """)
    
        if self.ds_groups is None:
            results.append_code(""" 
ResultsGraph(df).plot_tree_depth_and_size_analisis(tree_depth_and_size)   
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f""" 
ResultsGraph(df).plot_tree_depth_and_size_analisis(tree_depth_and_size, {self.ds_groups[key]})
                """)

########################################################

        results.append_text("""
# Errors
        """)
        results.append_code("""
parser_lexer_errors = ResultsCoverage(df).get_errors_with_generic_antlr_types(parser_lexer_errors)
        """)

        results.append_text("""
## Error detail by rule and dataset
        """)

        results.append_code("""
rule_errors_ds = ResultsCoverage(df).get_rule_errors_with_generic_antlr_types(rule_errors_ds)
        """)

        if self.ds_groups is None:
            results.append_text("""
#### What rules do we need to address first?
            """)
            results.append_code(f"""                               
ResultsGraph(df).plot_rule_priority_matrix(rule_errors_ds)
            """)
            results.append_text("""
#### What type of error are found in the dataset of the target model I need to improve detailed by rule?        
            """)
            for ds in self.datasets:
                results.append_code(f""" 
ResultsGraph(df).plot_rule_error_types_for_ds("{ds}", rule_errors_ds)
                """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_text("""
#### What rules do we need to address first?
                """)
                results.append_code(f"""
ResultsGraph(df).plot_rule_priority_matrix(rule_errors_ds, {self.ds_groups[key]})
                """)
                results.append_text("""
#### What type of error are found in the dataset of the target model I need to improve detailed by rule?        
                """)
                for ds in self.ds_groups[key]:
                    results.append_code(f""" 
ResultsGraph(df).plot_rule_error_types_for_ds("{ds}", rule_errors_ds)
                	""")

########################################################

        results.append_text("""
## Lexer and Parser errors detail
        """)

        if self.ds_groups is None:
            results.append_code("""
ResultsGraph(df).plot_error_stage_per_dataset(parser_lexer_errors)
            """)            
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f"""
ResultsGraph(df).plot_error_stage_per_dataset(parser_lexer_errors, {self.ds_groups[key]})
                """)

########################################################

        results.append_text("""
## Error detail per dataset
        """)

        if self.ds_groups is None:
            results.append_code("""
ResultsGraph(df).plot_error_type_ratio_per_dataset(parser_lexer_errors)
            """)
        else:
            for key in self.ds_groups.keys():
                results.append_text(f"### {key}")
                results.append_code(f"""
ResultsGraph(df).plot_error_type_ratio_per_dataset(parser_lexer_errors, {self.ds_groups[key]})
                """)

########################################################


        target_path = os.path.join(os.path.dirname(os.getcwd()), "analysis", f"{language}.ipynb")
        results.write_to_file(target_path)        
