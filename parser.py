import ply.yacc as yacc
from lexer import tokens
from HPTools import Health

# Defining parser rules
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
    print('All available doctors: ')
    p = Health()
    print(p.get_DoctorsAvailable())

def p_expression_doctors(p):
    'expression : DOCTORS COLON'
    print('Doctors: ')
    p = Health()
    print(p.get_Doctors())

def p_expression_patients(p):
    'expression : PATIENTS COLON'
    print('Patients: ')
    p = Health()
    print(p.get_Patients())

def p_expression_services(p):
    'expression : SERVICES COLON'
    print('All services to date:')
    p = Health()
    print(p.get_services())

def p_expression_info(p):
    'expression : INFO LP ID RP COLON'
    did = str(p[3])
    p = Health()
    if p.get_DoctorByID(did):
        print(p.get_DoctorByID(did))
    if p.get_PatientByID(did):
        print(p.get_PatientByID(did))
    else:
        print('No patient or doctor with that ID.')

def p_expression_update(p):
    'expression : UPDATE LP ID COMMA AVAILABILITY RP COLON'
    did = str(p[3])
    avail = str(p[5])
    p = Health()
    # Checking if avail is Yes or No and change value to True or False
    if avail == 'True' or 'true' or 'False' or 'false':
        print(p.updateDoctor(did, avail))
    else:
        # Error Handling
        print("Availability must be True or False")

def p_addDoctor(p):
    'expression : ADDDOCTOR LP NAME COMMA BIRTHDAY COMMA SSN COMMA AVAILABILITY COMMA ID RP COLON'
    name = str(p[3])
    birthday = str(p[5])
    ssn = str(p[7])
    availability = str(p[9])
    id = str(p[11])
    p = Health()
    print(p.addDoctor(name, birthday, ssn, availability, id))

def p_addPatient(p):
    'expression : ADDPATIENT LP NAME COMMA BIRTHDAY COMMA SSN COMMA PROTOCOL COMMA ID RP COLON'
    name = str(p[3])
    birthday = str(p[5])
    ssn = str(p[7])
    protocol = str(p[9])
    id = str(p[11])
    p = Health()
    print(p.addPatient(name, birthday, ssn, protocol, id))

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
    # print(result)
