# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import sys
from symbol_table import crea_variable
from generation import code, define
import ply.lex as lex
import ply.yacc as yacc

#for symbol_table
symbol_table = {}
reserved = 0

# List of token names.   This is always required
tokens = (
    #Control - Frases 
    'FOR', #'lasciate ogne i speranza voi chintrate'
    'IF',#'INFERNO' 
    'WHILE',#'PURGATORIO', 
    'ELSE',#'PARADISO', 
    'DEF', #'MALACODA', 
    
    
    #Variable
    'INT',#'DRAGHIGNAZZO', 
    'FLOAT',#'FARFARELLO', 
    'BOOL',#'GRAFFIACANE', 
    'STRING', #'CIRIATO',
    'ID', #'VARIABLE_ID',

    #IDs
    'TEXT',
    'NUMERO', 
    'REAL',

    #Reserved
    'PLUS', # ALICHINO
    'MINUS', # BARBARICCIA
    'TIMES', # ARGENTI
    'DIVIDE', # BRUTUS
    'ASSIGN', # BEATRICCE 
    'COMA', # ,
    'IGUALIGUAL',
    "NOIGUAL",
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'AND',
    'OR',
    'RPAREN', #'CAGNAZZO'
    'LPAREN', #'CALCABRINA'
    'RBRACKET',#
    'LBRACKET',#
    'SINGLEQUOTES',
    'DOUBLEQUOTES',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'TRUE', #'DANTE',
    'FALSE', #'VERGIL',
    'RETURN', # 'COSA FATTA,CAPPO HA' 
)


# ----------------- LEXIC ANALYSYS -----------------

# Regular expression rules for simple tokens
t_FOR = r'LASCIATE_OGNE_I_SPERANZA_VOI_CHINTRATE'
t_IF = r'INFERNO'
t_WHILE = r'PURGATORIO'
t_ELSE = r'PARADISO'
t_DEF = r'MALACODA'

t_INT = r'DRAGHINAZZO'
t_FLOAT = r'FARFARELLO'
t_BOOL = r'GRAFFICANE'
t_STRING = r'CIRIATO'
##t_ID = r'VARIABLE_ID'

t_PLUS    = r'ALICHINO'
t_MINUS   = r'BARBARICCIA'
t_TIMES   = r'ARGENTI'
t_DIVIDE  = r'BRUTUS'
t_ASSIGN = r'BEATTRICE'
t_LPAREN  = r'CALCABRINA'
t_RPAREN  = r'CAGNAZZO'
t_LBRACKET = r'IL_SUPPORTO'
t_RBRACKET = r'LA_PARENTESI'
t_COMA = r','
t_IGUALIGUAL = r'=='
t_NOIGUAL = r'!='
t_MAYORQUE = r'<'
t_MENORQUE = r'>'
t_MAYORIGUAL = r'<='
t_MENORIGUAL = r'>='
t_AND = r'E'
t_OR = r'O'
t_SINGLEQUOTES = r'CHERUBINO'
t_DOUBLEQUOTES = r'CHERUBINOS'
t_PUNTOCOMA = r'GUARDA_E_PASSA'
t_DOSPUNTOS = r'DOSPUNTOS'
t_TRUE = r'DANTE'
t_FALSE = r'VERGIL'


def t_RETURN(t):
    r'COSA_FATTA_CAPPO_HA'
    t.value = str(t.value)
    return t

def t_NUMERO(t):
    r'\d+' #numero
    t.value = int(t.value)    
    return t

def t_REAL(t):
    r'\d+\.\d+' #numero.numero
    t.value = float(t.value)    
    return t

def t_ID(t):
    r'[a-z]+'    
    return t

def t_TEXT(t):
    r'("[A-Za-z0-9 ,\.]")'
    t.value = str(t.value)
    return t
 #A string containing ignored characters (spaces and tabs)
t_ignore  = ' t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# ----------------- SYNTACTIC ANALYSIS -----------------

#raiz del programa
def p_program(t):
    '''
    program : statement
        | program statement
    '''
    pass


# Producciones para declaracion de variables

def p_declaration(t):
    '''
    declaration : init_declarator PUNTOCOMA
        | declarator ASSIGN function_call 
    '''
    pass
    
    
def p_init_declarator(t):
    '''
    init_declarator : declarator
        | declarator ASSIGN assignment_expression
    '''
    pass

    
def p_declarator(t):
    '''
    declarator : ID DOSPUNTOS type_specifier
        | NUMERO ID DOSPUNTOS type_specifier
    '''
    correcto, address = (crea_variable(t[2], t[4]) )
    if not correcto:
        print(f"Error: variable {t[2]} redefinida en la linea {t.lexer.lineno}")
    else:
        define(f"{t[2]}: RESB {address}")
    pass


#Especificaciones de tipos de variables

def p_type_specifier(t):
    '''
    type_specifier : INT
        | FLOAT
        | STRING
        | BOOL
    '''
    t[0] = t[1]
    pass
def p_literal(t):
    '''
    literal : NUMERO
        | REAL
        | STRING
    '''
    t[0] = t[1]
    pass  
# Expresiones con operadores
def p_primary_expression(t):
    '''
    primary_expression : ID
        | literal
        | LPAREN assignment_expression RPAREN
    '''
    t[0] = t[1]
    pass
def p_additive_expression(t):
    '''
    additive_expression : primary_expression          
        | additive_expression PLUS primary_expression
        | additive_expression MINUS primary_expression
    '''
    op = ""
    if len(t) > 2:
        t[0] = (False, "R1")
    else:
        t[0] = t[1]
    pass
