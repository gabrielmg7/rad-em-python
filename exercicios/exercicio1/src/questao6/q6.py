def copiar_arquivo(origem, destino):
    with open(origem, 'r') as arquivo_origem:
        with open(destino, 'w') as arquivo_destino:
            for linha in arquivo_origem:
                if not linha.startswith('//'):
                    arquivo_destino.write(linha)
    print(f'Arquivo {origem} copiado com sucesso para {destino}.')