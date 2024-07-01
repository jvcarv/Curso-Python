"""
Iterando strings com while
"""
#       012345678910
nome = input("Digite seu nome ")  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
num_1 = 0
nova_string = ''

while num_1 < tamanho_nome:
    nova_string += '*'
    nova_string += nome[num_1]
    num_1 += 1
    
print(nova_string)
