// Generated from /Users/david/My Drive/PhD/Output/low-resource-coverage/languages/plantuml/parser/PlantUML.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PlantUMLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, ASSOCIATION_NAME_FULL=37, 
		FLOAT_LITERAL=38, STRING1_LITERAL=39, STRING2_LITERAL=40, NULL_LITERAL=41, 
		NEWLINE=42, IDENT=43, NUMBER=44, COMMENT=45, WS=46;
	public static final int
		RULE_uml = 0, RULE_class_dclr = 1, RULE_enum_dclr = 2, RULE_class_type = 3, 
		RULE_extension_dclr = 4, RULE_attribute = 5, RULE_attributeAssignation = 6, 
		RULE_method = 7, RULE_association_left = 8, RULE_association_right = 9, 
		RULE_association_dclr = 10, RULE_association_detail = 11, RULE_association_name = 12, 
		RULE_stereotype = 13, RULE_cardinality = 14, RULE_cardinality_component = 15, 
		RULE_associative_class_dclr = 16, RULE_visibility = 17, RULE_value = 18, 
		RULE_ident = 19, RULE_modifiers = 20, RULE_type_dclr = 21, RULE_item_list = 22, 
		RULE_relation = 23, RULE_stringExpression = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"uml", "class_dclr", "enum_dclr", "class_type", "extension_dclr", "attribute", 
			"attributeAssignation", "method", "association_left", "association_right", 
			"association_dclr", "association_detail", "association_name", "stereotype", 
			"cardinality", "cardinality_component", "associative_class_dclr", "visibility", 
			"value", "ident", "modifiers", "type_dclr", "item_list", "relation", 
			"stringExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'@startuml'", "'@enduml'", "'class'", "'{'", "'}'", "'enum'", 
			"'abstract'", "'interface'", "'extends'", "':'", "'='", "'('", "')'", 
			"'\"'", "'>'", "'<'", "'<<'", "'>>'", "'..'", "'many'", "'*'", "'one'", 
			"','", "'.'", "'+'", "'-'", "'#'", "'{static}'", "'{abstract}'", "'List'", 
			"'['", "']'", "'o'", "'<|'", "'|>'", "'^'", null, null, null, null, "'null'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "ASSOCIATION_NAME_FULL", "FLOAT_LITERAL", "STRING1_LITERAL", "STRING2_LITERAL", 
			"NULL_LITERAL", "NEWLINE", "IDENT", "NUMBER", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PlantUML.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PlantUMLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UmlContext extends ParserRuleContext {
		public List<Class_dclrContext> class_dclr() {
			return getRuleContexts(Class_dclrContext.class);
		}
		public Class_dclrContext class_dclr(int i) {
			return getRuleContext(Class_dclrContext.class,i);
		}
		public List<Enum_dclrContext> enum_dclr() {
			return getRuleContexts(Enum_dclrContext.class);
		}
		public Enum_dclrContext enum_dclr(int i) {
			return getRuleContext(Enum_dclrContext.class,i);
		}
		public List<Association_dclrContext> association_dclr() {
			return getRuleContexts(Association_dclrContext.class);
		}
		public Association_dclrContext association_dclr(int i) {
			return getRuleContext(Association_dclrContext.class,i);
		}
		public List<Associative_class_dclrContext> associative_class_dclr() {
			return getRuleContexts(Associative_class_dclrContext.class);
		}
		public Associative_class_dclrContext associative_class_dclr(int i) {
			return getRuleContext(Associative_class_dclrContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(PlantUMLParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(PlantUMLParser.NEWLINE, i);
		}
		public List<TerminalNode> COMMENT() { return getTokens(PlantUMLParser.COMMENT); }
		public TerminalNode COMMENT(int i) {
			return getToken(PlantUMLParser.COMMENT, i);
		}
		public UmlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_uml; }
	}

	public final UmlContext uml() throws RecognitionException {
		UmlContext _localctx = new UmlContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_uml);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE || _la==COMMENT) {
				{
				{
				setState(50);
				_la = _input.LA(1);
				if ( !(_la==NEWLINE || _la==COMMENT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(56);
			match(T__0);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 48378511626696L) != 0)) {
				{
				setState(63);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__2:
				case T__6:
				case T__7:
					{
					setState(57);
					class_dclr();
					}
					break;
				case T__5:
					{
					setState(58);
					enum_dclr();
					}
					break;
				case IDENT:
					{
					setState(59);
					association_dclr();
					}
					break;
				case T__11:
					{
					setState(60);
					associative_class_dclr();
					}
					break;
				case NEWLINE:
					{
					setState(61);
					match(NEWLINE);
					}
					break;
				case COMMENT:
					{
					setState(62);
					match(COMMENT);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(68);
			match(T__1);
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE || _la==COMMENT) {
				{
				{
				setState(69);
				_la = _input.LA(1);
				if ( !(_la==NEWLINE || _la==COMMENT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(74);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Class_dclrContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Class_typeContext class_type() {
			return getRuleContext(Class_typeContext.class,0);
		}
		public StereotypeContext stereotype() {
			return getRuleContext(StereotypeContext.class,0);
		}
		public Extension_dclrContext extension_dclr() {
			return getRuleContext(Extension_dclrContext.class,0);
		}
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public List<MethodContext> method() {
			return getRuleContexts(MethodContext.class);
		}
		public MethodContext method(int i) {
			return getRuleContext(MethodContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(PlantUMLParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(PlantUMLParser.NEWLINE, i);
		}
		public Class_dclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_dclr; }
	}

	public final Class_dclrContext class_dclr() throws RecognitionException {
		Class_dclrContext _localctx = new Class_dclrContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class_dclr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6 || _la==T__7) {
				{
				setState(75);
				class_type();
				}
			}

			setState(78);
			match(T__2);
			setState(79);
			ident();
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(80);
				stereotype();
				}
			}

			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__8) {
				{
				setState(83);
				extension_dclr();
				}
			}

			setState(96);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(86);
				match(T__3);
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 13196253462528L) != 0)) {
					{
					setState(90);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						setState(87);
						attribute();
						}
						break;
					case 2:
						{
						setState(88);
						method();
						}
						break;
					case 3:
						{
						setState(89);
						match(NEWLINE);
						}
						break;
					}
					}
					setState(94);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(95);
				match(T__4);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Enum_dclrContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public StereotypeContext stereotype() {
			return getRuleContext(StereotypeContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(PlantUMLParser.NEWLINE, 0); }
		public Item_listContext item_list() {
			return getRuleContext(Item_listContext.class,0);
		}
		public Enum_dclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enum_dclr; }
	}

	public final Enum_dclrContext enum_dclr() throws RecognitionException {
		Enum_dclrContext _localctx = new Enum_dclrContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_enum_dclr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(T__5);
			setState(99);
			ident();
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(100);
				stereotype();
				}
			}

			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(103);
				match(T__3);
				setState(104);
				match(NEWLINE);
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==IDENT) {
					{
					setState(105);
					item_list();
					}
				}

				setState(108);
				match(T__4);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Class_typeContext extends ParserRuleContext {
		public Class_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_type; }
	}

	public final Class_typeContext class_type() throws RecognitionException {
		Class_typeContext _localctx = new Class_typeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_class_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_la = _input.LA(1);
			if ( !(_la==T__6 || _la==T__7) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Extension_dclrContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Extension_dclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extension_dclr; }
	}

	public final Extension_dclrContext extension_dclr() throws RecognitionException {
		Extension_dclrContext _localctx = new Extension_dclrContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_extension_dclr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(T__8);
			setState(114);
			ident();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttributeContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(PlantUMLParser.NEWLINE, 0); }
		public VisibilityContext visibility() {
			return getRuleContext(VisibilityContext.class,0);
		}
		public ModifiersContext modifiers() {
			return getRuleContext(ModifiersContext.class,0);
		}
		public List<Type_dclrContext> type_dclr() {
			return getRuleContexts(Type_dclrContext.class);
		}
		public Type_dclrContext type_dclr(int i) {
			return getRuleContext(Type_dclrContext.class,i);
		}
		public AttributeAssignationContext attributeAssignation() {
			return getRuleContext(AttributeAssignationContext.class,0);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attribute);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 234881024L) != 0)) {
				{
				setState(116);
				visibility();
				}
			}

			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__27 || _la==T__28) {
				{
				setState(119);
				modifiers();
				}
			}

			setState(123);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(122);
				type_dclr();
				}
				break;
			}
			setState(125);
			ident();
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(126);
				match(T__9);
				setState(127);
				type_dclr();
				}
			}

			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(130);
				attributeAssignation();
				}
			}

			setState(133);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttributeAssignationContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public AttributeAssignationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeAssignation; }
	}

	public final AttributeAssignationContext attributeAssignation() throws RecognitionException {
		AttributeAssignationContext _localctx = new AttributeAssignationContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_attributeAssignation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(T__10);
			setState(136);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(PlantUMLParser.NEWLINE, 0); }
		public VisibilityContext visibility() {
			return getRuleContext(VisibilityContext.class,0);
		}
		public ModifiersContext modifiers() {
			return getRuleContext(ModifiersContext.class,0);
		}
		public List<Type_dclrContext> type_dclr() {
			return getRuleContexts(Type_dclrContext.class);
		}
		public Type_dclrContext type_dclr(int i) {
			return getRuleContext(Type_dclrContext.class,i);
		}
		public MethodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method; }
	}

	public final MethodContext method() throws RecognitionException {
		MethodContext _localctx = new MethodContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_method);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 234881024L) != 0)) {
				{
				setState(138);
				visibility();
				}
			}

			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__27 || _la==T__28) {
				{
				setState(141);
				modifiers();
				}
			}

			setState(145);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(144);
				type_dclr();
				}
				break;
			}
			setState(147);
			ident();
			setState(148);
			match(T__11);
			setState(152);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(149);
					matchWildcard();
					}
					} 
				}
				setState(154);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			setState(155);
			match(T__12);
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(156);
				match(T__9);
				setState(157);
				type_dclr();
				}
			}

			setState(160);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Association_leftContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Association_detailContext association_detail() {
			return getRuleContext(Association_detailContext.class,0);
		}
		public Association_leftContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_association_left; }
	}

	public final Association_leftContext association_left() throws RecognitionException {
		Association_leftContext _localctx = new Association_leftContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_association_left);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			ident();
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(163);
				association_detail();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Association_rightContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Association_detailContext association_detail() {
			return getRuleContext(Association_detailContext.class,0);
		}
		public Association_rightContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_association_right; }
	}

	public final Association_rightContext association_right() throws RecognitionException {
		Association_rightContext _localctx = new Association_rightContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_association_right);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(166);
				association_detail();
				}
			}

			setState(169);
			ident();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Association_dclrContext extends ParserRuleContext {
		public Association_leftContext left;
		public Association_rightContext right;
		public RelationContext relation() {
			return getRuleContext(RelationContext.class,0);
		}
		public Association_leftContext association_left() {
			return getRuleContext(Association_leftContext.class,0);
		}
		public Association_rightContext association_right() {
			return getRuleContext(Association_rightContext.class,0);
		}
		public Association_nameContext association_name() {
			return getRuleContext(Association_nameContext.class,0);
		}
		public Association_dclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_association_dclr; }
	}

	public final Association_dclrContext association_dclr() throws RecognitionException {
		Association_dclrContext _localctx = new Association_dclrContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_association_dclr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			((Association_dclrContext)_localctx).left = association_left();
			setState(172);
			relation();
			setState(173);
			((Association_dclrContext)_localctx).right = association_right();
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(174);
				association_name();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Association_detailContext extends ParserRuleContext {
		public CardinalityContext cardinality() {
			return getRuleContext(CardinalityContext.class,0);
		}
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Association_detailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_association_detail; }
	}

	public final Association_detailContext association_detail() throws RecognitionException {
		Association_detailContext _localctx = new Association_detailContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_association_detail);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(T__13);
			setState(186);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				{
				setState(179);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==IDENT) {
					{
					setState(178);
					ident();
					}
				}

				setState(181);
				cardinality();
				}
				break;
			case 2:
				{
				setState(183);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17592193384448L) != 0)) {
					{
					setState(182);
					cardinality();
					}
				}

				setState(185);
				ident();
				}
				break;
			}
			setState(188);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Association_nameContext extends ParserRuleContext {
		public TerminalNode ASSOCIATION_NAME_FULL() { return getToken(PlantUMLParser.ASSOCIATION_NAME_FULL, 0); }
		public Association_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_association_name; }
	}

	public final Association_nameContext association_name() throws RecognitionException {
		Association_nameContext _localctx = new Association_nameContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_association_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			match(T__9);
			setState(191);
			match(ASSOCIATION_NAME_FULL);
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14 || _la==T__15) {
				{
				setState(192);
				_la = _input.LA(1);
				if ( !(_la==T__14 || _la==T__15) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StereotypeContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public StereotypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stereotype; }
	}

	public final StereotypeContext stereotype() throws RecognitionException {
		StereotypeContext _localctx = new StereotypeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_stereotype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(T__16);
			setState(196);
			ident();
			setState(197);
			match(T__17);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CardinalityContext extends ParserRuleContext {
		public Token two_dots;
		public List<Cardinality_componentContext> cardinality_component() {
			return getRuleContexts(Cardinality_componentContext.class);
		}
		public Cardinality_componentContext cardinality_component(int i) {
			return getRuleContext(Cardinality_componentContext.class,i);
		}
		public CardinalityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cardinality; }
	}

	public final CardinalityContext cardinality() throws RecognitionException {
		CardinalityContext _localctx = new CardinalityContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_cardinality);
		try {
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(199);
				cardinality_component();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(200);
				cardinality_component();
				setState(201);
				((CardinalityContext)_localctx).two_dots = match(T__18);
				setState(202);
				cardinality_component();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Cardinality_componentContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(PlantUMLParser.NUMBER, 0); }
		public Cardinality_componentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cardinality_component; }
	}

	public final Cardinality_componentContext cardinality_component() throws RecognitionException {
		Cardinality_componentContext _localctx = new Cardinality_componentContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_cardinality_component);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17592193384448L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Associative_class_dclrContext extends ParserRuleContext {
		public IdentContext left;
		public IdentContext right;
		public IdentContext target;
		public List<IdentContext> ident() {
			return getRuleContexts(IdentContext.class);
		}
		public IdentContext ident(int i) {
			return getRuleContext(IdentContext.class,i);
		}
		public Associative_class_dclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_associative_class_dclr; }
	}

	public final Associative_class_dclrContext associative_class_dclr() throws RecognitionException {
		Associative_class_dclrContext _localctx = new Associative_class_dclrContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_associative_class_dclr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(T__11);
			setState(209);
			((Associative_class_dclrContext)_localctx).left = ident();
			setState(210);
			match(T__22);
			setState(211);
			((Associative_class_dclrContext)_localctx).right = ident();
			setState(212);
			match(T__12);
			setState(213);
			_la = _input.LA(1);
			if ( !(_la==T__18 || _la==T__23) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(214);
			((Associative_class_dclrContext)_localctx).target = ident();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VisibilityContext extends ParserRuleContext {
		public VisibilityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_visibility; }
	}

	public final VisibilityContext visibility() throws RecognitionException {
		VisibilityContext _localctx = new VisibilityContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_visibility);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 234881024L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(PlantUMLParser.IDENT, 0); }
		public TerminalNode NUMBER() { return getToken(PlantUMLParser.NUMBER, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(PlantUMLParser.FLOAT_LITERAL, 0); }
		public TerminalNode NULL_LITERAL() { return getToken(PlantUMLParser.NULL_LITERAL, 0); }
		public StringExpressionContext stringExpression() {
			return getRuleContext(StringExpressionContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_value);
		try {
			setState(223);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(218);
				match(IDENT);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(219);
				match(NUMBER);
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(220);
				match(FLOAT_LITERAL);
				}
				break;
			case NULL_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(221);
				match(NULL_LITERAL);
				}
				break;
			case STRING1_LITERAL:
			case STRING2_LITERAL:
				enterOuterAlt(_localctx, 5);
				{
				setState(222);
				stringExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(PlantUMLParser.IDENT, 0); }
		public IdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ident; }
	}

	public final IdentContext ident() throws RecognitionException {
		IdentContext _localctx = new IdentContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_ident);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(IDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModifiersContext extends ParserRuleContext {
		public Token static_mod;
		public Token abstract_mod;
		public ModifiersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modifiers; }
	}

	public final ModifiersContext modifiers() throws RecognitionException {
		ModifiersContext _localctx = new ModifiersContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_modifiers);
		try {
			setState(229);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__27:
				enterOuterAlt(_localctx, 1);
				{
				setState(227);
				((ModifiersContext)_localctx).static_mod = match(T__27);
				}
				break;
			case T__28:
				enterOuterAlt(_localctx, 2);
				{
				setState(228);
				((ModifiersContext)_localctx).abstract_mod = match(T__28);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type_dclrContext extends ParserRuleContext {
		public Type_dclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_dclr; }
	 
		public Type_dclrContext() { }
		public void copyFrom(Type_dclrContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class List_typeContext extends Type_dclrContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public List_typeContext(Type_dclrContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Simple_typeContext extends Type_dclrContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Simple_typeContext(Type_dclrContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Array_typeContext extends Type_dclrContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Array_typeContext(Type_dclrContext ctx) { copyFrom(ctx); }
	}

	public final Type_dclrContext type_dclr() throws RecognitionException {
		Type_dclrContext _localctx = new Type_dclrContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_type_dclr);
		try {
			int _alt;
			setState(247);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				_localctx = new List_typeContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(231);
				match(T__29);
				setState(232);
				match(T__15);
				setState(233);
				ident();
				setState(234);
				match(T__14);
				}
				break;
			case 2:
				_localctx = new Array_typeContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				ident();
				setState(237);
				match(T__30);
				setState(241);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(238);
						matchWildcard();
						}
						} 
					}
					setState(243);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
				}
				setState(244);
				match(T__31);
				}
				break;
			case 3:
				_localctx = new Simple_typeContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(246);
				ident();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Item_listContext extends ParserRuleContext {
		public List<IdentContext> ident() {
			return getRuleContexts(IdentContext.class);
		}
		public IdentContext ident(int i) {
			return getRuleContext(IdentContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(PlantUMLParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(PlantUMLParser.NEWLINE, i);
		}
		public Item_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_list; }
	}

	public final Item_listContext item_list() throws RecognitionException {
		Item_listContext _localctx = new Item_listContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_item_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(249);
				ident();
				setState(250);
				match(NEWLINE);
				}
				}
				setState(254); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==IDENT );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelationContext extends ParserRuleContext {
		public RelationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relation; }
	 
		public RelationContext() { }
		public void copyFrom(RelationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Left_composes_rightContext extends RelationContext {
		public Left_composes_rightContext(RelationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Right_extends_leftContext extends RelationContext {
		public Right_extends_leftContext(RelationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Right_composes_leftContext extends RelationContext {
		public Right_composes_leftContext(RelationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Right_aggregates_leftContext extends RelationContext {
		public Right_aggregates_leftContext(RelationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Left_extends_rightContext extends RelationContext {
		public Left_extends_rightContext(RelationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Left_aggregates_rightContext extends RelationContext {
		public Left_aggregates_rightContext(RelationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssociationContext extends RelationContext {
		public AssociationContext(RelationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IgnoreContext extends RelationContext {
		public IgnoreContext(RelationContext ctx) { copyFrom(ctx); }
	}

	public final RelationContext relation() throws RecognitionException {
		RelationContext _localctx = new RelationContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_relation);
		int _la;
		try {
			setState(386);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				_localctx = new AssociationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(257);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14 || _la==T__15) {
					{
					setState(256);
					_la = _input.LA(1);
					if ( !(_la==T__14 || _la==T__15) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(259);
				match(T__25);
				setState(263);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__25) {
					{
					{
					setState(260);
					match(T__25);
					}
					}
					setState(265);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(267);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14 || _la==T__15) {
					{
					setState(266);
					_la = _input.LA(1);
					if ( !(_la==T__14 || _la==T__15) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				}
				break;
			case 2:
				_localctx = new IgnoreContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14 || _la==T__15) {
					{
					setState(269);
					_la = _input.LA(1);
					if ( !(_la==T__14 || _la==T__15) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(272);
				match(T__23);
				setState(276);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__23) {
					{
					{
					setState(273);
					match(T__23);
					}
					}
					setState(278);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(280);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14 || _la==T__15) {
					{
					setState(279);
					_la = _input.LA(1);
					if ( !(_la==T__14 || _la==T__15) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				}
				break;
			case 3:
				_localctx = new Right_composes_leftContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(283);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15) {
					{
					setState(282);
					match(T__15);
					}
				}

				setState(286); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(285);
					match(T__25);
					}
					}
					setState(288); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__25 );
				setState(290);
				match(T__20);
				}
				break;
			case 4:
				_localctx = new Left_composes_rightContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(291);
				match(T__20);
				setState(293); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(292);
					match(T__25);
					}
					}
					setState(295); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__25 );
				setState(298);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14) {
					{
					setState(297);
					match(T__14);
					}
				}

				}
				break;
			case 5:
				_localctx = new Right_aggregates_leftContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(301);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15) {
					{
					setState(300);
					match(T__15);
					}
				}

				setState(304); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(303);
					match(T__25);
					}
					}
					setState(306); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__25 );
				setState(308);
				match(T__32);
				}
				break;
			case 6:
				_localctx = new Left_aggregates_rightContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(309);
				match(T__32);
				setState(311); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(310);
					match(T__25);
					}
					}
					setState(313); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__25 );
				setState(316);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14) {
					{
					setState(315);
					match(T__14);
					}
				}

				}
				break;
			case 7:
				_localctx = new IgnoreContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(332);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__33:
					{
					{
					setState(318);
					match(T__33);
					setState(322);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__23) {
						{
						{
						setState(319);
						match(T__23);
						}
						}
						setState(324);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					}
					break;
				case T__23:
				case T__34:
					{
					{
					setState(328);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__23) {
						{
						{
						setState(325);
						match(T__23);
						}
						}
						setState(330);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(331);
					match(T__34);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 8:
				_localctx = new Right_extends_leftContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(334);
				_la = _input.LA(1);
				if ( !(_la==T__33 || _la==T__35) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(336); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(335);
					match(T__25);
					}
					}
					setState(338); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__25 );
				setState(341);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14) {
					{
					setState(340);
					match(T__14);
					}
				}

				}
				break;
			case 9:
				_localctx = new IgnoreContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(343);
				_la = _input.LA(1);
				if ( !(_la==T__33 || _la==T__35) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(345); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(344);
					match(T__23);
					}
					}
					setState(347); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__23 );
				setState(350);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14) {
					{
					setState(349);
					match(T__14);
					}
				}

				}
				break;
			case 10:
				_localctx = new Left_extends_rightContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(353);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15) {
					{
					setState(352);
					match(T__15);
					}
				}

				setState(356); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(355);
					match(T__25);
					}
					}
					setState(358); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__25 );
				setState(360);
				_la = _input.LA(1);
				if ( !(_la==T__34 || _la==T__35) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 11:
				_localctx = new IgnoreContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(362);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15) {
					{
					setState(361);
					match(T__15);
					}
				}

				setState(365); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(364);
					match(T__23);
					}
					}
					setState(367); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__23 );
				setState(369);
				_la = _input.LA(1);
				if ( !(_la==T__34 || _la==T__35) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 12:
				_localctx = new IgnoreContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(384);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__33:
					{
					{
					setState(370);
					match(T__33);
					setState(374);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__23) {
						{
						{
						setState(371);
						match(T__23);
						}
						}
						setState(376);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					}
					break;
				case T__23:
				case T__34:
					{
					{
					setState(380);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__23) {
						{
						{
						setState(377);
						match(T__23);
						}
						}
						setState(382);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(383);
					match(T__34);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringExpressionContext extends ParserRuleContext {
		public TerminalNode STRING1_LITERAL() { return getToken(PlantUMLParser.STRING1_LITERAL, 0); }
		public TerminalNode STRING2_LITERAL() { return getToken(PlantUMLParser.STRING2_LITERAL, 0); }
		public StringExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringExpression; }
	}

	public final StringExpressionContext stringExpression() throws RecognitionException {
		StringExpressionContext _localctx = new StringExpressionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_stringExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(388);
			_la = _input.LA(1);
			if ( !(_la==STRING1_LITERAL || _la==STRING2_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001.\u0187\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0001\u0000\u0005\u00004\b\u0000\n\u0000\f\u00007\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0005\u0000@\b\u0000\n\u0000\f\u0000C\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0005\u0000G\b\u0000\n\u0000\f\u0000J\t\u0000\u0001\u0001\u0003\u0001"+
		"M\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001R\b\u0001\u0001"+
		"\u0001\u0003\u0001U\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0005\u0001[\b\u0001\n\u0001\f\u0001^\t\u0001\u0001\u0001\u0003"+
		"\u0001a\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002f\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002k\b\u0002\u0001\u0002"+
		"\u0003\u0002n\b\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0003\u0005v\b\u0005\u0001\u0005\u0003\u0005"+
		"y\b\u0005\u0001\u0005\u0003\u0005|\b\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0003\u0005\u0081\b\u0005\u0001\u0005\u0003\u0005\u0084\b\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0003\u0007\u008c\b\u0007\u0001\u0007\u0003\u0007\u008f\b\u0007\u0001"+
		"\u0007\u0003\u0007\u0092\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005"+
		"\u0007\u0097\b\u0007\n\u0007\f\u0007\u009a\t\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007\u009f\b\u0007\u0001\u0007\u0001\u0007\u0001\b"+
		"\u0001\b\u0003\b\u00a5\b\b\u0001\t\u0003\t\u00a8\b\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0003\n\u00b0\b\n\u0001\u000b\u0001\u000b\u0003"+
		"\u000b\u00b4\b\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u00b8\b\u000b"+
		"\u0001\u000b\u0003\u000b\u00bb\b\u000b\u0001\u000b\u0001\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0003\f\u00c2\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00cd"+
		"\b\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003"+
		"\u0012\u00e0\b\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u00e6\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0005\u0015\u00f0\b\u0015\n"+
		"\u0015\f\u0015\u00f3\t\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003"+
		"\u0015\u00f8\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0004\u0016\u00fd"+
		"\b\u0016\u000b\u0016\f\u0016\u00fe\u0001\u0017\u0003\u0017\u0102\b\u0017"+
		"\u0001\u0017\u0001\u0017\u0005\u0017\u0106\b\u0017\n\u0017\f\u0017\u0109"+
		"\t\u0017\u0001\u0017\u0003\u0017\u010c\b\u0017\u0001\u0017\u0003\u0017"+
		"\u010f\b\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u0113\b\u0017\n\u0017"+
		"\f\u0017\u0116\t\u0017\u0001\u0017\u0003\u0017\u0119\b\u0017\u0001\u0017"+
		"\u0003\u0017\u011c\b\u0017\u0001\u0017\u0004\u0017\u011f\b\u0017\u000b"+
		"\u0017\f\u0017\u0120\u0001\u0017\u0001\u0017\u0001\u0017\u0004\u0017\u0126"+
		"\b\u0017\u000b\u0017\f\u0017\u0127\u0001\u0017\u0003\u0017\u012b\b\u0017"+
		"\u0001\u0017\u0003\u0017\u012e\b\u0017\u0001\u0017\u0004\u0017\u0131\b"+
		"\u0017\u000b\u0017\f\u0017\u0132\u0001\u0017\u0001\u0017\u0001\u0017\u0004"+
		"\u0017\u0138\b\u0017\u000b\u0017\f\u0017\u0139\u0001\u0017\u0003\u0017"+
		"\u013d\b\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u0141\b\u0017\n\u0017"+
		"\f\u0017\u0144\t\u0017\u0001\u0017\u0005\u0017\u0147\b\u0017\n\u0017\f"+
		"\u0017\u014a\t\u0017\u0001\u0017\u0003\u0017\u014d\b\u0017\u0001\u0017"+
		"\u0001\u0017\u0004\u0017\u0151\b\u0017\u000b\u0017\f\u0017\u0152\u0001"+
		"\u0017\u0003\u0017\u0156\b\u0017\u0001\u0017\u0001\u0017\u0004\u0017\u015a"+
		"\b\u0017\u000b\u0017\f\u0017\u015b\u0001\u0017\u0003\u0017\u015f\b\u0017"+
		"\u0001\u0017\u0003\u0017\u0162\b\u0017\u0001\u0017\u0004\u0017\u0165\b"+
		"\u0017\u000b\u0017\f\u0017\u0166\u0001\u0017\u0001\u0017\u0003\u0017\u016b"+
		"\b\u0017\u0001\u0017\u0004\u0017\u016e\b\u0017\u000b\u0017\f\u0017\u016f"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u0175\b\u0017\n\u0017"+
		"\f\u0017\u0178\t\u0017\u0001\u0017\u0005\u0017\u017b\b\u0017\n\u0017\f"+
		"\u0017\u017e\t\u0017\u0001\u0017\u0003\u0017\u0181\b\u0017\u0003\u0017"+
		"\u0183\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0002\u0098\u00f1\u0000"+
		"\u0019\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(*,.0\u0000\t\u0002\u0000**--\u0001\u0000\u0007"+
		"\b\u0001\u0000\u000f\u0010\u0002\u0000\u0014\u0016,,\u0002\u0000\u0013"+
		"\u0013\u0018\u0018\u0001\u0000\u0019\u001b\u0002\u0000\"\"$$\u0001\u0000"+
		"#$\u0001\u0000\'(\u01c1\u00005\u0001\u0000\u0000\u0000\u0002L\u0001\u0000"+
		"\u0000\u0000\u0004b\u0001\u0000\u0000\u0000\u0006o\u0001\u0000\u0000\u0000"+
		"\bq\u0001\u0000\u0000\u0000\nu\u0001\u0000\u0000\u0000\f\u0087\u0001\u0000"+
		"\u0000\u0000\u000e\u008b\u0001\u0000\u0000\u0000\u0010\u00a2\u0001\u0000"+
		"\u0000\u0000\u0012\u00a7\u0001\u0000\u0000\u0000\u0014\u00ab\u0001\u0000"+
		"\u0000\u0000\u0016\u00b1\u0001\u0000\u0000\u0000\u0018\u00be\u0001\u0000"+
		"\u0000\u0000\u001a\u00c3\u0001\u0000\u0000\u0000\u001c\u00cc\u0001\u0000"+
		"\u0000\u0000\u001e\u00ce\u0001\u0000\u0000\u0000 \u00d0\u0001\u0000\u0000"+
		"\u0000\"\u00d8\u0001\u0000\u0000\u0000$\u00df\u0001\u0000\u0000\u0000"+
		"&\u00e1\u0001\u0000\u0000\u0000(\u00e5\u0001\u0000\u0000\u0000*\u00f7"+
		"\u0001\u0000\u0000\u0000,\u00fc\u0001\u0000\u0000\u0000.\u0182\u0001\u0000"+
		"\u0000\u00000\u0184\u0001\u0000\u0000\u000024\u0007\u0000\u0000\u0000"+
		"32\u0001\u0000\u0000\u000047\u0001\u0000\u0000\u000053\u0001\u0000\u0000"+
		"\u000056\u0001\u0000\u0000\u000068\u0001\u0000\u0000\u000075\u0001\u0000"+
		"\u0000\u00008A\u0005\u0001\u0000\u00009@\u0003\u0002\u0001\u0000:@\u0003"+
		"\u0004\u0002\u0000;@\u0003\u0014\n\u0000<@\u0003 \u0010\u0000=@\u0005"+
		"*\u0000\u0000>@\u0005-\u0000\u0000?9\u0001\u0000\u0000\u0000?:\u0001\u0000"+
		"\u0000\u0000?;\u0001\u0000\u0000\u0000?<\u0001\u0000\u0000\u0000?=\u0001"+
		"\u0000\u0000\u0000?>\u0001\u0000\u0000\u0000@C\u0001\u0000\u0000\u0000"+
		"A?\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000BD\u0001\u0000\u0000"+
		"\u0000CA\u0001\u0000\u0000\u0000DH\u0005\u0002\u0000\u0000EG\u0007\u0000"+
		"\u0000\u0000FE\u0001\u0000\u0000\u0000GJ\u0001\u0000\u0000\u0000HF\u0001"+
		"\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000I\u0001\u0001\u0000\u0000"+
		"\u0000JH\u0001\u0000\u0000\u0000KM\u0003\u0006\u0003\u0000LK\u0001\u0000"+
		"\u0000\u0000LM\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NO\u0005"+
		"\u0003\u0000\u0000OQ\u0003&\u0013\u0000PR\u0003\u001a\r\u0000QP\u0001"+
		"\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RT\u0001\u0000\u0000\u0000"+
		"SU\u0003\b\u0004\u0000TS\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000"+
		"U`\u0001\u0000\u0000\u0000V\\\u0005\u0004\u0000\u0000W[\u0003\n\u0005"+
		"\u0000X[\u0003\u000e\u0007\u0000Y[\u0005*\u0000\u0000ZW\u0001\u0000\u0000"+
		"\u0000ZX\u0001\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[^\u0001\u0000"+
		"\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]_\u0001"+
		"\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000_a\u0005\u0005\u0000\u0000"+
		"`V\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000a\u0003\u0001\u0000"+
		"\u0000\u0000bc\u0005\u0006\u0000\u0000ce\u0003&\u0013\u0000df\u0003\u001a"+
		"\r\u0000ed\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fm\u0001\u0000"+
		"\u0000\u0000gh\u0005\u0004\u0000\u0000hj\u0005*\u0000\u0000ik\u0003,\u0016"+
		"\u0000ji\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000kl\u0001\u0000"+
		"\u0000\u0000ln\u0005\u0005\u0000\u0000mg\u0001\u0000\u0000\u0000mn\u0001"+
		"\u0000\u0000\u0000n\u0005\u0001\u0000\u0000\u0000op\u0007\u0001\u0000"+
		"\u0000p\u0007\u0001\u0000\u0000\u0000qr\u0005\t\u0000\u0000rs\u0003&\u0013"+
		"\u0000s\t\u0001\u0000\u0000\u0000tv\u0003\"\u0011\u0000ut\u0001\u0000"+
		"\u0000\u0000uv\u0001\u0000\u0000\u0000vx\u0001\u0000\u0000\u0000wy\u0003"+
		"(\u0014\u0000xw\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000y{\u0001"+
		"\u0000\u0000\u0000z|\u0003*\u0015\u0000{z\u0001\u0000\u0000\u0000{|\u0001"+
		"\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}\u0080\u0003&\u0013\u0000"+
		"~\u007f\u0005\n\u0000\u0000\u007f\u0081\u0003*\u0015\u0000\u0080~\u0001"+
		"\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0083\u0001"+
		"\u0000\u0000\u0000\u0082\u0084\u0003\f\u0006\u0000\u0083\u0082\u0001\u0000"+
		"\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000"+
		"\u0000\u0000\u0085\u0086\u0005*\u0000\u0000\u0086\u000b\u0001\u0000\u0000"+
		"\u0000\u0087\u0088\u0005\u000b\u0000\u0000\u0088\u0089\u0003$\u0012\u0000"+
		"\u0089\r\u0001\u0000\u0000\u0000\u008a\u008c\u0003\"\u0011\u0000\u008b"+
		"\u008a\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c"+
		"\u008e\u0001\u0000\u0000\u0000\u008d\u008f\u0003(\u0014\u0000\u008e\u008d"+
		"\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0091"+
		"\u0001\u0000\u0000\u0000\u0090\u0092\u0003*\u0015\u0000\u0091\u0090\u0001"+
		"\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0093\u0001"+
		"\u0000\u0000\u0000\u0093\u0094\u0003&\u0013\u0000\u0094\u0098\u0005\f"+
		"\u0000\u0000\u0095\u0097\t\u0000\u0000\u0000\u0096\u0095\u0001\u0000\u0000"+
		"\u0000\u0097\u009a\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000"+
		"\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0099\u009b\u0001\u0000\u0000"+
		"\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009b\u009e\u0005\r\u0000\u0000"+
		"\u009c\u009d\u0005\n\u0000\u0000\u009d\u009f\u0003*\u0015\u0000\u009e"+
		"\u009c\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000\u009f"+
		"\u00a0\u0001\u0000\u0000\u0000\u00a0\u00a1\u0005*\u0000\u0000\u00a1\u000f"+
		"\u0001\u0000\u0000\u0000\u00a2\u00a4\u0003&\u0013\u0000\u00a3\u00a5\u0003"+
		"\u0016\u000b\u0000\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a5\u0011\u0001\u0000\u0000\u0000\u00a6\u00a8\u0003"+
		"\u0016\u000b\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001"+
		"\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9\u00aa\u0003"+
		"&\u0013\u0000\u00aa\u0013\u0001\u0000\u0000\u0000\u00ab\u00ac\u0003\u0010"+
		"\b\u0000\u00ac\u00ad\u0003.\u0017\u0000\u00ad\u00af\u0003\u0012\t\u0000"+
		"\u00ae\u00b0\u0003\u0018\f\u0000\u00af\u00ae\u0001\u0000\u0000\u0000\u00af"+
		"\u00b0\u0001\u0000\u0000\u0000\u00b0\u0015\u0001\u0000\u0000\u0000\u00b1"+
		"\u00ba\u0005\u000e\u0000\u0000\u00b2\u00b4\u0003&\u0013\u0000\u00b3\u00b2"+
		"\u0001\u0000\u0000\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4\u00b5"+
		"\u0001\u0000\u0000\u0000\u00b5\u00bb\u0003\u001c\u000e\u0000\u00b6\u00b8"+
		"\u0003\u001c\u000e\u0000\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b7\u00b8"+
		"\u0001\u0000\u0000\u0000\u00b8\u00b9\u0001\u0000\u0000\u0000\u00b9\u00bb"+
		"\u0003&\u0013\u0000\u00ba\u00b3\u0001\u0000\u0000\u0000\u00ba\u00b7\u0001"+
		"\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00bd\u0005"+
		"\u000e\u0000\u0000\u00bd\u0017\u0001\u0000\u0000\u0000\u00be\u00bf\u0005"+
		"\n\u0000\u0000\u00bf\u00c1\u0005%\u0000\u0000\u00c0\u00c2\u0007\u0002"+
		"\u0000\u0000\u00c1\u00c0\u0001\u0000\u0000\u0000\u00c1\u00c2\u0001\u0000"+
		"\u0000\u0000\u00c2\u0019\u0001\u0000\u0000\u0000\u00c3\u00c4\u0005\u0011"+
		"\u0000\u0000\u00c4\u00c5\u0003&\u0013\u0000\u00c5\u00c6\u0005\u0012\u0000"+
		"\u0000\u00c6\u001b\u0001\u0000\u0000\u0000\u00c7\u00cd\u0003\u001e\u000f"+
		"\u0000\u00c8\u00c9\u0003\u001e\u000f\u0000\u00c9\u00ca\u0005\u0013\u0000"+
		"\u0000\u00ca\u00cb\u0003\u001e\u000f\u0000\u00cb\u00cd\u0001\u0000\u0000"+
		"\u0000\u00cc\u00c7\u0001\u0000\u0000\u0000\u00cc\u00c8\u0001\u0000\u0000"+
		"\u0000\u00cd\u001d\u0001\u0000\u0000\u0000\u00ce\u00cf\u0007\u0003\u0000"+
		"\u0000\u00cf\u001f\u0001\u0000\u0000\u0000\u00d0\u00d1\u0005\f\u0000\u0000"+
		"\u00d1\u00d2\u0003&\u0013\u0000\u00d2\u00d3\u0005\u0017\u0000\u0000\u00d3"+
		"\u00d4\u0003&\u0013\u0000\u00d4\u00d5\u0005\r\u0000\u0000\u00d5\u00d6"+
		"\u0007\u0004\u0000\u0000\u00d6\u00d7\u0003&\u0013\u0000\u00d7!\u0001\u0000"+
		"\u0000\u0000\u00d8\u00d9\u0007\u0005\u0000\u0000\u00d9#\u0001\u0000\u0000"+
		"\u0000\u00da\u00e0\u0005+\u0000\u0000\u00db\u00e0\u0005,\u0000\u0000\u00dc"+
		"\u00e0\u0005&\u0000\u0000\u00dd\u00e0\u0005)\u0000\u0000\u00de\u00e0\u0003"+
		"0\u0018\u0000\u00df\u00da\u0001\u0000\u0000\u0000\u00df\u00db\u0001\u0000"+
		"\u0000\u0000\u00df\u00dc\u0001\u0000\u0000\u0000\u00df\u00dd\u0001\u0000"+
		"\u0000\u0000\u00df\u00de\u0001\u0000\u0000\u0000\u00e0%\u0001\u0000\u0000"+
		"\u0000\u00e1\u00e2\u0005+\u0000\u0000\u00e2\'\u0001\u0000\u0000\u0000"+
		"\u00e3\u00e6\u0005\u001c\u0000\u0000\u00e4\u00e6\u0005\u001d\u0000\u0000"+
		"\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e4\u0001\u0000\u0000\u0000"+
		"\u00e6)\u0001\u0000\u0000\u0000\u00e7\u00e8\u0005\u001e\u0000\u0000\u00e8"+
		"\u00e9\u0005\u0010\u0000\u0000\u00e9\u00ea\u0003&\u0013\u0000\u00ea\u00eb"+
		"\u0005\u000f\u0000\u0000\u00eb\u00f8\u0001\u0000\u0000\u0000\u00ec\u00ed"+
		"\u0003&\u0013\u0000\u00ed\u00f1\u0005\u001f\u0000\u0000\u00ee\u00f0\t"+
		"\u0000\u0000\u0000\u00ef\u00ee\u0001\u0000\u0000\u0000\u00f0\u00f3\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f2\u0001\u0000\u0000\u0000\u00f1\u00ef\u0001"+
		"\u0000\u0000\u0000\u00f2\u00f4\u0001\u0000\u0000\u0000\u00f3\u00f1\u0001"+
		"\u0000\u0000\u0000\u00f4\u00f5\u0005 \u0000\u0000\u00f5\u00f8\u0001\u0000"+
		"\u0000\u0000\u00f6\u00f8\u0003&\u0013\u0000\u00f7\u00e7\u0001\u0000\u0000"+
		"\u0000\u00f7\u00ec\u0001\u0000\u0000\u0000\u00f7\u00f6\u0001\u0000\u0000"+
		"\u0000\u00f8+\u0001\u0000\u0000\u0000\u00f9\u00fa\u0003&\u0013\u0000\u00fa"+
		"\u00fb\u0005*\u0000\u0000\u00fb\u00fd\u0001\u0000\u0000\u0000\u00fc\u00f9"+
		"\u0001\u0000\u0000\u0000\u00fd\u00fe\u0001\u0000\u0000\u0000\u00fe\u00fc"+
		"\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001\u0000\u0000\u0000\u00ff-\u0001"+
		"\u0000\u0000\u0000\u0100\u0102\u0007\u0002\u0000\u0000\u0101\u0100\u0001"+
		"\u0000\u0000\u0000\u0101\u0102\u0001\u0000\u0000\u0000\u0102\u0103\u0001"+
		"\u0000\u0000\u0000\u0103\u0107\u0005\u001a\u0000\u0000\u0104\u0106\u0005"+
		"\u001a\u0000\u0000\u0105\u0104\u0001\u0000\u0000\u0000\u0106\u0109\u0001"+
		"\u0000\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0107\u0108\u0001"+
		"\u0000\u0000\u0000\u0108\u010b\u0001\u0000\u0000\u0000\u0109\u0107\u0001"+
		"\u0000\u0000\u0000\u010a\u010c\u0007\u0002\u0000\u0000\u010b\u010a\u0001"+
		"\u0000\u0000\u0000\u010b\u010c\u0001\u0000\u0000\u0000\u010c\u0183\u0001"+
		"\u0000\u0000\u0000\u010d\u010f\u0007\u0002\u0000\u0000\u010e\u010d\u0001"+
		"\u0000\u0000\u0000\u010e\u010f\u0001\u0000\u0000\u0000\u010f\u0110\u0001"+
		"\u0000\u0000\u0000\u0110\u0114\u0005\u0018\u0000\u0000\u0111\u0113\u0005"+
		"\u0018\u0000\u0000\u0112\u0111\u0001\u0000\u0000\u0000\u0113\u0116\u0001"+
		"\u0000\u0000\u0000\u0114\u0112\u0001\u0000\u0000\u0000\u0114\u0115\u0001"+
		"\u0000\u0000\u0000\u0115\u0118\u0001\u0000\u0000\u0000\u0116\u0114\u0001"+
		"\u0000\u0000\u0000\u0117\u0119\u0007\u0002\u0000\u0000\u0118\u0117\u0001"+
		"\u0000\u0000\u0000\u0118\u0119\u0001\u0000\u0000\u0000\u0119\u0183\u0001"+
		"\u0000\u0000\u0000\u011a\u011c\u0005\u0010\u0000\u0000\u011b\u011a\u0001"+
		"\u0000\u0000\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c\u011e\u0001"+
		"\u0000\u0000\u0000\u011d\u011f\u0005\u001a\u0000\u0000\u011e\u011d\u0001"+
		"\u0000\u0000\u0000\u011f\u0120\u0001\u0000\u0000\u0000\u0120\u011e\u0001"+
		"\u0000\u0000\u0000\u0120\u0121\u0001\u0000\u0000\u0000\u0121\u0122\u0001"+
		"\u0000\u0000\u0000\u0122\u0183\u0005\u0015\u0000\u0000\u0123\u0125\u0005"+
		"\u0015\u0000\u0000\u0124\u0126\u0005\u001a\u0000\u0000\u0125\u0124\u0001"+
		"\u0000\u0000\u0000\u0126\u0127\u0001\u0000\u0000\u0000\u0127\u0125\u0001"+
		"\u0000\u0000\u0000\u0127\u0128\u0001\u0000\u0000\u0000\u0128\u012a\u0001"+
		"\u0000\u0000\u0000\u0129\u012b\u0005\u000f\u0000\u0000\u012a\u0129\u0001"+
		"\u0000\u0000\u0000\u012a\u012b\u0001\u0000\u0000\u0000\u012b\u0183\u0001"+
		"\u0000\u0000\u0000\u012c\u012e\u0005\u0010\u0000\u0000\u012d\u012c\u0001"+
		"\u0000\u0000\u0000\u012d\u012e\u0001\u0000\u0000\u0000\u012e\u0130\u0001"+
		"\u0000\u0000\u0000\u012f\u0131\u0005\u001a\u0000\u0000\u0130\u012f\u0001"+
		"\u0000\u0000\u0000\u0131\u0132\u0001\u0000\u0000\u0000\u0132\u0130\u0001"+
		"\u0000\u0000\u0000\u0132\u0133\u0001\u0000\u0000\u0000\u0133\u0134\u0001"+
		"\u0000\u0000\u0000\u0134\u0183\u0005!\u0000\u0000\u0135\u0137\u0005!\u0000"+
		"\u0000\u0136\u0138\u0005\u001a\u0000\u0000\u0137\u0136\u0001\u0000\u0000"+
		"\u0000\u0138\u0139\u0001\u0000\u0000\u0000\u0139\u0137\u0001\u0000\u0000"+
		"\u0000\u0139\u013a\u0001\u0000\u0000\u0000\u013a\u013c\u0001\u0000\u0000"+
		"\u0000\u013b\u013d\u0005\u000f\u0000\u0000\u013c\u013b\u0001\u0000\u0000"+
		"\u0000\u013c\u013d\u0001\u0000\u0000\u0000\u013d\u0183\u0001\u0000\u0000"+
		"\u0000\u013e\u0142\u0005\"\u0000\u0000\u013f\u0141\u0005\u0018\u0000\u0000"+
		"\u0140\u013f\u0001\u0000\u0000\u0000\u0141\u0144\u0001\u0000\u0000\u0000"+
		"\u0142\u0140\u0001\u0000\u0000\u0000\u0142\u0143\u0001\u0000\u0000\u0000"+
		"\u0143\u014d\u0001\u0000\u0000\u0000\u0144\u0142\u0001\u0000\u0000\u0000"+
		"\u0145\u0147\u0005\u0018\u0000\u0000\u0146\u0145\u0001\u0000\u0000\u0000"+
		"\u0147\u014a\u0001\u0000\u0000\u0000\u0148\u0146\u0001\u0000\u0000\u0000"+
		"\u0148\u0149\u0001\u0000\u0000\u0000\u0149\u014b\u0001\u0000\u0000\u0000"+
		"\u014a\u0148\u0001\u0000\u0000\u0000\u014b\u014d\u0005#\u0000\u0000\u014c"+
		"\u013e\u0001\u0000\u0000\u0000\u014c\u0148\u0001\u0000\u0000\u0000\u014d"+
		"\u0183\u0001\u0000\u0000\u0000\u014e\u0150\u0007\u0006\u0000\u0000\u014f"+
		"\u0151\u0005\u001a\u0000\u0000\u0150\u014f\u0001\u0000\u0000\u0000\u0151"+
		"\u0152\u0001\u0000\u0000\u0000\u0152\u0150\u0001\u0000\u0000\u0000\u0152"+
		"\u0153\u0001\u0000\u0000\u0000\u0153\u0155\u0001\u0000\u0000\u0000\u0154"+
		"\u0156\u0005\u000f\u0000\u0000\u0155\u0154\u0001\u0000\u0000\u0000\u0155"+
		"\u0156\u0001\u0000\u0000\u0000\u0156\u0183\u0001\u0000\u0000\u0000\u0157"+
		"\u0159\u0007\u0006\u0000\u0000\u0158\u015a\u0005\u0018\u0000\u0000\u0159"+
		"\u0158\u0001\u0000\u0000\u0000\u015a\u015b\u0001\u0000\u0000\u0000\u015b"+
		"\u0159\u0001\u0000\u0000\u0000\u015b\u015c\u0001\u0000\u0000\u0000\u015c"+
		"\u015e\u0001\u0000\u0000\u0000\u015d\u015f\u0005\u000f\u0000\u0000\u015e"+
		"\u015d\u0001\u0000\u0000\u0000\u015e\u015f\u0001\u0000\u0000\u0000\u015f"+
		"\u0183\u0001\u0000\u0000\u0000\u0160\u0162\u0005\u0010\u0000\u0000\u0161"+
		"\u0160\u0001\u0000\u0000\u0000\u0161\u0162\u0001\u0000\u0000\u0000\u0162"+
		"\u0164\u0001\u0000\u0000\u0000\u0163\u0165\u0005\u001a\u0000\u0000\u0164"+
		"\u0163\u0001\u0000\u0000\u0000\u0165\u0166\u0001\u0000\u0000\u0000\u0166"+
		"\u0164\u0001\u0000\u0000\u0000\u0166\u0167\u0001\u0000\u0000\u0000\u0167"+
		"\u0168\u0001\u0000\u0000\u0000\u0168\u0183\u0007\u0007\u0000\u0000\u0169"+
		"\u016b\u0005\u0010\u0000\u0000\u016a\u0169\u0001\u0000\u0000\u0000\u016a"+
		"\u016b\u0001\u0000\u0000\u0000\u016b\u016d\u0001\u0000\u0000\u0000\u016c"+
		"\u016e\u0005\u0018\u0000\u0000\u016d\u016c\u0001\u0000\u0000\u0000\u016e"+
		"\u016f\u0001\u0000\u0000\u0000\u016f\u016d\u0001\u0000\u0000\u0000\u016f"+
		"\u0170\u0001\u0000\u0000\u0000\u0170\u0171\u0001\u0000\u0000\u0000\u0171"+
		"\u0183\u0007\u0007\u0000\u0000\u0172\u0176\u0005\"\u0000\u0000\u0173\u0175"+
		"\u0005\u0018\u0000\u0000\u0174\u0173\u0001\u0000\u0000\u0000\u0175\u0178"+
		"\u0001\u0000\u0000\u0000\u0176\u0174\u0001\u0000\u0000\u0000\u0176\u0177"+
		"\u0001\u0000\u0000\u0000\u0177\u0181\u0001\u0000\u0000\u0000\u0178\u0176"+
		"\u0001\u0000\u0000\u0000\u0179\u017b\u0005\u0018\u0000\u0000\u017a\u0179"+
		"\u0001\u0000\u0000\u0000\u017b\u017e\u0001\u0000\u0000\u0000\u017c\u017a"+
		"\u0001\u0000\u0000\u0000\u017c\u017d\u0001\u0000\u0000\u0000\u017d\u017f"+
		"\u0001\u0000\u0000\u0000\u017e\u017c\u0001\u0000\u0000\u0000\u017f\u0181"+
		"\u0005#\u0000\u0000\u0180\u0172\u0001\u0000\u0000\u0000\u0180\u017c\u0001"+
		"\u0000\u0000\u0000\u0181\u0183\u0001\u0000\u0000\u0000\u0182\u0101\u0001"+
		"\u0000\u0000\u0000\u0182\u010e\u0001\u0000\u0000\u0000\u0182\u011b\u0001"+
		"\u0000\u0000\u0000\u0182\u0123\u0001\u0000\u0000\u0000\u0182\u012d\u0001"+
		"\u0000\u0000\u0000\u0182\u0135\u0001\u0000\u0000\u0000\u0182\u014c\u0001"+
		"\u0000\u0000\u0000\u0182\u014e\u0001\u0000\u0000\u0000\u0182\u0157\u0001"+
		"\u0000\u0000\u0000\u0182\u0161\u0001\u0000\u0000\u0000\u0182\u016a\u0001"+
		"\u0000\u0000\u0000\u0182\u0180\u0001\u0000\u0000\u0000\u0183/\u0001\u0000"+
		"\u0000\u0000\u0184\u0185\u0007\b\u0000\u0000\u01851\u0001\u0000\u0000"+
		"\u0000A5?AHLQTZ\\`ejmux{\u0080\u0083\u008b\u008e\u0091\u0098\u009e\u00a4"+
		"\u00a7\u00af\u00b3\u00b7\u00ba\u00c1\u00cc\u00df\u00e5\u00f1\u00f7\u00fe"+
		"\u0101\u0107\u010b\u010e\u0114\u0118\u011b\u0120\u0127\u012a\u012d\u0132"+
		"\u0139\u013c\u0142\u0148\u014c\u0152\u0155\u015b\u015e\u0161\u0166\u016a"+
		"\u016f\u0176\u017c\u0180\u0182";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}