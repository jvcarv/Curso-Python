# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# lista = [
#     numero * 2
#     for numero in range(10)
# ] #é como se fosse um "for lambda"
# print(lista)

# # Mapeamento de dados em list comprehension
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# # print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

numeros_menores_que_30 = [numero for numero in range(50) if numero < 30]

p(numeros_menores_que_30)

 