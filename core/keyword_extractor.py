import sys
from antlr4 import *
from antlr4 import InputStream
from antlr4.error.ErrorListener import ErrorListener
from languages.antlr.parser.ANTLRv4ParserVisitor import ANTLRv4ParserVisitor
from languages.antlr.parser.ANTLRv4Lexer import ANTLRv4Lexer
from languages.antlr.parser.ANTLRv4Parser import ANTLRv4Parser
import re


class AntlrKeywordExtractorVisitor(ANTLRv4ParserVisitor):
    def __init__(self):
        super().__init__()
        self.literals = set()
        self.parser_rules = set()
        self.lexer_rules = set()        

    def visitTerminal(self, node):
        text = node.getText()

        # Match single-quoted string literals
        if text.startswith("'") and text.endswith("'") and len(text) > 2:
            literal = text[1:-1]
            self.literals.add(literal)
        return self.visitChildren(node)
    
    def visitParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        rule_name = ctx.RULE_REF().getText()
        self.parser_rules.add(rule_name)
        return self.visitChildren(ctx)

    def visitLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        rule_name = ctx.TOKEN_REF().getText()
        self.lexer_rules.add(rule_name)
        return self.visitChildren(ctx)    

class ExtractKeywords():
    def __init__(self):
        self.keywords = set()
        self.parser_rules = set()
        self.lexer_rules = set()        

    def filter_literals_alphabetically(self, literals):
        # Filter to remove symbols and operators, keep alphabetic literals only
        keywords = sorted(
            {kw for kw in literals if re.fullmatch(r"[A-Za-z]+", kw)}
        )     

        return keywords   

    def filter_literals(self, literals):   
        return self.filter_literals_alphabetically(literals)   

    def extract(self, grammar_path)->int:
        input_stream = FileStream(grammar_path, encoding='utf-8')
        lexer = ANTLRv4Lexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener( MyErrorListener() )
        stream = CommonTokenStream(lexer)
        parser = ANTLRv4Parser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener( MyErrorListener() )        
        
        tree = parser.grammarSpec()  # entry rule of ANTLR grammar

        visitor = AntlrKeywordExtractorVisitor()
        visitor.visit(tree)

        keywords = self.filter_literals(visitor.literals)

        self.keywords = keywords
        self.parser_rules = visitor.parser_rules
        self.lexer_rules = visitor.lexer_rules
    

class MyErrorListener( ErrorListener ):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception({line, column, msg})

