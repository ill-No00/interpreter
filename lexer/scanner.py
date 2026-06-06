

OPERATORS = {
    '+', '-', '*', '/', '(', ')',
    '=', ',', ';', ':'
}

def scanner(source):
    tokens = []
    i = 0

    while i < len(source):

        if source[i].isspace():
            i += 1
            continue
        
        if source[i] in ['=', '>', '<', '!'] and source[i+1] in ['=', '>', '<', '!']:
            tokens.append(source[i] + source[i+1])
            i += 2
            continue

        if source[i] in OPERATORS:
            tokens.append(source[i])
            i += 1
            continue

        start = i

        while (
            i < len(source)
            and not source[i].isspace()
            and source[i] not in OPERATORS
        ):
            if source[i] == "'":
                i += 1
                while i < len(source) and source[i] != "'":
                    i += 1
                if i < len(source):
                    i += 1  
            
            else:
                i += 1

        lexeme = source[start:i]

        if lexeme.isdigit():
            tokens.append(lexeme)
        else:
            tokens.append(lexeme)

    return tokens
    
