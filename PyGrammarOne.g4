grammar PyGrammarOne;

// Using java language with antlr's compatibility to implement stack fuctions to get the indention right for statements
// where indention and dedention is needed. Create tokens for easy use in the grammar.
@lexer::members {

    // Make a stack to keep track of the level of indents
    java.util.Stack<Integer> indStack = new java.util.Stack<>();
    {
        indStack.push(0);
    }

    // Create a queue to hold our pending indent and/or dedent tokens so they are ready for use
    // Used for when the indentation changes
    java.util.LinkedList<Token> tokens = new java.util.LinkedList<>();
    int currentInd = 0;

    // Use Override to create our own logic specific to our use for these tokens.
    @Override
    public Token nextToken(){
        if(!tokens.isEmpty()){
            return tokens.poll();
        }
        Token next = super.nextToken();
        if(next.getType() == NEWLINE){
            processInd(next);
        }
        return tokens.isEmpty() ? next : tokens.poll();
    }

    // When the program reaches the NEWLINE token I have created, this method
    // processes the indentation changes needed.
    private void processInd(Token newlineToken){
        String spaces = getText();
        int ind = spaces.length();
        // Creates indent
        if (ind > currentInd){
            indStack.push(ind);
            tokens.add(createToken(INDENT, newlineToken));
        }
        // Creates dedent
        else if(ind < currentInd){
            while(!indStack.isEmpty() && ind < indStack.peek()){
                indStack.pop();
                tokens.add(createToken(DEDENT, newlineToken));
            }
        }
        currentInd = ind;
    }

    // Method that creates the token itself
    privateToken createToken(int type, Token srcToken){
        CommonToken token = new CommonToken(type, "");

        // Gathers info from the source token on it's position
        token.setLine(srceToken.getLine());
        token.setCharPositionInLine(srcToken.getCharPositionInLine());
        token.setStartIndex(srcToken.getStartIndex());
        token.setStopIndex(srcToken.getStopIndex());

        // Returns the new token we created
        return token;
    }
}

// The 'templates' used for the rest of the grammar
prog: (exp NEWLINE?)* NEWLINE? EOF;

exp: assign | arith | types | statements;

types: SUB? INT | SUB? FLOAT | STRING | array | VARNAME;

// Assign and Arithmetic Definitions
assign: VARNAME (ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) exp;

arith: types ((ADD | SUB | MUL | DIV | MOD) types)*;

// Comparison and Logical Definitions
cond: exp ((LT | GT | LTE | GTE | EE | NE) exp)*;

logi: NOT? cond ((AND | OR) cond)* | LPAR logi RPAR (AND|OR)?| cond;

array: '[' (types (',' types)*)? ']';

// Arithmetic and Assignment Operators
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
LPAR: '(';
RPAR: ')';
COLON: ':';

// Comparison and Logical Operators
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
EE: '==';
NE: '!=';

AND: 'and';
OR: 'or';
NOT: 'not';

// if/elif/else Blocks
if_state: 'if' (logi)* COLON block INDENT block DEDENT (elif_state)* (else_state)?;
elif_state: 'elif' (logi)* COLON block  INDENT block DEDENT;
else_state: 'else' COLON block INDENT block DEDENT;

block: (exp NEWLINE?)+;

statements: (if_state | elif_state | else_state);

// Data Types and Variable Name
VARNAME: [A-Za-z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';

// Empty Space
NEWLINE: '\r'? '\n' -> skip;
WHITESPACE: [ \t\r\n]+ ->skip;

// INDENTION RULES
INDENT: '<INDENT>';
DEDENT: '<DEDENT>';
SPACES: [\t]+ -> skip;