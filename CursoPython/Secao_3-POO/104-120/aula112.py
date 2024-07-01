class Carro:
    def __init__(self, nome, marca):
        self._nome_geral = nome
        self.marca = marca

    @property
    def nome(self):
        print('GETTER')
        return self._nome_geral

    @nome.setter
    def nome(self, value):
        print('SETTER')
        self._nome_geral = value

c1 = Carro('Fusca','Volkswagen')

print(c1.nome)
c1.nome = 'Cavalo'
print(c1.nome)