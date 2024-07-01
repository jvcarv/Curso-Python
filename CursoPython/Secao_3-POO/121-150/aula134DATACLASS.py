from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    idade: int
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':

    p1 = Pessoa('Luiz', 18, 'Miranda')
    p1.nome_completo = 'Maria Helena'
    print(p1)
    print(p1.nome_completo)
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
