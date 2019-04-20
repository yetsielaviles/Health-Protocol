
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDDOCTOR ADDPATIENT ASSIGN AVAILABILITY AVAILABLE BEDS BIRTHDAY CHARACTER COLON COMMA CREATE DIGIT DOCTORS ID INFO LP NAME NEWLINE OPERATOR PROTOCOLS RP SERVICES SSN UPDATE WHITESPACEid : IDname : NAMEssn : SSNbirthday : BIRTHDAYavailability : AVAILABILITY expression : CREATE name COLON\n                   | PROTOCOLS COLON\n                   | BEDS COLON\n                   | BEDS LP DIGIT RP\n                   | DOCTORS LP AVAILABLE RP COLON\n                   | DOCTORS COLON\n                   | SERVICES COLON\n                   | INFO LP ID RP COLON\n                   | UPDATE LP ID COMMA AVAILABILITY RP\n    '
    
_lr_action_items = {'ID':([0,],[2,]),'$end':([1,2,],[0,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'id':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> id","S'",1,None,None,None),
  ('id -> ID','id',1,'p_id','parser.py',7),
  ('name -> NAME','name',1,'p_name','parser.py',10),
  ('ssn -> SSN','ssn',1,'p_ssn','parser.py',13),
  ('birthday -> BIRTHDAY','birthday',1,'p_birthday','parser.py',16),
  ('availability -> AVAILABILITY','availability',1,'p_availability','parser.py',19),
  ('expression -> CREATE name COLON','expression',3,'p_expression','parser.py',28),
  ('expression -> PROTOCOLS COLON','expression',2,'p_expression','parser.py',29),
  ('expression -> BEDS COLON','expression',2,'p_expression','parser.py',30),
  ('expression -> BEDS LP DIGIT RP','expression',4,'p_expression','parser.py',31),
  ('expression -> DOCTORS LP AVAILABLE RP COLON','expression',5,'p_expression','parser.py',32),
  ('expression -> DOCTORS COLON','expression',2,'p_expression','parser.py',33),
  ('expression -> SERVICES COLON','expression',2,'p_expression','parser.py',34),
  ('expression -> INFO LP ID RP COLON','expression',5,'p_expression','parser.py',35),
  ('expression -> UPDATE LP ID COMMA AVAILABILITY RP','expression',6,'p_expression','parser.py',36),
]
