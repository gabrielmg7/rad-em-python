import random

nomes = ["Alice", "Beatriz", "Caio", "Daniel", "Eduardo", "Felipe", "Gabriela", "Heloísa", "Isabela", "João",
         "Karine", "Larissa", "Marcelo", "Nathália", "Olívia", "Pedro", "Quintino", "Rafael", "Samantha", "Thiago"]

sobrenomes = ["Silva", "Santos", "Pereira", "Oliveira", "Rodrigues", "Ferreira", "Costa", "Alves", "Nascimento",
              "Lima", "Azevedo", "Mendes", "Souza", "Carvalho", "Barbosa", "Gomes", "Ribeiro", "Martins", "Moura", "Rocha"]

n = int(input("Digite o número de nomes a serem gerados: "))

with open("nomes.txt", "w") as arquivo:
    for i in range(n):
        nome = random.choice(nomes)
        sobrenome = random.choice(sobrenomes)
        idade = random.randint(18, 60)
        arquivo.write(f"{nome} {sobrenome};{idade}\n")

print(f"Arquivo com {n} nomes e idades gerado com sucesso!")