def somador(imput):
    on = True  
    somatorio = 0
    resultado = []

    a = 0
    while a < len(imput):  # utilização da função lower() para colocar as letras todas minusculas
        if imput[a:a+2].lower() == "on":
            on = True # como encontrou o on, o on fica True
            a += 2  
        elif imput[a:a+3].lower() == "off":
            on = False # como encontrou o off, o on fica False
            a += 3  
        elif imput[a] == "=":
            resultado.append(somatorio) # como encontra o =, então o valor do somatorio é adicionado ao fim da lista
            a += 1
        elif imput[a].isdigit() and on:
            start = a
            while a < len(imput) and imput[a].isdigit():
                a += 1
            somatorio += int(imput[start:a])
        else:
            a += 1
    return resultado

try:
    while True:
        texto = input("Introduza o texto pretendido (Ctrl+C para sair): ")
        resultado = somador(texto)
        print("Resultado:", resultado)

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo utilizador.")