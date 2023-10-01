# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import sys
import ply.lex as lex
import ply.yacc as yacc

##import yacc

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
    'INT'#'DRAGHIGNAZZO', 
    'FLOAT'#'FARFARELLO', 
    'BOOL'#'GRAFFIACANE', 
    'STRING', #'CIRIATO',
    'BOOL', # 
   
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

# Regular expression rules for simple tokens
t_FOR = r'LASCIATE OGNE I SPERANZA VOI CHINTRATE'
t_IF = r'INFERNO'
t_WHILE = r'PURGATORIO'
t_ELSE = r'PARADISO'
t_DEF = r'MALACODA'
t_SWITCH = r'GUARDA E PASSA'

##t_INT = r'DRAGHINAZZO'
##t_FLOAT = r'FARFARELLO'
t_BOOL = r'GRAFFICANE'
##t_STRING = r'CIRIATO'

t_PLUS    = r'ALICHINO'
t_MINUS   = r'BARBARICCIA'
t_TIMES   = r'ARGENTI'
t_DIVIDE  = r'BRUTUS'
t_ASSIGN = r'BEATTRICE'
t_LPAREN  = r'CALCABRINA'
t_RPAREN  = r'CAGNAZZO'
t_LBRACKET = r'IL SUPPORTO'
t_RBRACKET = r'LA PARENTESI'
t_TRUE = r'DANTE'
t_FALSE = r'VERGIL'
##t_RETURN = r'COSA FATTA,CAPPO HA'
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

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
"""

 


# -----------------  Build the lexer -----------------
lexer = lex.lex()

# Test it out
data = '''3ALICHINO4ARGENTI10ALICHINOBARBARICCIA20ARGENTI2'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print(tok)

# -----------------  Build the lexer -----------------