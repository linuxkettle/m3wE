
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementAND BAND BOR CARET COMMA COMMENT DEC DEC1 DOT ELSE EQ EQUALS FALSE FN FOR GT GTE HYPHEN ID IF IN INC INC1 LBRACE LBRACKET LINECOMMENT LSQ LT LTE NEQ NOT NUMBER OR PLUS RBRACE RBRACKET RSQ SEMI SLASH STAR STRING TRUE WHILEwhile : WHILE expression LBRACE statement RBRACEstatement : for : FOR LBRACKET statement COMMA expression COMMA statement RBRACKET LBRACE statement RBRACEstatement : expressionsum : termexpression : sumstatement : statement SEMI statementforeach : FOR ID IN expression LBRACE statement RBRACEsum : sum HYPHEN sumexpression : NOT expressionstatement : ifsum : sum PLUS sumif : IF expression LBRACE statement RBRACEexpression : sum EQ sumstatement : whileterm : factorif : IF expression LBRACE statement RBRACE ELSE LBRACE statement RBRACEexpression : sum NEQ sumstatement : foreachterm : term STAR termif : IF expression LBRACE statement RBRACE ELSE ifexpression : sum GT sumstatement : forterm : term SLASH termfn : FN ID list LBRACE statement RBRACEexpression : sum LT sumstatement : assignmentfactor : NUMBERexpression : sum GTE sumstatement : fnfactor : NUMBER DOT NUMBERexpression : sum LTE sumfactor : LBRACKET expression RBRACKETexpression : expression AND expressionfactor : HYPHEN NUMBERexpression : expression OR expressionfactor : HYPHEN NUMBER DOT NUMBERexpression : sum BOR sumfactor : ID listexpression : sum BAND sumfactor : IDfactor : listfactor : expression DOT IDfactor : expression CARET NUMBERfactor : TRUEfactor : FALSEfactor : STRINGlist : LBRACKET cpart RBRACKETlist : LSQ cpart RSQcpart : cpart : expressioncpart : cpart COMMA cpartassignment : ID EQUALS expression'
    
