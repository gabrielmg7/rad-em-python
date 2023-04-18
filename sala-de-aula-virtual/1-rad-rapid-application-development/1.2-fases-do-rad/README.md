# **CONCEITOS**

A metodologia RAD é caracterizada pelo desenvolvimento do projeto através de etapas iterativas e incrementais, onde um protótipo é entregue ao final de cada ciclo. A proposta é que haja redução nas atividades relacionadas ao planejamento em detrimento do processo de desenvolvimento através de um processo que se caracteriza por incrementos de funcionalidades a cada nova iteração. Desse modo, a expectativa é que as equipes produzam mais em menos tempo, maximizando a satisfação do cliente, uma vez que ele é envolvido no processo. Isso ocorre porque a RAD é estruturada para que as partes interessadas interajam e possam detectar a necessidade de alterações do projeto em tempo real, sem a necessidade de completar longos ciclos de desenvolvimento, e os desenvolvedores possam realizar as implementações rapidamente ao longo das iterações.

---

O ciclo de vida da RAD foi projetado para direcionar os desenvolvedores na criação de soluções de software que atendam às necessidades dos usuários. Este ciclo de vida trata das atividades que são necessárias para definir o escopo e os requisitos de negócios, além das atividades para projetar, desenvolver e implementar o sistema.  Na abordagem de James Martin (MARTIN, 1991), a metodologia RAD possui quatros fases distintas, que são:

1. **Planejamento de requisitos**
    
    As partes interessadas – usuários, gerentes e desenvolvedores – estudam as necessidades de negócios, escopo do projeto, restrições e requisitos do sistema. A gerência só autoriza a continuidade do projeto depois que os membros das equipes concordam sobre o entendimento dos requisitos do sistema.
    
2. **Design do usuário**
    
    São desenvolvidos modelos e protótipos – através da interação de usuários e desenvolvedores – para representar todos os processos, entradas e saídas do sistema. Para isso, são usadas uma combinação de técnicas JAD (Joint Application Development) e ferramentas CASE para representar as demandas do usuário em modelos de trabalho.
    
3. **Construção**
    
    É nesta fase que os protótipos são desenvolvidos. A interação entre usuários e desenvolvedores continua, para que haja sugestões sobre alterações, ajustes, ou melhorias, à medida que unidades do sistema – como telas ou relatórios reais, por exemplo – são desenvolvidas.
    
4. **Transição**
    
    São feitos processamento de dados, testes, mudança para o novo sistema e treinamento do usuário.
    

---

> **Resumindo**
> 
> 
> O planejamento de requisitos está focado em determinar as metas e expectativas do projeto e quais são os potenciais problemas que podem ser impeditivos para o desenvolvimento do software. No caso da RAD, onde a entrega rápida de resultados é um dos objetivos principais, a identificação prévia dos requisitos funcionais é muito importante. Na fase de design do usuário, a interação entre os desenvolvedores e os usuários é constante no desenvolvimento de modelos e protótipos que abordam todos os processos, entradas e saídas do sistema. Na fase de construção, converte o protótipo aprovado da fase de design do usuário em um modelo de trabalho. Como já houve bastante interação entre usuários e desenvolvedores na fase anterior, agora o foco dos desenvolvedores está na construção do modelo de trabalho final. Por fim, na fase de transição, o produto está pronto para ser lançado. Aqui, o usuário deve passar por treinamento para começar a usar o sistema.
> 

---

Existem outras abordagens sobre a divisão das fases da RAD. Por exemplo, uma das mais conhecidas é a de James Kerr (KERR & HUNTER, 1994), em que existem cinco fases distintas, que são:

1.  **Modelagem de negócios**
    
    Nesta fase, é feita a obtenção de informações a respeito dos requisitos funcionais do sistema reunidas por várias fontes relacionadas aos negócios, ou seja, o modelo de negócios do produto em desenvolvimento é tratado em termos de fluxo de informações, que são obtidas a partir de vários canais de negócios, tais como entrevistas com usuários do sistema e outras fontes de informação que auxiliem no entendimento do negócio que será tratado. Essas informações são então combinadas, para criar uma documentação que será utilizada para modelar o ciclo de vida dos dados: como os dados podem ser usados, quando são processados e a sua transformação em informações que serão utilizadas por alguma área, ou por algum setor específico do negócio. Portanto, é feita uma análise com viés comercial a fim de encontrar os dados vitais para os negócios: como podem ser obtidos, como e quando são processados e quais são os fatores que os transformam em informações úteis.
    
