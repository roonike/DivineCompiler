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
    'ID', #'VARIABLE_ID',

    
   
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
##t_ID = r'VARIABLE_ID'

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


def p_program(p):
    'program : bloque_compuesto'
    p[0] = {'name': p_program, p_bloque_compuesto:p[1]}

def p_bloque_compuesto(p):
    '''bloque_compuesto : declaracion_variable bloque_compuesto 
                        | declaracion_funcion bloque_compuesto
                        | asignacion_variable bloque_compuesto
                        | llamada_funcion bloque_compuesto
                        | empty'''
    if len(p) == 2:
        p[0] = {'name': p_bloque_compuesto, p_declaracion_variable: p[1]}
    else:
        p[0] = {'name': p_bloque_compuesto, p_declaracion_variable: p[1]}

def p_declaracion_funcion(p):
    '''declaracion_funcion : TEXT LPAREN parametros RPAREN LBRACKET bloque_compuesto retorno RBRACKET
                            | TEXT LPAREN parametros RPAREN LBRACKET bloque_compuesto RBRACKET '''

def p_parametros(p):
    '''parametros :  list_parametros'''

def p_list_parametros(p):
    '''list_parametros : type TEXT COMA list_parametros
                        | empty'''


def p_retorno(p):
    '''retorno : RETURN TEXT '''
#return 0

def p_type(p):
    ''' type : INT 
            | FLOAT
            | BOOL
            | STRING'''
    p[0] = p[1]


def p_llamada_funcion(p):
    'llamada_funcion : TEXT'
    '''llamada_funcion : ID LPAREN arg_list RPAREN'''
    print(f"Llamada a función: {p[1]}({p[3]})")


# Lista de argumentos separados por comas
def p_arg_list(p):
    '''arg_list : arg_list COMMA ID
                | ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
# sumar(2,2)

def p_declaracion_variable(p):
    'declaracion_variable : TEXT'
#int sumando

def p_expresion(p):
    'expresion : TEXT'  
    #expression PLUS expression
    #LPAREN expression RPAREN'''
    # 5 * 5 + 9(5-2)
    # '''expression : NUMBER
    #               | expression PLUS expression
    #               | expression MINUS expression
    #               | expression TIMES expression
    #               | expression DIVIDE expression
    #               | LPAREN expression RPAREN'''
    # if len(t) == 2:
    #     t[0] = t[1]
    # elif t[2] == '+':
    #     t[0] = t[1] + t[3]
    # elif t[2] == '-':
    #     t[0] = t[1] - t[3]
    # elif t[2] == '*':
    #     t[0] = t[1] * t[3]
    # elif t[2] == '/':
    #     t[0] = t[1] / t[3]
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]

# Función para analizar expresiones
def parse_expression(expression):
    return parser.parse(expression)

def p_asignacion_variable(p):
    '''asignacion_variable : TEXT ASSIGN TEXT SEMICOLON'''
    variable_name = p[1]
    variable_value = p[3]
    print(f"Asignación de variable: {variable_name} = {variable_value}") 
   
# Función para analizar asignaciones de variables
def parse_assignment(assignment):
    return parser.parse(assignment)

# Regla de condición
def p_condition(p):
    print("Expresión condicional:")
    print(f"Expresión: {p[3]}")
    print("Sentencias:")
    for statement in p[6]:
        print(f" - {statement}")

# Regla de lista de sentencias
def p_statements(p):
    '''statements : statements statement
                 | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# Regla de sentencia
def p_statement(p):
    '''statement : TEXT SEMICOLON'''
    p[0] = p[1]

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