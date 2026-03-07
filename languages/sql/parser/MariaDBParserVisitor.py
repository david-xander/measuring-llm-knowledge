# Generated from MariaDBParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MariaDBParser import MariaDBParser
else:
    from MariaDBParser import MariaDBParser

# This class defines a complete generic visitor for a parse tree produced by MariaDBParser.

class MariaDBParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MariaDBParser#root.
    def visitRoot(self, ctx:MariaDBParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#sqlStatements.
    def visitSqlStatements(self, ctx:MariaDBParser.SqlStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#sqlStatement.
    def visitSqlStatement(self, ctx:MariaDBParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setStatementFor.
    def visitSetStatementFor(self, ctx:MariaDBParser.SetStatementForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#emptyStatement_.
    def visitEmptyStatement_(self, ctx:MariaDBParser.EmptyStatement_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#ddlStatement.
    def visitDdlStatement(self, ctx:MariaDBParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dmlStatement.
    def visitDmlStatement(self, ctx:MariaDBParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#transactionStatement.
    def visitTransactionStatement(self, ctx:MariaDBParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#replicationStatement.
    def visitReplicationStatement(self, ctx:MariaDBParser.ReplicationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#preparedStatement.
    def visitPreparedStatement(self, ctx:MariaDBParser.PreparedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MariaDBParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#administrationStatement.
    def visitAdministrationStatement(self, ctx:MariaDBParser.AdministrationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#utilityStatement.
    def visitUtilityStatement(self, ctx:MariaDBParser.UtilityStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createDatabase.
    def visitCreateDatabase(self, ctx:MariaDBParser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createEvent.
    def visitCreateEvent(self, ctx:MariaDBParser.CreateEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createIndex.
    def visitCreateIndex(self, ctx:MariaDBParser.CreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createLogfileGroup.
    def visitCreateLogfileGroup(self, ctx:MariaDBParser.CreateLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createProcedure.
    def visitCreateProcedure(self, ctx:MariaDBParser.CreateProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createFunction.
    def visitCreateFunction(self, ctx:MariaDBParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createRole.
    def visitCreateRole(self, ctx:MariaDBParser.CreateRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createServer.
    def visitCreateServer(self, ctx:MariaDBParser.CreateServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#copyCreateTable.
    def visitCopyCreateTable(self, ctx:MariaDBParser.CopyCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#queryCreateTable.
    def visitQueryCreateTable(self, ctx:MariaDBParser.QueryCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#columnCreateTable.
    def visitColumnCreateTable(self, ctx:MariaDBParser.ColumnCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createTablespaceInnodb.
    def visitCreateTablespaceInnodb(self, ctx:MariaDBParser.CreateTablespaceInnodbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createTablespaceNdb.
    def visitCreateTablespaceNdb(self, ctx:MariaDBParser.CreateTablespaceNdbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createTrigger.
    def visitCreateTrigger(self, ctx:MariaDBParser.CreateTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#withClause.
    def visitWithClause(self, ctx:MariaDBParser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#commonTableExpressions.
    def visitCommonTableExpressions(self, ctx:MariaDBParser.CommonTableExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#cteName.
    def visitCteName(self, ctx:MariaDBParser.CteNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#cteColumnName.
    def visitCteColumnName(self, ctx:MariaDBParser.CteColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createView.
    def visitCreateView(self, ctx:MariaDBParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createSequence.
    def visitCreateSequence(self, ctx:MariaDBParser.CreateSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#sequenceSpec.
    def visitSequenceSpec(self, ctx:MariaDBParser.SequenceSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createDatabaseOption.
    def visitCreateDatabaseOption(self, ctx:MariaDBParser.CreateDatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#charSet.
    def visitCharSet(self, ctx:MariaDBParser.CharSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#currentUserExpression.
    def visitCurrentUserExpression(self, ctx:MariaDBParser.CurrentUserExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#ownerStatement.
    def visitOwnerStatement(self, ctx:MariaDBParser.OwnerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#preciseSchedule.
    def visitPreciseSchedule(self, ctx:MariaDBParser.PreciseScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#intervalSchedule.
    def visitIntervalSchedule(self, ctx:MariaDBParser.IntervalScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#timestampValue.
    def visitTimestampValue(self, ctx:MariaDBParser.TimestampValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#intervalExpr.
    def visitIntervalExpr(self, ctx:MariaDBParser.IntervalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#intervalType.
    def visitIntervalType(self, ctx:MariaDBParser.IntervalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#enableType.
    def visitEnableType(self, ctx:MariaDBParser.EnableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#indexType.
    def visitIndexType(self, ctx:MariaDBParser.IndexTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#indexOption.
    def visitIndexOption(self, ctx:MariaDBParser.IndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#procedureParameter.
    def visitProcedureParameter(self, ctx:MariaDBParser.ProcedureParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#functionParameter.
    def visitFunctionParameter(self, ctx:MariaDBParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#routineComment.
    def visitRoutineComment(self, ctx:MariaDBParser.RoutineCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#routineLanguage.
    def visitRoutineLanguage(self, ctx:MariaDBParser.RoutineLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#routineBehavior.
    def visitRoutineBehavior(self, ctx:MariaDBParser.RoutineBehaviorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#routineData.
    def visitRoutineData(self, ctx:MariaDBParser.RoutineDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#routineSecurity.
    def visitRoutineSecurity(self, ctx:MariaDBParser.RoutineSecurityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#serverOption.
    def visitServerOption(self, ctx:MariaDBParser.ServerOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createDefinitions.
    def visitCreateDefinitions(self, ctx:MariaDBParser.CreateDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#columnDeclaration.
    def visitColumnDeclaration(self, ctx:MariaDBParser.ColumnDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#constraintDeclaration.
    def visitConstraintDeclaration(self, ctx:MariaDBParser.ConstraintDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#indexDeclaration.
    def visitIndexDeclaration(self, ctx:MariaDBParser.IndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#periodDeclaration.
    def visitPeriodDeclaration(self, ctx:MariaDBParser.PeriodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#columnDefinition.
    def visitColumnDefinition(self, ctx:MariaDBParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nullColumnConstraint.
    def visitNullColumnConstraint(self, ctx:MariaDBParser.NullColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#defaultColumnConstraint.
    def visitDefaultColumnConstraint(self, ctx:MariaDBParser.DefaultColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#visibilityColumnConstraint.
    def visitVisibilityColumnConstraint(self, ctx:MariaDBParser.VisibilityColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#invisibilityColumnConstraint.
    def visitInvisibilityColumnConstraint(self, ctx:MariaDBParser.InvisibilityColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#autoIncrementColumnConstraint.
    def visitAutoIncrementColumnConstraint(self, ctx:MariaDBParser.AutoIncrementColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#primaryKeyColumnConstraint.
    def visitPrimaryKeyColumnConstraint(self, ctx:MariaDBParser.PrimaryKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#uniqueKeyColumnConstraint.
    def visitUniqueKeyColumnConstraint(self, ctx:MariaDBParser.UniqueKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#commentColumnConstraint.
    def visitCommentColumnConstraint(self, ctx:MariaDBParser.CommentColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#formatColumnConstraint.
    def visitFormatColumnConstraint(self, ctx:MariaDBParser.FormatColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#storageColumnConstraint.
    def visitStorageColumnConstraint(self, ctx:MariaDBParser.StorageColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#referenceColumnConstraint.
    def visitReferenceColumnConstraint(self, ctx:MariaDBParser.ReferenceColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#collateColumnConstraint.
    def visitCollateColumnConstraint(self, ctx:MariaDBParser.CollateColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#generatedColumnConstraint.
    def visitGeneratedColumnConstraint(self, ctx:MariaDBParser.GeneratedColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#serialDefaultColumnConstraint.
    def visitSerialDefaultColumnConstraint(self, ctx:MariaDBParser.SerialDefaultColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#checkColumnConstraint.
    def visitCheckColumnConstraint(self, ctx:MariaDBParser.CheckColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#primaryKeyTableConstraint.
    def visitPrimaryKeyTableConstraint(self, ctx:MariaDBParser.PrimaryKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#uniqueKeyTableConstraint.
    def visitUniqueKeyTableConstraint(self, ctx:MariaDBParser.UniqueKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#foreignKeyTableConstraint.
    def visitForeignKeyTableConstraint(self, ctx:MariaDBParser.ForeignKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#checkTableConstraint.
    def visitCheckTableConstraint(self, ctx:MariaDBParser.CheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#referenceDefinition.
    def visitReferenceDefinition(self, ctx:MariaDBParser.ReferenceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#referenceAction.
    def visitReferenceAction(self, ctx:MariaDBParser.ReferenceActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#referenceControlType.
    def visitReferenceControlType(self, ctx:MariaDBParser.ReferenceControlTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleIndexDeclaration.
    def visitSimpleIndexDeclaration(self, ctx:MariaDBParser.SimpleIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#specialIndexDeclaration.
    def visitSpecialIndexDeclaration(self, ctx:MariaDBParser.SpecialIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#periodDefinition.
    def visitPeriodDefinition(self, ctx:MariaDBParser.PeriodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionEngine.
    def visitTableOptionEngine(self, ctx:MariaDBParser.TableOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionEngineAttribute.
    def visitTableOptionEngineAttribute(self, ctx:MariaDBParser.TableOptionEngineAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionAutoextendSize.
    def visitTableOptionAutoextendSize(self, ctx:MariaDBParser.TableOptionAutoextendSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionAutoIncrement.
    def visitTableOptionAutoIncrement(self, ctx:MariaDBParser.TableOptionAutoIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionAverage.
    def visitTableOptionAverage(self, ctx:MariaDBParser.TableOptionAverageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionCharset.
    def visitTableOptionCharset(self, ctx:MariaDBParser.TableOptionCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionChecksum.
    def visitTableOptionChecksum(self, ctx:MariaDBParser.TableOptionChecksumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionCollate.
    def visitTableOptionCollate(self, ctx:MariaDBParser.TableOptionCollateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionComment.
    def visitTableOptionComment(self, ctx:MariaDBParser.TableOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionCompression.
    def visitTableOptionCompression(self, ctx:MariaDBParser.TableOptionCompressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionConnection.
    def visitTableOptionConnection(self, ctx:MariaDBParser.TableOptionConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionDataDirectory.
    def visitTableOptionDataDirectory(self, ctx:MariaDBParser.TableOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionDelay.
    def visitTableOptionDelay(self, ctx:MariaDBParser.TableOptionDelayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionEncryption.
    def visitTableOptionEncryption(self, ctx:MariaDBParser.TableOptionEncryptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionEncrypted.
    def visitTableOptionEncrypted(self, ctx:MariaDBParser.TableOptionEncryptedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionPageCompressed.
    def visitTableOptionPageCompressed(self, ctx:MariaDBParser.TableOptionPageCompressedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionPageCompressionLevel.
    def visitTableOptionPageCompressionLevel(self, ctx:MariaDBParser.TableOptionPageCompressionLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionEncryptionKeyId.
    def visitTableOptionEncryptionKeyId(self, ctx:MariaDBParser.TableOptionEncryptionKeyIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionIndexDirectory.
    def visitTableOptionIndexDirectory(self, ctx:MariaDBParser.TableOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionInsertMethod.
    def visitTableOptionInsertMethod(self, ctx:MariaDBParser.TableOptionInsertMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionKeyBlockSize.
    def visitTableOptionKeyBlockSize(self, ctx:MariaDBParser.TableOptionKeyBlockSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionMaxRows.
    def visitTableOptionMaxRows(self, ctx:MariaDBParser.TableOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionMinRows.
    def visitTableOptionMinRows(self, ctx:MariaDBParser.TableOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionPackKeys.
    def visitTableOptionPackKeys(self, ctx:MariaDBParser.TableOptionPackKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionPassword.
    def visitTableOptionPassword(self, ctx:MariaDBParser.TableOptionPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionRowFormat.
    def visitTableOptionRowFormat(self, ctx:MariaDBParser.TableOptionRowFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionStartTransaction.
    def visitTableOptionStartTransaction(self, ctx:MariaDBParser.TableOptionStartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionSecondaryEngineAttribute.
    def visitTableOptionSecondaryEngineAttribute(self, ctx:MariaDBParser.TableOptionSecondaryEngineAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionRecalculation.
    def visitTableOptionRecalculation(self, ctx:MariaDBParser.TableOptionRecalculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionPersistent.
    def visitTableOptionPersistent(self, ctx:MariaDBParser.TableOptionPersistentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionSamplePage.
    def visitTableOptionSamplePage(self, ctx:MariaDBParser.TableOptionSamplePageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionTablespace.
    def visitTableOptionTablespace(self, ctx:MariaDBParser.TableOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionTableType.
    def visitTableOptionTableType(self, ctx:MariaDBParser.TableOptionTableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionTransactional.
    def visitTableOptionTransactional(self, ctx:MariaDBParser.TableOptionTransactionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionUnion.
    def visitTableOptionUnion(self, ctx:MariaDBParser.TableOptionUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableOptionWithSystemVersioning.
    def visitTableOptionWithSystemVersioning(self, ctx:MariaDBParser.TableOptionWithSystemVersioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableType.
    def visitTableType(self, ctx:MariaDBParser.TableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tablespaceStorage.
    def visitTablespaceStorage(self, ctx:MariaDBParser.TablespaceStorageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionDefinitions.
    def visitPartitionDefinitions(self, ctx:MariaDBParser.PartitionDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionFunctionHash.
    def visitPartitionFunctionHash(self, ctx:MariaDBParser.PartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionFunctionKey.
    def visitPartitionFunctionKey(self, ctx:MariaDBParser.PartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionFunctionRange.
    def visitPartitionFunctionRange(self, ctx:MariaDBParser.PartitionFunctionRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionFunctionList.
    def visitPartitionFunctionList(self, ctx:MariaDBParser.PartitionFunctionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionSystemVersion.
    def visitPartitionSystemVersion(self, ctx:MariaDBParser.PartitionSystemVersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionSystemVersionDefinitions.
    def visitPartitionSystemVersionDefinitions(self, ctx:MariaDBParser.PartitionSystemVersionDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionSystemVersionDefinition.
    def visitPartitionSystemVersionDefinition(self, ctx:MariaDBParser.PartitionSystemVersionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#subPartitionFunctionHash.
    def visitSubPartitionFunctionHash(self, ctx:MariaDBParser.SubPartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#subPartitionFunctionKey.
    def visitSubPartitionFunctionKey(self, ctx:MariaDBParser.SubPartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionComparison.
    def visitPartitionComparison(self, ctx:MariaDBParser.PartitionComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionListAtom.
    def visitPartitionListAtom(self, ctx:MariaDBParser.PartitionListAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionListVector.
    def visitPartitionListVector(self, ctx:MariaDBParser.PartitionListVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionSimple.
    def visitPartitionSimple(self, ctx:MariaDBParser.PartitionSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionDefinerAtom.
    def visitPartitionDefinerAtom(self, ctx:MariaDBParser.PartitionDefinerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionDefinerVector.
    def visitPartitionDefinerVector(self, ctx:MariaDBParser.PartitionDefinerVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#subpartitionDefinition.
    def visitSubpartitionDefinition(self, ctx:MariaDBParser.SubpartitionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionEngine.
    def visitPartitionOptionEngine(self, ctx:MariaDBParser.PartitionOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionComment.
    def visitPartitionOptionComment(self, ctx:MariaDBParser.PartitionOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionDataDirectory.
    def visitPartitionOptionDataDirectory(self, ctx:MariaDBParser.PartitionOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionIndexDirectory.
    def visitPartitionOptionIndexDirectory(self, ctx:MariaDBParser.PartitionOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionMaxRows.
    def visitPartitionOptionMaxRows(self, ctx:MariaDBParser.PartitionOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionMinRows.
    def visitPartitionOptionMinRows(self, ctx:MariaDBParser.PartitionOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionTablespace.
    def visitPartitionOptionTablespace(self, ctx:MariaDBParser.PartitionOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionOptionNodeGroup.
    def visitPartitionOptionNodeGroup(self, ctx:MariaDBParser.PartitionOptionNodeGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterSimpleDatabase.
    def visitAlterSimpleDatabase(self, ctx:MariaDBParser.AlterSimpleDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterUpgradeName.
    def visitAlterUpgradeName(self, ctx:MariaDBParser.AlterUpgradeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterEvent.
    def visitAlterEvent(self, ctx:MariaDBParser.AlterEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterFunction.
    def visitAlterFunction(self, ctx:MariaDBParser.AlterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterInstance.
    def visitAlterInstance(self, ctx:MariaDBParser.AlterInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterLogfileGroup.
    def visitAlterLogfileGroup(self, ctx:MariaDBParser.AlterLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterProcedure.
    def visitAlterProcedure(self, ctx:MariaDBParser.AlterProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterServer.
    def visitAlterServer(self, ctx:MariaDBParser.AlterServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterTable.
    def visitAlterTable(self, ctx:MariaDBParser.AlterTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterTablespace.
    def visitAlterTablespace(self, ctx:MariaDBParser.AlterTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterView.
    def visitAlterView(self, ctx:MariaDBParser.AlterViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterSequence.
    def visitAlterSequence(self, ctx:MariaDBParser.AlterSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByTableOption.
    def visitAlterByTableOption(self, ctx:MariaDBParser.AlterByTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddColumn.
    def visitAlterByAddColumn(self, ctx:MariaDBParser.AlterByAddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddColumns.
    def visitAlterByAddColumns(self, ctx:MariaDBParser.AlterByAddColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddIndex.
    def visitAlterByAddIndex(self, ctx:MariaDBParser.AlterByAddIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddPrimaryKey.
    def visitAlterByAddPrimaryKey(self, ctx:MariaDBParser.AlterByAddPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddUniqueKey.
    def visitAlterByAddUniqueKey(self, ctx:MariaDBParser.AlterByAddUniqueKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddSpecialIndex.
    def visitAlterByAddSpecialIndex(self, ctx:MariaDBParser.AlterByAddSpecialIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddForeignKey.
    def visitAlterByAddForeignKey(self, ctx:MariaDBParser.AlterByAddForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddCheckTableConstraint.
    def visitAlterByAddCheckTableConstraint(self, ctx:MariaDBParser.AlterByAddCheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterBySetAlgorithm.
    def visitAlterBySetAlgorithm(self, ctx:MariaDBParser.AlterBySetAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByChangeDefault.
    def visitAlterByChangeDefault(self, ctx:MariaDBParser.AlterByChangeDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByChangeColumn.
    def visitAlterByChangeColumn(self, ctx:MariaDBParser.AlterByChangeColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByRenameColumn.
    def visitAlterByRenameColumn(self, ctx:MariaDBParser.AlterByRenameColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByLock.
    def visitAlterByLock(self, ctx:MariaDBParser.AlterByLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByModifyColumn.
    def visitAlterByModifyColumn(self, ctx:MariaDBParser.AlterByModifyColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDropColumn.
    def visitAlterByDropColumn(self, ctx:MariaDBParser.AlterByDropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDropConstraintCheck.
    def visitAlterByDropConstraintCheck(self, ctx:MariaDBParser.AlterByDropConstraintCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDropPrimaryKey.
    def visitAlterByDropPrimaryKey(self, ctx:MariaDBParser.AlterByDropPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByNotExistingPrimaryKey.
    def visitAlterByNotExistingPrimaryKey(self, ctx:MariaDBParser.AlterByNotExistingPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDropIndex.
    def visitAlterByDropIndex(self, ctx:MariaDBParser.AlterByDropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByRenameIndex.
    def visitAlterByRenameIndex(self, ctx:MariaDBParser.AlterByRenameIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAlterIndexVisibility.
    def visitAlterByAlterIndexVisibility(self, ctx:MariaDBParser.AlterByAlterIndexVisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAlterIndexIgnore.
    def visitAlterByAlterIndexIgnore(self, ctx:MariaDBParser.AlterByAlterIndexIgnoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDropForeignKey.
    def visitAlterByDropForeignKey(self, ctx:MariaDBParser.AlterByDropForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDisableKeys.
    def visitAlterByDisableKeys(self, ctx:MariaDBParser.AlterByDisableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByEnableKeys.
    def visitAlterByEnableKeys(self, ctx:MariaDBParser.AlterByEnableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByRename.
    def visitAlterByRename(self, ctx:MariaDBParser.AlterByRenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByOrder.
    def visitAlterByOrder(self, ctx:MariaDBParser.AlterByOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByConvertCharset.
    def visitAlterByConvertCharset(self, ctx:MariaDBParser.AlterByConvertCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDefaultCharset.
    def visitAlterByDefaultCharset(self, ctx:MariaDBParser.AlterByDefaultCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDiscardTablespace.
    def visitAlterByDiscardTablespace(self, ctx:MariaDBParser.AlterByDiscardTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByImportTablespace.
    def visitAlterByImportTablespace(self, ctx:MariaDBParser.AlterByImportTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByForce.
    def visitAlterByForce(self, ctx:MariaDBParser.AlterByForceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByValidate.
    def visitAlterByValidate(self, ctx:MariaDBParser.AlterByValidateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddDefinitions.
    def visitAlterByAddDefinitions(self, ctx:MariaDBParser.AlterByAddDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterPartition.
    def visitAlterPartition(self, ctx:MariaDBParser.AlterPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAddPartition.
    def visitAlterByAddPartition(self, ctx:MariaDBParser.AlterByAddPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDropPartition.
    def visitAlterByDropPartition(self, ctx:MariaDBParser.AlterByDropPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByDiscardPartition.
    def visitAlterByDiscardPartition(self, ctx:MariaDBParser.AlterByDiscardPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByImportPartition.
    def visitAlterByImportPartition(self, ctx:MariaDBParser.AlterByImportPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByTruncatePartition.
    def visitAlterByTruncatePartition(self, ctx:MariaDBParser.AlterByTruncatePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByCoalescePartition.
    def visitAlterByCoalescePartition(self, ctx:MariaDBParser.AlterByCoalescePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByReorganizePartition.
    def visitAlterByReorganizePartition(self, ctx:MariaDBParser.AlterByReorganizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByExchangePartition.
    def visitAlterByExchangePartition(self, ctx:MariaDBParser.AlterByExchangePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByAnalyzePartition.
    def visitAlterByAnalyzePartition(self, ctx:MariaDBParser.AlterByAnalyzePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByCheckPartition.
    def visitAlterByCheckPartition(self, ctx:MariaDBParser.AlterByCheckPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByOptimizePartition.
    def visitAlterByOptimizePartition(self, ctx:MariaDBParser.AlterByOptimizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByRebuildPartition.
    def visitAlterByRebuildPartition(self, ctx:MariaDBParser.AlterByRebuildPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByRepairPartition.
    def visitAlterByRepairPartition(self, ctx:MariaDBParser.AlterByRepairPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByRemovePartitioning.
    def visitAlterByRemovePartitioning(self, ctx:MariaDBParser.AlterByRemovePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterByUpgradePartitioning.
    def visitAlterByUpgradePartitioning(self, ctx:MariaDBParser.AlterByUpgradePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropDatabase.
    def visitDropDatabase(self, ctx:MariaDBParser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropEvent.
    def visitDropEvent(self, ctx:MariaDBParser.DropEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropIndex.
    def visitDropIndex(self, ctx:MariaDBParser.DropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropLogfileGroup.
    def visitDropLogfileGroup(self, ctx:MariaDBParser.DropLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropProcedure.
    def visitDropProcedure(self, ctx:MariaDBParser.DropProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropFunction.
    def visitDropFunction(self, ctx:MariaDBParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropServer.
    def visitDropServer(self, ctx:MariaDBParser.DropServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropTable.
    def visitDropTable(self, ctx:MariaDBParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropTablespace.
    def visitDropTablespace(self, ctx:MariaDBParser.DropTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropTrigger.
    def visitDropTrigger(self, ctx:MariaDBParser.DropTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropView.
    def visitDropView(self, ctx:MariaDBParser.DropViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropRole.
    def visitDropRole(self, ctx:MariaDBParser.DropRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setRole.
    def visitSetRole(self, ctx:MariaDBParser.SetRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropSequence.
    def visitDropSequence(self, ctx:MariaDBParser.DropSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#renameTable.
    def visitRenameTable(self, ctx:MariaDBParser.RenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#renameTableClause.
    def visitRenameTableClause(self, ctx:MariaDBParser.RenameTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#truncateTable.
    def visitTruncateTable(self, ctx:MariaDBParser.TruncateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#callStatement.
    def visitCallStatement(self, ctx:MariaDBParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#deleteStatement.
    def visitDeleteStatement(self, ctx:MariaDBParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#doStatement.
    def visitDoStatement(self, ctx:MariaDBParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerStatement.
    def visitHandlerStatement(self, ctx:MariaDBParser.HandlerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#insertStatement.
    def visitInsertStatement(self, ctx:MariaDBParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#loadDataStatement.
    def visitLoadDataStatement(self, ctx:MariaDBParser.LoadDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#loadXmlStatement.
    def visitLoadXmlStatement(self, ctx:MariaDBParser.LoadXmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#replaceStatement.
    def visitReplaceStatement(self, ctx:MariaDBParser.ReplaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleSelect.
    def visitSimpleSelect(self, ctx:MariaDBParser.SimpleSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#parenthesisSelect.
    def visitParenthesisSelect(self, ctx:MariaDBParser.ParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#unionSelect.
    def visitUnionSelect(self, ctx:MariaDBParser.UnionSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#unionParenthesisSelect.
    def visitUnionParenthesisSelect(self, ctx:MariaDBParser.UnionParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#withLateralStatement.
    def visitWithLateralStatement(self, ctx:MariaDBParser.WithLateralStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#updateStatement.
    def visitUpdateStatement(self, ctx:MariaDBParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#valuesStatement.
    def visitValuesStatement(self, ctx:MariaDBParser.ValuesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#insertStatementValue.
    def visitInsertStatementValue(self, ctx:MariaDBParser.InsertStatementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#updatedElement.
    def visitUpdatedElement(self, ctx:MariaDBParser.UpdatedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#assignmentField.
    def visitAssignmentField(self, ctx:MariaDBParser.AssignmentFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lockClause.
    def visitLockClause(self, ctx:MariaDBParser.LockClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#singleDeleteStatement.
    def visitSingleDeleteStatement(self, ctx:MariaDBParser.SingleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#multipleDeleteStatement.
    def visitMultipleDeleteStatement(self, ctx:MariaDBParser.MultipleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerOpenStatement.
    def visitHandlerOpenStatement(self, ctx:MariaDBParser.HandlerOpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerReadIndexStatement.
    def visitHandlerReadIndexStatement(self, ctx:MariaDBParser.HandlerReadIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerReadStatement.
    def visitHandlerReadStatement(self, ctx:MariaDBParser.HandlerReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerCloseStatement.
    def visitHandlerCloseStatement(self, ctx:MariaDBParser.HandlerCloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#singleUpdateStatement.
    def visitSingleUpdateStatement(self, ctx:MariaDBParser.SingleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#multipleUpdateStatement.
    def visitMultipleUpdateStatement(self, ctx:MariaDBParser.MultipleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#orderByClause.
    def visitOrderByClause(self, ctx:MariaDBParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#orderByExpression.
    def visitOrderByExpression(self, ctx:MariaDBParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableSources.
    def visitTableSources(self, ctx:MariaDBParser.TableSourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableSourceBase.
    def visitTableSourceBase(self, ctx:MariaDBParser.TableSourceBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableSourceNested.
    def visitTableSourceNested(self, ctx:MariaDBParser.TableSourceNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableJson.
    def visitTableJson(self, ctx:MariaDBParser.TableJsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#atomTableItem.
    def visitAtomTableItem(self, ctx:MariaDBParser.AtomTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#subqueryTableItem.
    def visitSubqueryTableItem(self, ctx:MariaDBParser.SubqueryTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableSourcesItem.
    def visitTableSourcesItem(self, ctx:MariaDBParser.TableSourcesItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#indexHint.
    def visitIndexHint(self, ctx:MariaDBParser.IndexHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#indexHintType.
    def visitIndexHintType(self, ctx:MariaDBParser.IndexHintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#innerJoin.
    def visitInnerJoin(self, ctx:MariaDBParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#straightJoin.
    def visitStraightJoin(self, ctx:MariaDBParser.StraightJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#outerJoin.
    def visitOuterJoin(self, ctx:MariaDBParser.OuterJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#naturalJoin.
    def visitNaturalJoin(self, ctx:MariaDBParser.NaturalJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#queryExpression.
    def visitQueryExpression(self, ctx:MariaDBParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#queryExpressionNointo.
    def visitQueryExpressionNointo(self, ctx:MariaDBParser.QueryExpressionNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#querySpecification.
    def visitQuerySpecification(self, ctx:MariaDBParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#querySpecificationNointo.
    def visitQuerySpecificationNointo(self, ctx:MariaDBParser.QuerySpecificationNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#unionParenthesis.
    def visitUnionParenthesis(self, ctx:MariaDBParser.UnionParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#unionStatement.
    def visitUnionStatement(self, ctx:MariaDBParser.UnionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lateralStatement.
    def visitLateralStatement(self, ctx:MariaDBParser.LateralStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonTable.
    def visitJsonTable(self, ctx:MariaDBParser.JsonTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonColumnList.
    def visitJsonColumnList(self, ctx:MariaDBParser.JsonColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonColumn.
    def visitJsonColumn(self, ctx:MariaDBParser.JsonColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonOnEmpty.
    def visitJsonOnEmpty(self, ctx:MariaDBParser.JsonOnEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonOnError.
    def visitJsonOnError(self, ctx:MariaDBParser.JsonOnErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectSpec.
    def visitSelectSpec(self, ctx:MariaDBParser.SelectSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectElements.
    def visitSelectElements(self, ctx:MariaDBParser.SelectElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectStarElement.
    def visitSelectStarElement(self, ctx:MariaDBParser.SelectStarElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx:MariaDBParser.SelectColumnElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectFunctionElement.
    def visitSelectFunctionElement(self, ctx:MariaDBParser.SelectFunctionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectExpressionElement.
    def visitSelectExpressionElement(self, ctx:MariaDBParser.SelectExpressionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectIntoVariables.
    def visitSelectIntoVariables(self, ctx:MariaDBParser.SelectIntoVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectIntoDumpFile.
    def visitSelectIntoDumpFile(self, ctx:MariaDBParser.SelectIntoDumpFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectIntoTextFile.
    def visitSelectIntoTextFile(self, ctx:MariaDBParser.SelectIntoTextFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectFieldsInto.
    def visitSelectFieldsInto(self, ctx:MariaDBParser.SelectFieldsIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#selectLinesInto.
    def visitSelectLinesInto(self, ctx:MariaDBParser.SelectLinesIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#fromClause.
    def visitFromClause(self, ctx:MariaDBParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#groupByClause.
    def visitGroupByClause(self, ctx:MariaDBParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#havingClause.
    def visitHavingClause(self, ctx:MariaDBParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#windowClause.
    def visitWindowClause(self, ctx:MariaDBParser.WindowClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#groupByItem.
    def visitGroupByItem(self, ctx:MariaDBParser.GroupByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#limitClause.
    def visitLimitClause(self, ctx:MariaDBParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#limitClauseAtom.
    def visitLimitClauseAtom(self, ctx:MariaDBParser.LimitClauseAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#startTransaction.
    def visitStartTransaction(self, ctx:MariaDBParser.StartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#beginWork.
    def visitBeginWork(self, ctx:MariaDBParser.BeginWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#commitWork.
    def visitCommitWork(self, ctx:MariaDBParser.CommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#rollbackWork.
    def visitRollbackWork(self, ctx:MariaDBParser.RollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#savepointStatement.
    def visitSavepointStatement(self, ctx:MariaDBParser.SavepointStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#rollbackStatement.
    def visitRollbackStatement(self, ctx:MariaDBParser.RollbackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#releaseStatement.
    def visitReleaseStatement(self, ctx:MariaDBParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lockTables.
    def visitLockTables(self, ctx:MariaDBParser.LockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#unlockTables.
    def visitUnlockTables(self, ctx:MariaDBParser.UnlockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setAutocommitStatement.
    def visitSetAutocommitStatement(self, ctx:MariaDBParser.SetAutocommitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setTransactionStatement.
    def visitSetTransactionStatement(self, ctx:MariaDBParser.SetTransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#transactionMode.
    def visitTransactionMode(self, ctx:MariaDBParser.TransactionModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lockTableElement.
    def visitLockTableElement(self, ctx:MariaDBParser.LockTableElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lockAction.
    def visitLockAction(self, ctx:MariaDBParser.LockActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#transactionOption.
    def visitTransactionOption(self, ctx:MariaDBParser.TransactionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#transactionLevel.
    def visitTransactionLevel(self, ctx:MariaDBParser.TransactionLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#changeMaster.
    def visitChangeMaster(self, ctx:MariaDBParser.ChangeMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#changeReplicationFilter.
    def visitChangeReplicationFilter(self, ctx:MariaDBParser.ChangeReplicationFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#purgeBinaryLogs.
    def visitPurgeBinaryLogs(self, ctx:MariaDBParser.PurgeBinaryLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#resetMaster.
    def visitResetMaster(self, ctx:MariaDBParser.ResetMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#resetSlave.
    def visitResetSlave(self, ctx:MariaDBParser.ResetSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#startSlave.
    def visitStartSlave(self, ctx:MariaDBParser.StartSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#stopSlave.
    def visitStopSlave(self, ctx:MariaDBParser.StopSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#startGroupReplication.
    def visitStartGroupReplication(self, ctx:MariaDBParser.StartGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#stopGroupReplication.
    def visitStopGroupReplication(self, ctx:MariaDBParser.StopGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#masterStringOption.
    def visitMasterStringOption(self, ctx:MariaDBParser.MasterStringOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#masterDecimalOption.
    def visitMasterDecimalOption(self, ctx:MariaDBParser.MasterDecimalOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#masterBoolOption.
    def visitMasterBoolOption(self, ctx:MariaDBParser.MasterBoolOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#masterRealOption.
    def visitMasterRealOption(self, ctx:MariaDBParser.MasterRealOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#masterUidListOption.
    def visitMasterUidListOption(self, ctx:MariaDBParser.MasterUidListOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#stringMasterOption.
    def visitStringMasterOption(self, ctx:MariaDBParser.StringMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#decimalMasterOption.
    def visitDecimalMasterOption(self, ctx:MariaDBParser.DecimalMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#boolMasterOption.
    def visitBoolMasterOption(self, ctx:MariaDBParser.BoolMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#channelOption.
    def visitChannelOption(self, ctx:MariaDBParser.ChannelOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#doDbReplication.
    def visitDoDbReplication(self, ctx:MariaDBParser.DoDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#ignoreDbReplication.
    def visitIgnoreDbReplication(self, ctx:MariaDBParser.IgnoreDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#doTableReplication.
    def visitDoTableReplication(self, ctx:MariaDBParser.DoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#ignoreTableReplication.
    def visitIgnoreTableReplication(self, ctx:MariaDBParser.IgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#wildDoTableReplication.
    def visitWildDoTableReplication(self, ctx:MariaDBParser.WildDoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#wildIgnoreTableReplication.
    def visitWildIgnoreTableReplication(self, ctx:MariaDBParser.WildIgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#rewriteDbReplication.
    def visitRewriteDbReplication(self, ctx:MariaDBParser.RewriteDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tablePair.
    def visitTablePair(self, ctx:MariaDBParser.TablePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#threadType.
    def visitThreadType(self, ctx:MariaDBParser.ThreadTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#gtidsUntilOption.
    def visitGtidsUntilOption(self, ctx:MariaDBParser.GtidsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#masterLogUntilOption.
    def visitMasterLogUntilOption(self, ctx:MariaDBParser.MasterLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#relayLogUntilOption.
    def visitRelayLogUntilOption(self, ctx:MariaDBParser.RelayLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#sqlGapsUntilOption.
    def visitSqlGapsUntilOption(self, ctx:MariaDBParser.SqlGapsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#userConnectionOption.
    def visitUserConnectionOption(self, ctx:MariaDBParser.UserConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#passwordConnectionOption.
    def visitPasswordConnectionOption(self, ctx:MariaDBParser.PasswordConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#defaultAuthConnectionOption.
    def visitDefaultAuthConnectionOption(self, ctx:MariaDBParser.DefaultAuthConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#pluginDirConnectionOption.
    def visitPluginDirConnectionOption(self, ctx:MariaDBParser.PluginDirConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#gtuidSet.
    def visitGtuidSet(self, ctx:MariaDBParser.GtuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xaStartTransaction.
    def visitXaStartTransaction(self, ctx:MariaDBParser.XaStartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xaEndTransaction.
    def visitXaEndTransaction(self, ctx:MariaDBParser.XaEndTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xaPrepareStatement.
    def visitXaPrepareStatement(self, ctx:MariaDBParser.XaPrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xaCommitWork.
    def visitXaCommitWork(self, ctx:MariaDBParser.XaCommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xaRollbackWork.
    def visitXaRollbackWork(self, ctx:MariaDBParser.XaRollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xaRecoverWork.
    def visitXaRecoverWork(self, ctx:MariaDBParser.XaRecoverWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#prepareStatement.
    def visitPrepareStatement(self, ctx:MariaDBParser.PrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#executeStatement.
    def visitExecuteStatement(self, ctx:MariaDBParser.ExecuteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#deallocatePrepare.
    def visitDeallocatePrepare(self, ctx:MariaDBParser.DeallocatePrepareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#routineBody.
    def visitRoutineBody(self, ctx:MariaDBParser.RoutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#blockStatement.
    def visitBlockStatement(self, ctx:MariaDBParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#caseStatement.
    def visitCaseStatement(self, ctx:MariaDBParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#ifStatement.
    def visitIfStatement(self, ctx:MariaDBParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#iterateStatement.
    def visitIterateStatement(self, ctx:MariaDBParser.IterateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#leaveStatement.
    def visitLeaveStatement(self, ctx:MariaDBParser.LeaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#loopStatement.
    def visitLoopStatement(self, ctx:MariaDBParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#repeatStatement.
    def visitRepeatStatement(self, ctx:MariaDBParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#returnStatement.
    def visitReturnStatement(self, ctx:MariaDBParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#whileStatement.
    def visitWhileStatement(self, ctx:MariaDBParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#CloseCursor.
    def visitCloseCursor(self, ctx:MariaDBParser.CloseCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#FetchCursor.
    def visitFetchCursor(self, ctx:MariaDBParser.FetchCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#OpenCursor.
    def visitOpenCursor(self, ctx:MariaDBParser.OpenCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#declareVariable.
    def visitDeclareVariable(self, ctx:MariaDBParser.DeclareVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#declareCondition.
    def visitDeclareCondition(self, ctx:MariaDBParser.DeclareConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#declareCursor.
    def visitDeclareCursor(self, ctx:MariaDBParser.DeclareCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#declareHandler.
    def visitDeclareHandler(self, ctx:MariaDBParser.DeclareHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerConditionCode.
    def visitHandlerConditionCode(self, ctx:MariaDBParser.HandlerConditionCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerConditionState.
    def visitHandlerConditionState(self, ctx:MariaDBParser.HandlerConditionStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerConditionName.
    def visitHandlerConditionName(self, ctx:MariaDBParser.HandlerConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerConditionWarning.
    def visitHandlerConditionWarning(self, ctx:MariaDBParser.HandlerConditionWarningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerConditionNotfound.
    def visitHandlerConditionNotfound(self, ctx:MariaDBParser.HandlerConditionNotfoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#handlerConditionException.
    def visitHandlerConditionException(self, ctx:MariaDBParser.HandlerConditionExceptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#procedureSqlStatement.
    def visitProcedureSqlStatement(self, ctx:MariaDBParser.ProcedureSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#caseAlternative.
    def visitCaseAlternative(self, ctx:MariaDBParser.CaseAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#elifAlternative.
    def visitElifAlternative(self, ctx:MariaDBParser.ElifAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterUserMysqlV56.
    def visitAlterUserMysqlV56(self, ctx:MariaDBParser.AlterUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#alterUserMysqlV80.
    def visitAlterUserMysqlV80(self, ctx:MariaDBParser.AlterUserMysqlV80Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createUserMysqlV56.
    def visitCreateUserMysqlV56(self, ctx:MariaDBParser.CreateUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createUserMysqlV80.
    def visitCreateUserMysqlV80(self, ctx:MariaDBParser.CreateUserMysqlV80Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dropUser.
    def visitDropUser(self, ctx:MariaDBParser.DropUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#grantStatement.
    def visitGrantStatement(self, ctx:MariaDBParser.GrantStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#roleOption.
    def visitRoleOption(self, ctx:MariaDBParser.RoleOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#grantProxy.
    def visitGrantProxy(self, ctx:MariaDBParser.GrantProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#renameUser.
    def visitRenameUser(self, ctx:MariaDBParser.RenameUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#detailRevoke.
    def visitDetailRevoke(self, ctx:MariaDBParser.DetailRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#shortRevoke.
    def visitShortRevoke(self, ctx:MariaDBParser.ShortRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#roleRevoke.
    def visitRoleRevoke(self, ctx:MariaDBParser.RoleRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#revokeProxy.
    def visitRevokeProxy(self, ctx:MariaDBParser.RevokeProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setPasswordStatement.
    def visitSetPasswordStatement(self, ctx:MariaDBParser.SetPasswordStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#userSpecification.
    def visitUserSpecification(self, ctx:MariaDBParser.UserSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#hashAuthOption.
    def visitHashAuthOption(self, ctx:MariaDBParser.HashAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#stringAuthOption.
    def visitStringAuthOption(self, ctx:MariaDBParser.StringAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#moduleAuthOption.
    def visitModuleAuthOption(self, ctx:MariaDBParser.ModuleAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleAuthOption.
    def visitSimpleAuthOption(self, ctx:MariaDBParser.SimpleAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#module.
    def visitModule(self, ctx:MariaDBParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#passwordModuleOption.
    def visitPasswordModuleOption(self, ctx:MariaDBParser.PasswordModuleOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tlsOption.
    def visitTlsOption(self, ctx:MariaDBParser.TlsOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#userResourceOption.
    def visitUserResourceOption(self, ctx:MariaDBParser.UserResourceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#userPasswordOption.
    def visitUserPasswordOption(self, ctx:MariaDBParser.UserPasswordOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#userLockOption.
    def visitUserLockOption(self, ctx:MariaDBParser.UserLockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#privelegeClause.
    def visitPrivelegeClause(self, ctx:MariaDBParser.PrivelegeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#privilege.
    def visitPrivilege(self, ctx:MariaDBParser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#currentSchemaPriviLevel.
    def visitCurrentSchemaPriviLevel(self, ctx:MariaDBParser.CurrentSchemaPriviLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#globalPrivLevel.
    def visitGlobalPrivLevel(self, ctx:MariaDBParser.GlobalPrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#definiteSchemaPrivLevel.
    def visitDefiniteSchemaPrivLevel(self, ctx:MariaDBParser.DefiniteSchemaPrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#definiteFullTablePrivLevel.
    def visitDefiniteFullTablePrivLevel(self, ctx:MariaDBParser.DefiniteFullTablePrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#definiteFullTablePrivLevel2.
    def visitDefiniteFullTablePrivLevel2(self, ctx:MariaDBParser.DefiniteFullTablePrivLevel2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#definiteTablePrivLevel.
    def visitDefiniteTablePrivLevel(self, ctx:MariaDBParser.DefiniteTablePrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#renameUserClause.
    def visitRenameUserClause(self, ctx:MariaDBParser.RenameUserClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#analyzeTable.
    def visitAnalyzeTable(self, ctx:MariaDBParser.AnalyzeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#checkTable.
    def visitCheckTable(self, ctx:MariaDBParser.CheckTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#checksumTable.
    def visitChecksumTable(self, ctx:MariaDBParser.ChecksumTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#optimizeTable.
    def visitOptimizeTable(self, ctx:MariaDBParser.OptimizeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#repairTable.
    def visitRepairTable(self, ctx:MariaDBParser.RepairTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#checkTableOption.
    def visitCheckTableOption(self, ctx:MariaDBParser.CheckTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#createUdfunction.
    def visitCreateUdfunction(self, ctx:MariaDBParser.CreateUdfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#installPlugin.
    def visitInstallPlugin(self, ctx:MariaDBParser.InstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#uninstallPlugin.
    def visitUninstallPlugin(self, ctx:MariaDBParser.UninstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setVariable.
    def visitSetVariable(self, ctx:MariaDBParser.SetVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setCharset.
    def visitSetCharset(self, ctx:MariaDBParser.SetCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setNames.
    def visitSetNames(self, ctx:MariaDBParser.SetNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setPassword.
    def visitSetPassword(self, ctx:MariaDBParser.SetPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setTransaction.
    def visitSetTransaction(self, ctx:MariaDBParser.SetTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setAutocommit.
    def visitSetAutocommit(self, ctx:MariaDBParser.SetAutocommitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#setNewValueInsideTrigger.
    def visitSetNewValueInsideTrigger(self, ctx:MariaDBParser.SetNewValueInsideTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showMasterLogs.
    def visitShowMasterLogs(self, ctx:MariaDBParser.ShowMasterLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showBinLogEvents.
    def visitShowBinLogEvents(self, ctx:MariaDBParser.ShowBinLogEventsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showRelayLogEvents.
    def visitShowRelayLogEvents(self, ctx:MariaDBParser.ShowRelayLogEventsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showObjectFilter.
    def visitShowObjectFilter(self, ctx:MariaDBParser.ShowObjectFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showColumns.
    def visitShowColumns(self, ctx:MariaDBParser.ShowColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showCreateDb.
    def visitShowCreateDb(self, ctx:MariaDBParser.ShowCreateDbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showCreateFullIdObject.
    def visitShowCreateFullIdObject(self, ctx:MariaDBParser.ShowCreateFullIdObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showCreatePackage.
    def visitShowCreatePackage(self, ctx:MariaDBParser.ShowCreatePackageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showCreateUser.
    def visitShowCreateUser(self, ctx:MariaDBParser.ShowCreateUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showEngine.
    def visitShowEngine(self, ctx:MariaDBParser.ShowEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showInnoDBStatus.
    def visitShowInnoDBStatus(self, ctx:MariaDBParser.ShowInnoDBStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showGlobalInfo.
    def visitShowGlobalInfo(self, ctx:MariaDBParser.ShowGlobalInfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showErrors.
    def visitShowErrors(self, ctx:MariaDBParser.ShowErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showCountErrors.
    def visitShowCountErrors(self, ctx:MariaDBParser.ShowCountErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showSchemaFilter.
    def visitShowSchemaFilter(self, ctx:MariaDBParser.ShowSchemaFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showRoutine.
    def visitShowRoutine(self, ctx:MariaDBParser.ShowRoutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showGrants.
    def visitShowGrants(self, ctx:MariaDBParser.ShowGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showIndexes.
    def visitShowIndexes(self, ctx:MariaDBParser.ShowIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showOpenTables.
    def visitShowOpenTables(self, ctx:MariaDBParser.ShowOpenTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showProfile.
    def visitShowProfile(self, ctx:MariaDBParser.ShowProfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showSlaveStatus.
    def visitShowSlaveStatus(self, ctx:MariaDBParser.ShowSlaveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showUserstatPlugin.
    def visitShowUserstatPlugin(self, ctx:MariaDBParser.ShowUserstatPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showExplain.
    def visitShowExplain(self, ctx:MariaDBParser.ShowExplainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showPackageStatus.
    def visitShowPackageStatus(self, ctx:MariaDBParser.ShowPackageStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#explainForConnection.
    def visitExplainForConnection(self, ctx:MariaDBParser.ExplainForConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#variableClause.
    def visitVariableClause(self, ctx:MariaDBParser.VariableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showCommonEntity.
    def visitShowCommonEntity(self, ctx:MariaDBParser.ShowCommonEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showFilter.
    def visitShowFilter(self, ctx:MariaDBParser.ShowFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showGlobalInfoClause.
    def visitShowGlobalInfoClause(self, ctx:MariaDBParser.ShowGlobalInfoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showSchemaEntity.
    def visitShowSchemaEntity(self, ctx:MariaDBParser.ShowSchemaEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#showProfileType.
    def visitShowProfileType(self, ctx:MariaDBParser.ShowProfileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#binlogStatement.
    def visitBinlogStatement(self, ctx:MariaDBParser.BinlogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#cacheIndexStatement.
    def visitCacheIndexStatement(self, ctx:MariaDBParser.CacheIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#flushStatement.
    def visitFlushStatement(self, ctx:MariaDBParser.FlushStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#killStatement.
    def visitKillStatement(self, ctx:MariaDBParser.KillStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#loadIndexIntoCache.
    def visitLoadIndexIntoCache(self, ctx:MariaDBParser.LoadIndexIntoCacheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#resetStatement.
    def visitResetStatement(self, ctx:MariaDBParser.ResetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#shutdownStatement.
    def visitShutdownStatement(self, ctx:MariaDBParser.ShutdownStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableIndexes.
    def visitTableIndexes(self, ctx:MariaDBParser.TableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleFlushOption.
    def visitSimpleFlushOption(self, ctx:MariaDBParser.SimpleFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#channelFlushOption.
    def visitChannelFlushOption(self, ctx:MariaDBParser.ChannelFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableFlushOption.
    def visitTableFlushOption(self, ctx:MariaDBParser.TableFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#flushTableOption.
    def visitFlushTableOption(self, ctx:MariaDBParser.FlushTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#loadedTableIndexes.
    def visitLoadedTableIndexes(self, ctx:MariaDBParser.LoadedTableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleDescribeStatement.
    def visitSimpleDescribeStatement(self, ctx:MariaDBParser.SimpleDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#fullDescribeStatement.
    def visitFullDescribeStatement(self, ctx:MariaDBParser.FullDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#formatJsonStatement.
    def visitFormatJsonStatement(self, ctx:MariaDBParser.FormatJsonStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#helpStatement.
    def visitHelpStatement(self, ctx:MariaDBParser.HelpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#useStatement.
    def visitUseStatement(self, ctx:MariaDBParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#signalStatement.
    def visitSignalStatement(self, ctx:MariaDBParser.SignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#resignalStatement.
    def visitResignalStatement(self, ctx:MariaDBParser.ResignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#signalConditionInformation.
    def visitSignalConditionInformation(self, ctx:MariaDBParser.SignalConditionInformationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#diagnosticsStatement.
    def visitDiagnosticsStatement(self, ctx:MariaDBParser.DiagnosticsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#diagnosticsConditionInformationName.
    def visitDiagnosticsConditionInformationName(self, ctx:MariaDBParser.DiagnosticsConditionInformationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#describeStatements.
    def visitDescribeStatements(self, ctx:MariaDBParser.DescribeStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#describeConnection.
    def visitDescribeConnection(self, ctx:MariaDBParser.DescribeConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#fullId.
    def visitFullId(self, ctx:MariaDBParser.FullIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tableName.
    def visitTableName(self, ctx:MariaDBParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#roleName.
    def visitRoleName(self, ctx:MariaDBParser.RoleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#fullColumnName.
    def visitFullColumnName(self, ctx:MariaDBParser.FullColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#indexColumnName.
    def visitIndexColumnName(self, ctx:MariaDBParser.IndexColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleUserName.
    def visitSimpleUserName(self, ctx:MariaDBParser.SimpleUserNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#hostName.
    def visitHostName(self, ctx:MariaDBParser.HostNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#userName.
    def visitUserName(self, ctx:MariaDBParser.UserNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#mysqlVariable.
    def visitMysqlVariable(self, ctx:MariaDBParser.MysqlVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#charsetName.
    def visitCharsetName(self, ctx:MariaDBParser.CharsetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#collationName.
    def visitCollationName(self, ctx:MariaDBParser.CollationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#engineName.
    def visitEngineName(self, ctx:MariaDBParser.EngineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#engineNameBase.
    def visitEngineNameBase(self, ctx:MariaDBParser.EngineNameBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#encryptedLiteral.
    def visitEncryptedLiteral(self, ctx:MariaDBParser.EncryptedLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#uuidSet.
    def visitUuidSet(self, ctx:MariaDBParser.UuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xid.
    def visitXid(self, ctx:MariaDBParser.XidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#xuidStringId.
    def visitXuidStringId(self, ctx:MariaDBParser.XuidStringIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#authPlugin.
    def visitAuthPlugin(self, ctx:MariaDBParser.AuthPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#uid.
    def visitUid(self, ctx:MariaDBParser.UidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleId.
    def visitSimpleId(self, ctx:MariaDBParser.SimpleIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dottedId.
    def visitDottedId(self, ctx:MariaDBParser.DottedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:MariaDBParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#fileSizeLiteral.
    def visitFileSizeLiteral(self, ctx:MariaDBParser.FileSizeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#stringLiteral.
    def visitStringLiteral(self, ctx:MariaDBParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:MariaDBParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#booleanValue.
    def visitBooleanValue(self, ctx:MariaDBParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#hexadecimalLiteral.
    def visitHexadecimalLiteral(self, ctx:MariaDBParser.HexadecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nullNotnull.
    def visitNullNotnull(self, ctx:MariaDBParser.NullNotnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#constant.
    def visitConstant(self, ctx:MariaDBParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#stringDataType.
    def visitStringDataType(self, ctx:MariaDBParser.StringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nationalStringDataType.
    def visitNationalStringDataType(self, ctx:MariaDBParser.NationalStringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nationalVaryingStringDataType.
    def visitNationalVaryingStringDataType(self, ctx:MariaDBParser.NationalVaryingStringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dimensionDataType.
    def visitDimensionDataType(self, ctx:MariaDBParser.DimensionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleDataType.
    def visitSimpleDataType(self, ctx:MariaDBParser.SimpleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#collectionDataType.
    def visitCollectionDataType(self, ctx:MariaDBParser.CollectionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#spatialDataType.
    def visitSpatialDataType(self, ctx:MariaDBParser.SpatialDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#longVarcharDataType.
    def visitLongVarcharDataType(self, ctx:MariaDBParser.LongVarcharDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#longVarbinaryDataType.
    def visitLongVarbinaryDataType(self, ctx:MariaDBParser.LongVarbinaryDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#uuidDataType.
    def visitUuidDataType(self, ctx:MariaDBParser.UuidDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#collectionOptions.
    def visitCollectionOptions(self, ctx:MariaDBParser.CollectionOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#collectionOption.
    def visitCollectionOption(self, ctx:MariaDBParser.CollectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#convertedDataType.
    def visitConvertedDataType(self, ctx:MariaDBParser.ConvertedDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lengthOneDimension.
    def visitLengthOneDimension(self, ctx:MariaDBParser.LengthOneDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lengthTwoDimension.
    def visitLengthTwoDimension(self, ctx:MariaDBParser.LengthTwoDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lengthTwoOptionalDimension.
    def visitLengthTwoOptionalDimension(self, ctx:MariaDBParser.LengthTwoOptionalDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#uidList.
    def visitUidList(self, ctx:MariaDBParser.UidListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#tables.
    def visitTables(self, ctx:MariaDBParser.TablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#indexColumnNames.
    def visitIndexColumnNames(self, ctx:MariaDBParser.IndexColumnNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#expressions.
    def visitExpressions(self, ctx:MariaDBParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#expressionsWithDefaults.
    def visitExpressionsWithDefaults(self, ctx:MariaDBParser.ExpressionsWithDefaultsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#constants.
    def visitConstants(self, ctx:MariaDBParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleStrings.
    def visitSimpleStrings(self, ctx:MariaDBParser.SimpleStringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#userVariables.
    def visitUserVariables(self, ctx:MariaDBParser.UserVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#defaultValue.
    def visitDefaultValue(self, ctx:MariaDBParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#currentTimestamp.
    def visitCurrentTimestamp(self, ctx:MariaDBParser.CurrentTimestampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#expressionOrDefault.
    def visitExpressionOrDefault(self, ctx:MariaDBParser.ExpressionOrDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#ifExists.
    def visitIfExists(self, ctx:MariaDBParser.IfExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#ifNotExists.
    def visitIfNotExists(self, ctx:MariaDBParser.IfNotExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#orReplace.
    def visitOrReplace(self, ctx:MariaDBParser.OrReplaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#waitNowaitClause.
    def visitWaitNowaitClause(self, ctx:MariaDBParser.WaitNowaitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#lockOption.
    def visitLockOption(self, ctx:MariaDBParser.LockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx:MariaDBParser.SpecificFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#aggregateFunctionCall.
    def visitAggregateFunctionCall(self, ctx:MariaDBParser.AggregateFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nonAggregateFunctionCall.
    def visitNonAggregateFunctionCall(self, ctx:MariaDBParser.NonAggregateFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx:MariaDBParser.ScalarFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#udfFunctionCall.
    def visitUdfFunctionCall(self, ctx:MariaDBParser.UdfFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#passwordFunctionCall.
    def visitPasswordFunctionCall(self, ctx:MariaDBParser.PasswordFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#simpleFunctionCall.
    def visitSimpleFunctionCall(self, ctx:MariaDBParser.SimpleFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dataTypeFunctionCall.
    def visitDataTypeFunctionCall(self, ctx:MariaDBParser.DataTypeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#valuesFunctionCall.
    def visitValuesFunctionCall(self, ctx:MariaDBParser.ValuesFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#caseExpressionFunctionCall.
    def visitCaseExpressionFunctionCall(self, ctx:MariaDBParser.CaseExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#caseFunctionCall.
    def visitCaseFunctionCall(self, ctx:MariaDBParser.CaseFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#charFunctionCall.
    def visitCharFunctionCall(self, ctx:MariaDBParser.CharFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#positionFunctionCall.
    def visitPositionFunctionCall(self, ctx:MariaDBParser.PositionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#substrFunctionCall.
    def visitSubstrFunctionCall(self, ctx:MariaDBParser.SubstrFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#trimFunctionCall.
    def visitTrimFunctionCall(self, ctx:MariaDBParser.TrimFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#weightFunctionCall.
    def visitWeightFunctionCall(self, ctx:MariaDBParser.WeightFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#extractFunctionCall.
    def visitExtractFunctionCall(self, ctx:MariaDBParser.ExtractFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#getFormatFunctionCall.
    def visitGetFormatFunctionCall(self, ctx:MariaDBParser.GetFormatFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonValueFunctionCall.
    def visitJsonValueFunctionCall(self, ctx:MariaDBParser.JsonValueFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#caseFuncAlternative.
    def visitCaseFuncAlternative(self, ctx:MariaDBParser.CaseFuncAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#levelWeightList.
    def visitLevelWeightList(self, ctx:MariaDBParser.LevelWeightListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#levelWeightRange.
    def visitLevelWeightRange(self, ctx:MariaDBParser.LevelWeightRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#levelInWeightListElement.
    def visitLevelInWeightListElement(self, ctx:MariaDBParser.LevelInWeightListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#aggregateWindowedFunction.
    def visitAggregateWindowedFunction(self, ctx:MariaDBParser.AggregateWindowedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nonAggregateWindowedFunction.
    def visitNonAggregateWindowedFunction(self, ctx:MariaDBParser.NonAggregateWindowedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#overClause.
    def visitOverClause(self, ctx:MariaDBParser.OverClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#windowSpec.
    def visitWindowSpec(self, ctx:MariaDBParser.WindowSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#windowName.
    def visitWindowName(self, ctx:MariaDBParser.WindowNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#frameClause.
    def visitFrameClause(self, ctx:MariaDBParser.FrameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#frameUnits.
    def visitFrameUnits(self, ctx:MariaDBParser.FrameUnitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#frameExtent.
    def visitFrameExtent(self, ctx:MariaDBParser.FrameExtentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#frameBetween.
    def visitFrameBetween(self, ctx:MariaDBParser.FrameBetweenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#frameRange.
    def visitFrameRange(self, ctx:MariaDBParser.FrameRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#partitionClause.
    def visitPartitionClause(self, ctx:MariaDBParser.PartitionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#scalarFunctionName.
    def visitScalarFunctionName(self, ctx:MariaDBParser.ScalarFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#passwordFunctionClause.
    def visitPasswordFunctionClause(self, ctx:MariaDBParser.PasswordFunctionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#functionArgs.
    def visitFunctionArgs(self, ctx:MariaDBParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#functionArg.
    def visitFunctionArg(self, ctx:MariaDBParser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#isExpression.
    def visitIsExpression(self, ctx:MariaDBParser.IsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#notExpression.
    def visitNotExpression(self, ctx:MariaDBParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MariaDBParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#predicateExpression.
    def visitPredicateExpression(self, ctx:MariaDBParser.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#soundsLikePredicate.
    def visitSoundsLikePredicate(self, ctx:MariaDBParser.SoundsLikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:MariaDBParser.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#subqueryComparisonPredicate.
    def visitSubqueryComparisonPredicate(self, ctx:MariaDBParser.SubqueryComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonMemberOfPredicate.
    def visitJsonMemberOfPredicate(self, ctx:MariaDBParser.JsonMemberOfPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#binaryComparisonPredicate.
    def visitBinaryComparisonPredicate(self, ctx:MariaDBParser.BinaryComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#inPredicate.
    def visitInPredicate(self, ctx:MariaDBParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx:MariaDBParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#isNullPredicate.
    def visitIsNullPredicate(self, ctx:MariaDBParser.IsNullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#likePredicate.
    def visitLikePredicate(self, ctx:MariaDBParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#regexpPredicate.
    def visitRegexpPredicate(self, ctx:MariaDBParser.RegexpPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx:MariaDBParser.UnaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#collateExpressionAtom.
    def visitCollateExpressionAtom(self, ctx:MariaDBParser.CollateExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#variableAssignExpressionAtom.
    def visitVariableAssignExpressionAtom(self, ctx:MariaDBParser.VariableAssignExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#mysqlVariableExpressionAtom.
    def visitMysqlVariableExpressionAtom(self, ctx:MariaDBParser.MysqlVariableExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nestedExpressionAtom.
    def visitNestedExpressionAtom(self, ctx:MariaDBParser.NestedExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#nestedRowExpressionAtom.
    def visitNestedRowExpressionAtom(self, ctx:MariaDBParser.NestedRowExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#mathExpressionAtom.
    def visitMathExpressionAtom(self, ctx:MariaDBParser.MathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#existsExpressionAtom.
    def visitExistsExpressionAtom(self, ctx:MariaDBParser.ExistsExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#intervalExpressionAtom.
    def visitIntervalExpressionAtom(self, ctx:MariaDBParser.IntervalExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonExpressionAtom.
    def visitJsonExpressionAtom(self, ctx:MariaDBParser.JsonExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#subqueryExpressionAtom.
    def visitSubqueryExpressionAtom(self, ctx:MariaDBParser.SubqueryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx:MariaDBParser.ConstantExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx:MariaDBParser.FunctionCallExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#binaryExpressionAtom.
    def visitBinaryExpressionAtom(self, ctx:MariaDBParser.BinaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#fullColumnNameExpressionAtom.
    def visitFullColumnNameExpressionAtom(self, ctx:MariaDBParser.FullColumnNameExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#bitExpressionAtom.
    def visitBitExpressionAtom(self, ctx:MariaDBParser.BitExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#unaryOperator.
    def visitUnaryOperator(self, ctx:MariaDBParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:MariaDBParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#logicalOperator.
    def visitLogicalOperator(self, ctx:MariaDBParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#bitOperator.
    def visitBitOperator(self, ctx:MariaDBParser.BitOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#mathOperator.
    def visitMathOperator(self, ctx:MariaDBParser.MathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#jsonOperator.
    def visitJsonOperator(self, ctx:MariaDBParser.JsonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#charsetNameBase.
    def visitCharsetNameBase(self, ctx:MariaDBParser.CharsetNameBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#transactionLevelBase.
    def visitTransactionLevelBase(self, ctx:MariaDBParser.TransactionLevelBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#privilegesBase.
    def visitPrivilegesBase(self, ctx:MariaDBParser.PrivilegesBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#intervalTypeBase.
    def visitIntervalTypeBase(self, ctx:MariaDBParser.IntervalTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#dataTypeBase.
    def visitDataTypeBase(self, ctx:MariaDBParser.DataTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#keywordsCanBeId.
    def visitKeywordsCanBeId(self, ctx:MariaDBParser.KeywordsCanBeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MariaDBParser#functionNameBase.
    def visitFunctionNameBase(self, ctx:MariaDBParser.FunctionNameBaseContext):
        return self.visitChildren(ctx)



del MariaDBParser