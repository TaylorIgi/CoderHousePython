
import pandas as pd
import functions_sql as sql
import functions_api as api
import transform_api as trf

api_list_df = api.get_api_list_from_xls()
table_index = api.choose_api(api_list_df)
df = api.get_dataframe(api_list_df, table_index)

print("DF Original:")
print(df.info())
# print(df.head())

print("-"*40)
print("DF Limpo:")
print(trf.transform_bancos(df).info())

# db = sql.connect_to_db("DB_TESTE.db")

# # Inclui df1 no db e nas tabelas da instancia de mydb
# sql.add_df_to_db(db, df, "tb_df")

# db_tables = sql.get_db_tables(db.db_conn)

# print("-"*40)
# print("Tabelas no DB:")
# for table in db_tables:
#     print(f"Tabela >> {table}")

# print("-"*40)
# print("Tabelas no objeto:")
# db.list_tables()