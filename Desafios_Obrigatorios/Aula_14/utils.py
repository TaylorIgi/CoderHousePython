def api_get_data(url_path):
    
    import requests
   
    response = requests.get(url_path)

    return response

def check_api_get_data(response_sts_code):
    if response_sts_code in range(200, 300):
        return True
    return False

def from_api_get_to_dataframe(my_object):
    
    import pandas as pd

    return pd.DataFrame(my_object.json())

def extract_and_print_tables():
    
    import pandas as pd
    import os
    import time
    import alerta_aula_04 as warning

    df = pd.read_excel("DE_PARA_API_URL.xlsx", sheet_name="de_para")

    table_qty = int(input("Quantas tabelas serão extraídas? "))
    table_number = 1

    while table_number <= table_qty:

        os.system('cls')
        print("-"*40)
        for my_row in range(0, len(df)):
            print(f"{df.index[my_row]} >> {df.loc[my_row, "API"]}")
        print("-"*40)
        
        choosen_table_index = int(input(f"Digite o número da {table_number}a tabela: "))

        if not check_api_get_data(api_get_data(df.loc[choosen_table_index, "URL"]).status_code):
            warning.alerta(3, df.loc[choosen_table_index, "API"], "Request GET URL")
            #continue
        else:
            choosen_table_url_data = api_get_data(df.loc[choosen_table_index, "URL"])
            choosen_table_df = from_api_get_to_dataframe(choosen_table_url_data)
            os.system('cls')
            print(f"Exemplo de dados da tabela {df.loc[choosen_table_index, "API"]}:\n")
            print(choosen_table_df.head(5))
            time.sleep(4)

        table_number +=1
    
    os.system('cls')
    print("Programa finalizado!")
    time.sleep(4)
    os.system('cls')