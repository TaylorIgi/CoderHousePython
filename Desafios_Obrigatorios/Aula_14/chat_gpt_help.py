
import sqlite3

def get_table_names(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Consulta para obter os nomes das tabelas no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [row[0] for row in cursor.fetchall()]

    conn.close()
    return table_names

# Substitua 'coderhouse_python_54360.db' pelo nome do seu banco de dados SQLite
db_name = 'coderhouse_python_54360.db'
tables = get_table_names(db_name)

print("Tabelas no banco de dados:")
for table in tables:
    print(table)

################################################################################

import os

def drop_database(db_name):
    # Verifica se o arquivo do banco de dados existe
    if os.path.exists(db_name):
        # Conecta ao banco de dados
        conn = sqlite3.connect(db_name)
        
        # Obtém um cursor
        cursor = conn.cursor()
        
        # Fecha a conexão com o banco de dados
        conn.close()
        
        # Remove o arquivo do banco de dados
        os.remove(db_name)
        print(f'Banco de dados {db_name} removido com sucesso.')
    else:
        print(f'O banco de dados {db_name} não existe.')

# Substitua 'nome_do_banco.db' pelo nome do seu banco de dados SQLite
drop_database('nome_do_banco.db')
