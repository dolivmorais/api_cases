import requests

url = 'https://httpbin.org/post'

dados = {
    "meus dados": [1,2,3],
    "pessoa": {
        "nome": "teste",
        "profissao": True
    }
}

params = {
    'dataInicio': '2024-01-01',
    'dataFim': '2024-02-04',
}

resposta = requests.post(url,json=dados, params=params)
print(resposta.request.url)
#print(resposta.json())