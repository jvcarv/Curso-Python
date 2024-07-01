# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from aula108_2 import Pessoa, salvar

dados = []

with open('aula108.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])

print(p1.nome)
print(p2.nome)