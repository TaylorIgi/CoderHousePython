
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