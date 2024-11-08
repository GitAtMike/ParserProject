grammar PyGrammarOne;

prog: (expr NEWLINE)* EOF;

expr: assign | arith | primary;

primary: INT | FLOAT | STRING | array | ID;

assign: ID (ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expr;

arith: primary ( (ADD | SUB | MUL | DIV | MOD) primary )* ;

array: '[' (primary (',' primary)*)? ']';

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

ID: [A-Za-z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';

NEWLINE: '\r'? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;
