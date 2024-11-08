import sys
from antlr4 import *
from PyGrammarOneLexer import PyGrammarOneLexer
from PyGrammarOneParser import PyGrammarOneParser
import re

def main(file_path):
    
    with open(file_path, 'r') as file:
        #Looks at each line in python file
        for line in file:
            input_stream = InputStream(line.strip())

            #Skips blank lines in python file
            if line.strip() == '':
                continue
            
            #Creates the lexer, parser, and token stream
            lexer = PyGrammarOneLexer(input_stream)
            tokenStream = CommonTokenStream(lexer)
            parser = PyGrammarOneParser(tokenStream)

            #Creates the parser tree and prints it out as a string  
            tree = parser.exp()
            print(f"Parse tree for '{line.strip()}':")
            print(tree.toStringTree(recog=parser))

#Accesses the python file to test parser and grammar
if __name__ == "__main__":
    main("project_deliverable_1.py")
