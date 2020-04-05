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
    t.lexer.lineno += len(t.value)


# Ejecución del lexer
lexer = lex.lex()
with open('archivo.txt', 'r') as f:
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
    print(p[1])
    print(run(p[1]))


# main → MAIN LK sentence RK | MAIN LK vacio RK
def p_main(p):
    '''
    main : MAIN LK sentence RK
         | MAIN LK vacio RK
    '''
    p[0] = p[3]

# vacio →
def p_vacio(p):
    '''
    vacio :
    '''
    p[0] = None


# sentence → single_stmt | if_stmt | sentence single_stmt | sentence if_stmt
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
                | sum_function PC
                | print
    '''
    p[0] = p[1]


# int_decl → INT ID IGUAL term PC
def p_int_decl(p):
    '''
      int_decl : INT ID IGUAL term PC
    '''
    p[0] = ('=', p[2], p[4])

# term → term operator_plus_minus term_2 | term_2
def p_term(p):
    '''
    term : term operator_plus_minus term_2
         | term_2
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term_2(p):
    '''
    term_2 : term_2 operator_mul_div DIGIT
            | term_2 operator_mul_div id
            | term_2 operator_mul_div sum_function
            | DIGIT
            | id
            | sum_function
            | term

    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])


# sum_function → SUM LP ID RP
def p_sum_function(p):
    '''
    sum_function : SUM LP ID RP
    '''
    p[0] = ('sum', p[3])


# operator_plus_minus → MAS | MENOS | MUL | DIV
def p_operator_plus_minus(p):
    '''
    operator_plus_minus : MAS
                        | MENOS
    '''
    p[0] = p[1]


# operator_mul_div → MUL | DIV
def p_operator_mul_div(p):
    '''
    operator_mul_div : MUL
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
    print : PRINT LP ID RP PC
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


# id → ID
def p_id(p):
   '''
   id : ID
   '''
   p[0] = ('var', p[1])


# ERROR
def p_error(p):
    if not p:
        print("Error de Sintaxis")

# Ambiente
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
        elif p[0] == "=":  # Asignación de variables
            env[p[1]] = run(p[2])
            print(env)
        elif p[0] == "if":
            if env[p[1]] > 0:  # Si la variable es > 0 se ejecuta el bloque dentro del if
                return run(p[2])
            elif len(p) > 3 and p[3] == "else":  # Si no se cumple la condicion y el if posee else, este se ejecuta
                return run(p[4])
        elif p[0] == "var":  # Si se asigna a una variable el valor de otra, se recupera su valor
            return env[p[1]]
        elif p[0] == "sum":  # Se imprime el valor de la variable ya que se hace sum a una variable de tipo entero
            return env[p[1]]
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
text = ""
with open('archivo.txt', 'r') as f:
    print("\n\nAnálisis Sintáctico")
    for line in f:
        try:
            text += line
        except EOFError:
            break
parser.parse(text)
