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

#Filtro por conjuntos 1
#setgrupo=1 retira todas na mesma combinacao de músicas, setgrupo=3 retira todas na mesma combinacao de vozes
def sem_cont_inte_conj1(listarecorrencias, distancia=0, setgrupo=1):
    listarecorrencias = sort_cont_conj1(listarecorrencias, setgrupo)
    print(f'sem cont inte:')
    start = time.perf_counter()
    semcontinte = []
    for grupo, segspos in listarecorrencias:
        quepassaram = []
        for segmento, posicoes in segspos:
            posicoessegmento = []
            for posicao in posicoes:
                if not contida(quepassaram, posicao) and not intercalada(posicoessegmento, posicao, distancia=distancia) and not intercalada(quepassaram, posicao, distancia=distancia):
                    posicoessegmento.append(posicao)
            setv = set()
            for v in posicoessegmento:
                quepassaram.append(v)
                setv.add(v[0:setgrupo])
            if tuple(sorted(setv)) == grupo:
                semcontinte.append((segmento,posicoessegmento))
            print(f'\rQuaSegUnicos: {len(semcontinte)} ', end='')
    stop = time.perf_counter()
    dadosseg(semcontinte)
    print(f'{stop-start} segundos\n')
    return sorted([(c, v) for c, v in semcontinte if len(v) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)

def sort_cont_conj1(listarecorrencias, setgrupo):
    #recorrencias em organizadas posicao, conjunto e segmentos
    p_pset_pseg = []
    for seg, pos in listarecorrencias:
        posset = {p[0:setgrupo] for p in pos}
        for p in pos:
            p_pset_pseg.append((p,tuple(sorted(posset)),seg))
    #sort por nome, conjunto, tamanho maior, posicao menor
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][3][0]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (len(item[2][0])), reverse=True)
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[1]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][0:3]))

    locpset = defaultdict(list)
    for p, pset, pseg in p_pset_pseg:
        locpset[(p[0:3], pset)].append((p,pseg))

    listapronta = []
    for grupo, ppsegs in locpset.items():
        diciogrupos = defaultdict(list)
        for p, pseg in ppsegs:
            diciogrupos[pseg].append(p)
        diciogrupos = [(c,v) for c, v in diciogrupos.items()]
        listapronta.append([grupo[1], diciogrupos])
    return listapronta

#Filtro por conjuntos 2
#setgrupo=1 retira todas na mesma combinacao de músicas, setgrupo=3 retira todas na mesma combinacao de vozes
def sem_cont_conj2(listarecorrencias, setgrupo=1):
    print(f'filtro sem cont:')
    start = time.perf_counter()
    listarecorrencias = sort_cont_conj2(listarecorrencias,setgrupo)
    dictrecorrencias = defaultdict(list)
    for grupo in listarecorrencias:
        quepassaram = []
        for posicao in grupo[1]:
            if not contida2(quepassaram, posicao[0]):
                quepassaram.append(posicao)
        for posicao, segmento in quepassaram:
            dictrecorrencias[(segmento, grupo[0])].append(posicao)
    stop = time.perf_counter()
    print('quantidade tudo:')
    dadosseg(dictrecorrencias)
    t = stop-start
    start = time.perf_counter()
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        if len(valor) > 1:
            setv = {v[0:setgrupo] for v in valor}
            if tuple(sorted(setv)) == chave[1]:
                listarecorrenciaspronta.append((chave[0], valor))
    stop = time.perf_counter()
    t = t+stop-start
    print('quantidade so recorrencias:')
    dadosseg(listarecorrenciaspronta)
    print(f'{t} segundos\n')
    return sorted([(c, v) for c, v in listarecorrenciaspronta if len(v) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)

#setgrupo=1 retira todas na mesma combinacao de músicas, setgrupo=3 retira todas na mesma combinacao de vozes
def sem_cont_inte_conj2(listarecorrencias, distancia=0, setgrupo=1):
    print(f'filtro sem cont inte:')
    start = time.perf_counter()
    listarecorrencias = sort_cont_conj2(listarecorrencias, setgrupo)
    dictrecorrencias = defaultdict(list)
    for grupovoz in listarecorrencias:
        quepassaram = []
        for posicao in grupovoz[1]:
            if not contida2(quepassaram, posicao[0]) and not intercalada2(quepassaram, posicao[0], distancia=distancia):
                quepassaram.append(posicao)
        for posicao, segmento in quepassaram:
            dictrecorrencias[(segmento, grupovoz[0])].append(posicao)
    stop = time.perf_counter()
    print('quantidade tudo:')
    dadosseg(dictrecorrencias)
    t = stop-start
    start = time.perf_counter()
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        if len(valor) > 1:
            setv = {v[0:setgrupo] for v in valor}
            if tuple(sorted(setv)) == chave[1]:
                listarecorrenciaspronta.append((chave[0], valor))
    stop = time.perf_counter()
    t = t+stop-start
    print('quantidade so recorrencias:')
    dadosseg(listarecorrenciaspronta)
    print(f'{t} segundos\n')
    return sorted([(c, v) for c, v in listarecorrenciaspronta if len(v) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)

def sort_cont_conj2(listarecorrencias, setgrupo):
    #recorrencias em organizadas posicao, conjunto e segmentos
    p_pset_pseg = []
    for seg, pos in listarecorrencias:
        posset = {p[0:setgrupo] for p in pos}
        for p in pos:
            p_pset_pseg.append((p,tuple(sorted(posset)),seg))
    #sort por nome, conjunto, tamanho maior, posicao menor
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][3][0]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (len(item[2][0])), reverse=True)
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[1]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][0:3]))

    locpset = defaultdict(list)
    for p, pset, pseg in p_pset_pseg:
        locpset[(p[0:3], pset)].append((p,pseg))
    return [(c[1],v) for c, v in locpset.items()]  
def contida2(listaposicoes, posicao):
    for quepassou in listaposicoes:
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][0] >= quepassou[0][3][0] and posicao[3][1] <= quepassou[0][3][1]:
            return True
    return False
def intercalada2(listaposicoes, posicao, distancia):
    for quepassou in listaposicoes:
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][0] > quepassou[0][3][0] and posicao[3][0] < quepassou[0][3][1]+distancia and posicao[3][1] > quepassou[0][3][1]:
            return True
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][1] > quepassou[0][3][0]-distancia and posicao[3][1] < quepassou[0][3][1] and posicao[3][0] < quepassou[0][3][0]:
            assert posicao[3][1] - posicao[3][0] < quepassou[0][3][1] - quepassou[0][3][0]
            return True
    return

#Por Quantidade
def porquantidade(segmentacao, quantidade, iguaiouigualemaior):
    quepassaram = []
    for item in segmentacao:
        nomes = {valor[0] for valor in item[1]}
        if iguaiouigualemaior == '==' and len(nomes) == quantidade:
            quepassaram.append(item)
        elif iguaiouigualemaior == '>=' and len(nomes) >= quantidade:
            quepassaram.append(item)
    return quepassaram