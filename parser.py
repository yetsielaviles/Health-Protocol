import ply.yacc as yacc
from lexer import tokens

# Defining parser rules

def p_expression(p):
    ''' expression : CREATE name COLON
                   | PROTOCOLS COLON
                   | BEDS COLON
                   | BEDS LP DIGIT RP COLON
                   | DOCTORS LP availability RP COLON
                   | DOCTORS COLON
                   | SERVICES COLON
                   | INFO LP id RP COLON
                   | ADDDOCTOR LP name COMMA birthday COMMA ssn COMMA availability COMMA id RP COLON
                   | ADDPATIENT LP name COMMA birthday COMMA ssn COMMA name COMMA id RP COLON
                   | UPDATE LP id COMMA AVAILABILITY RP COLON
    '''

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

# def p_bed(p):
#     'bed : BEDS LP DIGIT RP'
#
# def p_available_doctors(p):
#     'avail_doctors : DOCTORS LP AVAILABLE RP COLON'
#
# def p_doctors(p):
#     'doctors : DOCTORS COLON'
#
# def p_services(p):
#     'services : SERVICES COLON'
#
# def p_info(p):
#     'info : INFO LP ID RP COLON'
#
# def p_update(p):
#     'update : UPDATE LP ID COMMA AVAILABILITY RP'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error at ’%s’" % p)

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
