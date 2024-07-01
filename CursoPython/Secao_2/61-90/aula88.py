# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
import pprint
from aula88_package import produtos

def p(v):
    pprint.pprint(v,sort_dicts=False)



novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.1, 2  ) }for produto in copy.deepcopy(produtos)]
p(novos_produtos)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), key= lambda p : p['nome'], reverse=True)
p(produtos_ordenados_por_nome)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), key= lambda p : p['nome'], reverse=True)
produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), key= lambda p : p['preco'])
p(produtos_ordenados_por_preco)
