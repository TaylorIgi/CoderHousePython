import pandas as pd
import numpy as np

def to_int(my_dataframe, int_columns):
    for col in int_columns:
        my_dataframe[col] = my_dataframe[col].astype(int)
    return my_dataframe

def to_float(my_dataframe, float_columns):
    for col in float_columns:
        my_dataframe[col] = my_dataframe[col].astype(float)
    return my_dataframe

def to_date(my_dataframe, date_columns):
    for col in date_columns:
        my_dataframe[col] = pd.to_datetime(my_dataframe[col])
    return my_dataframe

def transform_bancos(my_dataframe):
    
    clean_dataframe = my_dataframe.copy()
    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0, subset=["ispb", "code"])
    
    subset_int = ["code"]
    clean_dataframe = to_int(clean_dataframe, subset_int)
    
    return clean_dataframe

def transform_corretoras(my_dataframe):
    
    clean_dataframe = my_dataframe.copy()
    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0, subset=["cnpj", "codigo_cvm"])
    
    subset_int = ["codigo_cvm"]
    clean_dataframe = to_int(clean_dataframe, subset_int)

    print(clean_dataframe["valor_patrimonio_liquido"].unique())
    clean_dataframe["valor_patrimonio_liquido"].replace(np.nan, 0, inplace=True)
    print("-"*40)
    print(clean_dataframe["valor_patrimonio_liquido"].unique())
    # subset_float = ["valor_pratrimonio_liquido"]
    # clean_dataframe = to_float(clean_dataframe, subset_float)
    
    subset_date = ["data_patrimonio_liquido", "data_inicio_situacao", "data_registro"]
    clean_dataframe = to_date(clean_dataframe, subset_date)
        
    return clean_dataframe

def transform_cidade_uf(my_dataframe):
    return True

def transform_clima(my_dataframe):
    return True

def transform_feriados(my_dataframe):
    return True

def transform_uf_regiao(my_dataframe):
    return True

def transform_ncm(my_dataframe):
    return True

def transform_pix(my_dataframe):
    return True

def transform_taxas(my_dataframe):
    return True