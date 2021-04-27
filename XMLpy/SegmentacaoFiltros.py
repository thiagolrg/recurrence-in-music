from collections import defaultdict
import dirEinp as f_d
import time

#Segmentação___________________________________________

#gera os segmentos de cada tamanho
def gerandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho):
    start = time.perf_counter()
    SegmentosLocalizacoes = dict()
    while True:
        SegmentosDoTam = defaultdict(list)
        for caminho in caminhosdict:
            musD = f_d.le_pickle(caminho)
            nome = musD.pop('nome')
            for parte in musD:
                for voz, caracteristicas in musD[parte].items():
                    if 'intDia' in caracteristicas and len(caracteristicas['intDia']) >=  tamanho:
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

                            SegmentosDoTam[segmento].append(localizacao)
                            p1 += 1
        tamanho += 1
        for localizacoes in SegmentosDoTam.values():
            if len(localizacoes) > 1:
                SegmentosLocalizacoes.update(SegmentosDoTam)
                break
        else:
            stop = time.perf_counter()
            print(f'gerados segmentos até tamanho: {tamanho-1} ')
            print('quantidade tudo:')
            dadosseg(SegmentosLocalizacoes)
            t = stop-start
            start = time.perf_counter()
            SegmentosLocalizacoes = [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]
            stop = time.perf_counter()
            t = t+stop-start
            print('quantidade so recorrencias:')
            dadosseg(SegmentosLocalizacoes)
            print(f'{t} segundos\n')
            return SegmentosLocalizacoes

#Verifica se as recorrências já foram feitas para o repertorio e caracteristicas especificadas, se não, gera as recorrencias
def Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, tamanho=1):
    print(f'segmentacao caracteristicas: {SegmentosCaracteristicas}')
    nomes = tuple([f_d.caminho_nome(x, ['.p']) for x in caminhosdict])
    chavearquivo = (nomes,tuple(SegmentosCaracteristicas))
    try:
        segmentacoes = f_d.le_pickle(diA+'\\_segmentacoes_.p')
        sorecorrencias = segmentacoes[chavearquivo]
        print(f'resgatada do arquivo:')
        print('quantidade so recorrencias:')
        dadosseg(sorecorrencias)
        print()
        return sorecorrencias
    except FileNotFoundError:
        sorecorrencias = gerandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho)
        segmentacoes = dict()
        segmentacoes.setdefault(chavearquivo,sorecorrencias)
        f_d.escreve_pickle(diA,segmentacoes, '_segmentacoes_', trunca=True)
        return sorecorrencias
    except KeyError:
        del(segmentacoes)
        sorecorrencias = gerandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho)
        segmentacoes = f_d.le_pickle(diA+'\\_segmentacoes_.p')
        segmentacoes.setdefault(chavearquivo,sorecorrencias)
        f_d.escreve_pickle(diA,segmentacoes, '_segmentacoes_', trunca=True)
        return sorecorrencias

#imprimi o tamanho das recorrencias e filtros
def dadosseg(sorecorrencias):
    QSu = len(sorecorrencias)
    if isinstance(sorecorrencias, list):
        QLoc = 0
        for segloc in sorecorrencias:
            QLoc = QLoc + len(segloc[1])
        print(f'QSuni: {QSu}')
        print(f'QSloc: {QLoc}')
    elif isinstance(sorecorrencias, dict):
        QLoc = 0
        for segloc in sorecorrencias.items():
            QLoc = QLoc + len(segloc[1])
        print(f'QSuni: {QSu}')
        print(f'QSloc: {QLoc}')

#Filtros___________________________________

#Antigo filtro geral
def sem_cont_inte(listarecorrencias, distancia):
    listarecorrencias = sort_recorrencias(listarecorrencias)
    print(f'sem cont inte:')
    start = time.perf_counter()
    semcontinte = []
    quepassaram = []
    for segmentoposicoes in listarecorrencias:
        posicoessegmento = []
        for posicao in segmentoposicoes[1]:
            if not contida(quepassaram, posicao) and not intercalada(posicoessegmento, posicao, distancia=distancia) and not intercalada(quepassaram, posicao, distancia=distancia):
                posicoessegmento.append(posicao)
        if len(posicoessegmento) > 1:
            for v in posicoessegmento:
                quepassaram.append(v)
            semcontinte.append((segmentoposicoes[0],posicoessegmento))
    stop = time.perf_counter()
    dadosseg(semcontinte)
    print(f'{stop-start} segundos\n')
    return sort_recorrencias(semcontinte)

def sem_cont(listarecorrencias):
    listarecorrencias = sort_recorrencias(listarecorrencias)
    print(f'sem cont:')
    start = time.perf_counter()
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
    stop = time.perf_counter()
    dadosseg(semcont)
    print(f'{stop-start} segundos\n')
    return sort_recorrencias(semcont)

