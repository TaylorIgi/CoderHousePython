'''
Descrição: Realizar o tratamento das bases coletadas via API do projeto final na aula 12.

1. Ajuste os nomes das colunas e linhas
2. Filtros de linhas e colunas, se necessário
3. Unstack e/ou stack
4. Tratamento do tipo das variáveis
5. Ajuste de missing values
6. Tratamento de colunas string

'''
import utils_aula_14
import time
import pandas as pd
import numpy as np

dict_df = utils_aula_14.get_table()

if len(dict_df["dataframe"]) == 0:
    print("Dataframe vazio")
elif dict_df["API"] == "Bancos":
    df = utils_aula_14.transform_bancos(dict_df["dataframe"])
elif dict_df["API"] == "Corretoras":
    df = utils_aula_14.transform_corretoras(dict_df["dataframe"])
elif dict_df["API"] == "Cidade / UF":
    df = utils_aula_14.transform_cidade_uf(dict_df["dataframe"])
elif dict_df["API"] == "Clima Capitais":
    df = utils_aula_14.transform_clima(dict_df["dataframe"])
elif dict_df["API"] == "Feriados Nacionais 2024":
    df = utils_aula_14.transform_feriados(dict_df["dataframe"])

print(dict_df["dataframe"].info())
print(df.info())
# print(dict_df["dataframe"].head(5))
# for col in df.columns:
#     print(df[col].head(5))
    
#print(df["cnpj"].unique())