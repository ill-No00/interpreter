
from ..errors.runtimeError import RuntimeError


class Evironment():
    
    def __init__(self):
        self.values = {}
    
    def add(self,name,value):
        self.values[name] = value
    
    def get(self,name):
        
        if self.values[name.lexeme]:
            
            return self.values.get(name.lexeme)
        
        return RuntimeError(f"Undefined variable {name.lexeme} .")