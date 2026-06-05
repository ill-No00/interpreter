

def lexer(input_code):
    
    print(f"Lexing input code:\n{input_code}")
    try:
        
        tokens = input_code.split()
        
        for token in tokens:
            if any(char in token for char in ['+', '-', '*', '/', '(', ')']):
                print(f"Token: {token} (Operator)")
                
        
        print(f"Generated tokens: {tokens}")
        return tokens
    except Exception as e:
        print(f"Error during lexing: {e}")
        return []
    
    