_lr_action_items = {'SEMI':([0,1,2,3,4,5,6,7,8,9,14,17,18,20,21,22,23,24,26,41,42,46,48,55,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,84,85,87,88,89,90,94,95,96,97,98,100,102,103,104,105,106,107,108,109,111,112,113,114,],[-2,26,-4,-11,-15,-19,-23,-27,-30,-6,-41,-42,-5,-16,-28,-45,-46,-47,-2,-10,-41,-2,-39,-35,26,-34,-36,-43,-44,-14,-18,-22,-26,-29,-32,-38,-40,-9,-12,-2,-2,26,-53,-33,-48,-20,-24,-31,-49,26,26,-2,-37,-13,-1,-2,26,26,-2,-25,-2,-21,-8,26,26,-17,-2,26,-3,]),'$end':([0,1,2,3,4,5,6,7,8,9,14,17,18,20,21,22,23,24,26,41,42,48,55,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,79,80,81,84,85,87,88,95,96,97,104,106,107,111,114,],[-2,0,-4,-11,-15,-19,-23,-27,-30,-6,-41,-42,-5,-16,-28,-45,-46,-47,-2,-10,-41,-39,-35,-7,-34,-36,-43,-44,-14,-18,-22,-26,-29,-32,-38,-40,-9,-12,-53,-33,-48,-20,-24,-31,-49,-37,-13,-1,-25,-21,-8,-17,-3,]),'NOT':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'IF':([0,26,46,75,76,94,98,101,103,105,112,],[11,11,11,11,11,11,11,11,11,11,11,]),'WHILE':([0,26,46,75,76,94,98,103,105,112,],[12,12,12,12,12,12,12,12,12,12,]),'FOR':([0,26,46,75,76,94,98,103,105,112,],[13,13,13,13,13,13,13,13,13,13,]),'ID':([0,10,11,12,13,15,16,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[14,42,42,42,45,42,52,42,14,42,42,62,42,42,42,42,42,42,42,42,42,42,14,42,42,42,42,14,14,42,42,42,14,14,14,14,14,]),'FN':([0,26,46,75,76,94,98,103,105,112,],[16,16,16,16,16,16,16,16,16,16,]),'NUMBER':([0,10,11,12,15,19,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,56,75,76,77,82,86,92,94,98,103,105,112,],[21,21,21,21,21,55,21,21,21,21,63,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,87,21,21,21,21,95,21,21,21,21,21,21,]),'LBRACKET':([0,10,11,12,13,14,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,42,46,47,49,52,53,54,75,76,77,82,92,94,98,103,105,112,],[15,15,15,15,46,49,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,49,15,15,15,49,15,15,15,15,15,15,15,15,15,15,15,15,]),'HYPHEN':([0,9,10,11,12,14,15,17,18,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,39,40,42,46,47,48,49,53,54,55,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,84,85,87,88,92,94,95,98,103,105,112,],[19,39,19,19,19,-41,19,-42,-5,-16,-28,-45,-46,-47,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-41,19,19,-39,19,19,19,-35,-43,-44,39,39,39,39,39,39,39,39,39,39,19,19,19,-33,-48,19,-5,-5,-31,-49,19,19,-37,19,19,19,19,]),'TRUE':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'FALSE':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'STRING':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'LSQ':([0,10,11,12,14,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,42,46,47,49,52,53,54,75,76,77,82,92,94,98,103,105,112,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'COMMA':([2,3,4,5,6,7,8,9,14,15,17,18,20,21,22,23,24,25,26,41,42,46,48,49,50,51,55,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,78,79,80,81,82,84,85,87,88,93,95,96,97,99,104,106,107,111,114,],[-4,-11,-15,-19,-23,-27,-30,-6,-41,-50,-42,-5,-16,-28,-45,-46,-47,-50,-2,-10,-41,-2,-39,-50,-51,82,-35,82,-51,-7,-34,-36,-43,-44,-14,-18,-22,-26,-29,-32,-38,-40,-9,-12,92,-53,-33,-48,-50,-20,-24,-31,-49,82,-37,-13,-1,103,-25,-21,-8,-17,-3,]),'RBRACE':([2,3,4,5,6,7,8,9,14,17,18,20,21,22,23,24,26,41,42,48,55,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,79,80,81,84,85,87,88,89,90,94,95,96,97,98,100,102,104,105,106,107,109,111,112,113,114,],[-4,-11,-15,-19,-23,-27,-30,-6,-41,-42,-5,-16,-28,-45,-46,-47,-2,-10,-41,-39,-35,-7,-34,-36,-43,-44,-14,-18,-22,-26,-29,-32,-38,-40,-9,-12,-2,-2,-53,-33,-48,-20,-24,-31,-49,96,97,-2,-37,-13,-1,-2,104,107,-25,-2,-21,-8,111,-17,-2,114,-3,]),'RBRACKET':([2,3,4,5,6,7,8,9,14,15,17,18,20,21,22,23,24,26,41,42,48,49,50,51,55,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,79,80,81,82,84,85,87,88,93,95,96,97,103,104,106,107,108,111,114,],[-4,-11,-15,-19,-23,-27,-30,-6,-41,-50,-42,-5,-16,-28,-45,-46,-47,-2,-10,-41,-39,-50,80,81,-35,-51,-7,-34,-36,-43,-44,-14,-18,-22,-26,-29,-32,-38,-40,-9,-12,-53,-33,-48,-50,-20,-24,-31,-49,-52,-37,-13,-1,-2,-25,-21,-8,110,-17,-3,]),'AND':([2,9,14,17,18,20,21,22,23,24,41,42,43,44,48,50,55,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,79,80,81,84,85,87,88,91,95,99,],[27,-6,-41,-42,-5,-16,-28,-45,-46,-47,27,-41,27,27,-39,27,-35,27,27,27,-43,-44,-6,27,-6,-6,-6,-6,-6,-6,-6,-6,-6,27,-33,-48,-5,-5,-31,-49,27,-37,27,]),'OR':([2,9,14,17,18,20,21,22,23,24,41,42,43,44,48,50,55,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,79,80,81,84,85,87,88,91,95,99,],[28,-6,-41,-42,-5,-16,-28,-45,-46,-47,28,-41,28,28,-39,28,-35,28,28,28,-43,-44,-6,28,-6,-6,-6,-6,-6,-6,-6,-6,-6,28,-33,-48,-5,-5,-31,-49,28,-37,28,]),'DOT':([2,9,14,17,18,20,21,22,23,24,41,42,43,44,48,50,55,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,79,80,81,84,85,87,88,91,95,99,],[29,-6,-41,-42,-5,-16,56,-45,-46,-47,29,-41,29,29,-39,29,86,29,29,29,-43,-44,-6,29,-6,-6,-6,-6,-6,-6,-6,-6,-6,29,-33,-48,-5,-5,-31,-49,29,-37,29,]),'CARET':([2,9,14,17,18,20,21,22,23,24,41,42,43,44,48,50,55,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,79,80,81,84,85,87,88,91,95,99,],[30,-6,-41,-42,-5,-16,-28,-45,-46,-47,30,-41,30,30,-39,30,-35,30,30,30,-43,-44,-6,30,-6,-6,-6,-6,-6,-6,-6,-6,-6,30,-33,-48,-5,-5,-31,-49,30,-37,30,]),'LBRACE':([9,17,18,20,21,22,23,24,41,42,43,44,48,55,60,61,62,63,64,66,67,68,69,70,71,72,73,74,80,81,83,84,85,87,88,91,95,101,110,],[-6,-42,-5,-16,-28,-45,-46,-47,-10,-41,75,76,-39,-35,-34,-36,-43,-44,-14,-18,-22,-26,-29,-32,-38,-40,-9,-12,-33,-48,94,-20,-24,-31,-49,98,-37,105,112,]),'RSQ':([9,17,18,20,21,22,23,24,25,41,42,48,55,57,58,60,61,62,63,64,66,67,68,69,70,71,72,73,74,80,81,82,84,85,87,88,93,95,],[-6,-42,-5,-16,-28,-45,-46,-47,-50,-10,-41,-39,-35,88,-51,-34,-36,-43,-44,-14,-18,-22,-26,-29,-32,-38,-40,-9,-12,-33,-48,-50,-20,-24,-31,-49,-52,-37,]),'EQ':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[31,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,31,31,31,31,31,31,31,31,31,31,-33,-48,-5,-5,-31,-49,-37,]),'NEQ':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[32,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,32,32,32,32,32,32,32,32,32,32,-33,-48,-5,-5,-31,-49,-37,]),'GT':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[33,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,33,33,33,33,33,33,33,33,33,33,-33,-48,-5,-5,-31,-49,-37,]),'LT':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[34,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,34,34,34,34,34,34,34,34,34,34,-33,-48,-5,-5,-31,-49,-37,]),'GTE':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[35,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,35,35,35,35,35,35,35,35,35,35,-33,-48,-5,-5,-31,-49,-37,]),'LTE':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[36,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,36,36,36,36,36,36,36,36,36,36,-33,-48,-5,-5,-31,-49,-37,]),'BOR':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[37,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,37,37,37,37,37,37,37,37,37,37,-33,-48,-5,-5,-31,-49,-37,]),'BAND':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[38,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,38,38,38,38,38,38,38,38,38,38,-33,-48,-5,-5,-31,-49,-37,]),'PLUS':([9,14,17,18,20,21,22,23,24,42,48,55,62,63,64,66,67,68,69,70,71,72,73,74,80,81,84,85,87,88,95,],[40,-41,-42,-5,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,40,40,40,40,40,40,40,40,40,40,-33,-48,-5,-5,-31,-49,-37,]),'EQUALS':([14,],[47,]),'STAR':([14,17,18,20,21,22,23,24,42,48,55,62,63,80,81,84,85,87,88,95,],[-41,-42,53,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,-33,-48,53,53,-31,-49,-37,]),'SLASH':([14,17,18,20,21,22,23,24,42,48,55,62,63,80,81,84,85,87,88,95,],[-41,-42,54,-16,-28,-45,-46,-47,-41,-39,-35,-43,-44,-33,-48,54,54,-31,-49,-37,]),'IN':([45,],[77,]),'ELSE':([96,],[101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,26,46,75,76,94,98,103,105,112,],[1,59,78,89,90,100,102,108,109,113,]),'expression':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[2,41,43,44,50,58,2,60,61,65,65,65,65,65,65,65,65,65,65,2,79,58,65,65,2,2,91,58,99,2,2,2,2,2,]),'if':([0,26,46,75,76,94,98,101,103,105,112,],[3,3,3,3,3,3,3,106,3,3,3,]),'while':([0,26,46,75,76,94,98,103,105,112,],[4,4,4,4,4,4,4,4,4,4,]),'foreach':([0,26,46,75,76,94,98,103,105,112,],[5,5,5,5,5,5,5,5,5,5,]),'for':([0,26,46,75,76,94,98,103,105,112,],[6,6,6,6,6,6,6,6,6,6,]),'assignment':([0,26,46,75,76,94,98,103,105,112,],[7,7,7,7,7,7,7,7,7,7,]),'fn':([0,26,46,75,76,94,98,103,105,112,],[8,8,8,8,8,8,8,8,8,8,]),'sum':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[9,9,9,9,9,9,9,9,9,64,66,67,68,69,70,71,72,73,74,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'list':([0,10,11,12,14,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,42,46,47,49,52,53,54,75,76,77,82,92,94,98,103,105,112,],[17,17,17,17,48,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,48,17,17,17,83,17,17,17,17,17,17,17,17,17,17,17,17,]),'term':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,84,85,18,18,18,18,18,18,18,18,18,18,]),'factor':([0,10,11,12,15,25,26,27,28,31,32,33,34,35,36,37,38,39,40,46,47,49,53,54,75,76,77,82,92,94,98,103,105,112,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'cpart':([15,25,49,82,],[51,57,51,93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('while -> WHILE expression LBRACE statement RBRACE','while',5,'p_while','loops.py',2),
  ('statement -> <empty>','statement',0,'p_statement_empty','statements.py',2),
  ('for -> FOR LBRACKET statement COMMA expression COMMA statement RBRACKET LBRACE statement RBRACE','for',11,'p_for','loops.py',6),
  ('statement -> expression','statement',1,'p_statement_expression','statements.py',6),
  ('sum -> term','sum',1,'p_sum_term','numeric.py',7),
  ('expression -> sum','expression',1,'p_expression_sum','expressions.py',10),
  ('statement -> statement SEMI statement','statement',3,'p_statements','statements.py',10),
  ('foreach -> FOR ID IN expression LBRACE statement RBRACE','foreach',7,'p_foreach','loops.py',11),
  ('sum -> sum HYPHEN sum','sum',3,'p_sum_minus','numeric.py',11),
  ('expression -> NOT expression','expression',2,'p_expression_not','expressions.py',14),
  ('statement -> if','statement',1,'p_statement_if','statements.py',14),
  ('sum -> sum PLUS sum','sum',3,'p_sum_plus','numeric.py',15),
  ('if -> IF expression LBRACE statement RBRACE','if',5,'p_if','loops.py',16),
  ('expression -> sum EQ sum','expression',3,'p_expression_eq','expressions.py',18),
  ('statement -> while','statement',1,'p_statement_while','statements.py',18),
  ('term -> factor','term',1,'p_term_factor','numeric.py',19),
  ('if -> IF expression LBRACE statement RBRACE ELSE LBRACE statement RBRACE','if',9,'p_ifelse','loops.py',20),
  ('expression -> sum NEQ sum','expression',3,'p_expression_neq','expressions.py',22),
  ('statement -> foreach','statement',1,'p_statement_foreach','statements.py',22),
  ('term -> term STAR term','term',3,'p_term_times','numeric.py',23),
  ('if -> IF expression LBRACE statement RBRACE ELSE if','if',7,'p_ifelif','loops.py',24),
  ('expression -> sum GT sum','expression',3,'p_expression_gt','expressions.py',26),
  ('statement -> for','statement',1,'p_statement_for','statements.py',26),
  ('term -> term SLASH term','term',3,'p_term_divide','numeric.py',27),
  ('fn -> FN ID list LBRACE statement RBRACE','fn',6,'p_fn','loops.py',28),
  ('expression -> sum LT sum','expression',3,'p_expression_lt','expressions.py',30),
  ('statement -> assignment','statement',1,'p_statement_assignment','statements.py',30),
  ('factor -> NUMBER','factor',1,'p_factor_number','numeric.py',31),
  ('expression -> sum GTE sum','expression',3,'p_expression_gte','expressions.py',34),
  ('statement -> fn','statement',1,'p_statement_fn','statements.py',34),
  ('factor -> NUMBER DOT NUMBER','factor',3,'p_factor_decimal','numeric.py',35),
  ('expression -> sum LTE sum','expression',3,'p_expression_lte','expressions.py',38),
  ('factor -> LBRACKET expression RBRACKET','factor',3,'p_factor_expression','numeric.py',39),
  ('expression -> expression AND expression','expression',3,'p_expression_and','expressions.py',42),
  ('factor -> HYPHEN NUMBER','factor',2,'p_factor_negative','numeric.py',43),
  ('expression -> expression OR expression','expression',3,'p_expression_or','expressions.py',46),
  ('factor -> HYPHEN NUMBER DOT NUMBER','factor',4,'p_factor_ndecimal','numeric.py',47),
  ('expression -> sum BOR sum','expression',3,'p_expression_bor','expressions.py',50),
  ('factor -> ID list','factor',2,'p_factor_fn','numeric.py',51),
  ('expression -> sum BAND sum','expression',3,'p_expression_band','expressions.py',54),
  ('factor -> ID','factor',1,'p_factor_id','numeric.py',55),
  ('factor -> list','factor',1,'p_factor_list','numeric.py',59),
  ('factor -> expression DOT ID','factor',3,'p_factor_attr','numeric.py',63),
  ('factor -> expression CARET NUMBER','factor',3,'p_factor_exp','numeric.py',67),
  ('factor -> TRUE','factor',1,'p_factor_true','numeric.py',71),
  ('factor -> FALSE','factor',1,'p_factor_false','numeric.py',75),
  ('factor -> STRING','factor',1,'p_factor_string','numeric.py',79),
  ('list -> LBRACKET cpart RBRACKET','list',3,'p_clist','numeric.py',89),
  ('list -> LSQ cpart RSQ','list',3,'p_list','numeric.py',93),
  ('cpart -> <empty>','cpart',0,'p_cpart_empty','numeric.py',97),
  ('cpart -> expression','cpart',1,'p_cpart_une','numeric.py',101),
  ('cpart -> cpart COMMA cpart','cpart',3,'p_cpart_mult','numeric.py',105),
  ('assignment -> ID EQUALS expression','assignment',3,'p_assignment','m3s.py',151),
]