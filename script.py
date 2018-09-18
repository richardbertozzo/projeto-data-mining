import requests 
import pandas as pd
import numpy as np

URL_BASE = 'https://dadosabertos.camara.leg.br/api/v2/'
params = ""


def get_deputado(id):
    url_deputados = URL_BASE + 'deputados/' + str(id)
    response = requests.get(url = url_deputados, params = params)
    return response.json()


# teste api deputados
print(get_deputado(74847))


# teste panda
print(pd.Series([1,3,5,np.nan,6,8]))