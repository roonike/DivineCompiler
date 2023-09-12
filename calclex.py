# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex

import lex
import yacc

# List of token names.   This is always required
tokens = (
    #Control - Frases
    'lasciate ogne i speranza voi chintrate', #FOR
    'BEATRICCE',
   'INFERNO', # IF
   'PURGATORIO', # WHILE
   'PARADISO', # ELSE
   'RUBICANTE', # RETURN
    'MALACODA', # DEF (la wea para hacer metodos)
    #Variable
   'DRAGHIGNAZZO', # INT
   'FARFARELLO', # FLOAT
   'GRAFFIACANE', # BOOL
   'LIBICOCCO', # STRING
   
    #IDs
    'TEXT',
    'INTEGER', 
    'BOOL',
    'FLOAT',

    #Reserved
   'ALICHINO', # +
   'BARBARICCIA', # -
   'CAGNAZZO', # )
   'CALCABRINA', # (
   'DANTE', # TRUE
   'VERGIL', # FALSE
   'CIRIATO', # STRING
    'SCARMIGLIONE', # ID
)

t_ALICHINO    = r'\+'
t_BARBARICCIA   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_CALCABRINA  = r'\('
t_CAGNAZZO  = r'\)'

"""
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

"""

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOAT(t):
    r'\d+'
    t.value = float(t.value)    
    return t

def t_STRING(t):
    r'\d+'
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
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
"""
# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print(tok)

 
"""
# ----------------- SYNTACTIC ANALYSIS -----------------

states = []
shapes = []
spaceCount = 0


def _log(value, reset=False):
    global spaceCount
    spaceCount += 1
    if(reset):
        spaceCount = 0
    for x in range(spaceCount):
        print(' ', end='')
    print(value)
    return

def p_error(t):
    print(t)
    print("Syntax error at '%s'" % t.value)

def p_ufo_file(t):
    'ufo_file : state_list shape_list event_list'

def p_state_list(t):
    'state_list : STATES_LIST_OPEN state_element STATES_LIST_CLOSE'
    global spaceCount
    spaceCount = 0

def p_state_element(t):
    '''state_element : STATE_OPEN state STATE_CLOSE
                     | state_element state_element'''


def p_state(t):
    'state : STATE'
    states.append(t[1])
    _log('<state>')

def p_shape_list(t):
    'shape_list : SHAPE_LIST_OPEN shape SHAPE_LIST_CLOSE'
    global spaceCount
    spaceCount = 0

def p_shape(t):
    'shape : SHAPE_EMPTY'
def p_shape(t):
    '''shape : SHAPE_OPEN SHAPE SHAPE_CLOSE
                     | shape shape'''

def p_event_list(t):
    'event_list : event'

def p_event(t):
    'event : EVENT_OPEN link date time city state_element country shape duration summary posted images EVENT_CLOSE'
    print('event')
    global spaceCount
    spaceCount = 0

def p_event2(t):
    'event : event event'
    global spaceCount
    spaceCount = 0

def p_link(t):
    'link : LINK_OPEN LINK LINK_CLOSE'
    _log('<link>')

def p_date_empty(t):
    'date : DATE_EMPTY'
    _log('<date>')
def p_date(t):
    'date : DATE_OPEN DATE DATE_CLOSE'
    _log('<date>')

def p_time(t):
    'time : TIME_OPEN TIME TIME_CLOSE'
    _log('<time>')

def p_city_empty(t):
    'city : CITY_EMPTY'
    _log('<city>')
def p_city(t):
    'city : CITY_OPEN CITY CITY_CLOSE'
    _log('<city>')

def p_country(t):
    'country : COUNTRY_OPEN COUNTRY COUNTRY_CLOSE'
    _log('<country>')

def p_duration(t):
    'duration : DURATION_OPEN DURATION DURATION_CLOSE'
    _log('<duration>')
def p_duration_empty(t):
    'duration : DURATION_EMPTY'
    _log('<duration>')


def p_summary_empty(t):
    'summary : SUMMARY_EMPTY'
    _log('<summary>')
def p_summary(t):
    'summary : SUMMARY_OPEN SUMMARY SUMMARY_CLOSE'
    _log('<summary>')

def p_posted(t):
    'posted : POSTED_OPEN POSTED POSTED_CLOSE'
    _log('<posted>')

def p_images_empty(t):
    'images : IMAGES_EMPTY'
    _log('<images>')
def p_images(t):
    'images : IMAGES_OPEN IMAGES IMAGES_CLOSE'
    _log('<images>')


"""