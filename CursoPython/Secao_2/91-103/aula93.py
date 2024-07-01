 # Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']
resultado = []
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(cidades, uf):
    
#     iterador = iter(uf)
#     for cidade in cidades:
#         resultado.append((cidade,next(iterador)))         
#     return resultado

def zipper(l1,l2):
    intervalo = min(len(l1),len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

r = zipper(cidades, uf)
print(r)
    