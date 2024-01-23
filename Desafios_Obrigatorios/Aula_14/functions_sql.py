import sqlite3
import classes

# Retorna o nome das tabelas de um database
def get_db_tables(conn):
    
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [row[0] for row in cursor.fetchall()]

    return table_names

# Conecta no database enviado e retorna um objeto MyDatabase
def connect_to_db(database_name):
    conn = sqlite3.connect(database_name)
    return classes.MyDatabase(database_name, conn)

# Adiciona um dataframe no database do object_mydatabase e inclui o nome da tabela no mesmo objeto
def add_df_to_db(object_mydatabase, dataframe, database_table_name):
    dataframe.to_sql(database_table_name, object_mydatabase.db_conn, if_exists="replace", index=False)
    object_mydatabase.add_table(database_table_name)