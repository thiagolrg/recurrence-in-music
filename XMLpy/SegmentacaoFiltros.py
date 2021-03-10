from collections import defaultdict
import dirEinp as f_d
import time

#essa função é chamada para cada tamanho da segmenatção
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

def Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, SegmentosLocalizacoes, tam=1):
    print(f'segmentacao caracteristicas: {SegmentosCaracteristicas}')

    #Verfica se a recorrencia já foi feita
    nomes = tuple([f_d.caminho_nome(x, ['.p']) for x in caminhosdict])
    chavearquivo = (nomes,tuple(SegmentosCaracteristicas))
    try:
        segmentacoes = f_d.le_pickle(diA+'\\_segmentacoes_.p')
        try:
            sorecorrencias = segmentacoes[chavearquivo]
            print(f'resgatada do arquivo\n')
            QSUr = len(sorecorrencias)
            QSRr = 0
            for seg, loc in sorecorrencias:
                QSRr = QSRr + len(loc)
            print(f'QuaSegUnicosRec: {QSUr}')
            print(f'QuaSegRepRec: {QSRr}')
            return sorecorrencias
        except KeyError:
            pass
    except FileNotFoundError:
        segmentacoes = dict()
        f_d.escreve_pickle(diA,segmentacoes, '_segmentacoes_')    

    #Se não foi feita verifica por tamanho
    def verificandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho=1):
        print(f'\rgerando segmentos de tamanho: {tamanho}', end='')
        SegmentosDoTam = Segmentos_do_tam(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho)
        for localizacoes in SegmentosDoTam.values():
            if len(localizacoes) > 1:
                SegmentosLocalizacoes.update(SegmentosDoTam)
                return verificandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho+1)
        return SegmentosLocalizacoes

    start = time.perf_counter()
    SegmentosLocalizacoes = verificandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict)
    sorecorrencias = [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]
    stop = time.perf_counter()
    
    #Salva o resultado 
    segmentacoes.setdefault(chavearquivo,sorecorrencias)
    f_d.escreve_pickle(diA,segmentacoes, '_segmentacoes_', trunca=True)

    #Imprime os dados das recorrencias e tempo de execução
    QSU = len(SegmentosLocalizacoes)
    QSR = 0
    for seg, loc in SegmentosLocalizacoes.items():
        QSR = QSR + len(loc)
    QSUr = len(sorecorrencias)
    QSRr = 0
    for seg, loc in sorecorrencias:
        QSRr = QSRr + len(loc)
    print(f'\nQuaSegUnicos: {QSU}')
    print(f'QuaSegRep: {QSR}')
    print(f'QuaSegUnicosRec: {QSUr}')
    print(f'QuaSegRepRec: {QSRr}')
    print(f'{stop-start} segundos\n')
    return sorecorrencias

def sort_continte3(listarecorrencias):
    p_pset_pseg = []
    for seg, pos in listarecorrencias:
        posset = {p[0:3] for p in pos}
        for p in pos:
            p_pset_pseg.append((p,tuple(posset),seg))
    #por nome, set, tamanho maior, posicao menor
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][3][0]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (len(item[2][0])), reverse=True)
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[1]))
    p_pset_pseg = sorted([(p, pset, pseg) for p, pset, pseg in p_pset_pseg], key=lambda item: (item[0][0:3]))
    locpset = defaultdict(list)
    for p, pset, pseg in p_pset_pseg:
        locpset[(p[0:3], pset)].append((p,pseg))
    locpset = [(c[1],v) for c, v in locpset.items()]
    return locpset

def contida3(listaposicoes, posicao):
    for quepassou in listaposicoes:
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][0] >= quepassou[0][3][0] and posicao[3][1] <= quepassou[0][3][1]:
            return True
    return False

def intercalada3(listaposicoes, posicao, distancia=0):
    for quepassou in listaposicoes:
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][0] > quepassou[0][3][0] and posicao[3][0] < quepassou[0][3][1]+distancia and posicao[3][1] > quepassou[0][3][1]:
            return True
        if posicao[0:3] == quepassou[0][0:3] and posicao[3][1] > quepassou[0][3][0]-distancia and posicao[3][1] < quepassou[0][3][1] and posicao[3][0] < quepassou[0][3][0]:
            assert posicao[3][1] - posicao[3][0] < quepassou[0][3][1] - quepassou[0][3][0]
            return True
    return 
    
def sem_cont3(listarecorrencias):
    print(f'sem cont:')
    start = time.perf_counter()
    listarecorrencias = sort_continte3(listarecorrencias)
    dictrecorrencias = defaultdict(list)
    for grupo in listarecorrencias:
        quepassaram = []
        for posicao in grupo[1]:
            if not contida3(quepassaram, posicao[0]):
                quepassaram.append(posicao)
        for posicao, segmento in quepassaram:
            dictrecorrencias[(segmento, grupo[0])].append(posicao)
            print(f'\rQuaSegUnicos: {len(dictrecorrencias)} ', end='')
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        c = chave[1]
        if len(valor) > 1:
            setv = set()
            for v in valor:
                setv.add(v[0:3])
            if tuple(setv) == chave[1]:
                listarecorrenciaspronta.append((chave[0], valor))
    stop = time.perf_counter()
    print(f'\rQuaSegUnicos: {len(listarecorrenciaspronta)} ', end='')
    QSR = 0
    for SegPos in listarecorrencias:
        for Pos in SegPos[1]:
            QSR = QSR + len(Pos)
    print(f'\nQuaSegRep: {QSR}')
    print(f'{stop-start} segundos\n')
    return listarecorrencias

def sem_cont_inte3(listarecorrencias, distancia=0):
    print(f'sem cont inte:')
    start = time.perf_counter()
    listarecorrencias = sort_continte3(listarecorrencias)
    dictrecorrencias = defaultdict(list)
    for grupo in listarecorrencias:
        quepassaram = []
        for posicao in grupo[1]:
            if not contida3(quepassaram, posicao[0]) and not intercalada3(quepassaram, posicao[0], distancia=distancia):
                quepassaram.append(posicao)
        for posicao, segmento in quepassaram:
            dictrecorrencias[(segmento, grupo[0])].append(posicao)
            print(f'\rQuaSegUnicos: {len(dictrecorrencias)} ', end='')
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        if len(valor) > 1:
            setv = {v[0:3] for v in valor}
            if tuple(setv) == chave[1]:
                listarecorrenciaspronta.append((chave[0], valor))
    stop = time.perf_counter()
    print(f'\rQuaSegUnicos: {len(listarecorrenciaspronta)} ', end='')
    QSR = 0
    for SegPos in listarecorrencias:
        for Pos in SegPos[1]:
            QSR = QSR + len(Pos)
    print(f'\nQuaSegRep: {QSR}')
    print(f'{stop-start} segundos\n')
    return listarecorrencias

#Por Qt
def porquantidade(segmentacao, quantidade, iguaiouigualemaior):
    quepassaram = []
    for item in segmentacao:
        nomes = {valor[0] for valor in item[1]}
        if iguaiouigualemaior == '==' and len(nomes) == quantidade:
            quepassaram.append(item)
        elif iguaiouigualemaior == '>=' and len(nomes) >= quantidade:
            quepassaram.append(item)
    return quepassaram