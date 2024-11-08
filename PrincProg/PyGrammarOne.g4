grammar PyGrammarOne;

prog: (exp NEWLINE)* EOF;

exp: assign | arith | types;

types: INT | FLOAT | STRING | array | VARNAME;

assign: VARNAME (ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) exp;

arith: types ( (ADD | SUB | MUL | DIV | MOD) types )* ;

array: '[' (types (',' types)*)? ']';

ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

VARNAME: [A-Za-z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';

NEWLINE: '\r'? '\n' -> skip;
WHITESPACE: [ \t\r\n]+ -> skip;
