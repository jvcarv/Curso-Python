# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import importlib
import aula86_modulo
from aula86_modulo import soma,variavel_modulo 

print('Este módulo se chama', __name__)

print('Este módulo se chama', __name__)

input("s")

# print('Este módulo se chama', __name__)
print(aula86_modulo.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula86_modulo.soma(2, 3))

importlib.reload(aula86_modulo) #serve para carregar novamente o import