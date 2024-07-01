pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

pessoa['formação'] = "Técnico"

print(pessoa)

condicao = pessoa.get('sobrenome') #se houver uma chave 'sobrenome' no dicionário, o valor do retorno é o valor armazenado na chave;
#se não, retorna None