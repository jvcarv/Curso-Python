# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding = "utf-8")
        yield arquivo
    finally:
        print("Fechando arquivo")
        arquivo.close()

# class MyOpen:
#     def __init__(self,caminho_arquivo, modo ):
#         self.caminho = caminho_arquivo
#         self.modo = modo
#         self._arquivo = None 

#     def __enter__(self):
#         self._arquivo = open(self.caminho, self.modo, encoding="utf-8")
#         return self._arquivo
    
#     def __exit__(self, class_exception_, exception_, traceback_):
#         self._arquivo.close()

#         # raise class_exception(*exception_.args).with_traceback(traceback_)

#         # print(class_exception)
#         # print(exception_)
#         # print(traceback_)
#         # exception_.add_note('Minha nota')

#         # return True  # Tratei a exceção

with my_open("aula128.txt","w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    print("WITH", arquivo)