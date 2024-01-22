'''
Arquivo com as funções referentes a banco de dados
Importante >> a bibliotexa SQLAlchemy deve estar instalada!!!!!!

'''

import sqlite3
from sqlalchemy import create_engine
import sys
import time

# Conecta no banco de dados e retorna esta conexão
def connect_to_db(db_name = "coderhouse_python_54360.db"):
    return sqlite3.connect(db_name)

# Checa se a tabela já existe no banco de dados
def check_table_in_db(table_name, db_conn):
    
    return True

# Carrega o dataFrame no banco de dados
def dataframe_to_db(my_dataframe, table_name, db_conn = "coderhouse_python_54360.db"):
    if not check_table_in_db(table_name, db_conn):
        my_dataframe.to_sql(table_name, db_conn, if_exists='replace', index=False)
        print(f"Tabela {table_name} carregada com sucesso no {db_conn}.")
        return True
    elif input(f"A tabela {table_name} já existe no banco de dados {my_dataframe}.\n _
               Gostaria de sobrescrever a tabela? Responda Sim ou Nao: ").lower() == "s":
        print(f"Tabela {table_name} carregada com sucesso no {db_conn}.")
        return True
    print(f"Sem alterações no {db_conn}.")
    return False
        


# Fechar a conexão com o banco de dados
conn.close()