2. **Modelagem de dados**
    
    Todas as informações que foram obtidas durante a fase modelagem de negócios são analisadas para formar conjuntos de objetos de dados essenciais para os negócios. Através da análise, as informações são agrupadas, de modo que sejam úteis para a empresa, como, por exemplo, na determinação de quais são as entidades principais que serão tratadas pelo sistema. A qualidade de cada grupo de dados, então, é examinada e recebe uma descrição precisa. Em seguida, é feito mapeamento que relaciona esses grupos entre si e qual o significado desses relacionamentos, conforme definido na etapa modelagem de negócios. Avançando um pouco mais, agora deve-se identificar e definir os atributos de todos os conjuntos de dados. Também é estabelecida e definida em detalhes de relevância para o modelo de negócios a relação entre esses objetos de dados.
    
3. **Modelagem de processos**
    
    Esta fase é a etapa da metodologia RAD em que todos os grupos de dados coletados durante a etapa modelagem de dados são analisados sob o ponto de vista de processamento, ou seja, como os dados são convertidos em informações úteis. Durante a fase de modelagem de processos, mudanças e otimizações podem ser feitas, e os conjuntos de dados podem ser definidos com mais detalhes. Quaisquer descrições para adicionar, remover ou alterar os objetos de dados também são criadas durante esta fase. A ideia é a seguinte: os conjuntos de objetos de dados definidos na fase de modelagem de dados são convertidos para estabelecer o fluxo de informações de negócios necessário para atingir objetivos de negócios específicos conforme o modelo de negócios. A modelagem de processamento dos dados para alterá-los, ou utilizá-los para fazer quaisquer outras operações que os transformem, é definida nesta fase. Aqui, também são feitas descrições dos processos para adicionar, excluir, recuperar ou modificar um objeto de dados.
    
4. **Geração da aplicação**
    
    Nesta fase, todas as informações coletadas são codificadas e é construído o sistema que será usado para criar o protótipo. Os modelos de dados criados são transformados em protótipos reais que podem ser testados na próxima fase. O sistema real é construído, e a codificação é feita usando ferramentas de automação para converter modelos de processo e dados em protótipos reais.
    
5. **Teste e modificação**
    
    Neste momento, são feitos testes dos protótipos criados. Cada módulo é testado de modo a identificar e adaptar os componentes para criar o produto mais eficaz. Como a maioria dos elementos já foi examinada anteriormente, a expectativa é que haja grandes problemas com o protótipo. O tempo total de teste é reduzido no modelo RAD, pois os protótipos são testados independentemente durante cada iteração. No entanto, o fluxo de dados e as interfaces entre todos os componentes precisam ser exaustivamente testados com uma cobertura de teste completa. Como a maioria dos componentes de programação já foi testada, o risco de problemas importantes é minimizado.
    

O princípio-chave do processo RAD é a redução de atividades burocráticas para se concentrar em um processo iterativo de design e construção, permitindo que as equipes realizem mais em menos tempo, sem afetar a satisfação do cliente. As fases de prototipagem e construção rápida podem ser repetidas, até que o proprietário e os usuários do produto se sintam seguros de que o protótipo e a forma como foi construído atendem aos requisitos do projeto.

Nos métodos tradicionais, como a metodologia **cascata**, por exemplo, demora bastante até que os desenvolvedores recebam comentários dos usuários, aumentando, assim, as chances de ser necessário refazer partes do sistema, ou seja, retrabalho. **Nesse sentido, um dos maiores benefícios da RAD são os comentários dos usuários através da constante interação.** O ponto do projeto em que fica mais evidente essa interação está nos componentes de **UI/UX**  do sistema. Com os protótipos, os usuários podem ter mais clareza sobre a forma como o projeto está avançando, e os desenvolvedores podem medir riscos na escolha de tecnologias que venham prejudicar a entrega do projeto, podendo, assim, fazer escolhas em tempo hábil.

# **CICLO DE DESENVOLVIMENTO**

O ciclo de desenvolvimento da metodologia RAD começa com as partes interessadas – usuários e desenvolvedores – definindo um conjunto de requisitos do projeto, que é equivalente ao que seria feito durante o escopo do projeto nos ciclos de desenvolvimento tradicionais. Esse estágio de planejamento é “rápido”, pois a ênfase da metodologia RAD está nas iterações de construção de protótipos que são mais importantes para o sucesso final de um projeto. Todos os envolvidos no projeto – desenvolvedores, clientes, usuários e equipes de software – são levados a interagir entre si, de modo a determinar os requisitos do projeto e, em caso de problemas, quais estratégias serão aplicadas durante o desenvolvimento.

### **Os requisitos incluem:**

- Metas
- Expectativas
- Cronogramas
- Orçamento

