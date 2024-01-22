'''
Arquivo com as funções referentes a banco de dados
Importante >> a bibliotexa SQLAlchemy deve estar instalada!!!!!!

'''

import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import sys
import time

# Conecta no banco de dados e retorna esta conexão
def connect_to_db(db_name = "coderhouse_python_54360.db"):
    return sqlite3.connect(db_name)

# Checa se a tabela já existe no banco de dados
def check_table_in_db(table_name, db_conn):
    if pd.io.sql.table_exists(table_name, db_conn):
        return True
    return False

# Fecha a conexão com o banco de dados
def close_db_connection(db_conn):
    db_conn.close()

# Retorna uma lista com os nomes das tabelas do banco de dados
def get_table_names(db_conn):
    
    cursor = db_conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [row[0] for row in cursor.fetchall()]

    return table_names

# Carrega o dataFrame no banco de dados
def dataframe_to_db(my_dataframe, table_name, db_name = "coderhouse_python_54360.db"):
    
    db_conn = connect_to_db(db_name)
    db_name = db_conn.execute("PRAGMA database_list;").fetchall()[0][2]
    db_name = db_name[db_name.rfind("\\")+1:]

    if check_table_in_db(table_name, db_conn):
    
        print(f"A tabela {table_name} já existe no banco de dados {db_name}.")
        ck_overwrite = input(f"Gostaria de sobrescrever a tabela? Responda Sim ou Nao: ").lower()
    
        if ck_overwrite == "s":
            my_dataframe.to_sql(table_name, db_conn, if_exists='replace', index=False)
            print(f"Tabela {table_name} carregada com sucesso no {db_name}.")
            close_db_connection(db_conn)
            return True
        else:
            print(f"Sem alterações no {db_name}.")
            close_db_connection(db_conn)
            return False
    
    print(f"Tabela {table_name} carregada com sucesso no {db_name}.")
    close_db_connection(db_conn)
    return True