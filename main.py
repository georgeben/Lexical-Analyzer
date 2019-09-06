fileName = "input.txt"
inputFile = open(file=fileName, mode="r", encoding="utf8")
inputContent = inputFile.read()
fileIndex=0
EOF = "EOF"
INVALID = "INVALID"

#Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

#Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

lexeme = ""
lexLen = 0

def lookup(character):
    if (character == "("):
        # addChar()
        nextToken = LEFT_PAREN
    elif (character == ")"):
        # addChar()
        nextToken = RIGHT_PAREN
    elif (character == "+"):
        # addChar()
        nextToken = ADD_OP
    elif (character == "-"):
        # addChar()
        nextToken = SUB_OP
    elif (character == "*"):
        # addChar()
        nextToken = MULT_OP
    elif (character == "/"):
        # addChar()
        nextToken = DIV_OP
    else:
        # addChar()
        nextToken = INVALID
    
    return nextToken


def getChar():
    # nextChar = inputFile.read(1)
    # if (nextChar == ""):
    #     return "EOF"
    # # while nextChar == " ":
    # #     nextChar = inputFile.read(1)
    # return nextChar
    global inputContent
    global fileIndex
    if (fileIndex < len(inputContent)):
        nextChar = inputContent[fileIndex]
        fileIndex+=1
        return nextChar
    else:
        return EOF
    

def getNonBlank():
    char = getChar()
    while (char.isspace()):
        char = getChar()
    return char

def getCharClass(char):
    if char.isalpha():
        charClass = LETTER
    elif char.isdigit():
        charClass = DIGIT
    else:
        charClass = UNKNOWN
    return charClass

def addChar(char):
    # Adds a character to the lexeme
    global lexeme
    global lexLen
    lexeme+=char

def lex(char):
    lexeme = ""
    charClass = getCharClass(char)
    print("Char class is:", charClass)
    global fileIndex

    if (charClass == LETTER):
        print("Letter here")
        # addChar(char)
        lexeme+=char
        nextChar = getChar()
        print("Next char here", nextChar)
        while(nextChar != "EOF" and nextChar != " " and (getCharClass(nextChar) == LETTER or getCharClass(nextChar) == DIGIT)):
            print("Boom")
            # addChar(nextChar)
            lexeme+=nextChar
            print("Lexeme now", lexeme)
            nextChar = getChar()
            print("New next char in loop", nextChar)
        nextToken = IDENT
        if nextChar != " ":
            fileIndex -= 1

    elif (charClass == DIGIT):
        print("Digit here")
        lexeme+=char
        nextChar = getChar()
        print("Next char here", nextChar)
        while( (nextChar != "EOF") and (nextChar != " ") and (getCharClass(nextChar) == DIGIT) ):
            print("Boom")
            # addChar(nextChar)
            lexeme+=nextChar
            print("Lexeme now", lexeme)
            nextChar = getChar()
            print("New next char in loop", nextChar)
        nextToken = INT_LIT
        if nextChar != " ":
            fileIndex -= 1

    elif (charClass == UNKNOWN):
        print("Symbol here")
        token = lookup(char)
        lexeme+=char
        nextToken = token

    print ("Next token is:", nextToken, " Next lexeme is: ", lexeme)
    return nextToken


def main():
    nextChar = getNonBlank()
    if (nextChar == "EOF"):
        print ("File is empty")
        return
    print("Next char", nextChar)
    # return
    while nextChar != "EOF":
        nextToken = lex(nextChar)
        if (nextToken == INVALID):
            break
        nextChar = getChar()
        print("why", nextChar)

main()