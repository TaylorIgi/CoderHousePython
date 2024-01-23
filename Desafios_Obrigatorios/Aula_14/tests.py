import classes
import pandas as pd
import sqlite3
import functions_sql

# Dataframe para teste 1
dados1 = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 22, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre']
}
df1 = pd.DataFrame(dados1)

# Dataframe para teste 2
dados2 = {
    'Produto': ['Maçã', 'Arroz', 'Feijão', 'Frango', 'Salada'],
    'Categoria': ['Fruta', 'Cereal', 'Legume', 'Proteína', 'Vegetal'],
    'Calorias': [52, 130, 230, 165, 50],
    'Preço': [2.5, 3.0, 4.5, 8.0, 2.0]
}
df2 = pd.DataFrame(dados2)

# Conecta no db e cria uma instancia de mydb
conn = sqlite3.connect("DB_TESTE.db")
TesteDb = classes.MyDatabase("DB_TESTE.db", conn)

# Inclui df1 no db e nas tabelas da instancia de mydb
df1.to_sql("df_teste1", conn, if_exists="replace", index=False)
TesteDb.add_table("df_teste1")

# Inclui df2 no db e nas tabelas da instancia de mydb
df2.to_sql("df_teste2", conn, if_exists="replace", index=False)
TesteDb.add_table("df_teste2")

db_tables = functions_sql.get_db_tables(conn)

print("-"*40)
print("Tabelas no DB:")
for table in db_tables:
    print(f"Tabela >> {table}")

print("-"*40)
print("Tabelas no objeto:")
TesteDb.list_tables()