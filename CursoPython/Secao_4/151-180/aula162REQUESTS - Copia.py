import requests

url = "http://192.168.1.125:8000/wisedoc/cadastros/setores"
response = requests.get(url)

print(response.status_code)
print(response.headers)
dados = response.json()

for dado in dados:
    print(dado)
