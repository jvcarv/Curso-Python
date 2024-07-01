import requests

# http -> 80
# https -> 443
#
maes = input("Deseja acessar as especialidades mães? [S] ou [N]")
filhas = input("Deseja acessar as especialidades filhas? [S] ou [N]")
ativas = input('Deseja acessas as especialidades ativas? [S] ou [N]')

cabecalho = {
    "X-API-Key": '25739ce1-fc60-4801-8245-622ad93db7e8',
    "usuario": 'enfermagem.hospitalviadutos@gmail.com',
    "senha": 'enfermagem',
    "cnes": '2249537'
}

url = 'https://apigateway-hom.procempa.com.br/apiman-gateway/saude/saude-api/1.0/gercon/especialidades?somenteMaes=' + \
    maes+'&somenteFilhas='+filhas+'&somenteAtivas='+ativas
response = requests.get(url, headers=cabecalho)

print(response.status_code)
print(response.headers)
dados = response.json()

for dado in dados:
    print(dado)
