from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula152.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av Brasil, 21, Centro'},
    {'Nome': 'Maria Sol', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'João da Silva', 'Endereço': 'Rua 22, 44, Nova Era'}
]

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
