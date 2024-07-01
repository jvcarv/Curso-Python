from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

ideias = caminho_arquivo.parent / 'ideias.txt'

with open(ideias, 'a', encoding='utf-8') as arquivo:
    arquivo.write("Oi!")
