import q1_pares_e_impares
import q2_ordena_linhas
import q3_ordena_alunos
import q4_dados_alunos
import q5_gravar_nome_idade
import q6_transcrever_informacoes

def main_menu():
    print("=== Menu Principal ===")
    print("Escolha uma opção:")
    print("1 - Separar números pares e ímpares")
    print("2 - Ordenar linhas de um arquivo")
    print("3 - Ordenar alunos por escore")
    print("4 - Inserir dados de alunos em arquivo")
    print("5 - Gerar arquivo com nomes e idades aleatórios")
    print("6 - Transcrever informações de um arquivo para outro")
    print("0 - Sair")

def sub_menu():
    print("\n=== Submenu ===")
    print("Escolha uma opção:")
    print("1 - Executar novamente")
    print("0 - Voltar ao menu principal")

while True:
    main_menu()
    opcao = input("Opção escolhida: ")
    if opcao == "1":
        q1_pares_e_impares.separa_pares_e_impares()
        sub_opcao = input("Deseja executar novamente? (1-Sim, 0-Não)")
        if sub_opcao == "0":
            continue
    elif opcao == "2":
        q2_ordena_linhas.ordena_linhas()
        sub_opcao = input("Deseja executar novamente? (1-Sim, 0-Não)")
        if sub_opcao == "0":
            continue
    elif opcao == "3":
        q3_ordena_alunos.ordena_alunos()
        sub_opcao = input("Deseja executar novamente? (1-Sim, 0-Não)")
        if sub_opcao == "0":
            continue
    elif opcao == "4":
        q4_dados_alunos.dados_alunos()
        sub_opcao = input("Deseja executar novamente? (1-Sim, 0-Não)")
        if sub_opcao == "0":
            continue
    elif opcao == "5":
        q5_gravar_nome_idade.gerar_arquivo()
        sub_opcao = input("Deseja executar novamente? (1-Sim, 0-Não)")
        if sub_opcao == "0":
            continue
    elif opcao == "6":
        q6_transcrever_informacoes.transcrever_informacoes()
        sub_opcao = input("Deseja executar novamente? (1-Sim, 0-Não)")
        if sub_opcao == "0":
            continue
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")