# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Workflow
Mermaid nao funcionando!
'''mermaid
flowchart LR
    ETL[Pipeline]
        A[Múltiplos arquivos Excel] --> B[Extract: extract_data_from_excel]
        B --> |Gera uma lista de DataFrames| C[Transformation: concat_dataframes]
        C --> |Gera um DataFrame consolidado| D[Load: Converte para Excel]
        D --> |Salva o DataFrame consolidado em Excel| E[Output: Um único arquivo Excel]
    end

'''

# Função de Extração
### ::: app.pipeline.extract.extract_data_from_excel


# Função de Transformação
### ::: app.pipeline.transform.concat_dataframes


# Função de Load
### ::: app.pipeline.load.load_excel
