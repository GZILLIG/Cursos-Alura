<h1>Business Inteligence - Conceitos de ETL</h1>

<h2>Construir a estrutura do Data Warehouse</h2>
Antes de realizarmos a Extração, Transformação e Carga, precisamos definir qual vai ser a estrutura que irá receber essas informações.
O diferencial da análise BI, para com aqueles relatórios comuns que cada sistema dentro de uma empresa emite, é que o profissional de BI olha para o todo. Isso porque o Datawarehouse, idealmente, contém todos os dados da empresa independente do sistema ou armazenamento usado. Além disso, o Datawarehouse tem sua estrutura construida justamente pensando nas análises que se deseja obter, e mais, a informação deve estar padronizada e limpa.

<h3>Definir Dimensões</h3>
Após definir através de reuniões e entrevistas o que se quer medir dentro da empresa, é necessário começar a estruturar o banco de dados que receberá a carga dessas informações.
**Dimensão** é o nome dado para um parametro que irá pertencer à diversas métricas, um catálogo.
Por exemplo, o cadastro dos clientes da empresa. Esse cadastro tem diversos campos: Razão Social, CNPJ, Endereço, Ramo de negócio, etc.
Isso tudo ficaria dentro de uma Dimensão, ou seja, tudo a respeito de clientes, fica nessa tabela (ou conjunto de tabelas).
Outro exemplo: Dimensão de produtos. Nela, vão tdas as informações sobre os produtos da empresa: Nome, Tamanho, Preço, Cor, etc...

<h3>Definir Tabelas de Fato</h3>
Tabela de Fato é o nome que se dá às tabelas que irão conter as informações da nossa análise. Ela irem herdar valores (chave estrangeira) das tabelas de Dimensão.
Por exemplo: A Tabela de Fato Vendas, irá herdar informações dos domínios Cliente, Vendedor, Produto... mas **também** terá suas próprias informações como "Valor total da venda", ou então "Quantidade de produtos". Esse valores exclusivos da tabela são chamados de **Atributos**.

<h2>**E**xtract - Extrair</h2>
A extração é feita quando criamos uma conexão com nossas fontes de dados. Suponhamos que em uma empresa, o cadastro de clientes esteja em uma planílha de Excel, o cadastro de produtos esteja em um banco de dados SQL, as finormações de venda em um servidor Web que salva os registros em .csv...
Precisamos configurar a configuração para cada uma dessas fontes de dados. Além disso, existe a possibilidade de agendar quando e com que frequencia essas extrações acontecem.

<h2>**T**ransform - Transformar, ou tratar</h2>
Geralmente esses dados não vem "limpos" e organizados da forma que precisamos para analise futura.

* Um exemplo: A pessoa que é responsavel por criar os cadastros de cliente, coloca a cidade e estado no mesmo campo que a razão social.

Precisamos extrair e separar essa informação para seus respectivos campos para rodar nossa análise.
TODA vez que realizarmos a extração da fonte de dados, essas informações precisam ser tratadas.
Evidentemente não vamos fazer isso manualmente (podemos ter milhares de registros nessa fonte). Para isso, criamos um fluxo de tratamento de dados, onde cada passo é programado e configurado, para no final, obtermos a informação do jeito q queremos. Esse "passo-a-passo" será nossa receita para que, toda vez que realizarmos uma extração, esses dados já são tratados de forma automática e ordenada.

<h3>**L**oad - Carga</h3>
Com o fluxo de dados configurado da Extração e Transformação, temos que gravar esses dados no Datawarehouse que criamos.
na fase de transformação, devemos conhecer bem a estrutura do Warehouse, pois é nela que vamos criar ou tratar os campos. Com essa estrutura já pronta, basta criar as conexões para o Banco de dados do DW.
É importante observar que, como todo banco relacional, devemos tomar cuidado para carregar as informações na ordem certa.

* Exemplo: Carregar os dados da tabela Produto, sem antes carregar a tabela Marcas. Nesse caso, Marcas é um campo chave estrangeira dentro de Produto, e precisa dessa informação antes de ser carregado.
