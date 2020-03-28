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


#