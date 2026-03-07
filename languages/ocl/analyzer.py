from antlr4 import *
from collections import Counter
import re

from core.keyword_analyzer import KeywordFrequencyAnalyzerBaseClass, AnalyzerCustomErrorListener

from languages.ocl.parser.OCLLexer import OCLLexer
from languages.ocl.parser.OCLParser import OCLParser
from languages.ocl.visitors.SyntacticAnalisisVisitor import SyntacticAnalisisVisitor
from languages.ocl.visitors.KeywordFrequencyVisitor import KeywordFrequencyVisitor
from languages.ocl.visitors.SequenceVisitor import SequenceVisitor
from languages.ocl.errors.ErrorTolerantErrorListener import ErrorTolerantErrorListener

from languages.ocl.lib import get_cleaned_valid_text_according_to_keywords


class KeywordFrequencyAnalyzer(KeywordFrequencyAnalyzerBaseClass):
    def __init__(self, keywords):
        self.keywords = keywords

    def extract_syntatically_valid_sequence_of_rules(self, code_string):
        input_stream = InputStream(code_string)
        lexer = OCLLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener( AnalyzerCustomErrorListener() )
 
        stream = CommonTokenStream(lexer)
        parser = OCLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener( AnalyzerCustomErrorListener() )        
        tree = parser.multipleContextSpecifications()
        
        visitor = SequenceVisitor()
        visitor.visit(tree)

        return " ".join(visitor.visited_rules)

    def compute_usage_with_error_tolerant_parser(self, code_string):
        input_stream = InputStream(code_string)
        lexer = OCLLexer(input_stream)
        error_listener = ErrorTolerantErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener( error_listener )
 
        stream = CommonTokenStream(lexer)
        parser = OCLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener( error_listener )        
        tree = parser.multipleContextSpecifications()

        # Rule-level keyword collector, now error-aware
        visitor = SyntacticAnalisisVisitor(
            keywords=self.keywords,
            parser=parser,
            parser_error_listener=error_listener,
        )
        visitor.visit(tree)

        tree_depth = self.tree_depth(tree)
        tree_size = self.tree_size(tree)

        return visitor.correct_keywords, visitor.used_keywords, visitor.rules_with_errors, visitor.rule_usage, visitor.rule_correct_usage, error_listener.errors, tree_depth, tree_size

    def compute_with_parser(self, code_string):
        input_stream = InputStream(code_string)
        lexer = OCLLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener( AnalyzerCustomErrorListener() )
 
        stream = CommonTokenStream(lexer)
        parser = OCLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener( AnalyzerCustomErrorListener() )        
        tree = parser.multipleContextSpecifications()
        
        visitor = KeywordFrequencyVisitor(self.keywords)
        visitor.visit(tree)
        freq_vector = [visitor.counts.get(k, 0) for k in self.keywords]

        return freq_vector
    
    def compute_with_lexer(self, code_string):
        input_stream = InputStream(code_string)
        lexer_kw = OCLLexer(input_stream)
        lexer_kw.removeErrorListeners()
        lexer_kw.addErrorListener( AnalyzerCustomErrorListener() )  

        test_tokens = lexer_kw.getAllTokens()
        test_counter = Counter()
        for token in test_tokens:
            text = token.text
            cleaned_text = get_cleaned_valid_text_according_to_keywords(text, self.keywords)
            if not cleaned_text == None:
                test_counter[cleaned_text] += 1
        freq_vector = [test_counter.get(k, 0) for k in self.keywords]

        return freq_vector
    
    def compute_with_regex(self, code_string):
        string_pattern = r"(['\"])(?:\\.|(?!\1).)*\1"
        code_no_strings_literals = re.sub(string_pattern, " ", code_string)        

        # Build a regex pattern that matches *any* keyword (alphabetical or symbolic)
        # Escape each keyword so special regex chars like '+' or '*' are handled properly.
        escaped_keywords = [re.escape(k) for k in self.keywords]
        
        # Sort by length (longest first) to avoid partial matches
        # e.g., match "->>" before "->"
        escaped_keywords.sort(key=len, reverse=True)

        keyword_pattern = r"|".join(escaped_keywords)

        # Find all keyword occurrences
        matches = re.findall(keyword_pattern, code_no_strings_literals)

        # Count frequencies
        counts = Counter(matches)

        # Create frequency vector aligned with `self.keywords`
        freq_vector = [counts.get(k, 0) for k in self.keywords]
        
        return freq_vector

