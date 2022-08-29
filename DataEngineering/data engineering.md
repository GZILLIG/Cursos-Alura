<h1>Introdução à Data Engineering</h1>

<h2>Conceitos/ Glossário:</h2>


<h3>Estrutura de dados</h3>
Os dados podem estar organizados das seguintes formas: 

* **Estruturado**: Tabelas de banco de dados, com valores dividos por colunas e linhas, de forma que os dados já estejam catalogados e de fácil acesso para consulta. (Ex.: SQL, planilha de Excel)
* **Semi-Estruturado**: Geralmente em formatos como .json, .xml .csv. Os dados possuem a informação necessária, mas ainda n]ao estão em formato de tabela, sendo necessário rodar algum software ou código para extrair essas informações.
* **Não-estruturado**: São dados brutos, sem classificação alguma. A informação está lá, mas sua extração não é simples, por exemplo (áudios, videos, imagens, textos não catalogados)

<h3>Conceitos de armazenamento</h3>

**Data Warehouse**: Em tradução livre "Armazém de dados", é mais próximo do  conceito dos tradicionais servidores de armazenamento, quando os dados da empresa estão guardados. Nessa modalidade, os dados já estão organizados e de forma estruturada, disponível para fácil consulta. Vale lembrar que, idealmente, os data warehouses são uma estrutura de armazenamento *à parte* dos banco de dados operacionais da empresa. Aqui, os dados já foram limpos, padronizados e integrados dos demais sistemas. Por exemplo, um e-commerce tem um sistema web, um sistema fiscal SAP e um sistema de estoque Oracle. O data warehouse existe para unificar todas as informações, mesmo que os sistemas não se comuniquem.

**Data Silo**: É a forma mais tradicional de armazenamento de dados. São os dados operacinais dos sistemas da empresa.

**Data Lake:** O data lake é o nome dado aos dados que possuem sua forma mais bruta, logo após a sua aquisição. Nele, as informações podem estar em diversos estágios de tratamento. As informações extraidas são direcionadas diretamente para ele, e é nesse ambiente que os dados começarão a ser tratados para gerar informações estruturadas. Também pode tem um volume enorme de dados, porém a idéia aqui não é manter o passado daquelas informações - é um ambiente de refinamento de dados.

<h3>Pipeline:</h3> Se existe o "lago de dados", existe a tubulação quem transporta o conteúdo para encher esse lago. Pipeline refere-se ao canal de comunicação criado para extrair os dados. Por exemplo, pode-se criar uma pipeline para extrair diariamente dados de uma conta do Twitter via uma API. O pipiline pode ser em: 
* Batch: Gera pacotes fechados de dados, em que o pipeline tem tarefas agendadas e configuradas para rodar em ciclos, com uma periodicidade definida.
* Streaming: os dados são extraídos em tempo real, idealmente são extraidos no momento de sua criação. Consome muitos recursos computacionais.

<h3>Processos dos dados</h3>
Siglas muito comuns de serem vistam são ETL e ELT. As letras significam:

* **E**xtract (Extrair)
* **T**ransform (Transformar, ou Tratar)
* **L**oad (Carregar)

Basicamente, o que altera é a ordem com que esses eventos acontecem. 
No *ETL*, a informação é extraida de uma fonte, passa por um processo de transformação automatizada e é carregada em um armazem para uso.
++recursos computacinais
+automação da engenharia de dados
-armazenamento

No *ELT*, a informação é extraida de uma fonte e já armazenada, para só após ser tratada.
+recursos computacinais
-automação da engenharia de dados
+armazenamento


<h3>Softwares utilizados em Engenharia de dados:</h3>

* **Agendadores** (Apache Airflow): Programas especializados em conectar com uma fonte (banco de dados, API, webserver, etc), e agendar as tarefas de extração de forma automatizada.

* **Processadores de dados** (Apache Spark, Apache Beam): Geralmente trabalham já em conjunto com os agendadores, e com base em um código feito pelo Engenheiro de Dados, começa a transformar o dado bruto em dados mais estruturados, podendo ter vários estágios de transformação.

<h3>Especificações para aquisição de dados:</h3>

Geralmente, os dados que irão ser analisados são especificados por um departamento estratégico, como o Marketing. é fundamental que nessa especificação esteja claro quais dados serão extraídos e como eles devem ser tratados. É preciso ter clareza nessa etapa, pois se a especificação não estiver clara, é possível termos o excesso ou falta de dados no final do processo.