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

dict_df = utils_aula_14.get_table()
print(dict_df["API"])


if len(dict_df["dataframe"]) == 0:
    print("Dataframe vazio")
elif dict_df["API"] == "Bancos":
    df = utils_aula_14.transform_bancos(dict_df["dataframe"])

print(dict_df["dataframe"].info())
print(df.info())