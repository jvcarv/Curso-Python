def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
    cls.__repr__ = meu_repr     
    return cls

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


def my_world(method):
    def intern(self, *args,**kwargs):
        result = method(self, *args, **kwargs)

        if 'Terra' in result:
            return "Você está em casa"

        return result
    return intern




@adiciona_repr
class Planet:
    def __init__(self, nome):
        self.nome = nome

    @my_world
    def show_name(self):
        return f'O Planeta é {self.nome}'

brasil = Time("Brasil")
portugal = Time('Portugal')

terra = Planet('Terra')
marte = Planet('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)