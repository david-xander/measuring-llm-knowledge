from antlr4 import *
from languages.r.parser.RVisitor import RVisitor
from languages.r.lib import get_cleaned_valid_text_according_to_keywords
from collections import Counter

class KeywordFrequencyVisitor(RVisitor):
    def __init__(self, keywords):
        super().__init__()
        self.keywords = set(keywords)
        self.counts = Counter()

    def visitTerminal(self, node):
        text = node.getText()

        cleaned_text = get_cleaned_valid_text_according_to_keywords(text, self.keywords)
        if not cleaned_text == None:
            self.counts[cleaned_text] += 1
        
        return self.visitChildren(node)
