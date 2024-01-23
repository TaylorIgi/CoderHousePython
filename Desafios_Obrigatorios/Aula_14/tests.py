
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

# print("-"*40)
# for col in df.columns:
#     print(col)
#     print(df[col].unique())
#     print("-"*40)

if table_index == 0:
    df=trf.transform_bancos(df)
elif table_index == 1:
    df=trf.transform_corretoras(df)
elif table_index == 2:
    df=trf.transform_cidade_uf(df)
elif table_index == 3:
    df=trf.transform_clima(df)
elif table_index == 4:
    df=trf.transform_feriados(df)
elif table_index == 6:
    df=trf.transform_uf_regiao(df)
elif table_index == 7:
    df=trf.transform_ncm(df)

print("-"*40)
print("DF Limpo:")

print(df.info())

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