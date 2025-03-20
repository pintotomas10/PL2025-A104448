# TPC6 - Analisador para expressões matemáticas

**Data:** 2025-03-20

## Autor

> **Nome:** Tomás Pinto Rodrigues
> **ID:** A104448
> **Foto:**
>![Foto Perfil](https://github.com/user-attachments/assets/575cd72e-b849-4e66-a39b-5c8552c4e80e)

## Resumo
Construir um programa que simule um analisador para expressões matemáticas.<br>
Para este trabalho foram utilizadas as bibliotecas ply.lex e ply.yacc<br>
Este analisador conhece Números (NUMBER) e as seguintes operações matemáticas: <br>
-> ADD - **Adição** `+` <br>
-> SUB - **Subtração** `-` <br>
-> DIV - **Divisão** `/` <br>
-> MULT - **Multiplicação** `*` <br>
Também reconhece os parenteses, o AP - `(` e o FP - `)` <br>

## Como Utilizar
1. Executar o programa no terminal:
   ```sh
   python3 tpc6.py
   ```
2. O analisador é iniciado e podem ser escritas expressões no terminal: <br>
   Ex.1
   ```sh
   (6 * 6) + 9
   ```
   Ex.2
   ```sh
   9/7 + 5 * 9
   ```
   Ex.3
   ```sh
   (47 * 3) - (33 / 6 + 4)
   ```


## Lista de Resultados 
- Os inputs são as expressões matemáticas realizadas no terminal
- Os outputs são apresentados no terminal de acordo com os comandos realizados