nome = input("Digite o seu nome: ") or "Sem nome"
idade = input("Digite a sua idade: ") or "Sem idade"
nome_invertido = nome[::-1]


if (nome == "Sem nome") or (idade == "Sem idade"):
    print("Desculpe, você deixou campos vazios.")
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if " " in nome:
        print(f'Seu nome contém espaços.')
    else:
        print("Seu nome não contém espaços.")
    print(f'Seu nome contém {len(nome)} letras.')
    print(f'A primeira letra de seu nome é {nome[0]}.')
    print(f'A última letra de seu nome é {nome[-1]}.')