import pandas as pd
import requests
import alerta_aula_04 as warning

# Faz a requisição dos dados da API
def api_get_data(url_path):
    response = requests.get(url_path)
    return response

# Checa se o retorno da API foi bem sucedido
def check_api_get_data(response_sts_code):
    if response_sts_code in range(200, 300):
        return True
    return False

# Retorna um dataframe com os dados da API
def from_api_to_dataframe(my_object):
    return pd.DataFrame(my_object.json())

# Retorna um dataframe com a lista de APIs
def get_api_list_from_xls(excel_path="DE_PARA_API_URL.xlsx", my_sheet_name="de_para"):
    return pd.read_excel(excel_path, sheet_name=my_sheet_name)

# "Printa" a lista de APIs disponíveis 
def print_api_list(api_list_df):
    if len(api_list_df) == 0:
        print("Lista vazia!")
        return False
    print("-"*40)
    for my_row in range(0, len(api_list_df)):
        print(f"{api_list_df.index[my_row]} >> {api_list_df.loc[my_row, "API"]}")
    print("-"*40)
    return True

# Retorna o índice da API escolhida (-1 se der erro na API)
def choose_api(api_list_df):
    print_api_list(api_list_df)
    choosen_table_index = int(input(f"Digite o número da API: "))
    if not check_api_get_data(api_get_data(api_list_df.loc[choosen_table_index, "URL"]).status_code):
        warning.alerta(3, api_list_df.loc[choosen_table_index, "API"], "Request GET URL")
        return -1
    return choosen_table_index

# Retorna um dataframe com os dados da API escolhida
def get_dataframe(api_list_df, choosen_table_index):
    if choosen_table_index == -1:
        return pd.DataFrame()
    choosen_table_url_data = api_get_data(api_list_df.loc[choosen_table_index, "URL"])
    return from_api_to_dataframe(choosen_table_url_data)