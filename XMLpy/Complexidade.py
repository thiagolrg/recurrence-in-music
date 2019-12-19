'''
A função abaixo apresenta a lógica básica usada na função principal para encontrar recorrências, ela faz recortes de lista gerando  todas as sublistas possíveis até tamanho, acrescentando cada uma dessas sublistas em listanova.
'''

def recorrencias1(lista, tamanho):
    listanova = []
    p1 = 0 #posicao 1
    while p1 < len(lista):
        p2 = p1+1 #posicao 2
        while p2-p1 <= tamanho and p2 <= len(lista):
            listanova.append(lista[p1:p2])
            p2 += 1
        p1 += 1
    return listanova

'''
É possível perceber seu funcionamento criando uma listateste com os números de 1 a 5  e experimentando o seu resultado com alguns tamanhos diferentes:
'''
listateste = [x for x in range(1,6)]
 
listanova = recorrencias1(listateste, 1)
print(listanova, '\n')
 
listanova = recorrencias1(listateste, 3)
print(listanova, '\n')
 
listanova = recorrencias1(listateste, 5)
print(listanova)
''' 
[[1], [2], [3], [4], [5]] 
 
[[1], [1, 2], [1, 2, 3], [2], [2, 3], [2, 3, 4], [3], [3, 4], [3, 4, 5], [4], [4, 5], [5]]
 
[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [3], [3, 4], [3, 4, 5], [4], [4, 5], [5]] 
'''

'''
Sendo possível criar as sublistas, para encontrar recorrências em lista é necessário saber se suas sublistas têm a mesma constituição, para isso as sublistas são acrescentadas como chaves em um defaultdict e suas posições de início e fim na lista de origem como valores das chaves. Isso significa que toda vez que uma sublista tem a mesma constituição de outra já acrescentada no defaultdict, sua posição é acrescentada como valor da chave já existente, se a sublista for nova será acrescentada uma nova chave para ela e sua posição como valor.
'''
from collections import defaultdict
def recorrencias2(lista, tamanho):
    dicio = defaultdict(list)
    p1 = 0 #posicao 1
    while p1 < len(lista):
        p2 = p1+1 #posicao 2
        while p2-p1 <= tamanho and p2 <= len(lista):
            dicio[tuple(lista[p1:p2])].append((p1,p2))
            p2 += 1
        p1 += 1
    return dicio

'''
Como o interesse está somente nas recorrências, podemos manter do dicionário resultante somente as chaves, ou seja, sublistas, que aparecem mais de uma vez, sou seja, que tem len(valor) > 1 e transformar o resultado novamente em lista, pois desse ponto em diante o propósito de identificar todas as recorrências já está cumprido e a lista é um formato de interação mais rápida para continuar sendo processada pelo programa.
Algumas premissas, que vão ter suas consequências discutidas na análise aplicada, foram feitas com relação a importância das recorrências para afirmar similaridade, a primeira delas é que as maiores recorrências são mais importantes, a segunda é que as que mais aparecem são mais importantes, por isso a lista resultante é organizada para refletir essa ordem de importância, das maiores para as menores e, entre as de mesmo tamanho, das que recorrem mais para as que recorrem menos.
Levando em conta essas mudanças observe como fica a função para recorrências e sua aplicação em uma lista que, de fato têm recorrências, porém, assumindo que não sabe-se qual o tamanho da sua maior recorrência a solução temporária será criar todas as sublistas possíveis, ou seja, tamanho = len(lista).
'''

listaentrada = [1,2,1,2,3,1,2,3,1,2]
def recorrencias3(lista, tamanho=0):
    if tamanho <= 0:
        tamanho = len(lista)
    dicio = defaultdict(list)
    p1 = 0 #posicao 1
    while p1 < len(lista):
        p2 = p1+1 #posicao 2
        while p2-p1 <= tamanho and p2 <= len(lista):
            dicio[tuple(lista[p1:p2])].append((p1,p2))
            p2 += 1
        p1 += 1
    return sorted([(c, v) for c, v in dicio.items() if len(v) > 1], key=lambda item: (len(item[0]), len(item[1])), reverse=True)
 
listarecorrencias = recorrencias3(listaentrada)
for i in listarecorrencias:
    print(i)
''' 
((1, 2, 3, 1, 2), [(2, 7), (5, 10)])
((1, 2, 3, 1), [(2, 6), (5, 9)])
((2, 3, 1, 2), [(3, 7), (6, 10)])
((1, 2, 3), [(2, 5), (5, 8)])
((2, 3, 1), [(3, 6), (6, 9)])
((3, 1, 2), [(4, 7), (7, 10)])
((1, 2), [(0, 2), (2, 4), (5, 7), (8, 10)])
((2, 3), [(3, 5), (6, 8)])
((3, 1), [(4, 6), (7, 9)])
((1,), [(0, 1), (2, 3), (5, 6), (8, 9)])
((2,), [(1, 2), (3, 4), (6, 7), (9, 10)])
((3,), [(4, 5), (7, 8)])
'''