def p_multiplicative_expression(t):
    '''
    multiplicative_expression : additive_expression
        | multiplicative_expression TIMES additive_expression
        | multiplicative_expression DIVIDE additive_expression
    '''
    op = ""
    #Cuidado con los () que aun no tienen soporte
    if len(t) > 2 and t[1] != "(":
        t[0] = (False, "R1")
    else:
        t[0] = t[1]
    pass
def p_relational_expression(t):
    '''
    relational_expression : multiplicative_expression
        | relational_expression MENORQUE multiplicative_expression
        | relational_expression MAYORQUE multiplicative_expression
        | relational_expression MENORIGUAL multiplicative_expression
        | relational_expression MAYORIGUAL multiplicative_expression
    '''
    #Suponga que el CMP puede retornar el resultado a un registro
    #Para no hacer toda la implementacion por ahora
    if len(t) > 3:
        t[0] = "R1"
    t[0] = t[1]
def p_equality_expression(t):
    '''
    equality_expression : relational_expression
        | equality_expression IGUALIGUAL relational_expression
        | equality_expression NOIGUAL relational_expression
    '''
    if len(t) > 3:
        t[0] = "R1"
    t[0] = t[1]
def p_and_expression(t):
    '''
    and_expression : equality_expression
        | and_expression AND equality_expression
    '''
    op = ""
    if len(t) > 3:
        t[0] = "R1"
    t[0] = t[1]
def p_or_expression(t):
    '''
    or_expression : and_expression
        | or_expression OR and_expression
    '''
    op = ""
    if len(t) > 3:
        t[0] = "R1"
    t[0] = t[1]
def p_assignment_expression(t):
    '''
    assignment_expression : or_expression
        | primary_expression ASSIGN multiplicative_expression
    '''
    t[0] = t[1]
    pass  
# Sentencia
def p_statement(t):
    '''
    statement : function_call
        | compound_statement
        | assignment_statement 
        | function_definition
        | declaration
        | selection_statement
        | iteration_statement
    '''
    pass
def p_statement_list(t):
    '''
    statement_list : statement
        | statement_list statement
    '''
def p_compound_statement(t):
    '''
    compound_statement : LPAREN RPAREN
        | LPAREN statement_list RPAREN
    '''
def p_assignment_statement(t):
    '''
    assignment_statement : assignment_expression PUNTOCOMA
        | primary_expression ASSIGN function_call
    '''
    pass
def p_ID_list(t):
    '''
    ID_list : empty 
        | ID DOSPUNTOS type_specifier
        | ID_list COMA ID  DOSPUNTOS  type_specifier
    '''
def p_parameter_list(t):
    '''
    parameter_list : empty 
        | assignment_expression
        | parameter_list COMA assignment_expression
    '''
# Definicion de funciones
def p_function_definition(t):
    '''
    function_definition : DEF ID LPAREN ID_list RPAREN compound_statement
    '''
#function_definition : FUNC ID LPAREN ID_list RPAREN ARROW
#type_specifier compound_statement

def p_function_call(t):
    '''
    function_call : ID LPAREN parameter_list RPAREN PUNTOCOMA
    '''
# Definicion de condicionales
def p_selection_statement(t):
    '''
    selection_statement : IF assignment_expression compound_statement
        | IF assignment_expression compound_statement ELSE compound_statement
    '''
# Definicion de los loops
def p_iteration_statement(t):
    '''
    iteration_statement : FOR LPAREN NUMERO RPAREN
    '''


    #iteration_statement : FROM BOX_PAR_OPEN assignment_expression COMA #assignment_expression BOX_PAR_CLOSE DOSPUNTOS INC_OP #compound_statement
    #    | FROM BOX_PAR_OPEN assignment_expression COMA #assignment_expression BOX_PAR_CLOSE DOSPUNTOS DEC_OP #compound_statement
    #    | WHILE assignment_expression compound_statement



def p_empty(p):
    'empty :'
    pass


# Manejo de errores de sintaxis 
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token: {p.value}")
    else:
        print("Error de sintaxis al final del archivo")

# -----------------  Build the lexer -----------------
lexer = lex.lex()

# Test it out
#data = '''italia BEATTRICE 0 LASCIATE_OGNE_I_SPERANZA_VOI_CHINTRATE CALCABRINA 5 CAGNAZZO italiados BEATTRICE italiatres ALICHINO 1'''
data = '''2 ALICHINO 1 GUARDA_E_PASSA'''
            

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print(tok)

parser = yacc.yacc()
parser.parse(data)
# ----------------------------------------------------
'''
EJEMPLOS
1)
italia = 0
for 5
	italia = italia + 1
return italia

--------------------------------------------------------------
italia beatricce 0
lasciate ogne i speranza voi chintrate 5 
	italia = italia alichino 1
cosa fatta cappo ha italia

2)
roma = 476
constantinopla = 1453
constantino = 0

if constantinopla > italia
	constantino = constantinopla - roma
return constantino

---------------------------------------------------------------
roma beatricce 476
constantinopla beatricce 1453
constantino beatricce 0

inferno constantinopla > italia
	constantino beatricce constantinopla barbariccia roma
cosa fatta cappo ha constantino

3)

def ciao mondo()
viaggiatore = true
ciao mondo = ""
if viaggiatore = true
	ciao mondo = "ciao mondo"
if viaggiatore = false
	ciao mondo = "arrivederci"
return ciao mondo

----------------------------------------------------------------
def ciao mondo cagnazzo calcabrina
viggiatore beatricce dante
ciao mondo beatricce cherubinos cherubinos
inferno viaggiatore beatricce dante
	ciao mondo beatricce cherubinos ciao mondo cherubinos
inferno viaggiatore beatricce vergil
	ciao mondo beatricce cherubinos arriverci cherubinos
cosa fatta cappo ha ciao mondo




'''