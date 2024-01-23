import classes
import pandas as pd
import sqlite3
import functions_sql
import functions_api
import utils

api_list_df = functions_api.get_api_list_from_xls()
table_index = functions_api.choose_api(api_list_df)
df = functions_api.get_dataframe(api_list_df, table_index)

print(df.head())



# # Dataframe para teste 1
# dados1 = {
#     'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Idade': [25, 30, 22, 35],
#     'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre']
# }
# df1 = pd.DataFrame(dados1)

# # Dataframe para teste 2
# dados2 = {
#     'Produto': ['Maçã', 'Arroz', 'Feijão', 'Frango', 'Salada'],
#     'Categoria': ['Fruta', 'Cereal', 'Legume', 'Proteína', 'Vegetal'],
#     'Calorias': [52, 130, 230, 165, 50],
#     'Preço': [2.5, 3.0, 4.5, 8.0, 2.0]
# }
# df2 = pd.DataFrame(dados2)

# teste = functions_sql.connect_to_db("DB_TESTE.db")

# # Inclui df1 no db e nas tabelas da instancia de mydb
# functions_sql.add_df_to_db(teste, df1, "tb_df1")

# # Inclui df2 no db e nas tabelas da instancia de mydb
# functions_sql.add_df_to_db(teste, df2, "tb_df2")

# db_tables = functions_sql.get_db_tables(teste.db_conn)

# print("-"*40)
# print("Tabelas no DB:")
# for table in db_tables:
#     print(f"Tabela >> {table}")

# print("-"*40)
# print("Tabelas no objeto:")
# teste.list_tables()