import os
import time
import pandas as pd
import functions_api as api
import functions_sql as sql
import transform_api as trf

# Retorna um dataframe com os dados da API escolhida pelo usuário
def get_user_df():
    api_list_df = api.get_api_list_from_xls()
    table_index = api.choose_api(api_list_df)
    api_name = api_list_df.loc[table_index, "API"]
    return {"user_df": api.get_dataframe(api_list_df, table_index), "table_index": table_index, "api_name": api_name}

# Retorna um datraframe tratado
def transform_user_api_df(df, table_index):
    if table_index == 0:
        return trf.transform_bancos(df)
    elif table_index == 1:
        return trf.transform_corretoras(df)
    elif table_index == 2:
        return trf.transform_cidade_uf(df)
    elif table_index == 3:
        return trf.transform_clima(df)
    elif table_index == 4:
        return trf.transform_feriados(df)
    elif table_index == 5:
        return pd.DataFrame()
    elif table_index == 6:
        return trf.transform_uf_regiao(df)
    elif table_index == 7:
        return trf.transform_ncm(df)
    elif table_index == 8:
        return trf.transform_pix(df)
    elif table_index == 9:
        return trf.transform_taxas(df)

# Checa se o usuário gostaria de salvar o df tratado na base de dados
# def check_save_api_df_to_db(api_name):
#     return input(f"Salvar os dados da API {api_name} no banco dados? (Responda sim ou não)\n").lower() == "sim"

# Salva o df tratado na base de dados e atualiza os dados do objeto MyDatabase
def save_api_df_to_db(df, api_name):
    conn = sql.connect_to_db("DB_PROJ_FINAL.db")
    sql.add_df_to_db(conn, df, "tb_" + api_name.lower())
    return conn

def check_next_action():
    print("O que deseja fazer agora?\n")
    print("1 >> Salvar outra API")
    print("2 >> Sair")
    return int(input("\nDigite o número da sua opção: "))

def main():
    
    check_continue = 1
    
    while check_continue == 1:
    
        dict_user_df = get_user_df()
        original_df = dict_user_df["user_df"]
        api_name = dict_user_df["api_name"]
        transformed_df = transform_user_api_df(original_df, dict_user_df["table_index"])

        os.system("cls")
        print(f"{dict_user_df["table_index"]} >> {api_name}")
        time.sleep(2)

        if dict_user_df["table_index"] != 6: # o dataframe desta API tem uma coluna com uma lista, estava dando erro para subir no DB
            save_api_df_to_db(original_df, api_name + "_original")
        
        connection = save_api_df_to_db(transformed_df, api_name + "_tratado")

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
        
        check_continue = check_next_action()
    
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

main()