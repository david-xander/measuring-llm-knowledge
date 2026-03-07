from antlr4 import *
from languages.ocl.parser.OCLVisitor import OCLVisitor
from languages.ocl.lib import get_cleaned_valid_text_according_to_keywords
from collections import Counter

class SyntacticAnalisisVisitor(OCLVisitor):
    def __init__(self, keywords, parser, parser_error_listener=None):
        super().__init__()
        self.keywords = set(keywords)
        self.parser = parser
        self.correct_keywords = Counter()  # flatten this, no rule separation needed
        self.used_keywords = Counter()     # NEW: count all keyword appearances
        self.rules_with_errors = {}
        self.rule_correct_usage = Counter()
        self.rule_usage = Counter()
        self.errors = []
        if parser_error_listener is not None:
            self.errors = parser_error_listener.errors or []

        # Track token indices to prevent double-counting
        self._counted_token_indices_correct = set()
        self._counted_token_indices_all = set()

    def _errors_in_node(self, node):
        if not isinstance(node, ParserRuleContext):
            return []
        start = getattr(node.start, "tokenIndex", None)
        stop = getattr(node.stop, "tokenIndex", None)
        if start is None or stop is None:
            return []
        found = []
        for err in self.errors:
            if err["stage"] == "lexer" or err["stage"] == "parser":
                tok_index = err.get("token_index")
                if tok_index is not None and start <= tok_index <= stop:
                    found.append(err)
        return found

    def visitChildren(self, node):
        if node is None:
            return

        rule_name = self.parser.ruleNames[node.getRuleIndex()]
        node_errors = self._errors_in_node(node)

        self.rule_usage[rule_name] += 1

        # Classify the node
        if node_errors:
            self.rules_with_errors.setdefault(rule_name, []).append({
                "start": getattr(node.start, "tokenIndex", None),
                "stop": getattr(node.stop, "tokenIndex", None),
                "errors": node_errors,
            })
        else:
            self.rule_correct_usage[rule_name] += 1

        # --- Scan all child tokens for keywords ---
        for child in getattr(node, "children", []) or []:
            if isinstance(child, TerminalNode):
                tok = getattr(child, "getSymbol", lambda: None)() or getattr(child, "symbol", None)
                tok_index = getattr(tok, "tokenIndex", None)
                token_id = tok_index if tok_index is not None else id(child)

                text = child.getText()
                cleaned_text = get_cleaned_valid_text_according_to_keywords(
                    text=text, keywords=self.keywords
                )
                if cleaned_text is None:
                    continue

                # --- Count every keyword occurrence once globally ---
                if token_id not in self._counted_token_indices_all:
                    self._counted_token_indices_all.add(token_id)
                    self.used_keywords[cleaned_text] += 1

                # --- Count only correct occurrences once globally ---
                if not node_errors and token_id not in self._counted_token_indices_correct:
                    self._counted_token_indices_correct.add(token_id)
                    self.correct_keywords[cleaned_text] += 1

        # Recurse
        for child in getattr(node, "children", []) or []:
            if not isinstance(child, TerminalNode):
                self.visit(child)

        return None