Espera-se que o cliente forneça a visão para o produto, e, em colaboração com outras partes interessadas, são realizadas pesquisas para finalizar os requisitos com a aprovação de cada parte interessada. É necessário que todos os interessados fiquem convencidos de que o entendimento do projeto está claro desde o início do ciclo de desenvolvimento, pois isso ajuda as equipes a evitar falhas de comunicação e erros dispendiosos.

---

<aside>
⚠️ **Atenção**

Outro ponto importante a ser destacado é que um dos princípios fundamentais da RAD é a capacidade de alterar os requisitos em qualquer momento do ciclo de desenvolvimento.

</aside>

---

1. **LEVANTAMENTO DE REQUISITOS**
    - Logo no início do levantamento de requisitos, é feita uma pesquisa do ambiente interno para compreender de que forma atender o projeto que será iniciado.
    - Logo depois, é desenvolvido o escopo do sistema proposto. Os processos de negócios e os dados com os quais o sistema trabalhará são usados para definir as suas respectivas funcionalidades. Características como benefícios, custos e riscos potenciais do sistema são identificadas.
    - Passa-se, então, para a documentação de possíveis problemas de gerenciamento, e, por fim, formaliza-se o escopo do sistema.
    - Faz-se também uma estimativa dos recursos e do tempo de implementação. Se o custo e a duração do desenvolvimento já forem definidos, é necessário analisar com mais cuidado o escopo do projeto para verificar se é viável.
2. **OFICINAS JAD**
    - Para completar a análise de negócios e de dados do sistema, são feitas as oficinas JAD, em que são realizados revisões e detalhamento do escopo do sistema para garantir que as entregas ocorram dentro do prazo.
    - Um exemplo de resultado obtido dessa fase são a definição das regras de negócios a serem aplicadas em cada atividade e os atributos de cada entidade.
    - Aqui, elementos de UI/UX, tais como layouts provisórios de telas e dos principais relatórios, são desenvolvidos.
    - Além disso, um esboço do projeto do sistema é desenvolvido.
    - Com a conclusão do design, passa-se a mapear as funcionalidades do sistema com seus componentes de interação.
3. **VALIDAÇÕES DOS PROTÓTIPOS**
    
    A consistência do projeto é confirmada através das sucessivas iterações, em que são apresentados protótipos para os usuários validarem. Através de testes, são identificados erros, ou a necessidade de se fazer ajustes no sistema. Ainda nesta fase, são iniciadas estratégias para a implementação do sistema. Em determinado momento, deve-se finalizar o escopo do projeto e o plano de implementação. Por fim, os resultados das interações entre desenvolvedores e usuários são incorporados ao projeto e ao plano de transição. Se tudo for aprovado, passa-se para a fase de construção rápida.
    
4. **BANCO DE DADOS**
    
    Agora, com o ambiente de desenvolvimento concluído, a próxima etapa é o projeto de banco de dados, que deve ser construído conforme a estrutura de dados desenvolvida na fase de design do usuário. O sistema passa a integrar as funcionalidades de banco de dados com os componentes de interação visual. Aplicam-se, agora, os testes, que devem ser executados com dados que simulem situações reais e auxiliem na detecção de possíveis falhas, para que sejam devidamente tratadas, e na documentação do sistema. Cada componente do sistema e as funcionalidades são verificadas de acordo com os requisitos do usuário. Por fim, são iniciados os preparos para a fase de transição através dos planos de trabalho e de contingência.
    
5. **TRANSIÇÃO**
    
    Nesta última fase, a de transição, são feitos treinamentos para o usuário utilizar o sistema antes que seja colocado em produção. Em seguida, o sistema é colocado em produção e, por fim, instalado no cliente. Configurações de hardware, instalações de bibliotecas e demais configurações são concluídas nesta etapa. A última tarefa a ser terminada é a aceitação do sistema por parte do usuário, conforme o que foi estabelecido na etapa inicial do projeto.
    

---

Após a definição do escopo do projeto, as equipes iniciam a construção dos modelos e protótipos. **O objetivo é demonstrar para o cliente um design funcional o mais rápido possível**.

