from abc import ABC, abstractmethod
from antlr4.error.ErrorListener import ErrorListener


class KeywordFrequencyAnalyzerBaseClass(ABC):
    def __init__(self, keywords):
        self.keywords = keywords

    @abstractmethod
    def compute_with_parser(self, code_string):
        pass
    
    @abstractmethod
    def compute_with_lexer(self, code_string):
        pass
    
    @abstractmethod
    def compute_with_regex(self, code_string):
        pass

    def tree_depth(self, node):
        if node.getChildCount() == 0:
            return 1
        return 1 + max(self.tree_depth(node.getChild(i)) for i in range(node.getChildCount()))

    def tree_size(self, node):
        count = 1
        for i in range(node.getChildCount()):
            count += self.tree_size(node.getChild(i))
        return count

    def analyze(self, code_string, method):
        """
        Parse a single code example (string) and return keyword frequency vector.
        """
        if method == "regex":
            return self.compute_with_regex(code_string)
        elif method == "lexer":
            return self.compute_with_lexer(code_string)
        else:
            return self.compute_with_parser(code_string)


class AnalyzerCustomErrorListener( ErrorListener ):
    def __init__(self):
        super(AnalyzerCustomErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception({line, column, msg})
