# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiply(fator):
    def number(num):
        return num * fator
    return number

duplica = multiply(2) 
triplica = multiply(3) 
quadruplica = multiply(4)

numero_desejado = int(input("Digite o número que deseja duplicar, triplicar e quadruplicar: "))

print(duplica(numero_desejado))
print(triplica(numero_desejado))
print(quadruplica(numero_desejado))