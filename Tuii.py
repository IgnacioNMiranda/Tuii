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
}


# Tokens
tokens = [
    'ID',
    'LP',
    'RP',
    'LK',
    'RK',
    'PC',
    'COMA',
    'MAS',
    'MENOS',
    'MUL',
    'DIV',
    'IGUAL',
    'DIGIT',
    'TEXT',
] + list(reserved.values())


# Tokens paréntesis
t_LP = r'\('
t_RP = r'\)'
t_LK = r'\{'
t_RK = r'\}'


# Tokens símbolos
t_PC = r'\;'
t_COMA = r'\,'


# Tokens operadores
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
    r'"[A-Za-z0-9: ]+"'
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
t_ignore = " \t"

# Saltos de línea
def t_newline(t):
    r'\n+'
    print("Newline")
    t.lexer.lineno += len(t.value)


# Ejecución del lexer
lexer = lex.lex()
with open('archivo', 'r') as f:
    contents = f.read()
    lex.input(contents)
    print("Análisis Léxico\n\nStructure: LexToken(type,value,lineno,lexpos)")
    for tok in lexer:
        print(tok)


# Reglas de Sintaxis
precedence = (
    ('left', 'IGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MUL', 'DIV'),
)

# ini → main | vacio
def p_ini(p):
    '''
    ini : main
        | vacio
    '''
    print(run(p[1]))


# main → MAIN LK sentence RK
def p_main(p):
    '''
    main : MAIN LK sentence RK
         | MAIN LK vacio RK
    '''
    p[0] = p[3]


def p_vacio(p):
    '''
    vacio :
    '''
    p[0] = None


# sentence → single_stmt | if_stmt | single_stmt sentence | if_stmt sentence
def p_sentence(p):
    '''
    sentence : single_stmt
            | if_stmt
            | sentence single_stmt
            | sentence if_stmt
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('sentence', p[1], p[2])


# single_stmt → int_decl | single_op | print | sum_function
def p_single_stmt(p):
    '''
    single_stmt : int_decl
                | single_op
                | sum_function
                | print
    '''
    p[0] = p[1]


# int_decl → INT ID IGUAL term PC
def p_int_decl(p):
    '''
      int_decl : INT ID IGUAL term PC
    '''
    p[0] = ('=', p[2], p[4])


# term → [term operator] (DIGIT | ID | sum_function)
def p_term(p):
    '''
    term : term operator DIGIT
         | DIGIT
         | term operator id
         | id
         | term operator sum_function
         | sum_function
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])


# sum_function → SUM LP ID RP PC
def p_sum_function(p):
    '''
    sum_function : SUM LP id RP PC
    '''
    p[0] = ('sum', p[3])


# operator → MAS | MENOS | MUL | DIV
def p_operator(p):
    '''
    operator : MAS
            | MENOS
            | MUL
            | DIV
    '''
    p[0] = p[1]


# single_op → ID IGUAL term PC
def p_single_op(p):
    '''
    single_op : ID IGUAL term PC
    '''
    p[0] = ('=', p[1], p[3])


# print → PRINT LP (ID | TEXT) RP PC
def p_print(p):
    '''
    print : PRINT LP id RP PC
          | PRINT LP TEXT RP PC
    '''
    p[0] = ('print', p[3])


# if_stmt → IF LP ID RP LK sentence RK [ELSE LK sentence RK]
def p_if_stmt(p):
    '''
    if_stmt : IF LP ID RP LK sentence RK
            | IF LP ID RP LK sentence RK ELSE LK sentence RK
    '''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if', p[3], p[6], 'else', p[10])


def p_id(p):
   '''
   id : ID
   '''
   p[0] = ('var', p[1])


def p_error(p):
    if not p:
        print("Error de Sintaxis")
#


#Ambiente
env = {}


def run(p):
    if type(p) == tuple:
        if p[0] == "+":
            return run(p[1]) + run(p[2])
        elif p[0] == "-":
            return run(p[1]) - run(p[2])
        elif p[0] == "*":
            return run(p[1]) * run(p[2])
        elif p[0] == "/":
            return run(p[1]) / run(p[2])
        elif p[0] == "=":
            env[p[1]] = run(p[2])
            print(env)
        elif p[0] == "if":
            if env[p[1]] > 0:
                return run(p[2])
            elif len(p) > 3 and p[3] == "else":
                return run(p[4])
        elif p[0] == "var":
            return env[p[1]]
        elif p[0] == "sum":
            print(env[p[1]])
        elif p[0] == "print":
            try:
                print(env[p[1]])  # En caso de ser una variable, imprime su valor
            except KeyError:
                print(p[1][1:-1])  # En caso de ser un string, lo imprime sin las comillas
        elif p[0] == "sentence":
            run(p[1])
            run(p[2])
    else:  # Reconoce un numero y lo retorna
        return p


# Construcción del analizador sintáctico
parser = yacc.yacc()

with open('archivo', 'r') as f:
    print("\n\nAnálisis Sintáctico")
    for line in f:
        try:
            yacc.parse(line)
        except EOFError:
            break
