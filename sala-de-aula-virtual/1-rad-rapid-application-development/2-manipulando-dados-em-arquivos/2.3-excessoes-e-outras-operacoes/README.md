# 2.3 - TRATAMENTO DE EXCEÇÕES E OUTRAS OPERAÇÕES

# Conceito de exceções

## Tratamento de exceções

Quando trabalhamos com arquivos, é comum encontrarmos alguns problemas, como arquivo inexistente e falta de permissão para escrever em um. A maioria desses problemas só pode ser detectada durante a execução do programa. Quando uma falha inesperada ocorre e o interpretador não consegue resolver o problema, dizemos que houve uma exceção.

Nesses casos, precisamos informar ao interpretador como tratar a exceção, para que o programa não seja interrompido. Se a exceção é um problema inesperado, como tratá-la? Ao desenvolver um programa, precisamos procurar na documentação da biblioteca, do módulo ou da própria linguagem de programação se as funcionalidades que vamos utilizar têm exceções mapeadas. Essas exceções são problemas que podem ocorrer, e é nossa tarefa tratá-las.

> ❓ Você deve estar se perguntando: “O que seria ‘tratar uma exceção?”. Isso nada mais é do que dizer ao Python o que fazer, ou quais instruções executar, quando ele encontrar um problema.
> 

Tratar uma exceção significa lidar com um erro ou situação inesperada que pode ocorrer durante a execução de um programa. Quando uma exceção é levantada em um programa, o programa interrompe sua execução normal e tenta encontrar um bloco de código que possa lidar com a exceção. Isso é importante para garantir que o programa continue a ser executado mesmo quando ocorrerem erros, evitando que ele quebre de forma inesperada.

Para ilustrar, observe os seguintes passos:

1. Quando abrimos um arquivo em modo leitura e esse arquivo não existe, o Python lança uma exceção do tipo FileNotFoundError.

2. Se **não** avisarmos ao Python o que fazer quando isso ocorrer, o programa será interrompido.

3. Nesse caso, um tratamento para essa exceção poderia ser: exibir um pop-up ao usuário informando que o arquivo não existe.


🗨️ Existem diversas formas de tratar exceções em Python, como a utilização de blocos try-except para capturar exceções específicas e realizar ações para lidar com elas, ou a utilização do bloco finally para executar ações que devem ser realizadas independentemente de ter ocorrido uma exceção ou não.



### Mas o que acontece quando uma exceção lançada não é tratada?

Ela interrompe a execução normal do programa e uma mensagem de erro é exibida no console. Essa mensagem contém informações sobre o tipo de exceção que ocorreu e a linha de código onde ela aconteceu. Se a exceção não for tratada, o programa irá parar de executar e o usuário poderá ter dificuldades para entender o que aconteceu e como corrigir o problema. 

Além disso, se o programa não estiver em um ambiente de desenvolvimento, a mensagem de erro pode não ser visível para o usuário final e o programa pode simplesmente travar ou fechar inesperadamente.

Para resolver isso, precisamos tratar a exceção, ou melhor, uma possível exceção. Esse tratamento informa ao Python uma rota alternativa, caso ele encontre um problema.

> Para tratar exceções, precisamos “envolver” o trecho de código passível de erro com a cláusula try/except ou try/except/finally. Veremos apenas a cláusula try/except. Essa estrutura permite que um trecho de código seja executado normalmente até que ocorra uma exceção, que será capturada e tratada no bloco **`except`**.
> 

```python
try:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    resultado = x / y
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except ValueError:
    print("Digite apenas números inteiros")
```

Ao usar o **`try-except`**, o programa tenta executar o bloco de código dentro do **`try`**. Se ocorrer uma exceção, o programa captura a exceção e executa o bloco **`except`** correspondente. No exemplo acima, se o usuário tentar dividir por zero, o programa exibirá a mensagem "Não é possível dividir por zero" em vez de gerar um erro e parar a execução. Se o usuário digitar um valor inválido, como uma letra, o programa exibirá a mensagem "Digite apenas números inteiros".

Dessa forma, com o tratamento de exceções, podemos evitar que o programa pare de funcionar de forma inesperada e podemos fornecer uma mensagem mais clara e compreensível para o usuário. Praticamente todas as exceções em Python são herdadas da classe *Exception*, ou seja, ela é uma exceção muito genérica, lançada por diversos tipos de erros diferentes. Quanto mais genérica, mais abrangente é a exceção.


⚠️ **Atenção!**

Não é uma boa prática utilizar exceções abrangentes, pois elas podem silenciar erros que não esperamos. O ideal é tratar as exceções utilizando a forma mais específica possível.



Confira algumas exceções específicas relacionadas à manipulação de arquivos e alguns motivos que podem gerar essas exceções:

- **PermissionError**
    
    Lançada quando não temos permissão para realizar uma operação.
    
- **FileExistsError**
    
    Lançada quando tentamos criar um arquivo ou diretório já existentes.
    
- **FileNotFoundError**
    
    Lançada quando tentamos abrir um arquivo ou diretório que não existem.
    

**Todas essas exceções herdam da exceção mais abrangente OSError, que, por sua vez, herda de *Exception.***

Saiba que o Python só consegue tratar a exceção caso o erro esteja mapeado em algum *except*. Se o interpretador não encontrar o *except* adequado, será gerado um erro, e o programa será interrompido.

Um problema clássico que ocorre quando lidamos com arquivos é tentar alterar o conteúdo de um arquivo quando ele está aberto em outro programa. No caso do sistema operacional Windows 10, é lançada uma exceção sobre permissão de acesso.


