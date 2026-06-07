from token import Token
from unittest import case



    
class Scanner:
    
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start= 0
        self.current = 0
        self.line = 1
        
    def scanTokens(self):
        self.tokens = scanner(self.source)
        return self.tokens
    
    def scanner(self):
        
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(Token("EOF", "", None, self.line))
        return self.tokens
    
    def isAtEnd(self):
        return self.current >= len(self.source)
    
    def scanToken(self):
        c = self.advance()
        
        match c:
            case '(':
                self.addToken("LEFT_PAREN")
            case ')':
                self.addToken("RIGHT_PAREN")
            case '{':
                self.addToken("LEFT_BRACE")
            case '}':
                self.addToken("RIGHT_BRACE")
            case ',': 
                self.addToken("COMMA")
            case '.':
                if self.is_number(self.source[self.current]):
                    print(f"Invalid Number format at line {self.line}")              
                else:
                    self.addToken("DOT")
            case '-':
                self.addToken("MINUS")
            case '+':
                self.addToken("PLUS")
            case ';':
                self.addToken("SEMICOLON")
            case '*':
                self.addToken("STAR")
            case '!':
                self.addToken("BANG_EQUAL" if self.match('=') else "BANG")
            case '=':
                self.addToken("EQUAL_EQUAL" if self.match('=') else "EQUAL")
            case '<':
                self.addToken("LESS_EQUAL" if self.match('=') else "LESS")
            case '>':
                self.addToken("GREATER_EQUAL" if self.match('=') else "GREATER")
            case '/':
                if self.match('/'):
                    while self.peek() != '\n' and not self.isAtEnd():
                        self.advance()
                else:
                    self.addToken("SLASH")
            case ' ' | '\r' | '\t':
                pass
            case '\n':
                self.line += 1
            case '"':
                self.scanTokenstring()
            
            case '0'| '1' | '2' |'3' |'4' |'5' |'6' |'7' |'8' |'9':
                self.scanTokenNum()
            
            case _:
                print(f"Unexpected character: {c} at line {self.line}")
                
    def is_number(num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def scanTokenNum(self):
        
        while not self.isAtEnd() and self.is_number(self.peek()):
            
            self.advance()
        
        if self.peek()== '.' and self.is_number(self.nextPeek()):

            self.advance()
            
            while self.is_number(self.peek()) and not self.isAtEnd() :
                self.advance()
                
        
        
    
    def nextPeek(self):
        
        if self.current + 1 > len(self.source) : 
            return '\0'
        return self.source[self.current+1]
        
            
    def scanTokenstring(self):
        
        while self.peek() != '"' and not self.isAtEnd : 
            if self.peek() == '\n' :
                self.line+=1
            self.advance()
        
        if self.isAtEnd:
            print(f"unterminated string at line {self.line}")
        
        value = self.source[self.start+1:self.current-1]
        self.addToken("STRING",value)


    def match(self, expected):
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False
        
        self.current += 1
        return True
    def peek(self):
        if self.isAtEnd():
            return '\0'
        return self.source[self.current]

    

    def addToken(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))
        
    def advance(self):
        self.current += 1
        return self.source[self.current - 1]