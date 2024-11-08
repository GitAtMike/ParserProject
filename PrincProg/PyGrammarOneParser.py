# Generated from PyGrammarOne.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write(">\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\7\6,\n\6\f\6\16\6/\13\6\3\7\3\7\3\7\3")
        buf.write("\7\7\7\65\n\7\f\7\16\78\13\7\5\7:\n\7\3\7\3\7\3\7\2\2")
        buf.write("\b\2\4\6\b\n\f\2\4\3\2\6\13\3\2\f\20\2A\2\23\3\2\2\2\4")
        buf.write("\33\3\2\2\2\6\"\3\2\2\2\b$\3\2\2\2\n(\3\2\2\2\f\60\3\2")
        buf.write("\2\2\16\17\5\4\3\2\17\20\7\25\2\2\20\22\3\2\2\2\21\16")
        buf.write("\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\26\3\2\2\2\25\23\3\2\2\2\26\27\7\2\2\3\27\3\3\2\2\2\30")
        buf.write("\34\5\b\5\2\31\34\5\n\6\2\32\34\5\6\4\2\33\30\3\2\2\2")
        buf.write("\33\31\3\2\2\2\33\32\3\2\2\2\34\5\3\2\2\2\35#\7\22\2\2")
        buf.write("\36#\7\23\2\2\37#\7\24\2\2 #\5\f\7\2!#\7\21\2\2\"\35\3")
        buf.write("\2\2\2\"\36\3\2\2\2\"\37\3\2\2\2\" \3\2\2\2\"!\3\2\2\2")
        buf.write("#\7\3\2\2\2$%\7\21\2\2%&\t\2\2\2&\'\5\4\3\2\'\t\3\2\2")
        buf.write("\2(-\5\6\4\2)*\t\3\2\2*,\5\6\4\2+)\3\2\2\2,/\3\2\2\2-")
        buf.write("+\3\2\2\2-.\3\2\2\2.\13\3\2\2\2/-\3\2\2\2\609\7\3\2\2")
        buf.write("\61\66\5\6\4\2\62\63\7\4\2\2\63\65\5\6\4\2\64\62\3\2\2")
        buf.write("\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67:\3\2\2\2")
        buf.write("8\66\3\2\2\29\61\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\7\5\2\2")
        buf.write("<\r\3\2\2\2\b\23\33\"-\669")
        return buf.getvalue()


class PyGrammarOneParser ( Parser ):

    grammarFileName = "PyGrammarOne.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "'='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "ID", "INT", "FLOAT", "STRING", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_primary = 2
    RULE_assign = 3
    RULE_arith = 4
    RULE_array = 5

    ruleNames =  [ "prog", "expr", "primary", "assign", "arith", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ASSIGN=4
    ADD_ASSIGN=5
    SUB_ASSIGN=6
    MUL_ASSIGN=7
    DIV_ASSIGN=8
    MOD_ASSIGN=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    MOD=14
    ID=15
    INT=16
    FLOAT=17
    STRING=18
    NEWLINE=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PyGrammarOneParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyGrammarOneParser.ExprContext)
            else:
                return self.getTypedRuleContext(PyGrammarOneParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PyGrammarOneParser.NEWLINE)
            else:
                return self.getToken(PyGrammarOneParser.NEWLINE, i)

        def getRuleIndex(self):
            return PyGrammarOneParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = PyGrammarOneParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PyGrammarOneParser.T__0) | (1 << PyGrammarOneParser.ID) | (1 << PyGrammarOneParser.INT) | (1 << PyGrammarOneParser.FLOAT) | (1 << PyGrammarOneParser.STRING))) != 0):
                self.state = 12
                self.expr()
                self.state = 13
                self.match(PyGrammarOneParser.NEWLINE)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(PyGrammarOneParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(PyGrammarOneParser.AssignContext,0)


        def arith(self):
            return self.getTypedRuleContext(PyGrammarOneParser.ArithContext,0)


        def primary(self):
            return self.getTypedRuleContext(PyGrammarOneParser.PrimaryContext,0)


        def getRuleIndex(self):
            return PyGrammarOneParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = PyGrammarOneParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.arith()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PyGrammarOneParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PyGrammarOneParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(PyGrammarOneParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(PyGrammarOneParser.ArrayContext,0)


        def ID(self):
            return self.getToken(PyGrammarOneParser.ID, 0)

        def getRuleIndex(self):
            return PyGrammarOneParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = PyGrammarOneParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_primary)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PyGrammarOneParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(PyGrammarOneParser.INT)
                pass
            elif token in [PyGrammarOneParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(PyGrammarOneParser.FLOAT)
                pass
            elif token in [PyGrammarOneParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(PyGrammarOneParser.STRING)
                pass
            elif token in [PyGrammarOneParser.T__0]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.array()
                pass
            elif token in [PyGrammarOneParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(PyGrammarOneParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PyGrammarOneParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PyGrammarOneParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(PyGrammarOneParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(PyGrammarOneParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(PyGrammarOneParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(PyGrammarOneParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(PyGrammarOneParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(PyGrammarOneParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return PyGrammarOneParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = PyGrammarOneParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(PyGrammarOneParser.ID)
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PyGrammarOneParser.ASSIGN) | (1 << PyGrammarOneParser.ADD_ASSIGN) | (1 << PyGrammarOneParser.SUB_ASSIGN) | (1 << PyGrammarOneParser.MUL_ASSIGN) | (1 << PyGrammarOneParser.DIV_ASSIGN) | (1 << PyGrammarOneParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 36
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyGrammarOneParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(PyGrammarOneParser.PrimaryContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(PyGrammarOneParser.ADD)
            else:
                return self.getToken(PyGrammarOneParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(PyGrammarOneParser.SUB)
            else:
                return self.getToken(PyGrammarOneParser.SUB, i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(PyGrammarOneParser.MUL)
            else:
                return self.getToken(PyGrammarOneParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(PyGrammarOneParser.DIV)
            else:
                return self.getToken(PyGrammarOneParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(PyGrammarOneParser.MOD)
            else:
                return self.getToken(PyGrammarOneParser.MOD, i)

        def getRuleIndex(self):
            return PyGrammarOneParser.RULE_arith

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith" ):
                listener.enterArith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith" ):
                listener.exitArith(self)




    def arith(self):

        localctx = PyGrammarOneParser.ArithContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arith)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.primary()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PyGrammarOneParser.ADD) | (1 << PyGrammarOneParser.SUB) | (1 << PyGrammarOneParser.MUL) | (1 << PyGrammarOneParser.DIV) | (1 << PyGrammarOneParser.MOD))) != 0):
                self.state = 39
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PyGrammarOneParser.ADD) | (1 << PyGrammarOneParser.SUB) | (1 << PyGrammarOneParser.MUL) | (1 << PyGrammarOneParser.DIV) | (1 << PyGrammarOneParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.primary()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyGrammarOneParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(PyGrammarOneParser.PrimaryContext,i)


        def getRuleIndex(self):
            return PyGrammarOneParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = PyGrammarOneParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(PyGrammarOneParser.T__0)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PyGrammarOneParser.T__0) | (1 << PyGrammarOneParser.ID) | (1 << PyGrammarOneParser.INT) | (1 << PyGrammarOneParser.FLOAT) | (1 << PyGrammarOneParser.STRING))) != 0):
                self.state = 47
                self.primary()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PyGrammarOneParser.T__1:
                    self.state = 48
                    self.match(PyGrammarOneParser.T__1)
                    self.state = 49
                    self.primary()
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 57
            self.match(PyGrammarOneParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





