---

# Introdução

Uma das razões pelas quais o Python se popularizou foi a facilidade de programar utilizando essa linguagem.

A manipulação de arquivos em Python não é diferente. Os criadores se preocuparam em disponibilizar aos desenvolvedores o que realmente importa!

Com nome de métodos intuitivos, como *read* (ler) e *write* (escrever), e tratamentos de exceções específicas para cada problema, o Python disponibiliza uma simples e poderosa forma de trabalhar com arquivos. Neste conteúdo, veremos como manipulá-los de forma correta, garantindo que o programa rode sem problemas.

É muito comum ajustarmos e prepararmos um texto antes de incluí-lo em um arquivo. Ajustes como remover espaço em branco, colocar todas as letras maiúsculas, substituir palavras e adicionar conteúdo de variável são alguns exemplos. Esses ajustes podem ser realizados a partir de métodos de manipulação de strings, que também serão tratados adiante.

---

# 1 - **Funções de manipulação de arquivos: Operações Básicas**

## Abrir um Arquivo

Para abrir um arquivo, o Python disponibiliza a função interna chamada open. Essa função está disponível globalmente, ou seja, não é preciso importá-la. A função *open* retorna um objeto do tipo arquivo. Sua forma mais simples de utilização tem a seguinte sintaxe: `arquivo = open (caminho)`

Veja como o Python trata o acesso aos arquivos a seguir. O caminho de um arquivo pode ser classificado em dois tipos:


🗨️ **Caminho Absoluto**

> É a referência completa para se encontrar um arquivo ou diretório. Ele deve começar com uma barra ( / ) ou o rótulo do drive ( C:, D: ...).
> 
> 
> > Exemplo:
> > 
> > 
> > > `open(“C:\Downloads\arquivo.txt”)`  → utilizado em ambiente Windows. 
> >`open(“/home/usuario/arquivo.txt”)` → utilizado em ambiente Linux.
> > > 


🗨️ **Caminho Relativo**

> É a referência para se encontrar um arquivo ou diretório a partir de outro diretório. Normalmente, a partir do diretório de onde o script está.
> 
> 
> > Exemplo:
> > 
> > 
> > > `open(“arquivo.txt”)` → para os casos em que o arquivo está no mesmo diretório do **script**.
> > `open(“../arquivo.txt”)` → para os casos em que o arquivo está no diretório acima do **script**.
> > > 

O Python também disponibiliza algumas funções para exibir os caminhos absolutos e relativos de um arquivo ou diretório, que são:

> **`path.relpath` → para obter o caminho relativo do arquivo em questão.**
> 
> 
> > Ex.:
> > 

> **`path.abspath` → para obter o caminho absoluto do arquivo em questão.**
> 
> 
> > Ex.:
> > 

### Modos de Acesso a um arquivo

Existem várias maneiras de acessar um arquivo em Python, mas as três mais comuns são:

1. Modo de Leitura (Read Mode): Abre um arquivo para leitura e retorna um objeto de arquivo. Isso permite que você leia o conteúdo do arquivo
    
    ```python
    with open('arquivo.txt', 'r') as f:
        conteudo = f.read()
    ```
    
2. Modo de Gravação (Write Mode): Abre um arquivo para gravação e retorna um objeto de arquivo. Isso permite que você escreva no arquivo e, se o arquivo não existir, ele será criado.
    
    ```python
    with open('arquivo.txt', 'w') as f:
        f.write('conteudo a ser gravado')
    ```
    
3. Modo de Anexação (Append Mode): Abre um arquivo para anexar dados e retorna um objeto de arquivo. Isso permite que você adicione novos dados ao final do arquivo sem apagar o conteúdo existente.
    
    ```python
    with open('arquivo.txt', 'a') as f:
        f.write('conteudo a ser adicionado')
    ```
    

O modo padrão da função *open* é o modo leitura (“r”). Esses modos podem ser combinados e para informar que desejamos ler e escrever em um arquivo, utilizamos a string “r+”, por exemplo.

O Python também nos permite diferenciar arquivos texto de arquivos binários, como uma imagem, por exemplo. ara informar que desejamos abrir um arquivo binário, adicionamos a string “b” ao modo, ficando “rb”, “wb” e “ab”.

| Caractere | Significado |
| --- | --- |
| 'r' | Abre o arquivo para leitura (default). |
| 'w' | Abre o arquivo para escrita, truncando o arquivo primeiro. |
| 'x' | Cria um arquivo para escrita e falha, caso ele exista. |
| 'a' | Abre o arquivo para escrita, acrescentando conteúdo ao final do arquivo, caso ele exista. |
| 'b' | Modo binário. |
| 't' | Modo texto (default). |
| '+' | Abre o arquivo para atualização (leitura ou escrita). |

