import sys
from antlr4 import *
from PyGrammarOneLexer import PyGrammarOneLexer
from PyGrammarOneParser import PyGrammarOneParser
import re

def main(file_path):
    
    with open(file_path, 'r') as file:
        #looks at each line in python file
        for line in file:
            input_stream = InputStream(line.strip())

            #skips blank lines in python file
            if line.strip() == '':
                continue
            
            #Creates the lexter, parser, and token stream
            lexer = PyGrammarOneLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = PyGrammarOneParser(token_stream)

            #Creates the parser tree and prints it out as a string  
            tree = parser.expr()
            print(f"Parse tree for '{line.strip()}':")
            print(tree.toStringTree(recog=parser))

#Accesses the python file
if __name__ == "__main__":
    main("project_deliverable_1.py")
