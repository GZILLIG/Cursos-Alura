<h1> Business Intelligence </h1>

<h2>Primeiros Conceitos</h2>
O BI surge a partir da necessidade empresarial de analisar dados, que podem vir de dentro da própria empresa ou de fora. Transformar **dados** em **informações** para auxiliar na tomada de decisões, é a principal missão do BI.

<h3>Criação do Data Warehouse</h3>
O Data Warehouse (armazém de dados) será a matéria-prima do BI.

Uma empresa pode ter diversos sistemas (Ex.: Controle de estoque, fiscal, financeiro, administrativo, logistico...), e quase sempre esses sistemas não se comunicam. 

Para obtermos dados valiosos sobre o negócio, deve ser possível cruzar informação de todas as plataformas insternas e externas da empresa, para medirmos as métricas da empresa.

O Data Warehouse, então, é esse armazém onde guardamos todas as informações extraídas, com dados já tratados e padronizados. De preferẽncia, o *DW* não deve ser um banco de dados utilizado para a operação da empresa.

<h3>Matriz Dimensão x Indicador</h3>

**Indicador: O que medir?**
São os valores, variáveis do que será medido.
(Ex.: Total de faturamento, ou então, quantidade de vendas).

**Dimensões? Como medir?**
São as diferentes formas de pesquisar o valor, critérios.
(Ex.: Faturamento por cidade, ou então, vendas por cliente).

Na matriz, os indicadores são as linhas, e as dimensões, as colunas. É importante fazer o levantamento de que indicadores fazem sentido para quais dimensões.


<h3>Tabela de Fato</h3>
Com a matriz de dados montada, é necessário identificar os padrões entre os cruzamentos DimensãoxIndicador.
Suponhamos que 2 indicadores fazem sentido serem registrados com as mesmas 8 dimensões. Sendo assim, não faz sentido ter um registro separado para cada indicador.

<h3>Mais conceitos sobre dimensões</h3>
Dentro de uma dimensão podemos agrupar vários indicadores em comum para aquele tema.

Por exemplo:
* Em um registro de venda para um cliente, e nesse registro constam diversas colunas dcom informações cadastrais (CNPJ, Razão Social, Endereço).

Faz muito mais sentido criarmos uma tabela de fato contendo apenas dados cadastrais dos Clientes, e atribuir um código para cada cliente.
Dessa forma, quando consultarmos o registro de venda, teremos apenas um campo: Código do Cliente.


**Existem então dois modelos de tabelas de dimensão:**

* **Estrela (Star Schema)**: Modelo desnormalizado, onde a informação fica toda concentrada apenas em uma tabela de fato, e os valores se repetem sempre que necessário

* **Floco de Neve (Snow Flake Schema)**: Modelo normalizado, com diversas tabelas de fato, uma para cada tipo de informação, afim de evitar dados repetidos. Elas se relacionam através de hierarquia e atributos.

<h3>Hierarquias e Atributos dentro de dimensões</h3>

A hierarquia dos dados é necessária para entendermos valores que depende um do outro. Por exemplo, existe a hierarquia País, Estado e Município. Nessa exemplo, são 3 níveis de hierarquia, sendo o nível mais alto o País e o nivel mais baixo (nível de folha), o Município.

Pode existir também, o **Atributo**. Ele é associado á exclusivamente uma entidade. É utilizado quando a relação entre duas entidades é 1:1, ou seja, aquele valor se relaciona apenas para outro valor. Por exemplo, o número de telefone de um cliente. telefone é um valor único e serve apenas à aquele cliente. Logo, sabemos que a entidade Telefone é um Atributo.
O atributo também pode ser quando existem poucos valores a serem atribuidos, por exemplo, quando a entidade Tamanho só pode ser 3 valores: Pequeno, Médio e Grande.

**Dimensão Irregular**
A dimensão irregular é comum, e existe quando temos algumas entidades que não se relacionam no mesmo nível que as outras.

Por exemplo, podemos cadastrar fornecedores nacionais com Pais, Estado e Cidade, mas quando temos um fornecedor internacional cadastramos apenas País e Cidade.
Nesse caso, criamos a tabela pai-filho-nivel, que irá atribuir um número índice que percorre toda a árvore de hierarquia.

<h3>Dimensão Tempo - Granularidade e Periodicidade</h3>

* **Periodicidade**: É a resolução na qual aquele evento é medido e registrado, com que frequência.

* **Granularidade**: É a medida de tempo que é usada naquele processo.

Exemplo: O custo de energia elétrica é medido de segundo em segundo (em tempo, real, na verdade) pelo medidor de energia - porém a granularidade que a conta de luz apresenta, é de mês em mês.

