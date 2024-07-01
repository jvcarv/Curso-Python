frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum".lower()

i = 0
letra_atual = ""
qtd_apareceu_mais_vezes = 0
qtd_anterior = 0
letra_que_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
         i += 1
         continue

    qtd_apareceu_mais_vezes = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes > qtd_anterior:
        qtd_anterior = qtd_apareceu_mais_vezes
        letra_que_apareceu_mais = letra_atual

    i += 1

print(f'A letra {letra_que_apareceu_mais} apareceu mais, sendo exibida {qtd_anterior} vezes na frase.')