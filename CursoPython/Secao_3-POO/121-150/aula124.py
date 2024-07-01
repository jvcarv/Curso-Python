# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
#No pythoon 3.11. é possível adicionar notas aos exceptions através do comando .add_note()

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def raiseException():
    _exception = MyError('A','B','C')
    raise _exception

try:
    raiseException()    
except MyError as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('Vou lançar de novo')
    raise exception_ from error