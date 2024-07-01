#GENERATOR E ITERATOR 
#todo generator é um iterator, mas um iterator não é um generator
#generator não são salvos na memória do computador


generator = (x for x in range(10))

iterable = [1,2,3,4,5,6]
iterador = iter(iterable)

# for item in iterable:
#     print(next(iterador))


pares = [x for x in range(10) if x % 2 == 0]

# print(pares)

for n in generator:
    print(n)


def generator1(n=0):
    yield 1 #funciona como o return, mas não mata a função, só pausa ela, assim podendo retornar o funcionamento dela depois
    print("Continuando...")
    yield 2 #portando, caso eu chame o generator 2 vezes, a primeira vez me retorna 1 e a 2 me retorna 2



#portanto, generator funcions são funções que podem pausar o código e retornar a ele depois
#usar um yield from faz com que uma funcao corra entre a pausa do generator  