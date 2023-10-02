# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import sys
import ply.lex as lex
import ply.yacc as yacc


# List of token names.   This is always required
tokens = (
    #Control - Frases 
    'FOR', #'lasciate ogne i speranza voi chintrate'
    'IF',#'INFERNO' 
    'WHILE',#'PURGATORIO', 
    'ELSE',#'PARADISO', 
    'DEF', #'MALACODA', 
    'SWITCH', #
    
    
    #Variable
    'INT',#'DRAGHIGNAZZO', 
    'FLOAT',#'FARFARELLO', 
    'BOOL',#'GRAFFIACANE', 
    'STRING', #'CIRIATO',
   
    #IDs
    'TEXT',
    'NUMERO', 
    'REAL',

    #Reserved
    'PLUS', # ALICHINO
    'MINUS', # BARBARICCIA
    'TIMES', # * ARGENTI
    'DIVIDE', # BRUTUS
    'ASSIGN', # BEATRICCE 
    'COMA', # ,
    'RPAREN', #'CAGNAZZO'
    'LPAREN', #'CALCABRINA'
    'RBRACKET',#
    'LBRACKET',#
    'TRUE', #'DANTE',
    'FALSE', #'VERGIL',
    'RETURN', # 'COSA FATTA,CAPPO HA' # RETURN
    'CASE',#'SCARMIGLIONE' 
    'BREAK',#
)


# ----------------- LEXIC ANALYSYS -----------------

# Regular expression rules for simple tokens
t_FOR = r'LASCIATE OGNE I SPERANZA VOI CHINTRATE'
t_IF = r'INFERNO'
t_WHILE = r'PURGATORIO'
t_ELSE = r'PARADISO'
t_DEF = r'MALACODA'
t_SWITCH = r'GUARDA E PASSA'

t_INT = r'DRAGHINAZZO'
t_FLOAT = r'FARFARELLO'
t_BOOL = r'GRAFFICANE'
t_STRING = r'CIRIATO'

t_PLUS    = r'ALICHINO'
t_MINUS   = r'BARBARICCIA'
t_TIMES   = r'ARGENTI'
t_DIVIDE  = r'BRUTUS'
t_ASSIGN = r'BEATTRICE'
t_LPAREN  = r'CALCABRINA'
t_RPAREN  = r'CAGNAZZO'
t_LBRACKET = r'IL SUPPORTO'
t_RBRACKET = r'LA PARENTESI'
t_COMA = r','
t_TRUE = r'DANTE'
t_FALSE = r'VERGIL'
t_CASE = r'SCARMIGLIONE'
t_BREAK = r'NON MI TANGE'



def t_NUMERO(t):
    r'\d+' #numero
    t.value = int(t.value)    
    return t

def t_REAL(t):
    r'\d+\.\d+' #numero.numero
    t.value = float(t.value)    
    return t

def t_ID(t):
    r'([a-z])'    
    return t

def t_TEXT(t):
    r'("[A-Za-z0-9 ,\.]")'
    t.value = str(t.value)
    return t
def t_RETURN(t):
    r'COSA FATTA,CAPPO HA'
    t.value = str(t.value)
    return t
 #A string containing ignored characters (spaces and tabs)
t_ignore  = ' t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

""""
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'n+'
    t.lexer.lineno += len(t.value)

'


"""

# ----------------- SYNTACTIC ANALYSIS -----------------


def p_program(t):
    'program : bloque_compuesto'
    #t[0] = t[1]

def p_bloque_compuesto(t):
    '''bloque_compuesto : declaracion_variable bloque_compuesto 
                        | declaracion_funcion bloque_compuesto
                        | asignacion_variable bloque_compuesto
                        | llamada_funcion bloque_compuesto
                        | empty'''

def p_declaracion_funcion(t):
    '''declaracion_funcion : TEXT parametros LBRACKET bloque_compuesto retorno RBRACKET'''

def p_parametros(t):
    '''declaracion_funcion : LPAREN INT TEXT COMA INT TEXT RPAREN 
                           | LPAREN STRING TEXT COMA STRING TEXT RPAREN'''


def p_retorno(t):
    '''retorno : RETURN INT
                | RETURN STRING
                | RETURN BOOL
                | RETURN FLOAT '''
#return 0

def p_llamada_funcion(t):
    'llamada_funcion : TEXT'
# sumar(2,2)

def p_declaracion_variable(t):
    'declaracion_variable : TEXT'
#int sumando

def p_expresion(t):
    'expresion : TEXT'  
# 5 * 5 + 9(5-2)
def p_asignacion_variable(t):
    'asignacion_variable : TEXT'    
#sumando = 5

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error in input!")

# -----------------  Build the lexer -----------------
lexer = lex.lex()

# Test it out
data = '''3 ALICHINO 4 ARGENTI 10 ALICHINO BARBARICCIA 20 ARGENTI 2'''

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