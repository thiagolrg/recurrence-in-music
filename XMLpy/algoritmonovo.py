from collections import defaultdict
import dirEinp as f_d

def Segmentos_do_tam(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho):
    SegmentosLocalizacoes = defaultdict(list)
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        for parte in musD:
            for voz, caracteristicas in musD[parte].items():
                if 'intDia' in caracteristicas:
                    p1 = 0
                    while p1 + tamanho <= len(caracteristicas['intDia']):
                        p2 = p1 + tamanho

                        segmento = []
                        for caracteristica in SegmentosCaracteristicas:
                            if caracteristica[1] == 'p1':
                                segmento.append(tuple(caracteristicas[caracteristica[0]][p1:p1+1]))
                            elif caracteristica[1] == 'p1p2':
                                segmento.append(tuple(caracteristicas[caracteristica[0]][p1:p2]))
                            elif caracteristica[1] == 'p2':
                               segmento.append(tuple(caracteristicas[caracteristica[0]][p2-1:p2]))
                            else:
                                raise ValueError('caracteristica deve ser p1, p1p2 ou p2')
                        segmento = tuple(segmento)
                        
                        localizacao = [nome, parte, voz, (p1, p2)]
                        for caracteristica in LocalizacoesCaracteristicas:
                            if caracteristica[1] == 'p1':
                                localizacao.append(tuple(caracteristicas[caracteristica[0]][p1:p1+1]))
                            elif caracteristica[1] == 'p1p2':
                                localizacao.append(tuple(caracteristicas[caracteristica[0]][p1:p2]))
                            elif caracteristica[1] == 'p2':
                                localizacao.append(tuple(caracteristicas[caracteristica[0]][p2-1:p2]))
                            else:
                                raise ValueError('caracteristica deve ser p1, p1p2 ou p2')
                        localizacao = tuple(localizacao)

                        SegmentosLocalizacoes[segmento].append(localizacao)
                        p1 += 1
    return SegmentosLocalizacoes

def Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, TamMax, diA, SegmentosLocalizacoes=defaultdict(list), tam=1):
    if TamMax == False:
        print(f'gerando segmentos de tamanho: {tam}')
        SegmentosDoTam = Segmentos_do_tam(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho=tam)
        print(f'verificando Tamanho Máximo:')
        for localizacoes in SegmentosDoTam.values():
            if len(localizacoes) > 1:
                SegmentosLocalizacoes.update(SegmentosDoTam)
                return Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, TamMax, diA, SegmentosLocalizacoes=SegmentosLocalizacoes, tam=tam+1)
        TamMax = tam-1
        print(f'encontrado TamMax: {TamMax}')
        f_d.escreve_pickle(diA,TamMax, '_tamanho_', trunca=True)
        return [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]

    print(f'TamMax: {TamMax}')
    for tam in range(1,TamMax+1):
        print(f'gerando segmentos de tamanho: {tam}')
        SegmentosDoTam = Segmentos_do_tam(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho=tam)
        SegmentosLocalizacoes.update(SegmentosDoTam)
    return [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]

#Recorrências sem contidos e intercalados
def sort_recorrencias(segmentacao):
    return sorted([(c, v) for c, v in segmentacao if len(v) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)

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

def sem_cont(listarecorrencias):
    listarecorrencias = sort_recorrencias(listarecorrencias)
    semcont = []
    quepassaram = []
    for segmento, posicoes in listarecorrencias:
        posicoessegmento = []
        for posicao in posicoes:
            if not contida(quepassaram, posicao):
                posicoessegmento.append(posicao)
        if len(posicoessegmento) > 1:
            for v in posicoessegmento:
                quepassaram.append(v)
            semcont.append((segmento,posicoessegmento))
    return semcont

def sem_cont_inter(listarecorrencias):
    listarecorrencias = sort_recorrencias(listarecorrencias)
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
    
#Sequencias sem contidos e intecalados

def sorts_sequencias(dicio):
    seq = sort_sequencias(dicio)
    seq = so_seq(seq)
    seq = sortsoseq(seq)
    return seq

def sort_sequencias(dicio):
    return sorted([(c, v) for c, v in dicio.items() if len(v) > 1 and len(c[0]) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)    

def so_seq(listarecorrencias):
    soseq = []
    for segmento, posicoes in listarecorrencias:
        posicoesseq = seq(posicoes)
        if len(posicoesseq) > 1:
            soseq.append((segmento,posicoesseq))
    return soseq

def seq(posicoes):
    posicoesseq = []
    p = 0
    while p+1 < len(posicoes):
        if posicoes[p+1][3][0] - posicoes[p][3][1] == 1 and posicoes[p+1][0:3] == posicoes[p][0:3]:
            s1 = p
            while posicoes[p+1][3][0] - posicoes[p][3][1] == 1 and posicoes[p+1][0:3] == posicoes[p][0:3]:
                p = p+1
                if p == len(posicoes)-1:
                    break
            s2 = p+1
            posicoesseq.append(posicoes[s1:s2])
        p = p+1
    return posicoesseq

def sortsoseq(listarecorrencias):
    listasort = []
    for segmento, posicoes in listarecorrencias:
        for posicao in posicoes:
            tamanhoseq = posicao[-1][3][1] - posicao[0][3][0]
            listasort.append((segmento,posicoes,tamanhoseq))
    listasort = sorted(listasort, key= lambda x: x[2], reverse=True)
    listasort = [(s,p) for s,p,t in listasort]
    return listasort

def sem_cont_inter_seq(listarecorrencias):
    semcontinter = []
    quepassaram = []
    for segmento, posicoes in listarecorrencias:
        posicoessegmento = []
        for posicao in posicoes:
            if not intercalada_seq(posicoessegmento, posicao) and not intercalada_seq(quepassaram, posicao) and not contida_seq(quepassaram, posicao):
                posicoessegmento.append(posicao)
        if len(posicoessegmento) > 0:
            for v in posicoessegmento:
                quepassaram.append(v)
            semcontinter.append((segmento,posicoessegmento))
    return semcontinter

def contida_seq(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0][0:3] == outra[0][0:3] and posicao[0][3][0] >= outra[0][3][0] and posicao[-1][3][1] <= outra[-1][3][1]:
            return True
    return False

def intercalada_seq(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0][0:3] == outra[0][0:3] and posicao[0][3][0] > outra[0][3][0] and posicao[0][3][0] < outra[-1][3][1] and posicao[-1][3][1] > outra[-1][3][1]:
            return True
        if posicao[0][0:3] == outra[0][0:3] and posicao[-1][3][1] > outra[0][3][0] and posicao[-1][3][1] < outra[0][3][1] and posicao[0][3][0] < outra[0][3][0]:
            return True
    return False

#Por Quantidade
def porquantidade(segmentacao, quantidade, iguaiouigualemaior):
    quepassaram = []
    for item in segmentacao:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0])
        if iguaiouigualemaior == '==' and len(nomes) == quantidade:
            quepassaram.append(item)
        elif iguaiouigualemaior == '>=' and len(nomes) >= quantidade:
            quepassaram.append(item)
    if len(quepassaram) == 0:
        return None
    return quepassaram