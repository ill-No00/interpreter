import sys
import os   
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from interpreter.interpreter import Interpreter
from lexer.scanner import Scanner
from parser.parser import Parser



class Darija:
    
    
    
    def __init__(self):
        args = sys.argv
        self.hadError = False
        self.interpreter = Interpreter()
        self.hadRuntimeError = False
        if len(args) - 1 > 1:
            raise Exception("Too many arguments provided. Please provide only the file name.")
        elif len(args) - 1 == 1:
            self.fileName = args[1]
            self.runFile()
        else:
            self.fileName = None
            self.run_prompt()
        
        
    
    def runFile(self):
        
        print(f"Processing file: {self.fileName}")
        with open(self.fileName, 'rb') as file:
            content = file.read()
            code = content.decode()
            self.run(code)
            if self.hadError:
                print("An error occurred. Exiting.")
                sys.exit(65)
            if self.hadRuntimeError:
                print("A runtime error occurred. Exiting.")
                sys.exit(70)
            
            
    
    def run(self,input_code):
        
        if self.fileName:
            print(f"Running {self.fileName}...")
        
        
        
        scanner = Scanner(input_code)
        scanner.scanTokens()
        
        parser = Parser(scanner.tokens)
        statements = parser.parse()
        
        if statements is not None:
            print("Parsed expression successfully.")    
            self.interpreter.interpret(statements)
        else:
            print("Parsing failed. No expression to interpret.")
        
    
    def run_prompt(self):
        
        print("Running prompt mode...")
        while True:
            input_code = input(">>> ")
            if input_code.lower() in ['exit', 'quit']:
                print("Exiting prompt mode.")
                break
            self.run(input_code)
            if self.hadError:
                print("An error occurred. Exiting prompt mode.")
                sys.exit(65)    
            self.hadError = False
    
    def error(self,line, message):
        self.report(line, "", message)
    
    def report(self,line, where, message):
        print(f"[line {line}] Error{where}: {message}")
        self.hadError = True
        
        

lang = Darija()

