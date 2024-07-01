# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

lista = []
desfeitos = []


def desfazer():
    if len(lista) == 0:
        return "Nada a desfazer."
    try:
        desfeitos.append(lista[-1])
        lista.pop()
    except IndexError:
        return "Nada a desfazer."

def refazer():
    if desfeitos == 0:
        return "Nada a refazer."
      
    try:
        lista.append(desfeitos[-1])
        desfeitos.pop()
    except IndexError:
        return print("Nada a refazer.\r\n")

def listar():
    if len(lista) == 0:
        return print("Nada a listar.\r\n")
    
    print("TAREFAS: ")

    for item in lista:
        print(item, end= "\r\n")

while True:
    print("Comandos: listar, desfazer e refazer")
    comando = input("Digite uma tarefa ou comando: ")

    if comando == 'listar':
        listar()
        continue
    elif comando == 'refazer':
        refazer()
        listar()
    elif comando == 'desfazer':
        desfazer()
        listar()
    elif comando == 'clear':
        os.system('clear')
        continue
    else:
        lista.append(comando)
        listar()

