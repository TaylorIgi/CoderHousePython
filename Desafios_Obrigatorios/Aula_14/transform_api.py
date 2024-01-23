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
    
    subset_float = []
    clean_dataframe = to_float(clean_dataframe, subset_float)

    subset_date = []
    clean_dataframe = to_date(clean_dataframe, subset_date)

    return clean_dataframe

def transform_corretoras(my_dataframe):
    
    clean_dataframe = my_dataframe.copy()
    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0, subset=["cnpj", "codigo_cvm"])
    
    subset_int = ["codigo_cvm"]
    clean_dataframe = to_int(clean_dataframe, subset_int)

    clean_dataframe["valor_patrimonio_liquido"].replace(np.nan, 0, inplace=True)
    
    '''
    Analisar pq não foi possível converter do mesmo modo dos inteiros!!!!!!!!!!!!!
    '''
    # subset_float = ["valor_pratrimonio_liquido"]
    # clean_dataframe = to_float(clean_dataframe, subset_float)
    clean_dataframe["valor_patrimonio_liquido"] = list(map(float, clean_dataframe["valor_patrimonio_liquido"]))
    
    subset_date = ["data_patrimonio_liquido", "data_inicio_situacao", "data_registro"]
    clean_dataframe = to_date(clean_dataframe, subset_date)
        
    return clean_dataframe

def transform_cidade_uf(my_dataframe):
    
    clean_dataframe = my_dataframe.copy()
    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0, subset=["nome", "id"])

    subset_int = ["id"]
    clean_dataframe = to_int(clean_dataframe, subset_int)

    subset_float = []
    clean_dataframe = to_float(clean_dataframe, subset_float)

    subset_date = []
    clean_dataframe = to_date(clean_dataframe, subset_date)

    return clean_dataframe

def transform_clima(my_dataframe):

    clean_dataframe = my_dataframe.copy()
    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0, subset=["codigo_icao", "atualizado_em"])

    subset_int = ["umidade", "pressao_atmosferica", "vento", "direcao_vento", "temp"]
    clean_dataframe = to_int(clean_dataframe, subset_int)

    subset_float = []
    clean_dataframe = to_float(clean_dataframe, subset_float)

    subset_date = ["atualizado_em"]
    clean_dataframe = to_date(clean_dataframe, subset_date)
    
    return clean_dataframe

def transform_feriados(my_dataframe):

    clean_dataframe = my_dataframe.copy()
    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0)

    subset_int = []
    clean_dataframe = to_int(clean_dataframe, subset_int)

    subset_float = []
    clean_dataframe = to_float(clean_dataframe, subset_float)

    subset_date = ["date"]
    clean_dataframe = to_date(clean_dataframe, subset_date)
    
    return clean_dataframe

def transform_uf_regiao(my_dataframe):
    
    clean_dataframe = my_dataframe.copy()

    clean_dataframe["regiao_id"] = clean_dataframe["regiao"].apply(lambda x: x["id"])
    clean_dataframe["regiao_sigla"] = clean_dataframe["regiao"].apply(lambda x: x["sigla"])
    clean_dataframe["regiao_nome"] = clean_dataframe["regiao"].apply(lambda x: x["nome"])
    clean_dataframe = clean_dataframe.drop(columns=["regiao"])

    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0)

    subset_int = ["id", "regiao_id"]
    clean_dataframe = to_int(clean_dataframe, subset_int)

    subset_float = []
    clean_dataframe = to_float(clean_dataframe, subset_float)

    subset_date = []
    clean_dataframe = to_date(clean_dataframe, subset_date)
    
    return clean_dataframe

def transform_ncm(my_dataframe):
    
    clean_dataframe = my_dataframe.copy()
    clean_dataframe.replace("", np.nan, inplace=True)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0, subset=["codigo", "data_inicio", "numero_ato", "ano_ato"])
    clean_dataframe = clean_dataframe.drop(columns=["data_fim"])

    subset_int = ["numero_ato", "ano_ato"]
    clean_dataframe = to_int(clean_dataframe, subset_int)

    subset_float = []
    clean_dataframe = to_float(clean_dataframe, subset_float)

    subset_date = ["data_inicio"]
    clean_dataframe = to_date(clean_dataframe, subset_date)
    
    return clean_dataframe

def transform_pix(my_dataframe):
    return True

def transform_taxas(my_dataframe):
    return True