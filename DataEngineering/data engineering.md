<h1>Introdução à Data Engineering</h1>

<h2>Conceitos/ Glossário:</h2>


**Estrutura de dados**: Os dados podem estar organizados das seguintes formas: 
* **Estruturado**: Tabelas de banco de dados, com valores dividos por colunas e linhas, de forma que os dados já estejam catalogados e de fácil acesso para consulta. (Ex.: SQL, planilha de Excel)
* **Semi-Estruturado**: Geralmente em formatos como .json, .xml .csv. Os dados possuem a informação necessária, mas ainda n]ao estão em formato de tabela, sendo necessário rodar algum software ou código para extrair essas informações.
* **Não-estruturado**: São dados brutos, sem classificação alguma. A informação está lá, mas sua extração não é simples, por exemplo (áudios, videos, imagens, textos não catalogados)

**Data Warehouse**: Em tradução livre "Armazém de dados", é o  conceito dado oas tradicionais servidores de armazenamento, quando os dados da empresa estão guardados. Nessa modalidade, os dados já estão organizados e de forma estruturada, disponível para fácil consulta. Os dados são guardados sempre para consulta futura, o que pode fazer o Warehouse ter um tamanho enorme de informações.

**Data Lake:** O data lake é o nome dado aos dados que possuem sua forma mais bruta, logo após a sua aquisição. Nele, as informações podem estar em diversos estágios de tratamento. As informações extraidas são direcionadas diretamente para ele, e é nesse ambiente que os dados começarão a ser tratados para gerar informações estruturadas. Também pode tem um volume enorme de dados, porém a idéia aqui não é manter o passado daquelas informações - é um ambiente de refinamento de dados.

**Pipeline:** Se existe o "lago de dados", existe a tubulação quem transporta o conteúdo para encher esse lago. Pipeline refere-se ao canal de comunicação criado para extrair os dados. Por exemplo, pode-se criar uma pipeline para extrair diariamente dados de uma conta do Twitter via uma API. O pipiline pode ser em: 
* Batch: Gera pacotes fechados de dados, em que o pipeline tem tarefas agendadas e configuradas para rodar em ciclos, com uma periodicidade definida.
* Streaming: os dados são extraídos em tempo real, idealmente são extraidos no momento de sua criação. Consome muitos recursos computacionais.

**Processos dos dados**
Siglas muito comuns de serem vistam são ETL e ELT. As letras significam:
* **E**xtract (Extrair)
* **T**ransform (Transformar, ou Tratar)
* **L**oad (Carregar)

Basicamente, o que altera é a ordem com que esses eventos acontecem. 
No ETL, a informação é extraida de uma fonte, passa por um processo de transformação automatizada e é carregada em um armazem para uso.
++recursos computacinais
+automação da engenharia de dados
-armazenamento

No ELT, a informação é extraida de uma fonte e já armazenada, para só após ser tratada.
+recursos computacinais
-automação da engenharia de dados
+armazenamento


**Softwares utilizados em Engenharia de dados:**
* Agendadores (Apache Airflow): Programas especializados em conectar com uma fonte (banco de dados, API, webserver, etc), e agendar as tarefas de extração de forma automatizada.

* Processadores de dados: (Apache Spark, Apache Beam): Geralmente trabalham já em conjunto com os agendadores, e com base em um código feito pelo Engenheiro de Dados, começa a transformar o dado bruto em dados mais estruturados, podendo ter vários estágios de transformação.

**Especificações para aquisição de dados:**
Geralmente, os dados que irão ser analisados são especificados por um departamento estratégico, como o Marketing. é fundamental que nessa especificação esteja claro quais dados serão extraídos e como eles devem ser tratados. É preciso ter clareza nessa etapa, pois se a especificação não estiver clara, é possível termos o excesso ou falta de dados no final do processo.