# Abrir o arquivo CSV no modo leitura
with open("obras.csv", "r", encoding="utf-8") as file:

    armazena_linha = ""  
    dados = []
    aspas = False  # para identificar se estamos dentro de um campo entre aspas
    cabecalho = []
    dados_obra = {}
    linha_atual = 0
    contador = 0

    for linha in file:
        posicao = 0
        if linha_atual == 0:  # cabeçalho
            cabecalho = linha.split(";")  
            cabecalho = [campo.strip() for campo in cabecalho]  # remover o \n
            linha_atual += 1
        else:
            while posicao < len(linha):
                caractere = linha[posicao]
                if caractere == '"':
                    if aspas and posicao + 1 < len(linha) and linha[posicao + 1] == '"':
                        armazena_linha += '"'
                        posicao += 1  # avança para depois do segundo "
                    else:
                        aspas = not aspas  # alterna o estado de aspa
                elif caractere == ";" and not aspas:  # ";" encontrado e fora de aspas
                    dados_obra[cabecalho[contador]] = armazena_linha
                    armazena_linha = ""
                    contador += 1
                elif caractere == '\n' and not aspas:
                    dados_obra[cabecalho[contador]] = armazena_linha
                    dados.append(dados_obra)
                    contador = 0
                    armazena_linha = ""
                    dados_obra = {}
                else:
                    armazena_linha += caractere
                posicao += 1
    if contador != 0:
        dados_obra[cabecalho[contador]] = armazena_linha
        dados.append(dados_obra)

# Listar compositores
compositores_lista = []
for obra in dados:
    compositor = obra['compositor']
    if compositor not in compositores_lista:
        compositores_lista.append(compositor)

compositores_ordenados = sorted(compositores_lista)
print("Compositores:")
print(compositores_ordenados)

# Distribuição de obras por período
distribuicao_por_periodo = {}
for obra in dados:
    periodo = obra['periodo']
    if periodo in distribuicao_por_periodo:
        distribuicao_por_periodo[periodo] += 1
    else:
        distribuicao_por_periodo[periodo] = 1
print("\nDistribuição das Obras por Período:")
for periodo, quantidade in distribuicao_por_periodo.items():
    print(f"{periodo}: {quantidade}")

# Dicionário associando períodos a títulos das obras
obras_por_periodo = {}
for obra in dados:
    periodo = obra['periodo']
    nome_obra = obra['nome']
    if periodo in obras_por_periodo:
        obras_por_periodo[periodo].append(nome_obra)
    else:
        obras_por_periodo[periodo] = [nome_obra]
for periodo in obras_por_periodo:
    obras_por_periodo[periodo].sort()
print("\nObras por Período:")
for periodo, titulos in obras_por_periodo.items():
    print(f"Período: {periodo}\nTítulos das Obras: {titulos}")
