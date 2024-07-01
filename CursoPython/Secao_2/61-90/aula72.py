# Métodos úteis dos dicionários em Python
# len - retorna quantas chaves há no dicionário
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    "nome": "João Victor",
}

print(len(pessoa)) #retorna quantidade de chaves no dicionário

print(pessoa.keys()) #retorna quais chaves existem no dicionário
#pode virar tupla se usar o método tuple(), ou lista se usar o mpetodo list()

print(pessoa.values()) #retorna os valores armazenados nas chaves

print(pessoa.items()) #retorna as chaves e os valores armazenados no dict

pessoa.setDefault("idade",0) #configura um valor padrão para a chave

pessoa_2 = pessoa.copy() #cria uma shallow copy do 1 dict, que basicamente faz uma cópia apenas dos dados imutáveis mas, se você alterar um dado mutável, ele muda nas duas listas
#caso você use uma deepcopy, através da biblioteca copy, todos os dados são copiados e podem ser mudados de forma independente nos dicionários

print(pessoa.get('nome')) #retorna o valor da chave indicada

print(pessoa.pop('nome')) #elimina e retorna o valor da chave

print(pessoa.popitem()) #elimina e retorna a última chave do dicionário

print(pessoa.update({
    'idade': 30
}))
# atualiza o dict

tupla = ('nome', 'novo valor'), ('idade',30)

pessoa_2.update(tupla) #outro jeito de fazer update