import enum


class Directions(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Direção não suportada')

    print(f'Movendo para {direction}')


move(Directions.ESQUERDA)
move(Directions.DIREITA)
move(Directions.ACIMA)
move(Directions.ABAIXO)
