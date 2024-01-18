
def extract_and_print_tables_new():
    
    import pandas as pd
    import os
    import time
    import alerta_aula_04 as warning
    import utils

    df = pd.read_excel("DE_PARA_API_URL.xlsx", sheet_name="de_para")

    table_qty = 1 #int(input("Quantas tabelas serão extraídas? "))
    table_number = 1

    while table_number <= table_qty:

        #os.system('cls')
        print("-"*40)
        for my_row in range(0, len(df)):
            print(f"{df.index[my_row]} >> {df.loc[my_row, "API"]}")
        print("-"*40)
        
        choosen_table_index = int(input(f"Digite o número da {table_number}a tabela: "))

        if not utils.check_api_get_data(utils.api_get_data(df.loc[choosen_table_index, "URL"]).status_code):
            warning.alerta(3, df.loc[choosen_table_index, "API"], "Request GET URL")
        else:
            choosen_table_url_data = utils.api_get_data(df.loc[choosen_table_index, "URL"])
            choosen_table_df = utils.from_api_get_to_dataframe(choosen_table_url_data)
    #        os.system('cls')
            print(f"Exemplo de dados da tabela {df.loc[choosen_table_index, "API"]}:\n")
            print(choosen_table_df.head(5))
     #       time.sleep(4)

        table_number +=1
    