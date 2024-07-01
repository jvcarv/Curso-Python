class Pessoa():
    def __init__(self, nome, sobrenome, endereco, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.idade = idade


p1 = Pessoa('João Victor', 'Barbosa Carvalho', 'Rua Rogério Zandavalli, 86', 18)
print(p1.nome, p1.sobrenome, p1.idade, p1.endereco, sep='\r\n' )
        