import ply.lex as lex
import re

tokens = ['CHARACTER',
          'OPERATOR',
          'DIGIT',
          'LP',
          'RP',
          'COLON',
          'COMMA',
          'ASSIGN',     # EQUAL IN DOCUMENTATION
          'ID',
          'NAME',
          'BIRTHDAY',
          'SSN',
          'AVAILABILITY',
          'NEWLINE',
          'WHITESPACE'
]

reserved = {
    'create': 'CREATE',
    'protocols': 'PROTOCOLS',
    'beds': 'BEDS',
    'doctors': 'DOCTORS',
    'services': 'SERVICES',
    'information': 'INFO',
    'update': 'UPDATE',
    'addDoctor': 'ADDDOCTOR',
    'addPatient': 'ADDPATIENT'
}

tokens = tokens + list(reserved.values())

# ------------------- TOKEN DECLARATION -------------------------------

t_ignore = '\t \n'
t_ignore_COMMENT = r'\#.*'
t_LP = r'\('
t_RP = r'\)'
t_COLON = r':'
t_COMMA = r','
t_ASSIGN = r'='
# t_OPERATOR = "'.-/"
literals = ".-'"  # operators

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_NAME(t):
    r'[a-zA-Z_]+[a-zA-Z_]'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Error
def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build Lexer
lexer = lex.lex()


# Testing
def fileRead():
    # read file
    # self.filename = filename
    file = open("Test", "r")
    lines = file.readlines()
    file.close()

    fileTokens = []
    for line in lines:
        # fileTokens += line
        lexer.input(line)
        for tok in lexer:
            print(tok)
            fileTokens.append(tok)
    # print(fileTokens)
    return fileTokens


fileRead()

