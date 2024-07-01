import pessoa
import contas

class Banco():
    def __init__(self, agencias = list[int], contas = list[contas.Conta], clientes = list[pessoa.Cliente]) -> None:
        self.agencias = agencias or []
        self.contas = contas or []
        self.clientes = clientes or []

    def checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            print("A agência da conta está dentro das agências do banco.")
            return True
        print("A agência da conta não está dentro das agências do banco.")
        return False
    def checar_cliente(self, cliente):
        if cliente in self.clientes:
            print("O cliente da conta está dentro das agências do banco.")
            return True
        print("O cliente da conta não está dentro das agências do banco.")
        return False
    def checar_conta(self, conta):
        if conta in self.contas:
            print("A conta está dentro das agências do banco.")
            return True
        print("A conta não está dentro das agências do banco.")
        return False
    def checa_se_conta_do_cliente(self, conta, cliente):
        if conta.num_conta == cliente._conta.num_conta:
            print("A conta informada é do cliente informado.")
            return True
        print("A conta informada não é do cliente informado.")
        return False
    
    def autentica(self, cliente: pessoa.Pessoa, conta: contas.Conta):
         return self.checar_agencia(conta) and \
            self.checar_cliente(cliente) and \
            self.checar_conta(conta) and \
            self.checa_se_conta_do_cliente(conta, cliente)
if __name__ == '__main__':
    
    c1 = pessoa.Cliente('João', 18)
    c1.conta = contas.ContaCorrente(7,1,1200,1000)
    c1.conta.detalhes()
    c2 = pessoa.Cliente('Tobias', 19)
    c2.conta = contas.ContaPoupanca(7,2,1500)
    c2.conta.detalhes()


    b1 = Banco([1,2,3,4,5,6,7],[c1.conta],[c1])

    b1.autentica(c1, c1.conta)
    b1.autentica(c2, c2.conta)