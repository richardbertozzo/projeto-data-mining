import requests 
import pandas as pd
import numpy as np

URL_BASE = 'https://dadosabertos.camara.leg.br/api/v2/'
DATA_INICIO = '2014-01-01'
DATA_FIM = '2018-12-31'


def get_deputado(id):
    url_deputados = URL_BASE + 'deputados/' + str(id)
    response = requests.get(url = url_deputados)
    return response.json()


def get_deputados():
    url_get_deputados = URL_BASE + 'deputados'
    params = 'itens=1&ordem=ASC&ordenarPor=nome'
    response = requests.get(url = url_get_deputados, params = params)
    return response.json()


def get_proposicoes_deputado(id_deputado):
    url_get = URL_BASE + 'proposicoes' 
    params = 'idAutor={}&itens=100&dataInicio={}&dataFim={}'.format(id_deputado, DATA_INICIO, DATA_FIM)
    response = requests.get(url = url_get, params = params)
    return response.json()


def get_deputados_with_despesas(deputados):
    for deputado in deputados:
        preposicoes_deputado = get_proposicoes_deputado(deputado['id'])
        deputado['preposicoes'] = preposicoes_deputado['dados'] 

        print(deputado)
    

deputados = get_deputados()
get_deputados_with_despesas(deputados['dados'])


# print("Deputados: " + str(deputados['dados']))
#print("Length deputados: {}".format(len(deputados['dados'])))


#despesas_deputado_1 = get_despesas_deputado(deputados['dados'][0]['id'])
#print(despesas_deputado_1)
