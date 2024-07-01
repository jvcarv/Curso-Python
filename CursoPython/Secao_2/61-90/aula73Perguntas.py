perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    print()


    lista = pergunta['Opções']

    print('Opções:')
    for i, opcao in enumerate(lista):
        print(f'{i}) {opcao}')
    print()

    resposta = input("Escolha uma opção: ")

    if resposta == pergunta['Resposta']:
        acertos += 1
        print("Acertou 👌")
    else:
        print("Errou ❌")

print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")