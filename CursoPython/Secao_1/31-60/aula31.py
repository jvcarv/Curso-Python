"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero_usuario = input("Digite um número inteiro: ")
    numero_int = int(numero_usuario)

    if numero_int % 2 == 0:
        print("O número digitado é par.")

    else:
        print("O número digitado é ímpar.")
except:
    print("Você não digitou um número inteiro.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = input("Que horas são? ")
    hora_int = int(hora)

    if (hora_int >= 0) and (hora_int <= 11):
        print("Bom dia!")
    elif (hora_int >= 12) and (hora_int <= 17):
        print("Boa tarde!")
    elif ((hora_int >= 18) and (hora_int <= 23)):
        print("Boa noite!")
    else:
        print("Você não informou um horário válido.")
except:
    print("Você não informou um horário válido.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho_nome == 5 or tamanho_nome == 6:
        print("Seu nome é normal")
    elif tamanho_nome > 6:
        print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra")