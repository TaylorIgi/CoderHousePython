def api_get_data(url_path):
    
    import requests
   
    response = requests.get(url_path)

    return response

def object_to_df(my_object):
    
    import pandas as pd

    return pd.DataFrame(my_object.json())