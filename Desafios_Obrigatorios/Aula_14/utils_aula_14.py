
def get_table():
    
    import pandas as pd

    df_apis = pd.read_excel("DE_PARA_API_URL.xlsx", sheet_name="de_para")

    for my_row in range(0, len(df_apis)):
        print(f"{df_apis.index[my_row]} >> {df_apis.loc[my_row, "API"]}")
    print("-"*40)
    
    choosen_table = int(input(f"Digite o número da tabela: "))
    df = extract_tables(df_apis, choosen_table)

    return {"API": df_apis.loc[choosen_table, "API"], "dataframe": df}

def extract_tables(df, table_index):
    
    import pandas as pd
    import alerta_aula_04 as warning
    import utils

    df = pd.read_excel("DE_PARA_API_URL.xlsx", sheet_name="de_para")

    # Retorna um dataframe vazio se der erro no request
    if not utils.check_api_get_data(utils.api_get_data(df.loc[table_index, "URL"]).status_code):
        warning.alerta(3, df.loc[table_index, "API"], "Request GET URL")
        return pd.DataFrame()
    
    choosen_table_url_data = utils.api_get_data(df.loc[table_index, "URL"])
    choosen_table_df = utils.from_api_get_to_dataframe(choosen_table_url_data)
    
    return choosen_table_df

def transform_bancos(dataframe):

    transformed_df = dataframe.drop_duplicates()
    transformed_df = transformed_df.dropna(axis=0, subset=["ispb", "code"])
    
    subset_int = ["ispb", "code"]
    for col in subset_int:
        transformed_df[col] = transformed_df[col].astype("int")

    transformed_df.rename(columns={"fullName": "full_name"}, inplace = True)

    return transformed_df

def transform_corretoras(dataframe):

    import pandas as pd
    import numpy as np

    dataframe.replace("", np.nan, inplace=True)
    transformed_df = dataframe

    transformed_df["valor_patrimonio_liquido"] = transformed_df["valor_patrimonio_liquido"].fillna(0)

    transformed_df = transformed_df.dropna(axis=0, subset=["cnpj", "codigo_cvm"])

    transformed_df = transformed_df.drop_duplicates()

    subset_int = ["codigo_cvm"]
    for col in subset_int:
        transformed_df[col] = transformed_df[col].astype("int")
    
    subset_float = ["valor_patrimonio_liquido"]
    for col in subset_float:
        transformed_df[col] = transformed_df[col].astype("float")

    subset_date = ["data_patrimonio_liquido", "data_inicio_situacao", "data_registro"]
    for col in subset_date:
        transformed_df[col] = pd.to_datetime(transformed_df[col])

    return transformed_df

def transform_cidade_uf (dataframe):
    
    import pandas as pd
    import numpy as np

    dataframe.replace("", np.nan, inplace=True)
    transformed_df = dataframe.drop_duplicates()
    transformed_df["id"] = transformed_df["id"].astype("int")

    return transformed_df