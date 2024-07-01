# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
            
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._motor
            
    @motor.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def print_informations(self):
        print(f'O {self.nome} possui um {self._motor.modelo}, e é fabricado pela {self._fabricante.nome}')

class Motor:
    def __init__(self, modelo):
        self.modelo = modelo

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca, scenic, uno, corsa = Carro('Fusca'),Carro('Gran Scenic'),Carro('Uno'),Carro('Corsa')
motor_1_0, motor_2_0 = Motor('Motor 1.0'), Motor('Motor 2.0')
volks, renault, fiat, chevrolet = Fabricante('Volkswagen'), Fabricante('Renault'), Fabricante('Fiat'), Fabricante('Chevrolet')

fusca.motor = motor_1_0
scenic.motor = motor_2_0
uno.motor = motor_1_0
corsa.motor = motor_1_0

carros = [fusca, scenic, uno, corsa]

fusca.fabricante = volks
scenic.fabricante = renault
uno.fabricante = fiat
corsa.fabricante = chevrolet

if __name__ == '__main__':
    for carro in carros:
        carro.print_informations()