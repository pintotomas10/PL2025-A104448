import re

def markdown_to_html(input):
    pagina_html = []
    lista_ordenada = False 

    for linha in input.split("\n"):
        match = re.match(r'^(#{1,3})\s*(.+)', linha)
        if match:
            nivelTitulo = len(match.group(1)) 
            titulo = match.group(2).strip()
            pagina_html.append(f"<h{nivelTitulo}>{titulo}</h{nivelTitulo}>")
        elif (match := re.match(r'\d+\.\s+(.+)', linha)):  
            if not lista_ordenada:
                pagina_html.append("<ol>")
                lista_ordenada = True
            pagina_html.append(f"<li>{match.group(1)}</li>")
        else:
            if lista_ordenada:
                pagina_html.append("</ol>")
                lista_ordenada = False
            linha = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" style="width: 150px; height: auto; display: block; margin-top: 5px;">', linha) #imagem
            linha = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', linha) #link
            linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha) #negrito
            linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha) #itálico
            pagina_html.append(linha)  
    
    if lista_ordenada:
        pagina_html.append("</ol>")  
    
    return "\n".join(pagina_html)

def convert_markdown_file(ficheiro_input, ficheiro_output):
    with open(ficheiro_input, 'r', encoding='utf-8') as infile: #abertura em modo de leitura
        input = infile.read()
    html_output = markdown_to_html(input)
    with open(ficheiro_output, 'w', encoding='utf-8') as outfile: #abertura em modo de escrita
        outfile.write(html_output)

ficheiro_input = "input.md"
ficheiro_output = "output.html"
convert_markdown_file(ficheiro_input, ficheiro_output)