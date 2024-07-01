class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

c1 = Carro('Fusca')
c1.acelerar()

c2 = Carro('Celta')
c2.acelerar()
