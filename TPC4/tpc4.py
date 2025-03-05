import sys
import ply.lex as lex

# Palavras reservadas
keywords = {
    'select': 'SELECT',
    'where': 'WHERE',
    'limit': 'LIMIT'
}

# Palavras reservadas sensíveis a maiúsculas
case_sensitive_keywords = {
    'a': 'TYPE'
}

# Lista de tokens
tokens = ['VAR', 'CLASS', 'NUMBER', 'STRING', 'DOT', 'LBRACE', 'RBRACE', 'IDENTIFIER'] + \
         list(keywords.values()) + list(case_sensitive_keywords.values())

# Tokens fixos
t_DOT = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_VAR(t):
    r'\?[a-zA-Z_]\w*'
    return t

def t_CLASS(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*:[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_STRING(t):
    r'\".*?\"(@[a-zA-Z]+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    lower_value = t.value.lower()
    if lower_value in keywords:
        t.type = keywords[lower_value]
    elif t.value in case_sensitive_keywords:
        t.type = case_sensitive_keywords[t.value]
    return t

def t_COMMENT(t):
    r'\#.*'
    pass  # Comentários são ignorados

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

# Criar o lexer
lexer = lex.lex()

def run_lexer(input_data):
    lexer.input(input_data)
    for token in lexer:
        print(token)

def main():
    with open("input.txt", "r") as file:
        user_input = file.read()
    run_lexer(user_input)

if __name__ == "__main__":
    main()