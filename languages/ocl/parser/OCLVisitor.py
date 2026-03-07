# Generated from OCL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OCLParser import OCLParser
else:
    from OCLParser import OCLParser

# This class defines a complete generic visitor for a parse tree produced by OCLParser.

class OCLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OCLParser#multipleContextSpecifications.
    def visitMultipleContextSpecifications(self, ctx:OCLParser.MultipleContextSpecificationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#contextSpecification.
    def visitContextSpecification(self, ctx:OCLParser.ContextSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#singleInvariant.
    def visitSingleInvariant(self, ctx:OCLParser.SingleInvariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#singleDerivedAttribute.
    def visitSingleDerivedAttribute(self, ctx:OCLParser.SingleDerivedAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#type.
    def visitType(self, ctx:OCLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#expressionList.
    def visitExpressionList(self, ctx:OCLParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#expression.
    def visitExpression(self, ctx:OCLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:OCLParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#letExpression.
    def visitLetExpression(self, ctx:OCLParser.LetExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#letBinding.
    def visitLetBinding(self, ctx:OCLParser.LetBindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#basicExpression.
    def visitBasicExpression(self, ctx:OCLParser.BasicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#logicalExpression.
    def visitLogicalExpression(self, ctx:OCLParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#equalityExpression.
    def visitEqualityExpression(self, ctx:OCLParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:OCLParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:OCLParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#unaryExpression.
    def visitUnaryExpression(self, ctx:OCLParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#navigationExpression.
    def visitNavigationExpression(self, ctx:OCLParser.NavigationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#primaryFactor.
    def visitPrimaryFactor(self, ctx:OCLParser.PrimaryFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#postfixSuffix.
    def visitPostfixSuffix(self, ctx:OCLParser.PostfixSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#identOptType.
    def visitIdentOptType(self, ctx:OCLParser.IdentOptTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#identOptTypeList.
    def visitIdentOptTypeList(self, ctx:OCLParser.IdentOptTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#setExpression.
    def visitSetExpression(self, ctx:OCLParser.SetExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#identifier.
    def visitIdentifier(self, ctx:OCLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OCLParser#qualified_name.
    def visitQualified_name(self, ctx:OCLParser.Qualified_nameContext):
        return self.visitChildren(ctx)



del OCLParser