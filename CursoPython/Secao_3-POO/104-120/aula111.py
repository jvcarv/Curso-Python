class Carro:
    def __init__(self, nome, marca):
        self.nome_geral = nome
        self.marca = marca

    @property
    def nome(self):
        return self.nome_geral
    
    @classmethod
    def salvar_carros_renault(cls, nome):
       return cls(nome, 'Renault')

c1 = Carro('Fusca','Volkswagen')

print(c1.nome_geral)