Em resumo, é importante se atentar para que a periodicidade seja frequente o suficiente para atender as informações da menor Granularidade do seu BI.
* * **Tabela ODS**: Quando temos uma Periodicidade menor (ou seja, com uma frenquencia alta) e uma Granularidade de periodos maiores, armazenamos esses dados ao longo do tempo numa ODS (Operational Data Storage). Esse banco de dados tem como função armazenar dados, para que sejam extraídos futuramente, na frenquencia que a Granularidade pede. O ODS então é apagado, e o processo reinicia.

<h3>OLAP - Online Analytical Processing</h3>

As estruturas transacionais (OLTP) de bancos de dados, como o Star Schema, podem ser muito bons do ponto de vista de organização da informação, mas quando vamos fazer consultas cruzando informações o desenpenho dessas arquiteturas deixa a desejar.

Imagine que para buscar uma informação como "Todas as vendas para clientes com caracteristica X", teriamos que fazer Scan em várias tabelas (já que a informação está distribuída), para chegar no resultado. Isso não é eficiente para o BI.

OLAP foi a solução imaginada para esse problema, que tem como principal caracteristica "pivotear" os dados da tablea com mais facilidade. Os dados nele, são organizados por fórmulas matemáticas. 

* Por exemplo, na dimensão produtos de uma adega

```
Suco = Suco de Laranja + Suco de Maça
Águas = Água com Gás + Agua sem Gás 
Todos os produtos = Sucos + Águas
```
Dessa forma, as relações dimensionais são criadas no OLAP.

Suponhamos que queremos fazer um cruzamento de dados entre as dimensões Cliente e Produto.

A estrutura OLAP irá criar uma tabela grande, onde temos TODOS os membros da dimensão *Cliente* nas linhas, e TODOS os membros da dimensão *Produto* nas colunas. Dessa forma, todos as informações são colocadas em um único plano.
Assim, os dados ficam prontos para serem acessados utilizando uma fração do esforço que seria consultar o banco de dados OLTP.

Sendo assim, o OLAP é construido baseado **no tipo de análise que vamos fazer**. Ele construidá uma matriz que será calculada previamente e irá armazenar os dados de TODAS os cruzamentos de dados possível. Por isso, as matrizes OLAPs são gigantescas e aumentam exponencialmente o número de dados.

Existe um indicador que avalia o quanto dessas informações pré-calculadas são realmente úteis.

```
densidade =  Número de Combinações Reais
               -----------------------------
               Número de Combinações Possíveis
```

Precisamos manter o equilíbrio entre poder computacional e armazenamento. Para isso, existe 3 tipos de OLAPs:

* **MOLAP - Multidimensional OLAP**: É o modelo descrito acima, onde todos os cruzamentos de dados possíveis são pré-calculados e armazenados. É o que possui o melhor desempenho para consulta, porém pode tem facilmente bilhões ou trilhões de combinações, o que faz ele gigantesco e demandar muito tempo para ser calculado.

* **HOLAP - Hibrid OLAP**: Cria a matriz capenas com dados mais consolidados (por exemplo, total de vendas, total de entregas), e deixa as consultas mais específicas serem pesquisadas pela tabela de fato. Os relatórios feitos pelo Holaps não deixam transparente se o dado veio da matriz ou da tabela de fato.

* **ROLAP - Relational OLAP**: Consolida a matriz OLAP apenas no momento da consulta, e armazena esses resultados em cache. Dessa forma, a matriz vai crescendo conforme as solicitações, deixando mais fácil acesso para as relações de dados mais frequentes. Oferecem o melhor equilíbrio entre esforço computacional e tamanho de armazenamento.

<h3>Resumindo o Fluxo do BI e Data Warehouse</h3>
1. Matriz (identificar quais dados são necessários);
2. Construção do Data Warehouse;
3. Identificação das fontes de dados;
4. Criação do processo de ETL e/ou construção de ODS;
5. Carga do Data Warehouse;
6. Criação e carga dos OLAPs;
7. Construção e criação dos aplicativos para consulta dos; dados por parte dos usuários.

<h3>Glossário de outros termos</h3>
* Data Minning: Ciência de dados, tende a identificar padrõesde comportamento nos dados do passado e criar insights para o futuro

* Balance ScoreCard: Determinar em uma linguagem simples as métricas da empresa (KPI), onde fica claro qual é o status daquele objeto de estudo. Por exemplo: A eficiência da produção está em amarelo, ou então as  vendas estão em verde.

* Big Data: Engenharia de dados, é a carga de dados de uma massa de dados de tráfego de informações (Data Lake).

<h3>Valores Importantes de BI</h3>

* **Democratizar a Informação** : Não basta cirar um DW eficiente, é preciso disponibilizar aos usuários envolvidos no processos, formas de eles mesmos fazerem suas consultas. O BI gera relatórios específicos geralmente para um grupo pequeno, e o restante dos envolvidos não pode depender apenas desses relatórios.