### 📄 Atributos de um Objeto do tipo Arquivo

Os objetos do tipo arquivo em Python possuem vários atributos, os principais são:

1. name: Retorna o nome do arquivo.
2. mode: Retorna o modo de acesso ao arquivo (leitura, escrita, anexação, etc.).
3. closed: Retorna True se o arquivo está fechado e False se está aberto.
4. encoding: Retorna a codificação de caracteres usada para ler ou escrever no arquivo (apenas em modo texto).
5. buffer: Retorna o objeto buffer usado para armazenar dados lidos ou escritos no arquivo (apenas em modo binário).

Você pode acessar esses atributos usando a notação de ponto (objeto.atributo). Por exemplo:

```python
# Abrir um arquivo em modo de leitura
f = open('arquivo.txt', 'r')

# Acessar os atributos do objeto arquivo
print(f.name)
print(f.mode)
print(f.closed)
print(f.encoding)

# Fechar o arquivo
f.close()
```

Note que o atributo "buffer" só está disponível em arquivos abertos em modo binário (por exemplo, com o modo 'rb' ou 'wb'). 

Além disso, o atributo "closed" retornará False enquanto o arquivo estiver aberto e True após o fechamento do arquivo (por exemplo, usando o método close() ou ao final do bloco with).

---

## 👁 Lendo o Conteúdo de um Arquivo

Em Python, existem vários métodos para ler o conteúdo de um arquivo. Os principais métodos são:

1. read(): Lê todo o conteúdo do arquivo e retorna como uma string.
2. readline(): Lê a próxima linha do arquivo e retorna como uma string.
3. readlines(): Lê todas as linhas do arquivo e retorna como uma lista de strings.

Abaixo estão exemplos de como usar cada um desses métodos:

```python
# Abrir um arquivo em modo de leitura
f = open('arquivo.txt', 'r')

# Ler todo o conteúdo do arquivo usando o método read()
conteudo = f.read()
print(conteudo)

# Ler a primeira linha do arquivo usando o método readline()
linha1 = f.readline()
print(linha1)

# Ler todas as linhas do arquivo usando o método readlines()
linhas = f.readlines()
print(linhas)

# Fechar o arquivo
f.close()
```

- Observe que, depois de ler todo o conteúdo do arquivo usando o método read(), o ponteiro do arquivo é movido para o final do arquivo.
- Para ler novamente o arquivo, você precisará reabrir o arquivo ou usar o método seek( ) passando o valor 0 para mover o ponteiro do arquivo para o início do arquivo.
- Além disso, é importante sempre fechar o arquivo usando o método close() quando você terminar de usá-lo.

---

## ✍🏼 **Escrevendo conteúdo em um arquivo**

A primeira modificação é alterar o modo de acesso ao arquivo. Para escrita de texto, podemos utilizar o modo w (*write*) ou o modo a (*append*), a seguir:

- O modo **w** abre o arquivo para escrita, truncando o arquivo em primeiro lugar. Caso ele não exista, será criado um.
- O modo **a** abre o arquivo para escrita, acrescentando conteúdo ao final dele, caso ele exista; do contrário, será criado um arquivo.

O Python disponibiliza dois métodos para escrita de conteúdo em um arquivo texto, para o modo **w** e para o modo **a**. Os métodos *write* e *writelines* são descritos abaixo:


⌨️ ***Write* (texto)**

Escreve todo o conteúdo passado como parâmetro no arquivo. Se o arquivo já contém dados, o método write() sobrescreverá o conteúdo anterior.



⌨️ ***Writelines* (iterável)**

Escreve uma lista de strings no arquivo. Cada string é escrita como uma nova linha iterada no arquivo.


```python
# Abrir um arquivo em modo de escrita
f = open('arquivo.txt', 'w')

# Escrever uma string no arquivo usando o método write()
f.write('Conteúdo a ser escrito no arquivo')

# Escrever uma lista de strings no arquivo usando o método writelines()
linhas = ['linha 1\n', 'linha 2\n', 'linha 3\n']
f.writelines(linhas)

# Escrever uma string no arquivo usando a função print() com a opção file
print('outra linha', file=f)

# Fechar o arquivo
f.close()
```

Observe que, ao escrever uma lista de strings usando o método writelines(), cada string deve conter o caractere de nova linha '\n' para indicar o fim da linha. Além disso, o método print() pode ser usado com a opção file para escrever no arquivo em vez de imprimir na saída padrão. Sempre lembre-se de fechar o arquivo usando o método close() após terminar de escrever.

---

# ✔ Boas práticas

