def api_get_data(url_path):
    
    import requests
   
    response = requests.get(url_path)

    return response

def from_api_get_to_dataframe(my_object):
    
    import pandas as pd

    return pd.DataFrame(my_object.json())

def show_tables():
    
    import pandas as pd
    import os

    df = pd.read_excel("Entrega_Parcial_1\\DE_PARA_API_URL_00.xlsx", sheet_name="de_para")

    os.system('cls')
    print("-"*40)
    for my_row in range(0, len(df)):
        print(f"{df.index[my_row]} >> {df.loc[my_row, "API"]}")
    print("-"*40)
    