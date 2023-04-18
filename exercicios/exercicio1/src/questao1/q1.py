with open('arquivo_de_entrada.txt', 'r') as arquivo_entrada:
    numeros_pares = []
    numeros_impares = []
    
    for linha in arquivo_entrada:
        numeros = linha.strip().split()
        
        for numero in numeros:
            if int(numero) % 2 == 0:
                numeros_pares.append(numero)
            else:
                numeros_impares.append(numero)
                
with open('numeros_pares.txt', 'w') as arquivo_pares, open('numeros_impares.txt', 'w') as arquivo_impares:
    for numero in numeros_pares:
        arquivo_pares.write(numero + '\n')
    
    for numero in numeros_impares:
        arquivo_impares.write(numero + '\n')