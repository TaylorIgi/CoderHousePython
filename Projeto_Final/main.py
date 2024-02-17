#import functions_api as api
import functions_sql as sql
import utils
import os
import time
    
sql.drop_db("DB_PROJ_FINAL.db")
check_continue = 1

while check_continue == 1:

    dict_user_df = utils.get_user_df()
    original_df = dict_user_df["user_df"]
    api_name = dict_user_df["api_name"]
    transformed_df = utils.transform_user_api_df(original_df, dict_user_df["table_index"])

    os.system("cls")
    print(f"{dict_user_df["table_index"]} >> {api_name}")
    time.sleep(2)

    if dict_user_df["table_index"] != 6: # o dataframe desta API tem uma coluna com uma lista, estava dando erro para subir no DB
        utils.save_api_df_to_db(original_df, api_name + "_original")
    
    connection = utils.save_api_df_to_db(transformed_df, api_name + "_tratado")

    os.system("cls")
    if dict_user_df["table_index"] != 6:
        print(f"O banco de dados foi atualizado com os dados tratados e os dados originais da API {api_name}!\n")
    else:
        print(f"O banco de dados foi atualizado somente com os dados tratados da API {api_name}!\n")

    if input("Deseja ver as informações das APIs carregadas? (Responda sim ou nao)\n").lower() == "sim":
        print("-"*100)
        print("\nOriginal:\n")
        print(original_df.info())
        print("- "*50)
        print("\nTratado:\n")
        print(transformed_df.info())
        print("-"*100)
        time.sleep(5)
    else:
        print("-"*100)
    
    check_continue = utils.check_next_action()

time.sleep(1)
os.system("cls")

print("-"*100)
db_tables = sql.get_db_tables(connection.db_conn)
print("Tabelas atualizadas no banco de dados:\n")
for table in db_tables:
    print(table)
print("-"*100)
time.sleep(5)
print("Programa finalizado!")