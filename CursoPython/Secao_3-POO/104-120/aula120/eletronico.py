from aula141 import LogPrintMixin

class Eletronico():
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    @property
    def ligado(self):
        return self._ligado

    @ligado.setter
    def ligado(self, valor):
        self._ligado = valor

    def ligar(self):
        if not self._ligado:
            self.ligado = True

    def desligar(self):
        if self._ligado:
            self.ligado = False
                
class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self.nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self.nome} está desligado'
            self.log_success(msg)