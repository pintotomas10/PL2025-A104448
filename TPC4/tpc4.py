import sys
import re 
import ply.lex as lex

# Palavras reservadas
tokens = (
    'SELECT', 
    'WHERE', 
    'LIMIT', 
    'TYPE',
    'VAR', 
    'CLASSE', 
    'NUMBER', 
    'STRING', 
    'POINT', 
    'LBRACE', 
    'RBRACE',
    'ID'
    )

t_POINT = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Procura SELECT
def t_SELECT(t):
    r'(?i)select'
    return t

# Procura WHERE
def t_WHERE(t):
    r'(?i)where'
    return t

# Procura LIMIT
def t_LIMIT(t):
    r'(?i)limit'
    return t

# Procura TYPE
def t_TYPE(t):
    r'\ba\b'
    return t

# Procura CLASSE 
def t_CLASSE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*:[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Procura NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Procura STRING
def t_STRING(t):
    r'\".*?\"(@[a-zA-Z]+)?'
    return t

# Procura COMMENT e ignora
def t_COMMENT(t):
    r'\#.*'
    pass # descartar os comentários

# Procura VAR
def t_VAR(t):
    r'\?[a-zA-Z_]\w*'
    return t

# Procura ID
def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

# Procura New Line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignora espaços e tabs    
t_ignore = ' \t'

# Define o resto como erro
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Criar o lexer
lexer = lex.lex()


def test_lexer(data):
    lexer.input(data)
    for tok in lexer:
        print(tok)

def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        query = file.read()  # Lê o conteúdo do ficheiro
    test_lexer(query)  # Processa os tokens normalmente

if __name__ == "__main__":
    main()
