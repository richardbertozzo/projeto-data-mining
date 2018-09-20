import requests 
import pandas as pd
import numpy as np

URL_BASE = 'https://dadosabertos.camara.leg.br/api/v2/'


def get_deputado(id):
    url_deputados = URL_BASE + 'deputados/' + str(id)
    response = requests.get(url = url_deputados)
    return response.json()


def get_deputados():
    url_get_deputados = URL_BASE + 'deputados' 
    params = 'itens=1&ordem=ASC&ordenarPor=nome'
    response = requests.get(url = url_get_deputados, params = params)
    return response.json()


def get_despesas_deputado(id_deputado):
    url_get = URL_BASE + 'deputados/{}/despesas'.format(id_deputado) 
    params = 'itens=100'
    response = requests.get(url = url_get, params = params)
    return response.json()


def get_deputados_with_despesas(deputados):
    for deputado in deputados:
        despesas_deputado = get_despesas_deputado(deputado['id'])
        deputado['despesas'] = despesas_deputado['dados']

        print(deputado)
    

deputados = get_deputados()
get_deputados_with_despesas(deputados['dados'])


# print("Deputados: " + str(deputados['dados']))
#print("Length deputados: {}".format(len(deputados['dados'])))


#despesas_deputado_1 = get_despesas_deputado(deputados['dados'][0]['id'])
#print(despesas_deputado_1)
