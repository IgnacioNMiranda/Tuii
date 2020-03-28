import ply.lex as lex
import ply.yacc as yacc
import sys


# 'RE':'NombreToken'
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
    'sum': 'SUM',
    'main': 'MAIN',
    'int': 'INT',
    'matrix': 'MATRIX'
}


#Tokens
tokens = [
    'ID',
    'LP',
    'RP',
    'LC',
    'RC',
    'LK',
    'RK',
    'PC',
    'COMA',
    'COMILLA',
    'BV',
    'MAS',
    'MENOS',
    'MUL',
    'DIV',
    'IGUAL',
    'DIGIT',
    'TEXT'
] + list(reserved.values())


#Tokens paréntesis
t_LP = r'\('
t_RP = r'\)'
t_LC = r'\['
t_RC = r'\]'
t_LK = r'\{'
t_RK = r'\}'


#Tokens símbolos
t_PC = r'\;'
t_COMA = r'\,'
t_COMILLA = r'\''
t_BV = r'\|'


#Tokens operadores
t_MAS = r'\+'
t_MENOS = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_IGUAL = r'\='


def t_ID(t):
    r'[A-Za-z]([A-Za-z0-9]){0,14}'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_DIGIT(t):
    r'\-[1-9][0-9]*|[0-9]+'
    t.value = int(t.value)
    return t


def t_TEXT(t):
    r'"[A-Za-z0-9]+"'
    t.type = reserved.get(t.value, 'TEXT')
    return t


def t_COMMENT(t):
    r'\#.*\#'
    pass
    # No considera comentarios


def t_error(t):
    print("Illegal character '{0}'".format(t.value[0]))
    # Tratamiento de errores.
    t.lexer.skip(1)


# Validación de espacios en blanco#
t_ignore = ' \t'


#Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#Ejecución del lexer
lexer = lex.lex()
with open('archivo', 'r') as f:
    contents = f.read()
    lex.input(contents)
    print("Structure: LexToken(type,value,lineno,lexpos)\n")
    for tok in lexer:
        print(tok)



#Reglas de Sintaxis

# ini → main | vacio
def p_ini(p):
    '''
    ini : main
        | vacio
    '''
    print(p[1])


# main → MAIN LK sentence RK
def p_main(p):
    '''
    main : MAIN LK sentence RK
    '''
    p[0] = (p[1], p[2], p[3], p[4])


def p_vacio(p):
    '''
    vacio :
    '''
    p[0] = None


# sentence → single_stmt | if_stmt6 | single_stmt sentence | if_stmt sentence
def p_sentence(p):
    '''
    sentence : single_stmt
            | if_stmt
            | single_stmt sentence
            | if_stmt sentence
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])


# single_stmt → decl | single_op | print
def p_single_stmt(p):
    '''
    single_stmt : decl
                | single_op
                | print
    '''
    p[0] = p[1]


# decl → int_decl | matrix_decl
def p_decl(p):
    '''
    decl : int_decl
        | matrix_decl
    '''
    p[0] = p[1]


# int_decl → INT ID IGUAL term PC
def p_int_decl(p):
    '''
      int_decl : INT ID IGUAL term PC
    '''
    p[0] = ('=', p[1], p[2], p[4], p[5])


# term → DIGIT | ID | sum_function [operator term]
def p_term(p):
    '''
    term : DIGIT
        | ID
        | sum_function operator_term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])


def p_operator_term(p):
    '''
    operator_term : operator_term operator term
                  | vacio
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])


# sum_function → SUM LP ID RP
def p_sum_function(p):
    '''
    sum_function : SUM LP ID RP
    '''
    p[0] = (p[1], p[2], p[3], p[4])


#operator -> MAS | MENOS | MUL | DIV
def p_operator(p):
    '''
    operator : MAS
            | MENOS
            | MUL
            | DIV
    '''
    p[0] = p[1]


#matrix_decl -> MATRIX ID IGUAL LC matrix_value RC PC
def p_matrix_decl(p):
    '''
    matrix_decl : MATRIX ID IGUAL LC matrix_value RC PC
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5],p[6], p[7])


#matrix_value ->  DIGIT [(COMA matrix_value)] [matrix_nextvalue]
def p_matrix_value(p):
    '''
    matrix_value : DIGIT possibly_next_matrix_row_value possibly_next_matrix_row
    '''
    p[0] = (p[1], p[2], p[3])


def p_possibly_next_matrix_row_value(p):
    '''
    possibly_next_matrix_row_value : COMA matrix_value possibly_next_matrix_row_value
                                   | vacio
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])


def p_possibly_next_matrix_row(p):
    '''
    possibly_next_matrix_row : matrix_nextvalue possibly_next_matrix_row
                             | vacio
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])


#matrix_nextvalue -> BV matrix_value
def p_matrix_nextvalue(p):
    '''
    matrix_nextvalue : BV matrix_value
                     | vacio
    '''
    if len(p) == 0:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])


#single_op -> ID IGUAL term
def p_single_op(p):
    '''
    single_op : ID IGUAL term
    '''
    p[0] = (p[2], p[1], p[3])


#print -> PRINT LP (ID | TEXT) RP
def p_print(p):
    '''
    print : PRINT LP ID RP
          | PRINT LP TEXT RP
    '''
    p[0] = p[1]


#if_stmt -> IF ID LK single_stmt RK [ELSE LK single_stmt RK
def p_if_stmt(p):
    '''
    if_stmt : IF ID LK single_stmt RK
            | IF ID LK single_stmt RK ELSE LK single_stmt RK
    '''
    if len(p) == 6:
        p[0] = (p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])


def p_error(p):
    print("Error de sintaxis!!!")
#


#Construcción del analizador sintáctico
parser = yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)
