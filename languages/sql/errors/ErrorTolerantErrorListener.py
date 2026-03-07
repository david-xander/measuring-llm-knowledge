from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

class ErrorTolerantErrorListener( ErrorListener ):
    def __init__(self):
        super(ErrorTolerantErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        try:
            tok_index = offendingSymbol.tokenIndex
        except Exception:
            tok_index = None
        
        stage = "lexer" if isinstance(recognizer, Lexer) else "parser"
        self.errors.append({
            "stage": stage,
            "line": line, 
            "column": column,
            "token_index": tok_index, 
            "msg": msg
        })