1. **Use a instrução `with` para abrir arquivos:** 
    
    a instrução **`with`** é uma forma mais segura e fácil de abrir arquivos, pois ela garante que o arquivo será fechado automaticamente quando a operação de leitura ou escrita for concluída. Além disso, ela também ajuda a evitar vazamentos de recursos, o que pode ocorrer se o arquivo não for fechado adequadamente. Um exemplo de uso da instrução **`with`** é o seguinte:
    
    ```python
    with open(caminho, modo) as nome: #(seu código para ler o arquivo)
    ```
    
2. **Use caminhos de arquivo absolutos ou relativos:** 
    
    é importante usar caminhos de arquivo precisos e confiáveis, para garantir que o código possa encontrar e acessar os arquivos corretamente. Você pode usar caminhos de arquivo absolutos (por exemplo, **`/Users/nomedousuario/meuarquivo.txt`**) ou caminhos de arquivo relativos (por exemplo, **`./meuarquivo.txt`** ou **`../meudiretorio/meuarquivo.txt`**).
    
3. **Especifique o modo de abertura correto:** 
    
    ao abrir arquivos, é importante especificar o modo de abertura correto, dependendo da operação que você deseja realizar. Por exemplo, use o modo **`r`** para ler um arquivo, o modo **`w`** para gravar em um arquivo (apagando seu conteúdo anterior) e o modo **`a`** para anexar a um arquivo existente. Também é possível especificar o modo de abertura e o formato de codificação do arquivo, como no exemplo abaixo:
    
    ```python
    with open('arquivo.txt', mode='r', encoding='utf-8') as f:
        # código para ler o arquivo
    ```
    
4. **Trate exceções e erros adequadamente:** 
    
    ao manipular arquivos, podem ocorrer vários tipos de exceções e erros, como FileNotFoundError (arquivo não encontrado), PermissionError (permissão negada) ou IOError (erro de entrada/saída). É importante tratar essas exceções e erros adequadamente, para evitar falhas inesperadas no código. Você pode usar as instruções **`try`** e **`except`** para capturar exceções e tratá-las de forma adequada, como no exemplo abaixo:
    
    ```python
    try:
        with open('arquivo.txt', 'r') as f:
            conteudo = f.read()
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')
    ```
    
5. **Limpe o conteúdo de arquivos ao terminar:** 
    
    se você estiver gravando dados em um arquivo, é uma boa prática garantir que o conteúdo anterior do arquivo seja limpo ou apagado antes de gravar novos dados. Você pode fazer isso usando o método **`truncate()`** do objeto de arquivo, como no exemplo abaixo:
    
    ```python
    with open('arquivo.txt', 'w') as f:
        f.truncate(0)
        f.write('Novo conteúdo do arquivo.')
    ```
    
6. **Use nomes descritivos de variáveis:** 
    
    ao trabalhar com arquivos, use nomes descritivos de variáveis para identificar o objeto de arquivo e seu conteúdo. Por exemplo, se você estiver lendo o conteúdo de um arquivo, pode usar um nome como **`conteudo_arquivo`** para a variável que armazena os dados lidos. Isso torna o código mais legível e fácil de entender.
    
7. **Use a biblioteca `os.path` para trabalhar com caminhos de arquivo:** 
    
    a biblioteca `os.path` oferece várias funções úteis para trabalhar com caminhos de arquivo, como a função **`join()`** para unir caminhos de diretório e arquivo, e a função **`abspath()`** para retornar o caminho absoluto do arquivo. Essas funções podem ajudar a garantir que os caminhos de arquivo sejam formatados e manipulados corretamente, especialmente em diferentes sistemas operacionais.
    
8. **Use formatos de arquivo padronizados:** 
    
    se você estiver trabalhando com arquivos de dados estruturados, como arquivos CSV, JSON ou XML, use formatos de arquivo padronizados e bibliotecas relevantes para manipulá-los. Por exemplo, a biblioteca csv do Python pode ser usada para ler e gravar arquivos CSV, enquanto a biblioteca json pode ser usada para trabalhar com arquivos JSON.
    
9. Evite usar arquivos temporários desnecessariamente: 
    
    o uso excessivo de arquivos temporários pode levar a problemas de desempenho e segurança em sistemas com recursos limitados. Se possível, tente evitar criar arquivos temporários desnecessários ou limpe-os adequadamente após o uso.
    
10. **Documente adequadamente o código de arquivo:** 
    
    a manipulação de arquivos pode ser complexa e difícil de entender em alguns casos. É importante documentar adequadamente o código de arquivo, incluindo comentários claros e explicativos, para ajudar outros desenvolvedores a entender o código e modificá-lo posteriormente, se necessário.
    

---