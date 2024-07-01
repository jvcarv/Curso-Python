from abc import ABC, abstractmethod
import contas

class Pessoa(ABC):
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, name):
        self._nome = name

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
        self._conta = contas.Conta

    @property
    def conta(self):
        return self._conta
    
    @conta.setter
    def conta(self,conta):
        if not isinstance(conta, contas.Conta):
            raise TypeError("A instÂncia esperada é do tipo Conta: outro tipo foi recebido.")
        
        self._conta = conta


if __name__ == '__main__':
    c1 = Cliente('João', 18)
    c1.conta = contas.ContaCorrente(7,1,1200,1000)
    c1.conta.detalhes()
    c2 = Cliente('Tobias', 19)
    c2.conta = contas.ContaPoupanca(5,2,1500)
    c2.conta.detalhes()