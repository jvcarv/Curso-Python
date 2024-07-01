"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - remove os espaços da frase
lstrip - remove os espaços a esquerda
rstrip - remove os espaços a direita
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)