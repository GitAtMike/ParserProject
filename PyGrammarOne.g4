grammar PyGrammarOne;

tokens { INDENT, DEDENT }

// Library that helps with Indents and Dedents
@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from MyCoolParser import MyCoolParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: MyCoolLexer = lexer

    def pull_token(self):
        return super(MyCoolLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NL, MyCoolParser.INDENT, MyCoolParser.DEDENT, ***Should Ignore EOF***)
    return self.denter.next_token()

}

// Lexer Rules
NEWLINE: ('\r'? '\n' ' '*);
WS: [ \t]+ -> skip; // Skip spaces and tabs

COMMENT: '#' ~[\r\n]* -> skip;
MULTILINE_COMMENT: SQ SQ SQ.*? SQ SQ SQ -> skip;

// Keywords
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
IN: 'in';
AND: 'and';
OR: 'or';
NOT: 'not';

// Operators and Punctuation
COLON: ':';
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SQ: '\'';
DQ: '"';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQ: '=';
PLUSEQ: '+=';
MINUSEQ: '-=';
MULTEQ: '*=';
DIVEQ: '/=';
EE: '==';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
NE: '!=';

// Identifiers and Literals
VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]*;
STRING: DQ (~["\\])* DQ | SQ (~['\\])* SQ;

// Parser Rules
program: (stmt NEWLINE*)+ EOF;

stmt
    : simple_stmt
    | compound_stmt
    ;

simple_stmt
    : assign_stmt
    | expr_stmt
    ;

assign_stmt
    : VARNAME (EQ | PLUSEQ | MINUSEQ | MULTEQ | DIVEQ) expr
    ;

expr_stmt
    : expr
    ;

expr
    : term ((PLUS | MINUS) term)*;

term
    : factor ((MULT | DIV | MOD) factor)*;

factor
    : atom
    | LPAREN expr RPAREN;

comparison
    : expr (GT | LT | GE | LE | EQ | NE | EE) expr;

logical_expr
    : comparison ((AND | OR) comparison)*
    | LPAREN NOT? expr* RPAREN
    | expr
    ;

atom
    : VARNAME
    | INT
    | MINUS INT
    | FLOAT
    | STRING
    | array
    ;

array
    : LBRACK (expr (',' expr)*)? RBRACK
    ;

compound_stmt
    : if_stmt
    | elif_stmt
    | else_stmt
    | while_stmt
    | for_stmt
    ;

if_stmt
    : IF logical_expr COLON NEWLINE suite (NEWLINE suite)*
    ;
    
elif_stmt
    : ELIF logical_expr ((AND|OR) logical_expr)* COLON NEWLINE suite
    ;

else_stmt
    : ELSE COLON NEWLINE suite
    ;

while_stmt
    : WHILE (LPAREN* logical_expr RPAREN*) COLON NEWLINE suite 
    (NEWLINE suite)*
    ;

for_stmt
    : FOR VARNAME IN expr COLON NEWLINE suite (NEWLINE suite)*
    | FOR VARNAME IN expr LPAREN INT COMMA INT RPAREN 
    COLON NEWLINE suite (NEWLINE suite)*
    ;

suite
    : stmt+ 
    ;