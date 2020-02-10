from collections import defaultdict
import dirEinp as f_d

def segmentacao_tam(caminhosdict, tamanho=0):
    dicio = defaultdict(list)
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        for parte in musD:
                for voz, caracteristicas in musD[parte].items():
                    if 'intDia' in caracteristicas:
                        if tamanho <= 0:
                            tamanho = len(caracteristicas['intDia'])
                        p1 = 0
                        while p1 + tamanho <= len(caracteristicas['intDia']):
                            p2 = p1 + tamanho
                            dicio[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]))].append((nome, parte, voz, (p1, p2), (caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1]),(caracteristicas['Ncompasso'][p2-1], caracteristicas['Pcompasso'][p2-1])))
                            p1 += 1
    return [(c, v) for c, v in dicio.items() if len(v) > 1]
 
def tam_min(caminhosdict, tamanho=1):
    listarecorrencias = segmentacao_tam(caminhosdict, tamanho=tamanho)
    listarecorrencias = sem_cont_inter(listarecorrencias)
    while len(listarecorrencias) != 0:
        return tam_min(caminhosdict, tamanho=tamanho+1)
    print(f'tamanho: {tamanho-1}')
    return tamanho-1

def segmentacao(caminhosdict, tamanho=0):
    dicio = defaultdict(list)
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        print(f'analisando {nome}, ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
        for parte in musD:
                for voz, caracteristicas in musD[parte].items():
                    if 'intDia' in caracteristicas:
                        if tamanho <= 0:
                            tamanho = len(caracteristicas['intDia'])
                        p1 = 0 #posicao 1
                        while p1 < len(caracteristicas['intDia']):
                            p2 = p1+1 #posicao 2
                            while p2-p1 <= tamanho and p2 <= len(caracteristicas['intDia']):
                                dicio[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]))].append((nome, parte, voz, (p1, p2), (caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1]),(caracteristicas['Ncompasso'][p2-1], caracteristicas['Pcompasso'][p2-1])))
                                p2 += 1
                            p1 += 1
    return sorted([(c, v) for c, v in dicio.items() if len(v) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)
 
def contida(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0:3] == outra[0:3] and posicao[3][0] >= outra[3][0] and posicao[3][1] <= outra[3][1]:
            return True
    return False

def intercalada(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0:3] == outra[0:3] and posicao[3][0] > outra[3][0] and posicao[3][0] < outra[3][1] and posicao[3][1] > outra[3][1]:
            return True
        if posicao[0:3] == outra[0:3] and posicao[3][1] > outra[3][0] and posicao[3][1] < outra[3][1] and posicao[3][0] < outra[3][0]:
            return True
    return False

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
    return {x:y for x,y in semcontinter}

"""
"""

lista = [-3, 4, -3, 4, -3, 4, -3, -2, -3, 4, -3, 4, -3, 4, -3, -2, -3, 4, -3, 4, -3, 4, -3, 2]

def cortes(lista,tamanho, p1=0):
    listacortes = []
    p2 = p1+tamanho
    while p2 <= len(lista):
        listacortes.append((p1,p2))
        p1 = p2+1
        p2 = p1+tamanho
    return listacortes

def maiorsequencia(lista):
    sequencia1 = []
    sequencia2 = []
    while len(lista) > 2:
        tamanho = 1
        while True:
            listacortes = cortes(lista,tamanho)
            if len(listacortes) == 1:
                break
            if len({tuple(lista[p1:p2]) for p1,p2 in listacortes}) == 1:
                sequencia1 = listacortes
            tamanho += 1
        for x in sequencia1:
            sequencia2.append(x)
    return sequencia2

listapronta = maiorsequencia(lista)