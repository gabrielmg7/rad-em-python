# 2.2 - FUNÇÕES DE MANIPULAÇÃO DE STRINGS

---

# Métodos de manipulação de strings

Durante a vida de programador, é muito comum nos depararmos com situações em que precisamos realizar alguns ajustes e operações sobre os textos lidos de arquivos, como remover espaço em branco, colocar todas as letras maiúsculas, substituir e contar palavras. Neste módulo, veremos alguns métodos presentes nos objetos do tipo str (string), que são muito utilizados em conjunto com a manipulação de arquivos.

## Método *strip*

Ao ler o conteúdo do arquivo, o Python retorna os caracteres de final de linha (\r e \n). Muitas vezes, essa informação não é necessária, principalmente se estivermos tratando uma linha de cada vez.

Dependendo do objetivo, esses caracteres são considerados lixo e podem atrapalhar o processamento que desejamos realizar. Para remover esses caracteres e também espaços em branco adicionais, o tipo str disponibiliza o método strip(). O método `strip()` é usado em Python para remover caracteres indesejados no início e no final de uma string. Ele retorna uma nova string após remover todos os caracteres especificados de ambos os lados da string original.

A seguir estão alguns exemplos de como usar o método `strip()`:

1. Removendo espaços em branco:
    
    ```python
    texto = "   Olá, mundo!   "
    print(texto.strip()) 
    
    # saída: "Olá, mundo!"
    ```
    
2. Removendo caracteres específicos:
    
    ```python
    texto = ".....Olá, mundo!....."
    print(texto.strip('.')) 
    
    # saída: "Olá, mundo!"
    ```
    
3. Removendo caracteres apenas no início:
    
    ```python
    texto = "   Olá, mundo!   "
    print(texto.lstrip()) 
    
    # saída: "Olá, mundo!   "
    ```
    
4. Removendo caracteres apenas no final:
    
    ```python
    texto = "   Olá, mundo!   "
    print(texto.rstrip()) 
    
    # saída: "   Olá, mundo!"
    ```
    
5. Usando o método strip() em um loop:
    
    ```python
    lista_textos = ["   Olá", "mundo!   ", "   Python   "]
    for texto in lista_textos:
        print(texto.strip())
    
    # saída:
    # "Olá"
    # "mundo!"
    # "Python"
    ```
    

## **Métodos *count* e *split***

Outra atividade muito comum na manipulação de arquivos é a contagem do número de vezes que determinada palavra aparece. O Python disponibiliza o método *count* para strings, que recebe como parâmetro a palavra que desejamos contar e retorna o total de ocorrências dela. Sua sintaxe é a seguinte:

`contagem = variavel_string.count(palavra)`

### Exemplos com c*ount*

1. Contagem de palavras em uma string:
    
    ```python
    texto = "Python é uma linguagem de programação poderosa e fácil de aprender"
    contagem = texto.count("de")
    print(contagem) # saída: 1
    ```
    
2. Verificando a presença de um caractere em uma string:
    
    ```python
    texto = "Eu amo Python"
    if texto.count("o") > 0:
        print("A letra 'o' está presente na string")
    else:
        print("A letra 'o' não está presente na string")
    
    # saída: "A letra 'o' está presente na string"
    ```
    
3. Contagem de vogais em uma string:
    
    ```python
    texto = "O Python é incrível!"
    vogais = "aeiouAEIOU"
    contagem_vogais = sum([texto.count(v) for v in vogais])
    print(contagem_vogais) 
    
    # saída: 7
    ```
    
4. Contagem de palavras em um arquivo de texto:
    
    ```python
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        contagem = conteudo.count("Python")
    print(contagem) 
    
    # retorna o número de ocorrências da palavra "Python" no arquivo
    ```
    
