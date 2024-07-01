# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def mult (*args):
    total = 1
    for num in args:
        total *= num
        
    return total

print(mult(1,2,3,4,5))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
    
def checar_se_par_ou_impar(num):
    condicao =  num % 2 == 0 

    if condicao:
        return f"O número {num} é par."
    
    return f"O número {num} ímpar."

num = int(input("Digite um número: "))

print(checar_se_par_ou_impar(num))

