# TPC4 - Analisador Léxico

**Data:** 2025-03-05

## Autor

> **Nome:** Tomás Pinto Rodrigues
> **ID:** A104448
> **Foto:**
>![Foto Perfil](https://github.com/user-attachments/assets/575cd72e-b849-4e66-a39b-5c8552c4e80e)

## Resumo
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases.<br>
Para este trabalho foi utilizada a biblioteca ply.lex<br>
Os tokens que este analisador identifica são os seguintes: <br>
-> Variavéis (VAR)<br>
-> Classes (CLASSE)<br>
-> Strings (STRING)<br>
-> Números inteiros (NUMBER)<br>
-> O ponto '.' (POINT)<br>
-> As chavetas '{' (LBRACE) e '}' (RBRACE)<br>
-> Palavras reservadas como (SELECT),(WHERE),(LIMIT) e o predicado "a"<br>
-> Identificadores não reconhecidos (ID)<br>
Os espaços brancos e os comentários serão ignorados<br>

## Como Utilizar
1. Criar um ficheiro `input.txt` com o input desejado.
2. Executar o programa no terminal:
   ```sh
   python3 tpc4.py > output.txt
   ```
3. O ficheiro `output.txt` será criado com o output.

Para ver o output diretamente no terminal basta fazer 
   ```sh
   python3 tpc4.py
   ```

## Lista de Resultados 
- [Ficheiro de Inputs](input.txt) 
- [Ficheiro de Outputs](output.txt)  