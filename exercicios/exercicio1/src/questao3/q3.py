with open("alunos.txt", "w") as arquivo:

    while True:
        matricula = input("Digite a matrícula do aluno (ou pressione ENTER para sair): ")
        if not matricula:
            break
        nome = input("Digite o nome do aluno: ")
        ano_ingresso = input("Digite o ano de ingresso do aluno: ")
        escore_atual = input("Digite o escore atual do aluno: ")

        aluno = f"{matricula};{nome};{ano_ingresso};{escore_atual}\n"
        arquivo.write(aluno)

print("Informações de alunos gravadas com sucesso!")