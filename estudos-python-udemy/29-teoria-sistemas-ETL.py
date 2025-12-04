"""
ETL -> extração, Transformação e Carga
É um processo utilizado para coletar dados de diferentes fontes, processá-los 
e carregá-los em um destino, como um banco de dados ou data warehouse(casa dos dados).

-> COMPONENTES DO ETL
Extração: coleta de dados de fontes como APIs, arquivos, bancos de dados ou web scraping.
Transformação: processamento, limpeza e formatação dos dados para atender aos requisitos.
Carga: inserção dos dados processados em um banco de dados ou sistemas de destino.

-> BENEFÍCIOS DO ETL
- integração de dados de várias fontes.
- melhoria da qualidades dos dados.
- automatização de processos repetitivos.
- preparação de dados para análises e relatórios.

PIPELINE DE DADOS
É uma série de etapas automatizadas que processam dados desde a sua origem até um destino
final, permitindo integração contínua. 

-> COMO A PIPELINE SE RELACIONA COM A ETL
- o ETL é apenas uma forma de pipeline de dados. (existe LTE/ EL/ ELT)
- uma pipeline pode incluir mais etapas além de ETL, como análise ou marchine learning.
- pipelines são frequentemente utilizados para integração contínua de dados.

-> EXEMPLOS REAIS DE ETL
1. Relatório financeiro: 
    - extração de dados de sistemas contábeis.
    - transformação para normalizar contas.
    - carga em um data warehouse para relatórios.
2. E-commerce:
    - coleta de dados de vendas.
    - processamento para calcular tendências.
    - armazenamento em um banco de dados para análise.

-> DESAFIOS DO ETL
- dados inconsistentes e incompletos
- manuntenção de pipelines complexos.
- escabilidade para grandes volumes de dados.
- latência em processos com alta frequência.

-> FERRAMENTAS COMUNS PARA ETL
- Apache Airflow: gerenciamento de pipelines.
- Talend: plataforma comppleta para ETL.
- Python: scripts customizados para ETL.

-> ESTRUTURA BÁSICA DE UM PIPELINE ETL
- Entrada: dados brutos de fontes diversas (ex: APIs, bancos).
- Processamento: limpeza, normalização e transformação.
- Saída: dados organizados em destino (ex: banco de dados, arquivo).

-> AUTOMAÇÃO NO ETL
- automação reduz erros manuais.
- integração com agendadores como cron ou ferramentas como Apache Airflow.
- fluxos contínuos para dados em tempo real.

-> QUANDO USAR ETL
- integração de dados diferentes fontes.
- preparação de daodos para análise ou relatórios.
- migração de dados entre sistemas .
- alimentação de data warehouses.

-> BOAS PRÁTICAS
- validar dados em cada etapa
- monitorar e registrar erros
- projetar pipelines escaláveis
- automatizar processos para evitar tarefas repetitivas

ETL é um processo específico de dados que extrai, transforma e carrega informações para um destino.
Pipelines são fluxos automatizados de tarefas, podendo incluir ETL, ML, testes ou qualquer sequência de passos.
Ou seja, ETL é um tipo de pipeline, mas pipelines vão muito além apenas do tratamento de dados.

"""
