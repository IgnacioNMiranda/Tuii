import ply.lex as lex
import ply.yacc as yacc
#import sys


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
#Fin de la ejecución del lexer


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

# sentence → single_stmt | if_stmt6 | single_stmt sentence | if_stmt sentence
def p_sentence(p):
    '''
    sentence : single_stmt
            | if_stmt6
            | single_stmt sentence
            | if_stmt sentence
    '''
    if len(p) == 2:
        p[0] = Atom(p[1], 1)
    elif len(p) == 3:
        p[0] = Atom(p[1], p[2])

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
        | sum_function [operator term]
    '''
    #???????? khie pero khie

# sum_function → SUM LP ID RP
def p_sum_function(p):
    '''
    sum_function : SUM LP ID RP
    '''
    p[0] = (p[1], p[2], p[3], p[4])
