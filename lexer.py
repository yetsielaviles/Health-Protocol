import ply.lex as lex
import re

tokens = ['CHARACTER',
          'OPERATOR',
          'DIGIT',
          'LP',
          'RP',
          'COLON',
          'COMMA',
          'ASSIGN',
          'ID',
          'NAME',
          'BIRTHDAY',
          'SSN',
          'AVAILABILITY']

reserved = {
    'create_protocol': 'CREATE',
    'protocols': 'PROTOCOLS',
    'beds': 'BEDS',
    'doctors': 'DOCTORS',
    'patients': 'PATIENTS',
    'services': 'SERVICES',
    'info': 'INFO',
    'update': 'UPDATE',
    'addDoctor': 'ADDDOCTOR',
    'addPatient': 'ADDPATIENT',
    'available': 'AVAILABLE',
    'gsw': 'PROTOCOL',
    'broken bone': 'PROTOCOL',
    'heart attack': 'PROTOCOL'
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

def t_AVAILABILITY(t):
    r'True|False|true|false'
    return t

def t_BIRTHDAY(t):
    r'([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}'
    return t

def t_SSN(t):
    r'[0-9]{4}'
    return t

def t_NAME(t):
    r'((Dr|Mrs?|Ms)\.\s)?[A-Za-z]([A-Za-z](\s|\.|\_)?)+[a-zA-Z]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_ID(t):
    r'[0-9a-zA-Z][a-zA-Z0-9\-]+'
    return t

def t_DIGIT(t):
    r'[0-9]'
    return t

# t_OPERATOR = "'.-/"
literals = ".-'"  # operators

# Error
def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build Lexer
lexer = lex.lex()

# Testing
def fileRead():
    # read file
    file = open("Test", "r")
    lines = file.read().splitlines()
    file.close()

    fileTokens = []
    for line in lines:
        lexer.input(line)
        for tok in lexer:
            print(tok)
            fileTokens.append(tok)
    return fileTokens

# fileRead()
