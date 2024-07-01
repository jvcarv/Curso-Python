"""
Higher Order Functions
Funções de primeira classe
"""

def funcao_1(msg, nome):
    return f'{msg}, {nome}!'

def funcao_2(funcao, *args):
    return funcao(*args)
    
variavel_que_recebe_funcao = funcao_1


print(funcao_2(variavel_que_recebe_funcao,"Bom dia","João"))