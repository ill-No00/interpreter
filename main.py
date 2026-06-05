import sys



class Darija:
    
    def __init__(self):
        args = sys.argv
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
    
            
        
        
        
lang = Darija()

