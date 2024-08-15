import requests
from pprint import pprint


url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'

params = {
}

resposta = requests.get(url, params=params)

print(resposta.request.url)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request: {e}')
    resultado = None
else:
    print("Resposta:")
    resultado = resposta.json()
    pprint(resultado)