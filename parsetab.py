
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDDOCTOR ADDPATIENT ASSIGN AVAILABILITY AVAILABLE BEDS BIRTHDAY CHARACTER COLON COMMA CREATE DIGIT DOCTORS ID INFO LP NAME NEWLINE OPERATOR PROTOCOLS RP SERVICES SSN UPDATE WHITESPACE expression : CREATE name COLON\n                   | PROTOCOLS COLON\n                   | BEDS COLON\n                   | BEDS LP DIGIT RP COLON\n                   | DOCTORS LP availability RP COLON\n                   | DOCTORS COLON\n                   | SERVICES COLON\n                   | INFO LP id RP COLON\n                   | ADDDOCTOR LP name COMMA birthday COMMA ssn COMMA availability COMMA id RP COLON\n                   | ADDPATIENT LP name COMMA birthday COMMA ssn COMMA name COMMA id RP COLON\n                   | UPDATE LP id COMMA AVAILABILITY RP COLON\n    id : IDname : NAMEssn : SSNbirthday : BIRTHDAYavailability : AVAILABILITY'
    
_lr_action_items = {'CREATE':([0,],[2,]),'PROTOCOLS':([0,],[3,]),'BEDS':([0,],[4,]),'DOCTORS':([0,],[5,]),'SERVICES':([0,],[6,]),'INFO':([0,],[7,]),'ADDDOCTOR':([0,],[8,]),'ADDPATIENT':([0,],[9,]),'UPDATE':([0,],[10,]),'$end':([1,13,14,17,18,23,38,39,40,51,62,63,],[0,-2,-3,-6,-7,-1,-4,-5,-8,-11,-9,-10,]),'NAME':([2,20,21,53,],[12,12,12,12,]),'COLON':([3,4,5,6,11,12,32,33,34,47,60,61,],[13,14,17,18,23,-13,38,39,40,51,62,63,]),'LP':([4,5,7,8,9,10,],[15,16,19,20,21,22,]),'COMMA':([12,26,28,29,30,31,41,42,43,48,49,50,54,55,],[-13,-16,-12,35,36,37,45,-15,46,52,-14,53,56,57,]),'DIGIT':([15,],[24,]),'AVAILABILITY':([16,37,52,],[26,44,26,]),'ID':([19,22,56,57,],[28,28,28,28,]),'RP':([24,25,26,27,28,44,58,59,],[32,33,-16,34,-12,47,60,61,]),'BIRTHDAY':([35,36,],[42,42,]),'SSN':([45,46,],[49,49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'name':([2,20,21,53,],[11,29,30,55,]),'availability':([16,52,],[25,54,]),'id':([19,22,56,57,],[27,31,58,59,]),'birthday':([35,36,],[41,43,]),'ssn':([45,46,],[48,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> CREATE name COLON','expression',3,'p_expression','parser.py',7),
  ('expression -> PROTOCOLS COLON','expression',2,'p_expression','parser.py',8),
  ('expression -> BEDS COLON','expression',2,'p_expression','parser.py',9),
  ('expression -> BEDS LP DIGIT RP COLON','expression',5,'p_expression','parser.py',10),
  ('expression -> DOCTORS LP availability RP COLON','expression',5,'p_expression','parser.py',11),
  ('expression -> DOCTORS COLON','expression',2,'p_expression','parser.py',12),
  ('expression -> SERVICES COLON','expression',2,'p_expression','parser.py',13),
  ('expression -> INFO LP id RP COLON','expression',5,'p_expression','parser.py',14),
  ('expression -> ADDDOCTOR LP name COMMA birthday COMMA ssn COMMA availability COMMA id RP COLON','expression',13,'p_expression','parser.py',15),
  ('expression -> ADDPATIENT LP name COMMA birthday COMMA ssn COMMA name COMMA id RP COLON','expression',13,'p_expression','parser.py',16),
  ('expression -> UPDATE LP id COMMA AVAILABILITY RP COLON','expression',7,'p_expression','parser.py',17),
  ('id -> ID','id',1,'p_id','parser.py',21),
  ('name -> NAME','name',1,'p_name','parser.py',24),
  ('ssn -> SSN','ssn',1,'p_ssn','parser.py',27),
  ('birthday -> BIRTHDAY','birthday',1,'p_birthday','parser.py',30),
  ('availability -> AVAILABILITY','availability',1,'p_availability','parser.py',33),
]
