# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def adiar(y):
        return funcao(x,y)
    return adiar


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(5))
print(multiplica_por_dez(241))
print(soma_com_cinco(124))
print(multiplica_por_dez(324))
print(soma_com_cinco(5423))
print(multiplica_por_dez(15))
print(soma_com_cinco(123513))
print(multiplica_por_dez(5314))
print(soma_com_cinco(14325))
print(multiplica_por_dez(432))