'''
O resultado contém todas as recorrências dentro de listaentrada, porém, em consequência a premissa de que as recorrências maiores têm mais importância, é possível reduzi-lo retirando todas as recorrências que acontecem contidas em outras maiores, é possível reduzi-lo ainda mais se forem retiradas todas as recorrências que acontecem intercaladas e, nesse caso, é necessário uma premissa nova, a de que as que acontecem intercaladas antes são mais importantes, pois na música, ouvir a instância de uma recorrência intercalada que acontece depois significa voltar a música para o momento exato em que essa começa. Em resumo: recorrências maiores têm prioridade, todas as contidas e intercaladas são retiradas do resultado, o que significa que, se existe algum intercalado maior com o atual, por consequência o atual é o intercalado menor do outro e será retirado. Resta definir exatamente o que contidas e intercaladas são:
Uma recorrência é contida em outra quando:
Sua posição de início >= a posição de início da outra e
sua posição de fim <= a posição de fim da outra
Uma recorrência é intercalada em outra quando:
	Sua posição de início >< que posição de início da outra e
sua posição de fim > posição de fim da outra ou
sua posição de fim >< posição de fim da outra e
sua posição de inicio < posição de início da outra

As funções abaixo verificam se a posição de uma recorrência é contida e intercalada com qualquer outra em uma lista de posições.
'''

def contida(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0] >= outra[0] and posicao[1] <= outra[1]:
            return True
    return False

def intercalada(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0] > outra[0] and posicao[0] < outra[1] and posicao[1] > outra[1]:
            return True
        if posicao[1] > outra[0] and posicao[1] < outra[1] and posicao[0] < outra[0]:
            return True
    return False

'''
Para retirar de listarecorrencias as contidas e intercaladas é necessário verificar se as posições das recorrências, das maiores para as menores, não são intercaladas com as posições da mesma sublista e intercaladas ou contidas com posições de outras sublistas maiores que já passaram pelo filtro. Depois, se a sublista ainda recorrer, ou seja, aparecer mais de uma vez, ela é mantida no resultado.
A função para retirar contidas e intercaladas da listarecorrencias  fica assim:
'''

def sem_cont_inter(listarecorrencias):
    semcontinter = []
    quepassaram = []
    for segmento, posicoes in listarecorrencias:
        posicoessegmento = []
        for posicao in posicoes:
            if not intercalada(posicoessegmento, posicao) and not intercalada(quepassaram, posicao) and not contida(quepassaram, posicao):
                posicoessegmento.append(posicao)
        if len(posicoessegmento) > 1:
            for v in posicoessegmento:
                quepassaram.append(v)
            semcontinter.append((segmento,posicoessegmento))
    return semcontinter

'''
Juntando tudo, a função pronta e seu resultado ficam assim:
'''

listaentrada = [1,2,1,2,3,1,2,3,1,2]
 
def recorrencias(lista,tamanho=0):
    return sem_cont_inter(recorrencias3(lista, tamanho=tamanho))
 
listarecorrencias = recorrencias(listaentrada)
for v in listarecorrencias:
    print(v)
''' 
((1, 2, 3), [(2, 5), (5, 8)])
((1, 2), [(0, 2), (8, 10)])
'''

'''
Observando que o resultado a maior recorrência de tamanho 3, esse seria o tamanho necessário para calcular todas as recorrências e qualquer outra sublista maior do que esse tamanho seria retirada no filtro e esta sendo criada desnecessáriamente, para isso existe uma função similar recorrencias3 que testa  recursivamente sublistas por tamanho até que não existam recorrências no resultado, definindo assim, o tamanho mínimo necessário para encontrar as recorrências. Uma função assim faz sentido como alternativa a calcular sempre todas as sublistas possíveis, primeiro porque ela só é executada pelo programa na primeira vez ou quando existem músicas novas no diretório, em outros casos o tamanho mínimo já foi calculado e salvo, segundo porque nos casos reais da aplicação nas sonatas de Scarlatti, D. as listas tem tamanhos em torno de 300 a 700 notas e seu tamanho mínimo para recorrências é em torno de 30 a 100, é mais vantajoso verificar as recorrências até tamanho mínimo e depois calcular as mesmas recorrências do que sempre calcular todas as sublistas possíveis.
'''

def recorrencias4(lista, tamanho=0):
    if tamanho <= 0:
        tamanho = len(lista)
    dicio = defaultdict(list)
    p1 = 0 #posicao 1
    while p1 + tamanho <= len(lista):
        p2 = p1 + tamanho
        dicio[tuple(lista[p1:p2])].append((p1,p2))
        p1 += 1
    return [(c, v) for c, v in dicio.items() if len(v) > 1]
 
def tam_min(lista, tamanho=1):
    listarecorrencias = recorrencias4(lista, tamanho=tamanho)
    listarecorrencias = sem_cont_inter(listarecorrencias)
    while len(listarecorrencias) != 0:
        return tam_min(lista, tamanho=tamanho+1)
    return tamanho-1
 
tammin = tam_min(listaentrada)
print('tamanho minimo: ', tammin)
''' 
tamanho minimo:  3
'''

'''
def tamanhoslista(caminhosdict):
    TintDia = []
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        for parte in musD:
                for voz, caracteristicas in musD[parte].items():
                    if 'intDia' in caracteristicas:
                        TintDia.append(len(caracteristicas['intDia']))
    return TintDia

def segmentacao(lista, janela=0):
    seg = []
    lenlista = len(lista)
    if janela == 0:
	    janela = len(lista)
    p1 = 0
    while p1 < lenlista:
        p2 = p1+1
        while p2-p1 <= janela and p2 <= lenlista:
            seg.append(lista[p1:p2])
            p2 += 1
        p1 += 1
    return seg

n = 0
for lista in TindDia:
    n = complexidade_segmentacao(lista, janela=133)+n

debug = 0
'''