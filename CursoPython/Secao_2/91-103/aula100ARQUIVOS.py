# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\projetosPython\\CursoPython\\Manipulação de arquivos\\'
caminho_arquivo  += 'aula101.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

#deve-se ter cuidado: sempre que se abre um arquivo, se fecha o arquivo
#para isso, with open ajuda consideravelmente, pois abre e fecha o arquivo ao fim

texto_arquivo = []

with open (caminho_arquivo, 'w', encoding= 'utf-8') as arquivo:
      for i in range(10):
        arquivo.write(f"Linha {i+1} \n")

with open (caminho_arquivo, 'r') as arquivo:
      texto_arquivo = arquivo.read()  


print(texto_arquivo)

# os.remove(caminho_arquivo) # ou unlink
# os.rename(caminho_arquivo, 'aula116-2.txt')
