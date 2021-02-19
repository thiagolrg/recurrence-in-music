from collections import defaultdict
import dirEinp as f_d

#Para calcular o tamanho mínimo
def segmentacao_IntDia_Dur_tam(caminhosdict, tamanho=0):
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
    print(f'testando tamanho: {tamanho}')
    listarecorrencias = segmentacao_IntDia_Dur_tam(caminhosdict, tamanho=tamanho)
    listarecorrencias = sem_cont_inter(listarecorrencias)
    while len(listarecorrencias) != 0:
        return tam_min(caminhosdict, tamanho=tamanho+1)
    print(f'tamanho min: {tamanho-1}')
    return tamanho-1

#Segmentações
def segmentacao_IntDia_Dur(caminhosdict, tamanho=0):
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
    return dicio

def segmentacao_IntDia_Dur_Ptempo(caminhosdict, tamanho=0):
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
                                dicio[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]),caracteristicas['Ptempo'][p1])].append((nome, parte, voz, (p1, p2), (caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1]),(caracteristicas['Ncompasso'][p2-1], caracteristicas['Pcompasso'][p2-1])))
                                p2 += 1
                            p1 += 1
    return dicio

def segmentacao_IntDia_Dur_Pcompasso(caminhosdict, tamanho=0):
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
                                dicio[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]),tuple(caracteristicas['Pcompasso'][p1:p2]))].append((nome, parte, voz, (p1, p2), (caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1]),(caracteristicas['Ncompasso'][p2-1], caracteristicas['Pcompasso'][p2-1])))
                                p2 += 1
                            p1 += 1
    return dicio

#Recorrências sem contidos e intercalados
def sort_recorrencias(dicio):
    return sorted([(c, v) for c, v in dicio.items() if len(v) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)

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

def contida(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0:3] == outra[0:3] and posicao[3][0] >= outra[3][0] and posicao[3][1] <= outra[3][1]:
            return True
    return False

def intercalada(listaposicoes, posicao, distancia=1):
    for outra in listaposicoes:
        if posicao[0:3] == outra[0:3] and posicao[3][0] > outra[3][0] and posicao[3][0] < outra[3][1]+distancia and posicao[3][1] > outra[3][1]:
            return True
        if posicao[0:3] == outra[0:3] and posicao[3][1] > outra[3][0]-distancia and posicao[3][1] < outra[3][1] and posicao[3][0] < outra[3][0]:
            return True
    return False