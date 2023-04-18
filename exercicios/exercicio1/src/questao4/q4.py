
with open("alunos.txt", "r") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    # separa os valores da linha
    valores = linha.strip().split(";")
    matricula, nome, ano_ingresso, escore_atual = valores

    if float(escore_atual) < 6.0:
        frase = "em fase de adaptação"
    elif 6.0 <= float(escore_atual) <= 7.0:
        frase = "familiarizado com o curso"
    elif 7.0 < float(escore_atual) < 8.5:
        frase = "em excelência no curso"
    else:
        frase = "Nasceu para o curso"

    print(f"{nome} está {frase}.")