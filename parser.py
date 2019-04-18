import ply.yacc as yacc
from lexer import tokens

# Defining parser rules

def p_id(p):
    'id : ID'

def p_name(p):
    'name : NAME'

def p_ssn(p):
    'ssn : SSN'

def p_birthday(p):
    'birthday : BIRTHDAY'

def p_availability(p):
    'availability : AVAILABILITY'

# def p_expression_create(p):
#     'expression : CREATE name COLON'
#
# def p_expression_protocols(p):
#     'expression : PROTOCOLS COLON'

def p_expression(p):
    ''' expression : CREATE name COLON
                   | PROTOCOLS COLON
                   | BEDS COLON
                   | BEDS LP DIGIT RP
                   | DOCTORS LP AVAILABLE RP COLON
                   | DOCTORS COLON
                   | SERVICES COLON
                   | INFO LP ID RP COLON
                   | UPDATE LP ID COMMA AVAILABILITY RP
    '''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build parser
parser = yacc.yacc()

while True:
    try:
        s = input('Health >> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)