- Desenvolvedores e designers – que desenvolvem telas e componentes interativos – trabalham em colaboração com os clientes até que o produto esteja pronto, para que os requisitos funcionais sejam atendidos.
- Essa etapa é repetida à medida que o projeto é construído.
- Durante a fase inicial de prototipagem, os desenvolvedores focam seus esforços em elementos essenciais do sistema para produzir um produto que seja aceitável pelo proprietário do produto.
- O uso de protótipos construídos rapidamente incentiva o envolvimento do usuário nos testes do sistema e, como consequência, são obtidos comentários que podem ser utilizados para aperfeiçoar o trabalho que está sendo executado, em vez de tentar fazer avaliações abstratas de um documento de design.
- Com esses comentários, os desenvolvedores podem ajustar os modelos de forma incremental, até que se atenda aos requisitos do projeto. A experiência compartilhada entre as partes interessadas é obtida através da boa comunicação. O aprendizado habilita a identificação rápida do que funciona e o que não funciona.
- A liberação rápida de protótipos aumenta as chances de descobrir erros precocemente, o que leva ao aumento da confiabilidade do sistema. Através da criação de protótipos, a equipe de desenvolvimento pode avaliar a viabilidade de componentes complexos. Consequentemente, aumenta-se a robustez do software, além de facilitar adições de design futuras.

****O desenvolvimento rápido torna possível que protótipos evoluam para a versão comercial do sistema, ou seja, que as versões parciais progridam para o software que vai atender às expectativas do cliente. Através de incrementos ao longo das iterações, novos componentes e novas alterações são feitas. As equipes de desenvolvimento usam ferramentas computacionais que viabilizam o progresso rápido para a versão final do sistema. Na metodologia RAD, a maioria dos problemas e ajustes são tratados durante a fase de prototipagem iterativa.****

Nas metodologias tradicionais, os desenvolvedores consomem muito tempo com atividades que não estão diretamente ligadas ao desenvolvimento do projeto. No caso da RAD, são feitos muitos testes, aumentando, assim, as chances de que o resultado satisfaça as expectativas do cliente. A colaboração entre desenvolvedores e usuários finais auxilia na construção de interfaces e funcionalidades que melhorarão todos os aspectos do produto. Os clientes fornecem informações detalhadas com sugestões de alterações – ajustes, ou novas ideias – que resolvem os problemas à medida que são descobertos.

A metodologia RAD se baseia no desenvolvimento iterativo e incremental. Ela é dividida em fases, caracterizando-a, assim, como um método com definição de procedimentos que devem ser seguidos para se atingir a meta do projeto: atender às necessidades do cliente dentro de um prazo curto e sem erros, ou, pelo menos, com o mínimo possível de erros. A existência de mais de uma abordagem para tratar as suas fases não muda a essência do processo, que se caracteriza pela interação constante entre usuários e desenvolvedores.

---

# **REFERÊNCIAS**

BERGER, H.; BEYNON-DAVIES, P.: **The utility of rapid application development in large-scale, complex projects**. Information Systems Journal, 2009. 19 (6), 549– 570.

bottlepy. Consultado em meio eletrônico em: 4 ago. 2020.

cherrypy. Consultado em meio eletrônico em: 4 ago. 2020.

Django. Consultado em meio eletrônico em: 4 ago. 2020.

flask. Consultado em meio eletrônico em: 4 ago. 2020.

Fitzgerald, B. **A Preliminary Investigation of Rapid Application Development in Practice, Proceedings of 6th International Conference on Information Systems Methodologies**, editors Wood-Harper AT, Jayarantna N., Wood J R G, pp. 77–87, 1998.

Kerr, J.; Hunter, R. **Inside RAD**: How to Build Fully Functional Computer Systems in 90 Days or Less. New York: McGraw-Hill, 1994.

Kivy. Consultado em meio eletrônico em: 4 ago. 2020.

Martin, J. **Rapid Application Development**, Macmillan, USA, 1991.

matplotlib. Consultado em meio eletrônico em: 4 ago. 2020.

NAZ, R.; KHAN, M. N. A. **Rapid applications development techniques**: A critical review, Int. J. Softw. Eng. its Appl., vol. 9, nº. 11, pp. 163–176, 2015.

NumPy. Consultado em meio eletrônico em: 4 ago. 2020.

Pandas. Consultado em meio eletrônico em: 4 ago. 2020.

PyQt. Consultado em meio eletrônico em: 4 ago. 2020.

PySide. Consultado em meio eletrônico em: 4 ago. 2020.

Python 3.8.5 documentation. Consultado em meio eletrônico em: 4 ago. 2020.

Spyder. Consultado em meio eletrônico em: 4 ago. 2020.

Tcl Developer Xchange. Consultado em meio eletrônico em: 4 ago. 2020.

The Falcon Web Framework. Consultado em meio eletrônico em: 4 ago. 2020.

turbogears. Consultado em meio eletrônico em: 4 ago. 2020.

wxPython. Consultado em meio eletrônico em: 4 ago. 2020.

# **CONTEUDISTA**

Sérgio Assunção Monteiro