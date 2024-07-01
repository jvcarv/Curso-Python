"""
Closure e funções que retornam outras funções
"""
# É POSSÍVEL CRIAR UM PADRÃO DE REPETIÇÃO EM UMA MESMA FUNÇÃO, FAZENDO COM QUE ELA RETORNE DIFERENTES TIPOS DE VALORES EXECUTANDO OUTRA FUNÇÃO DENTRO DELA

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")
falar_desculpa = criar_saudacao("Desculpa")
falar_tudo_bem = criar_saudacao("Tudo bem")

lista_de_alunos = "Maria", "José", "Matheus", "Otávio", "Luiz", "João"

for nome in lista_de_alunos:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
    print(falar_desculpa(nome))
    print(falar_tudo_bem(nome))