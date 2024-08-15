import requests
from pprint import pprint


def pegar_ids_estados():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

    params = {
        "view": "nivelado",
    }
    dados_estados = fazer_requests(url=url,params=params)
    dict_estados = {}
    for dados in dados_estados:
        id_estado = dados['UF-id']
        nome_estado = dados['UF-nome']
        dict_estados[id_estado] = nome_estado
    return dict_estados


def pegar_frequancia_nome_por_estado(nome):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

    params = {
        "groupBy": "UF",
    }
    dados_frequencias = fazer_requests(url=url,params=params)
    dict_frequencias = {}
    for dados in dados_frequencias:
        #print(dados)
        id_estado = int(dados['localidade'])
        frequancia = dados['res'][0]['proporcao']
        dict_frequencias[id_estado] = frequancia
    return dict_frequencias


def fazer_requests(url, params=None):
    resposta = requests.get(url, params=params)

    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        resultado = None
    else:
        print("Resposta:")
        resultado = resposta.json()
    return resultado

def main(nome):
    dict_estados = pegar_ids_estados()
    dict_frequencias = pegar_frequancia_nome_por_estado(nome)
    print(f'Frequencia do nome {nome} nos Estados (por 100.000 habitantes)')
    for id_estado, nome_estado in dict_estados.items():
        frequancia_estado = dict_frequencias[id_estado]
        print(f'-> {nome_estado} : {frequancia_estado}')

if __name__ == '__main__':
    main('diego')