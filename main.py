import sys



class Darija:
    
    
    
    def __init__(self,hadError=False):
        args = sys.argv
        if len(args) - 1 > 1:
            raise Exception("Too many arguments provided. Please provide only the file name.")
        elif len(args) - 1 == 1:
            self.fileName = args[1]
            self.runFile()
        else:
            self.fileName = None
            self.run_prompt()
        self.hadError = hadError
        
    
    def runFile(self):
        
        print(f"Processing file: {self.fileName}")
        with open(self.fileName, 'rb') as file:
            content = file.read()
            code = content.decode()
            self.run(code)
            if self.hadError:
                print("An error occurred. Exiting.")
                sys.exit(65)
            
            print(f"File content:\n{code}")
    
    def run(self,input_code):
        
        if self.fileName:
            print(f"Running {self.fileName}...")
        
        print(f"Input code:\n{input_code}")
    
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

