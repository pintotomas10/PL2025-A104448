import json
import ply.lex as lex

tokens = ("LISTAR", "MOEDA", "SELECIONAR", "ADICIONAR", "SAIR")

t_LISTAR = r'LISTAR'
t_SAIR = r'SAIR'

def t_MOEDA(t):
    r'MOEDA\s+((\d+[ec](,\s*)?)+)\s+\.'
    t.value = t.value.rstrip(".")[6:].replace(" ", "").split(",")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s+([A-Z0-9]+)'
    t.value = t.value.split()[1]
    return t

def t_ADICIONAR(t):
    r'ADICIONAR\s+([A-Z0-9]+)\s+(\d+)'
    t.value = tuple(t.value.split()[1:])
    t.value = (t.value[0], int(t.value[1]))
    return t

t_ignore = " \t"

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def carregar_stock():
    with open("stock.json", "r", encoding="utf-8") as f:
        return json.load(f)

def atualizar_stock(stock):
    with open("stock.json", "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4, ensure_ascii=False)

def exibir_produtos(stock):
    print(f"{'COD':<8} | {'NOME':<20} | {'QTD':>6} | {'PREÇO (€)':>8}")
    print("-" * 50)
    for item in stock:
        print(f"{item['cod']:<8} {item['nome']:<20} {item['quant']:>6} {item['preco']:>8.2f}€")

def buscar_produto(codigo, stock):
    return next((item for item in stock if item['cod'] == codigo), None)

moedas_disponiveis = {"2e": 200, "1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

def formatar_moeda(valor):
    euros, centimos = divmod(valor, 100)
    return f"{euros}e{centimos}c" if euros and centimos else f"{euros}e" if euros else f"{centimos}c"

def calcular_saldo(moedas, saldo):
    for moeda in moedas:
        if moeda in moedas_disponiveis:
            saldo += moedas_disponiveis[moeda]
        else:
            print(f"Moeda inválida: {moeda}")
    print(f"Saldo: {formatar_moeda(saldo)}")
    return saldo

def dar_troco(saldo):
    if saldo <= 0:
        print("Saldo insuficiente para satisfazer o seu pedido.")
        return None

    troco = saldo
    trocoMoedas = {}  # Dicionário para contar moedas no troco

    # Ordenar moedas do maior para o menor valor
    moedasOrdenadas = sorted(moedas_disponiveis.items(), key=lambda x: -x[1])

    for nome, valor in moedasOrdenadas:
        if troco >= valor:
            quantidade = troco // valor
            trocoMoedas[nome] = quantidade
            troco -= quantidade * valor  # Reduz o saldo restante

    # Criar a string do troco
    trocoEcra = [f"{quantidade}x {moeda}" for moeda, quantidade in trocoMoedas.items()]
    
    if trocoEcra:
        print("Pode retirar o troco: " + ", ".join(trocoEcra) + ".")
    else:
        print("Não há troco a devolver.")


def selecionar_produto(codigo, saldo, stock):
    produto = buscar_produto(codigo, stock)
    if not produto:
        print("Produto não encontrado.")
    elif produto['quant'] == 0:
        print("Produto sem stock.")
    elif saldo < int(produto['preco'] * 100):
        print(f"Saldo insuficiente. Saldo: {formatar_moeda(saldo)}, Necessário: {formatar_moeda(int(produto['preco'] * 100))}")
    else:
        produto['quant'] -= 1
        saldo -= int(produto['preco'] * 100)
        print(f"Produto dispensado: {produto['nome']} - Saldo restante: {formatar_moeda(saldo)}")
    return saldo, stock

def adicionar_produto(parametros, stock):
    produto = buscar_produto(parametros[0], stock)
    if produto:
        produto['quant'] += parametros[1]
        print(f"{parametros[1]} unidades adicionadas a {produto['nome']}. Novo stock: {produto['quant']}.")
    else:
        print("Produto não encontrado.")
    return stock

def maquina_vendas():
    stock = carregar_stock()
    saldo = 0
    print("Sistema iniciado. Stock carregado.")
    while True:
        comando = input(">> ").strip()
        lexer.input(comando)
        tokens = [token for token in lexer]
        if not tokens:
            print("Comando inválido.")
            continue
        if tokens[0].type == "LISTAR":
            exibir_produtos(stock)
        elif tokens[0].type == "MOEDA":
            saldo = calcular_saldo(tokens[0].value, saldo)
        elif tokens[0].type == "SELECIONAR":
            saldo, stock = selecionar_produto(tokens[0].value, saldo, stock)
        elif tokens[0].type == "ADICIONAR":
            stock = adicionar_produto(tokens[0].value, stock)
        elif tokens[0].type == "SAIR":
            if saldo > 0:
                dar_troco(saldo)
            atualizar_stock(stock)
            print("Sessão encerrada. Até logo!")
            break
        else:
            print("Comando não reconhecido.")

if __name__ == "__main__":
    maquina_vendas()
