

class Exp:
    ...

class Literal(Exp):
    
    def __init__(self,value):
        self.value = value
    
    


class Binary(Exp): 
    
    def __init__(self,left,operator,right):
        self.left = left
        self.operator = operator
        self.right = right
    
    
    
class Unary(Exp):
    
    def __init__(self,un,exp):
        self.un = un
        self.exp = exp 
        
    
    
    
class Grouping(Exp): 
    
    def __init__(self,exp):
        self.exp = exp
    
    