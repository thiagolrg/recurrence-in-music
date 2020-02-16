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

def segmentacao_rec(caminhosdict, tamanho=0):
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

def recorrencias(caminhosdict,tamanho=0):
    return sem_cont_inter(segmentacao_rec(caminhosdict, tamanho=tamanho))

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

def seq(posicoes):
    posicoesseq = []
    p = 0
    while p+1 < len(posicoes):
        if posicoes[p+1][3][0] - posicoes[p][3][1] == 1:
            s1 = p
            while posicoes[p+1][3][0] - posicoes[p][3][1] == 1:
                p = p+1
                if p == len(posicoes)-1:
                    break
            s2 = p+1
            posicoesseq.append(posicoes[s1:s2])
        p = p+1
    return posicoesseq

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