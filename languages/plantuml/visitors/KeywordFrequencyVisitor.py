from antlr4 import *
from collections import Counter
from languages.plantuml.parser.PlantUMLVisitor import PlantUMLVisitor
from languages.plantuml.lib import get_cleaned_valid_text_according_to_keywords

class KeywordFrequencyVisitor(PlantUMLVisitor):
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
