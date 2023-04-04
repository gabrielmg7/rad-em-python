with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

linhas_ordenadas = sorted(linhas)

with open('arquivo.txt', 'w') as arquivo:
    for linha in linhas_ordenadas:
        arquivo.write(linha)