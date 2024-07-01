# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = { 1, 2, 3}  # com dados
#set's eliminam automaticamente valores duplicados

#sets são iteráveis, podendo usar in, not in, for e while neles
#mas não aceitam indexes

# Métodos úteis:
# add, update, clear, discard

s1.add(4) #adiciona itens no set

s1.update({
    5,6,7,8
}) #atualiza o set com mais de um item

s1.discard(7) #remove um item do set

s1.clear() #remove todos os itens do set

print(s1) 

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s2 = {2,3,4,5}

s3 = s1 & s2 #soma os dois
s4 = s1 | s2 #mostra os que estão nos dois
s5 = s1 - s2 #mostra os itens que o set da esquerda tem, e o direito não
s6 = s1 ^ s2 #mostra os itens que não coincidem em ambos 

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)