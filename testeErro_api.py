import requests

url = 'https://httpbin.org/get'

resposta = requests.get(url)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f' Impossível fazer requests! ERRO: {e}')
else:
    print("Resposta:")
    print(resposta.json())