5. Contagem de caracteres em uma string:
    
    ```python
    texto = "Python é uma linguagem de programação muito popular"
    contagem_caracteres = len(texto) - texto.count(" ")
    print(contagem_caracteres) 
    
    # saída: 39 (desconsiderando os espaços em branco)
    ```
    
    ---
    
    Apesar de ser muito simples a utilização do método *count* do tipo str, pode gerar alguns efeitos indesejáveis, pois esse método também conta as palavras que contêm parte da string passada como argumento. Considere a frase: “Eu amo comer amoras no café da manhã”. Se utilizarmos o método *count*, com a string “amo” como argumento, o retorno será 2, pois o método irá considerar tanto a palavra amo quanto a palavra amoras. 
    
    Para contornar esse problema, podemos “quebrar” uma frase em palavras e depois verificar se cada palavra é igual à string que buscamos.
    
    Isso nos leva a outro método muito utilizado em processamento de textos, o método split, que é usado para quebrar uma string em partes menores, retornando uma lista com essas partes. Sua sintaxe é a seguinte:
    
    `lista_termos = variavel_string.split(separador)`
    
    ### Exemplos com split
    
    1. Quebrando uma string em palavras:
        
        ```python
        frase = "O Python é uma linguagem de programação incrível"
        palavras = frase.split()
        print(palavras) # saída: ['O', 'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'incrível']
        ```
        
    2. Quebrando uma string em palavras separadas por um caractere específico:
        
        ```python
        texto = "apple,banana,orange"
        frutas = texto.split(",")
        print(frutas) # saída: ['apple', 'banana', 'orange']
        ```
        
    3. Contando o número de palavras em uma frase:
        
        ```python
        frase = "O Python é uma linguagem de programação incrível"
        palavras = frase.split()
        contagem = len(palavras)
        print(contagem) # saída: 8
        ```
        
    4. Verificando se uma palavra está presente em uma lista de palavras:
        
        ```python
        frase = "Eu amo comer amoras no café da manhã"
        palavras = frase.split()
        busca = "amo"
        contagem = sum([1 for palavra in palavras if palavra == busca])
        print(contagem) # saída: 1
        ```
        
    5. Usando o método split() em um arquivo de texto:
        
        ```python
        with open("arquivo.txt", "r") as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            contagem = palavras.count("Python")
        print(contagem) # retorna o número de ocorrências da palavra "Python" no arquivo
        ```
        

---

## Método *join*

Assim como há a necessidade de quebrar uma frase em uma lista de palavras, podem existir situações em que ocorra o inverso, ou seja, temos uma lista de palavras ou frases e desejamos concatená-las em uma única string.

Para essa operação, utilizamos o método join do tipo str, que retorna uma única string com todos os elementos da lista concatenados, utilizando determinado conector. Sua sintaxe é a seguinte:

`string_final = “conector”.join(iteravel)`

### Exemplos com *join*

1. Concatenando uma lista de palavras com espaços em branco:
    
    ```python
    palavras = ['O', 'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'incrível']
    frase = " ".join(palavras)
    print(frase) # saída: "O Python é uma linguagem de programação incrível"
    ```
    
2. Concatenando uma lista de palavras com um caractere específico como conector:
    
    ```python
    frutas = ['apple', 'banana', 'orange']
    texto = ", ".join(frutas)
    print(texto) # saída: "apple, banana, orange"
    ```
    
3. Concatenando uma lista de frases com quebra de linha como conector:
    
    ```python
    frases = ['O Python é uma linguagem de programação incrível', 'Eu amo programar em Python']
    texto = "\n".join(frases)
    print(texto)
    # saída:
    # O Python é uma linguagem de programação incrível
    # Eu amo programar em Python
    ```
    
4. Concatenando uma lista de palavras sem separação:
    
    ```python
    palavras = ['Python', 'é', 'incrível']
    texto = "".join(palavras)
    print(texto) # saída: "Pythonéincrível"
    ```
    
5. Usando o método join() para escrever em um arquivo de texto:
    
    ```python
    conteudo = ['Python é uma linguagem de programação incrível', 'Eu amo programar em Python']
    texto = "\n".join(conteudo)
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write(texto)
    ```
    
    O arquivo "arquivo.txt" será criado com o conteúdo das strings.
    

