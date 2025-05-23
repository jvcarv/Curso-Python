"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

lista_soma = [x + y for x,y in zip(lista_a,lista_b)]

#lista_soma = [x + y for x,y in zip_longest(lista_a,lista_b, fillvalue - 0)]

# def soma_listas(l1, l2):
#     intervalo = min(len(l1),len(l2))

#     lista_soma = [l1[i] + l2[i] for i in range(intervalo)]
#     return lista_soma

# print(soma_listas(lista_a,lista_b))
print(lista_soma)

