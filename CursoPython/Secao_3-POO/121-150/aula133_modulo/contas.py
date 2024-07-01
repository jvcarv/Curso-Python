from abc import ABC, abstractmethod

#metodo abstrato Conta -> sacar

class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        self._saldo = saldo
        self.agencia = agencia
        self.num_conta = num_conta

    @abstractmethod
    def sacar(self,quantidade):
        ...
    
    def depositar(self,quantidade):
        self._limite += quantidade

    def detalhes(self):
        return print(f'O seu saldo é {self._saldo}')

class ContaCorrente(Conta):
    def __init__(self, agencia, num_conta, saldo, limite):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite     

    def sacar(self,quantidade):
        if quantidade <= self.limite + 500:
            self.limite -= quantidade


class ContaPoupanca(Conta):
    def sacar(self,quantidade):
        if quantidade <= self.saldo:
            self.saldo -= quantidade