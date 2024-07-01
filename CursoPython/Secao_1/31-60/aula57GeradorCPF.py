import random

for d in range(100):
     
    numeros_gerados = ''

    for num in range(9):
        numeros_gerados += str(random.randint(0, 9))

    i = 10
    soma_da_multiplicação = 0

    cpf_int_listado = numeros_gerados[:9]

    for numero in cpf_int_listado:
        resultado = int(numero) * i

        i -= 1
        soma_da_multiplicação += resultado

    soma_da_multiplicação *= 10

    soma_da_multiplicação %= 11

    digito_1 = soma_da_multiplicação if soma_da_multiplicação <= 9 else 0

    cpf_int_listado += str(digito_1)

    x = 11
    soma_da_multiplicação_2 = 0

    for numero in cpf_int_listado:
        resultado = int(numero) * x

        x -= 1
        soma_da_multiplicação_2 += resultado

    soma_da_multiplicação_2 *= 10

    soma_da_multiplicação_2 %= 11

    digito_2 = soma_da_multiplicação_2 if soma_da_multiplicação_2 <= 9 else 0

    cpf_int_listado += str(digito_2)

    print(f'{cpf_int_listado}')