---

# Métodos de Formatação de Strings

Até o momento, realizamos operações sobre strings pré-existentes. No entanto, é muito comum precisarmos juntar valores de variáveis com strings.

Agora, veremos algumas funções relacionadas às strings, começando pela formatação de strings (*string formatting*).

A formatação de strings permite ajustar como uma string será exibida ou gravada em um arquivo, por exemplo. Ajustes como: número de casas decimais em *float*, exibição de datas, inclusão de variáveis e espaçamento são alguns dos exemplos.

Existem basicamente três formas de realizar a formatação de strings. São elas:

- Utilizando **f-strings** (*formatted string literals*).
- Utilizando o método format() das strings.
- Fazendo manualmente.

Veremos como utilizar f-strings, recurso adicionado na versão 3.6 do Python.

## F-strings

O objetivo principal da criação das *f-strings* foi facilitar a formatação de strings. Para definimos uma variável *f-string*, precisamos incluir, antes das aspas que definem uma string, a letra f (ou F), por exemplo: 

`minha_string = f”Olá Mundo {expr}”`

> Dentro das *f-strings*, podemos utilizar expressões em Python entre as chaves, delimitadas pelos caracteres `{ e }`.
> 
> - Essas expressões incluem variáveis ou **literais**. Inclusive, podemos fazer chamada para funções ou utilizar métodos de variáveis dentro desses delimitadores.
> - Todo o conteúdo entre os caracteres `{ e }` é substituído pelo resultado da expressão e interpolado à string.

### Exemplos com *f-string*

1. Utilizando uma variável dentro da f-string:
    
    ```python
    nome = "João"
    print(f"Olá, {nome}!") # saída: "Olá, João!"
    ```
    
2. Utilizando uma expressão matemática:
    
    ```python
    a = 10
    b = 5
    print(f"O resultado da soma entre {a} e {b} é {a + b}") # saída: "O resultado da soma entre 10 e 5 é 15"
    ```
    
3. Utilizando um método de uma variável dentro da f-string:
    
    ```python
    nome = "maria"
    print(f"Olá, {nome.capitalize()}!") # saída: "Olá, Maria!"
    ```
    
4. Utilizando uma função dentro da f-string:
    
    ```python
    def duplicar(x):
        return x * 2
    
    numero = 5
    print(f"O dobro de {numero} é {duplicar(numero)}") # saída: "O dobro de 5 é 10"
    ```
    
5. Utilizando um operador ternário dentro da f-string:
    
    ```python
    idade = 18
    maioridade = "maior" if idade >= 18 else "menor"
    print(f"Esta pessoa é {maioridade} de idade") # saída: "Esta pessoa é maior de idade"
    ```
    

---

Veja agora algumas funcionalidades adicionais de formatação de string utilizando f-string, como a definição de largura de uma string, formatação de float e de datas:

1. Definindo a largura de uma string:
    
    ```python
    nome = "João"
    print(f"Olá, {nome:>10}!") # saída: "Olá,       João!"
    ```
    
    Nesse exemplo, utilizamos o caractere **`>`** para indicar que a string **`nome`** deve ser alinhada à direita e ocupar uma largura de 10 caracteres.
    
2. Formatando um float:
    
    ```python
    preco = 99.99
    print(f"O preço do produto é R${preco:.2f}") # saída: "O preço do produto é R$99.99"
    ```
    
    Nesse exemplo, utilizamos **`:.2f`** para formatar o float **`preco`** com duas casas decimais.
    
3. Formatando uma data:
    
    ```python
    from datetime import datetime
    data = datetime(2023, 4, 3)
    print(f"A data é {data:%d/%m/%Y}") # saída: "A data é 03/04/2023"
    ```
    
    Nesse exemplo, utilizamos **`%d`** para representar o dia, **`%m`** para representar o mês e **`%Y`** para representar o ano da data.