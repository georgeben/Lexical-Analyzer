# TODO: Code is a mess, needs refactoring

# Global variables
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

def lookupSymbol(character):
    if (character == "("):
        nextToken = LEFT_PAREN
    elif (character == ")"):
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
    global fileIndex

    if (charClass == LETTER):
        lexeme+=char
        nextChar = getChar()
        while(nextChar != EOF and nextChar != " " and (getCharClass(nextChar) == LETTER or getCharClass(nextChar) == DIGIT)):
            lexeme+=nextChar
            nextChar = getChar()
        nextToken = IDENT
        if nextChar != " " and nextChar != EOF:
            fileIndex -= 1

    elif (charClass == DIGIT):
        lexeme+=char
        nextChar = getChar()
        while( (nextChar != EOF) and (nextChar != " ") and (getCharClass(nextChar) == DIGIT) ):
            lexeme+=nextChar
            nextChar = getChar()
        nextToken = INT_LIT
        if nextChar != " " and nextChar != EOF:
            fileIndex -= 1

    elif (charClass == UNKNOWN):
        token = lookupSymbol(char)
        lexeme+=char
        nextToken = token

    print ("Next token is:", nextToken, " Next lexeme is: ", lexeme)
    return nextToken


def main():
    nextChar = getNonBlank()
    if (nextChar == "EOF"):
        print ("File is empty")
        return
    # return
    while nextChar != "EOF":
        nextToken = lex(nextChar)
        if (nextToken == INVALID):
            break
        nextChar = getChar()

main()