#Essas funções são compartilhadas pelos dois filtros, ordenação e condicao para contidos e inercalados
def sort_recorrencias(segmentacao):
    return sorted([(c, v) for c, v in segmentacao], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)
def contida(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0:3] == outra[0:3] and posicao[3][0] >= outra[3][0] and posicao[3][1] <= outra[3][1]:
            return True
    return False
def intercalada(listaposicoes, posicao, distancia=0):
    for outra in listaposicoes:
        if posicao[0:3] == outra[0:3] and posicao[3][0] > outra[3][0] and posicao[3][0] < outra[3][1]+distancia and posicao[3][1] > outra[3][1]:
            return True
        if posicao[0:3] == outra[0:3] and posicao[3][1] > outra[3][0]-distancia and posicao[3][1] < outra[3][1] and posicao[3][0] < outra[3][0]:
            return True
    return False


#Novo Filtro por conjuntos
#conj = 1 monta conjuntos de músicas, conj = 3 monta conjuntos de vozes, gostei mais do 1
def sem_cont_inte_conj(listarecorrencias, distancia, conj):
    print(f'sem cont inte conj:')
    start = time.perf_counter()
    listarecorrencias = sort_recorrencias(listarecorrencias)
    listarecorrencias = dictConj(listarecorrencias, conj)
    semcontinte = []
    denovo = False
    for grupo, segpos in listarecorrencias.items():
        quepassaram = []
        for segmentoposicoes in segpos:
            posicoessegmento = []
            for posicao in segmentoposicoes[1]:
                if not contida(quepassaram, posicao) and not intercalada(posicoessegmento, posicao, distancia=distancia) and not intercalada(quepassaram, posicao, distancia=distancia):
                    posicoessegmento.append(posicao)
            if len(posicoessegmento) > 1:
                for v in posicoessegmento:
                    quepassaram.append(v)
                gruponovo = tuple(sorted({p[0:conj] for p in posicoessegmento}))
                if grupo != gruponovo:
                    denovo = True
                semcontinte.append((segmentoposicoes[0],posicoessegmento))
    stop = time.perf_counter()
    dadosseg(semcontinte)
    print(f'{stop-start} segundos\n')
    if denovo:
        return sem_cont_inte_conj(semcontinte, distancia, conj)
    return sort_recorrencias(semcontinte)

def sem_cont_conj(listarecorrencias, distancia, conj):
    print(f'sem cont conj:')
    start = time.perf_counter()
    listarecorrencias = sort_recorrencias(listarecorrencias)
    listarecorrencias = dictConj(listarecorrencias, conj)
    semcontinte = []
    denovo = False
    for grupo, segpos in listarecorrencias.items():
        quepassaram = []
        for segmentoposicoes in segpos:
            posicoessegmento = []
            for posicao in segmentoposicoes[1]:
                if not contida(quepassaram, posicao):
                    posicoessegmento.append(posicao)
            if len(posicoessegmento) > 1:
                for v in posicoessegmento:
                    quepassaram.append(v)
                gruponovo = tuple(sorted({p[0:conj] for p in posicoessegmento}))
                if grupo != gruponovo:
                    denovo = True
                semcontinte.append((segmentoposicoes[0],posicoessegmento))
    stop = time.perf_counter()
    dadosseg(semcontinte)
    print(f'{stop-start} segundos\n')
    if denovo:
        return sem_cont_inte_conj(semcontinte, distancia, conj)
    return sort_recorrencias(semcontinte)

def dictConj(listarecorrencias, conj):
    dictConj = defaultdict(list)
    for segpos in listarecorrencias:
        dictConj[tuple(sorted({p[0:conj] for p in segpos[1]}))].append(segpos)
    return dictConj

#Por Quantidade para antigo filtro geral
def porquantidade(segmentacao, quantidade, iguaiouigualemaior):
    quepassaram = []
    for item in segmentacao:
        nomes = {valor[0] for valor in item[1]}
        if iguaiouigualemaior == '==' and len(nomes) == quantidade:
            quepassaram.append(item)
        elif iguaiouigualemaior == '>=' and len(nomes) >= quantidade:
            quepassaram.append(item)
    return quepassaram

#Por quantidade para novo filtro conjuntos
def porquantidade2(segmentacao, quantidade, iguaiouigualemaior):
    quepassaram = defaultdict(list)
    for key, value in segmentacao.items():
        if iguaiouigualemaior == '==' and len(key) == quantidade:
            quepassaram.update({key:value})
        elif iguaiouigualemaior == '>=' and len(key) >= quantidade:
            quepassaram.update({key:value})
    return quepassaram