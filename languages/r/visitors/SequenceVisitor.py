from antlr4 import *
from languages.r.parser.RVisitor import RVisitor

class SequenceVisitor(RVisitor):
    def __init__(self):
        super().__init__()
        self.visited_rules = []

    def visitChildren(self, node):
        # Capture rule name if it's a parser rule context
        if hasattr(node, 'getRuleIndex') and node.getRuleIndex() >= 0:
            rule_name = type(node).__name__
            self.visited_rules.append(rule_name)
        
        return super().visitChildren(node)

