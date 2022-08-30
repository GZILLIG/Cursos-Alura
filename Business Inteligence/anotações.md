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

Essa lógica contribui tanto para a organização do banco de dados, quanto para a eficiência do armazenamento, reaproveitando informações ao invés de repeti-las.

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