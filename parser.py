import ply.yacc as yacc
from lexer import tokens
from functions import Health

# Defining parser rules

# def p_expression(p):
#     ''' expression : CREATE name COLON
#                    | PROTOCOLS COLON
#                    | BEDS COLON
#                    | BEDS LP DIGIT RP COLON
#                    | DOCTORS LP availability RP COLON
#                    | DOCTORS COLON
#                    | SERVICES COLON
#                    | INFO LP id RP COLON
#                    | ADDDOCTOR LP name COMMA birthday COMMA ssn COMMA availability COMMA id RP COLON
#                    | ADDPATIENT LP name COMMA birthday COMMA ssn COMMA PROTOCOL COMMA id RP COLON
#                    | UPDATE LP id COMMA AVAILABILITY RP COLON
#     '''

def p_expression_create(p):
    'expression : CREATE LP NAME RP COLON'
    protocol = p[3]
    p = Health()
    print(p.add_protocol(protocol))

def p_expression_protocols(p):
    'expression : PROTOCOLS COLON'
    print('All protocols to date:')
    p = Health()
    print(p.get_protocols())

def p_expression_bed(p):
    'expression : BEDS LP DIGIT RP COLON'
    level = str(p[3])
    print('Available beds at level ' + level)
    p = Health()
    print(p.get_bedsByLevel(level))

def p_beds(p):
    'expression : BEDS COLON'
    print('All available beds: ')
    p = Health()
    print(p.get_beds())

def p_available_doctors(p):
    'expression : DOCTORS LP AVAILABLE RP COLON'

def p_expression_doctors(p):
    'expression : DOCTORS COLON'

def p_expression_services(p):
    'expression : SERVICES COLON'

def p_expression_info(p):
    'expression : INFO LP ID RP COLON'

def p_expression_update(p):
    'expression : UPDATE LP ID COMMA AVAILABILITY RP'

def p_addDoctor(p):
    'expression : ADDDOCTOR LP name COMMA birthday COMMA ssn COMMA availability COMMA id RP COLON'

def p_addPatient(p):
    'expression : ADDPATIENT LP name COMMA birthday COMMA ssn COMMA PROTOCOL COMMA id RP COLON'

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
