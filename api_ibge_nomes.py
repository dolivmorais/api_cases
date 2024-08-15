import requests
from pprint import pprint

nome = 'diego'
url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

params = {
    'sexo':'m',
    'GroupBy':'SP',
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