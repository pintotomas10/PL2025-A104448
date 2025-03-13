# TPC5 - Maquina de Vending

**Data:** 2025-03-13

## Autor

> **Nome:** Tomás Pinto Rodrigues
> **ID:** A104448
> **Foto:**
>![Foto Perfil](https://github.com/user-attachments/assets/575cd72e-b849-4e66-a39b-5c8552c4e80e)

## Resumo
Construir um programa que simule uma máquina de vending.<br>
Para este trabalho foi utilizada a biblioteca ply.lex<br>
Esta máquina de vending suporta as seguintes operações: <br>
-> LISTAR - listar os produtos da máquina<br>
-> MOEDA - adicionar moedas á maquina <br>
-> SELECIONAR - selecionar um produto da máquina<br>
-> ADICIONAR - adicionar stock a um produto<br>
-> SAIR - sair da máquina recebendo o troco<br>

## Como Utilizar
1. Executar o programa no terminal:
   ```sh
   python3 tpc5.py
   ```
2. A maquina é iniciada e podem ser realizados os seguintes comandos: <br>
   2.1. Utilizar o LISTAR para ver os produtos em formato de lista
   ```sh
   LISTAR
   ```
   2.2. Utilizar o MOEDA com as moedas pretendidas separadas por virgulas e com . no fim da linha
   ```sh
   MOEDA 1e, 50c .
   ```
   2.3. Utilizar o SELECIONAR com o produto pretendido á frente
   ```sh
   SELECIONAR B12
   ```
   2.4. Utilizar o ADICIONAR seguido do produto que se pretende adicionar seguido da quantidade a adicionar
   ```sh
   ADICIONAR A23 2
   ```
   2.5. Utilizar o SAIR para fechar á maquina recebendo assim o troco
   ```sh
   SAIR
   ```


## Lista de Resultados 
- [Ficheiro de Inputs](stock.json) 
- Os outputs são apresentados no terminal de acordo com os comandos realizados