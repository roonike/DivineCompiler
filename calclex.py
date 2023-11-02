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
    'TIMES', # ARGENTI
    'DIVIDE', # BRUTUS
    'ASSIGN', # BEATRICCE 
    'COMA', # ,
    'IGUALIGUAL',
    'MAYORQUE',
    'MENORQUE',
    'AND',
    'OR',
    'RPAREN', #'CAGNAZZO'
    'LPAREN', #'CALCABRINA'
    'RBRACKET',#
    'LBRACKET',#
    'SINGLEQUOTES'
    'DOUBLEQUOTES' 
    'TRUE', #'DANTE',
    'FALSE', #'VERGIL',
    'RETURN', # 'COSA FATTA,CAPPO HA' # RETUR N
    'CASE',#'SCARMIGLIONE' 
    'BREAK',#
)


# ----------------- LEXIC ANALYSYS -----------------

# Regular expression rules for simple tokens
t_FOR = r'LASCIATE_OGNE_I_SPERANZA_VOI_CHINTRATE'
t_IF = r'INFERNO'
t_WHILE = r'PURGATORIO'
t_ELSE = r'PARADISO'
t_DEF = r'MALACODA'
t_SWITCH = r'GUARDA_E_PASSA'

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
t_MAYORQUE = r'<'
t_MENORQUE = r'>'
t_AND = r'E'
t_OR = r'O'
t_SINGLEQUOTEs = r'cherubino'
t_DOUBLEQOTES = r'cherubinos'
t_TRUE = r'DANTE'
t_FALSE = r'VERGIL'
t_CASE = r'SCARMIGLIONE'
t_BREAK = r'NON_MI_TANGE'


def t_RETURN(t):
    r'COSA_FATTA_CAPPO_HA'
    t.value = str(t.value)
    return t

t_COMA = r','
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
def p_program(p):
    'program : statement'

# Bloques de Codigo

def p_statement(p):
    '''statement : function_call
                    | compound_statement
                    | function_declaration
                    | assign_statement
                    | if_statement
                    | cycle_statement'''

def p_statement_list(p):
    '''statement_list : statement
                        | statement_list statement'''
                        
def p_compound_statement(p):
    '''compound_statement : LPAREN RPAREN
                            | LPAREN statement_list RPAREN'''

def p_assign_statement(p):
    ''' assign_statement : var_declaration 
                        | var_assign'''

def p_parameters(p):
    '''parametros : empty
                    | var_declaration
                    | parametros COMA var_declaration'''

def p_cycle_statement(p):
    '''cycle_statement : FOR LPAREN lit RPAREN LBRACK'''
                

# Funciones

def p_function_call(p):
    '''function_call : empty'''

def p_function_declaration(p):
    '''function_declaration : empty'''
    
# IF ELSE

def p_if_statement(p):
    '''if_statement : empty'''
    
                        
#declarasion y declaracion con asignacion
def p_var_declaration(p): 
    '''var_declaration : type ID '''

#assignacion
def p_var_assign(p):
    '''var_assign : ID ASSIGN exp'''

def p_type(p):
    ''' type : INT 
            | FLOAT
            | BOOL
            | STRING'''
    p[0] = p[1]   



def p_retorno(p):
    '''retorno : RETURN ID '''

def p_llamada_funcion(p):
    'llamada_funcion : TEXT'
    '''llamada_funcion : ID LPAREN arg_list RPAREN'''
    print(f"Llamada a función: {p[1]}({p[3]})")

def p_operador_binario(p):
  '''operador_binario : exp TIMES exp
           | exp PLUS exp
           | exp DIVIDE exp
           | exp MINUS exp
           | var ASSIGN exp
           | exp IGUALIGUAL exp
           | exp MENORQUE exp
           | exp MAYORQUE exp
           | exp AND exp
           | exp OR exp'''

def p_exp(p):
    '''exp : INT 
            | FLOAT'''


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
data = '''italia BEATTRICE 0 LASCIATE_OGNE_I_SPERANZA_VOI_CHINTRATE CAGNAZZO 5 CALCABRINA
            italia BEATTRICE ALICHINO 1
            COSA_FATTA_CAPPO_HA italia'''
            

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