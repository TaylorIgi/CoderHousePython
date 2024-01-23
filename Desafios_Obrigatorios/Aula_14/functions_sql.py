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