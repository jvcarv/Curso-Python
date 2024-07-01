
import re
import sys

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  1   1  6  8  7  0  4  7  9
   10  9 48 56 42  0 16 21 18

Somar todos os resultados: 
10 + 9 + 48 + 56 + 42 + 0 + 16 + 21 + 18 = 220
Multiplicar o resultado anterior por 10
220 * 10 = 2200
Obter o resto da divisão da conta anterior por 11
2200 % 11 = 
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_informado = input("Digite seu CPF: ")
cpf_e_sequencia = cpf_informado == cpf_informado[0] * len(cpf_informado)

cpf_informado_formatado = re.sub(r'[^0-9]', '', cpf_informado)

if cpf_e_sequencia:
     print("Você enviou caracteres repetidos.")
     sys.exit()

cpf_int_listado = cpf_informado_formatado[:9]

i = 10
soma_da_multiplicação = 0

for numero in cpf_int_listado:
     resultado = int(numero) * i

     i -= 1
     soma_da_multiplicação += resultado

soma_da_multiplicação *= 10

soma_da_multiplicação %= 11

digito_1 = soma_da_multiplicação if soma_da_multiplicação <= 9 else 0


#SEGUNDO DIGITO

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

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

if cpf_informado == cpf_int_listado:
    print(f'O CPF gerado pelo sistema é {cpf_int_listado}, que coincide com o informado pelo usuário!')
else: 
    print("Houve um erro desconhecido no sistema :(")

