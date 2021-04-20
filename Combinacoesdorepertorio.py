"""
Buscar similaridades em qualquer combinação de músicas do repertório
Gerar qualquer combinação de músicas em 155 é um número absurdamente grande
O Programa consegue chegar no resultando de apresentar as músicas do repertório por grupos de similaridade
"""

import math
import itertools as it

def combinacoes_semRepeticoes_semOrdem(n,r):
    return int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

n = 155
numCombinacoes = 0
for r in range(1,n+1):
    numCombinacoes = numCombinacoes + combinacoes_semRepeticoes_semOrdem(n,r)

lista = [x for x in range(n)]
exCombinacoes = list(it.combinations(lista, 2))