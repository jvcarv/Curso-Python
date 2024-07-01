# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade, endereco,telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone

p1 = Pessoa('João Victor', 'Barbosa Carvalho', 18, 'Rua Rogério Zandavalli, 86', '54 98159-1553')
p2 = Pessoa('Matheus Augusto', 'Barbosa Carvalho', 15, 'Rua Rogério Zandavalli, 86', '54 98131-6688')

dados = [vars(p1), p2.__dict__]

def salvar(p1):    
    with open('aula108.json', 'a+', encoding='utf-8') as arquivo:
       json.dump(p1,arquivo, ensure_ascii=False, indent=2)
if __name__ == '__main__':
    salvar(dados)