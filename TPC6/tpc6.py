import ply.lex as lex
import ply.yacc as yacc 
import sys

tokens = (
    'NUMBER', # 5, 4, 8...
    'ADD',    # +
    'SUB',    # -
    'DIV',    # *
    'MULT',   # /
    'AP',     # (
    'FP'      # )
)

def t_NUMBER(t):
    r"-?\d+"
    t.value = int(t.value)
    return t

t_ADD = r"\+"
t_SUB = r"\-"
t_MULT = r"\*"
t_DIV = r"/"
t_AP = r"\("
t_FP = r"\)"

t_ignore = " \t"

def t_newline(t):
    r"\n"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Símbolo inválido na linha {t.lineno}: {t.value[0]}")
    t.lexer.skip(1)
    pass

lexer = lex.lex()

def p_operation_1(p):
    "operacao : calc"
    p[0] = p[1] 

def p_operation_2(p):
    "operacao : operacao ADD calc"
    p[0] = p[1] + p[3]

def p_operation_3(p):
    "operacao : operacao SUB calc"
    p[0] = p[1] - p[3]

def p_calc_1(p):
    "calc : expressao"
    p[0] = p[1]

def p_calc_2(p):
    "calc : calc MULT expressao"
    p[0] = p[1] * p[3]

def p_calc_3(p):
    "calc : calc DIV expressao "
    p[0] = p[1] / p[3]

def p_expressao_1(p):
    "expressao : NUMBER"
    p[0] = p[1]

def p_expressao_2(p):
    "expressao : AP operacao FP"
    p[0] = p[2]

def p_error(p):
    print("Erro sintático no input!")

parser = yacc.yacc()

for line in sys.stdin:
    line = line.strip()
    if line:
        r = parser.parse(line)
        print("Resultado:", r)