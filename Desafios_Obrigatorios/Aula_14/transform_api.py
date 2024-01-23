import pandas as pd
import numpy as np

def transform_bancos(my_dataframe):
    clean_dataframe = my_dataframe.copy()
    clean_dataframe = clean_dataframe.replace("", np.nan)
    clean_dataframe.drop_duplicates()
    clean_dataframe = clean_dataframe.dropna(axis=0, subset=["ispb", "code"])
    clean_dataframe["code"] = clean_dataframe["code"].astype(int)
    return clean_dataframe

def transform_corretoras(my_dataframe):
    return True

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