⚠️ **O Python direciona o fluxo de execução para o trecho onde é realizado o tratamento da exceção lançada.**



## Operações adicionais em arquivos

Além das opções para leitura e escrita em arquivos, o Python disponibiliza um conjunto de operações adicionais, como renomear e apagar arquivo, além de operações em diretórios, como listar arquivos de diretórios, criar diretórios etc. A partir de agora, apresentaremos algumas dessas operações.

Vamos iniciar pela operação de remover um arquivo, que está disponível por meio da função **remove** do módulo **os** do Python.

A função **remove** tem a seguinte sintaxe: `os.remove(caminho)`

### Exemplos

1. Renomeando um arquivo:
    
    ```python
    import os
    
    try:
        # Renomeando um arquivo
        os.rename('arquivo_antigo.txt', 'arquivo_novo.txt')
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except FileExistsError:
        print("O arquivo novo já existe!")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    ```
    
2. Apagando um arquivo:
    
    ```python
    import os
    
    try:
        # Apagando um arquivo
        os.remove('arquivo_a_ser_removido.txt')
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    ```
    
3. Listando arquivos de um diretório:
    
    ```python
    import os
    
    try:
        # Listando arquivos de um diretório
        diretorio = './meu_diretorio'
        for nome_arquivo in os.listdir(diretorio):
            print(nome_arquivo)
    except FileNotFoundError:
        print("Diretório não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    ```
    
4. Criando um novo diretório:
    
    ```python
    import os
    
    try:
        # Criando um novo diretório
        os.mkdir('novo_diretorio')
    except FileExistsError:
        print("O diretório já existe!")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    ```
    
5. Removendo um diretório:
    
    ```python
    import os
    
    try:
        # Removendo um diretório
        os.rmdir('diretorio_a_ser_removido')
    except FileNotFoundError:
        print("Diretório não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    ```
    
    
    💡 **Dica**
    
    Para os casos em que desejamos renomear sobrescrevendo o arquivo destino, caso ele exista, podemos utilizar a função *replace*, também do módulo os.
    
    
    

---

# Manipulação de diretórios

## Criando e removendo diretórios

Trabalhar com arquivos significa trabalhar com diretórios. Vejamos as principais funcionalidades relacionadas à manipulação de diretórios em Python começando pela criação e remoção de um diretório.

Para criar um diretório, utilizamos a função mkdir do módulo os, enquanto, para remover um diretório, utilizamos a função rmdir, também do módulo **os**.

A sintaxe dessas duas funções são as seguintes: 

`os.mkdir(caminho)`

`os.rmdir(caminho)`

### Exemplos:

Exemplo de criação de um diretório com a função **`mkdir`**:

```python
import os

# criando um diretório chamado "exemplo"
os.mkdir("exemplo")
```

- Caso não tenhamos permissão para criar o diretório, será lançada a exceção **PermissionError**.
- Caso o diretório já exista, a exceção **FileExistsError** é lançada.

---

Exemplo de remoção de um diretório com a função **`rmdir`**:

```python
import os

# removendo o diretório "exemplo"
os.rmdir("exemplo")
```

Para os casos em que o diretório a ser removido não esteja vazio, será lançada a exceção OSError. Essa exceção é mais abrangente. Não temos como garantir, a princípio, que a exceção lançada ocorre especificamente pelo fato de o diretório não estar vazio. Nessas situações, precisamos analisar mais o erro, principalmente o seu número, para verificar o que realmente aconteceu. O número do erro está disponível no atributo errno do objeto erro. 

Os códigos dos possíveis erros estão no módulo errno do Python e podem ser utilizados no tratamento das exceções para descobrir o que realmente deu errado. Como a exceção OSError é mais abrangente que as outras exceções que estudamos, ela deve ficar por último. Caso contrário, nunca alcançaremos as exceções mais específicas.

```python
import os
import errno

try:
    os.rmdir('meu_diretorio')
except OSError as e:
    if e.errno == errno.ENOTEMPTY:
        print("O diretório não está vazio.")
    else:
        print(f"Ocorreu um erro inesperado: {e}")
```

É importante lembrar que a função **`rmdir`** só pode ser utilizada para remover diretórios vazios. Caso o diretório contenha arquivos ou subdiretórios, é necessário utilizar a função **`rmtree`** do módulo shutil para remover o diretório e todo o seu conteúdo:

```python
import shutil

# removendo o diretório "exemplo" e todo o seu conteúdo
shutil.rmtree("exemplo")
```

## Listando conteúdo de diretórios

Outra tarefa muito comum quando estamos tratando com arquivos é listar os arquivos presentes em um diretório.

Para isso, podemos utilizar a função scandir do módulo os. Sua sintaxe é a seguinte:

`os.scandir(caminho)`

Nesse exemplo, temos o nome do módulo **os**, seguido de um ponto e o nome da função scandir. Como parâmetro, a função espera o caminho para o **diretório**.

Como resultado, teremos um iterável (iterator) que retorna objetos do tipo os.DirEntry, que podem ser arquivos ou diretórios. Dentre os atributos e métodos desse tipo de objetos, destacamos:

`Name`: Nome do diretório ou arquivo.

`Path`: Caminho completo do diretório ou arquivo.

`is_dir()`: Retorna verdadeiro se o objeto é um diretório.

`is_file()`: Retorna verdadeiro se o objeto é um arquivo.

`stat()`: Retorna alguns atributos do arquivo ou diretório, como tamanho.