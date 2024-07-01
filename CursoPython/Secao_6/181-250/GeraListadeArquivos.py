from pathlib import Path

num = int(input("Quantos arquivos quer gerar?"))
nome = input(
    'Que nome quer dar aos arquivos? Ex: Se o nome for nome, os arquivos' +
    'ficarão: "nome1.py", "nome2.py')
ext = input("Qual as extensões dos arquivos?")
numero = input("A partir de que número? Por exemplo, aula1 ou aula 10")
num_aula = range(num)
num_aulas = [int(numero) + x for x in num_aula]
caminho = Path(__file__)


for i in num_aula:
    nome_arquivo = f"{caminho.parent}\\{nome}{num_aulas[i]}{ext}"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        print("")

    num += 1
