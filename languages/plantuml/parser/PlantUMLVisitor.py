# Generated from PlantUML.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PlantUML import PlantUML
else:
    from PlantUML import PlantUML

# This class defines a complete generic visitor for a parse tree produced by PlantUML.

class PlantUMLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PlantUML#uml.
    def visitUml(self, ctx:PlantUML.UmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#class_dclr.
    def visitClass_dclr(self, ctx:PlantUML.Class_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#class_body.
    def visitClass_body(self, ctx:PlantUML.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#body_content.
    def visitBody_content(self, ctx:PlantUML.Body_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#nested_body.
    def visitNested_body(self, ctx:PlantUML.Nested_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#class_type.
    def visitClass_type(self, ctx:PlantUML.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#stereotype.
    def visitStereotype(self, ctx:PlantUML.StereotypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#extension_dclr.
    def visitExtension_dclr(self, ctx:PlantUML.Extension_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#ident.
    def visitIdent(self, ctx:PlantUML.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#enum_dclr.
    def visitEnum_dclr(self, ctx:PlantUML.Enum_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#association_dclr.
    def visitAssociation_dclr(self, ctx:PlantUML.Association_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#relation.
    def visitRelation(self, ctx:PlantUML.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#association_left.
    def visitAssociation_left(self, ctx:PlantUML.Association_leftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#association_right.
    def visitAssociation_right(self, ctx:PlantUML.Association_rightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#association_detail.
    def visitAssociation_detail(self, ctx:PlantUML.Association_detailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#association_name.
    def visitAssociation_name(self, ctx:PlantUML.Association_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUML#associative_class_dclr.
    def visitAssociative_class_dclr(self, ctx:PlantUML.Associative_class_dclrContext):
        return self.visitChildren(ctx)



del PlantUML