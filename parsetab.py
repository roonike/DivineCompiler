
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BOOL BREAK CASE DEF DIVIDE ELSE FALSE FLOAT FOR IF INT LBRACKET LPAREN MINUS NUMERO PLUS RBRACKET REAL RETURN RPAREN STRING SWITCH TEXT TIMES TRUE WHILEprogram : bloque_compuestobloque_compuesto : declaracion_variable bloque_compuesto \n                        | declaracion_funcion bloque_compuesto\n                        | asignacion_variable bloque_compuesto\n                        | llamada_funcion bloque_compuesto\n                        | emptydeclaracion_funcion : TEXT LPAREN llamada_funcion : declaracion_variable : expresion : asignacion_variable : empty :'
    
_lr_action_items = {'TEXT':([0,3,4,5,6,13,],[8,8,8,8,8,-7,]),'$end':([0,1,2,3,4,5,6,7,9,10,11,12,13,],[-8,0,-1,-8,-8,-8,-8,-6,-2,-3,-4,-5,-7,]),'LPAREN':([8,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'bloque_compuesto':([0,3,4,5,6,],[2,9,10,11,12,]),'declaracion_variable':([0,3,4,5,6,],[3,3,3,3,3,]),'declaracion_funcion':([0,3,4,5,6,],[4,4,4,4,4,]),'asignacion_variable':([0,3,4,5,6,],[5,5,5,5,5,]),'llamada_funcion':([0,3,4,5,6,],[6,6,6,6,6,]),'empty':([0,3,4,5,6,],[7,7,7,7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> bloque_compuesto','program',1,'p_program','calclex.py',136),
  ('bloque_compuesto -> declaracion_variable bloque_compuesto','bloque_compuesto',2,'p_bloque_compuesto','calclex.py',140),
  ('bloque_compuesto -> declaracion_funcion bloque_compuesto','bloque_compuesto',2,'p_bloque_compuesto','calclex.py',141),
  ('bloque_compuesto -> asignacion_variable bloque_compuesto','bloque_compuesto',2,'p_bloque_compuesto','calclex.py',142),
  ('bloque_compuesto -> llamada_funcion bloque_compuesto','bloque_compuesto',2,'p_bloque_compuesto','calclex.py',143),
  ('bloque_compuesto -> empty','bloque_compuesto',1,'p_bloque_compuesto','calclex.py',144),
  ('declaracion_funcion -> TEXT LPAREN','declaracion_funcion',2,'p_declaracion_funcion','calclex.py',147),
  ('llamada_funcion -> <empty>','llamada_funcion',0,'p_llamada_funcion','calclex.py',153),
  ('declaracion_variable -> <empty>','declaracion_variable',0,'p_declaracion_variable','calclex.py',157),
  ('expresion -> <empty>','expresion',0,'p_expresion','calclex.py',161),
  ('asignacion_variable -> <empty>','asignacion_variable',0,'p_asignacion_variable','calclex.py',164),
  ('empty -> <empty>','empty',0,'p_empty','calclex.py',168),
]