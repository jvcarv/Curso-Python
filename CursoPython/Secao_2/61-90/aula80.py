# isinstace - checa se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, str):
        print("STR")
        print(item, isinstance(item, str))
    elif isinstance(item, (int, float)):
        print("NUM") 
        print(item, isinstance(item, (int, float)))
    elif isinstance(item, set):
        print("SET")
        print(item,isinstance(item, set))
    elif isinstance(item, dict):
        print("DICT")
        print(item,isinstance(item, dict))
    elif isinstance(item, tuple):
        print("TUPLA")
        print(item,isinstance(item, tuple))
    elif isinstance(item, list):
        print("LISTA")
        print(item,isinstance(item, list))
    else:
        print("TIPO DE ITEM DESCONHECIDO")
        print(item)