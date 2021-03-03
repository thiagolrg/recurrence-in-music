from collections import defaultdict
import dirEinp as f_d
import time

#Segmentação
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
    """
    print('lTV:')
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        for parte in musD:
            for voz, caracteristicas in musD[parte].items():
                if 'intDia' in caracteristicas:
                    print([nome, parte, voz, 'IntDia', len(caracteristicas["intDia"])])
    """
    print(f'segmentacao caracteristicas: {SegmentosCaracteristicas}')
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
    segmentacoes.setdefault(chavearquivo,sorecorrencias)
    f_d.escreve_pickle(diA,segmentacoes, '_segmentacoes_', trunca=True)

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



#Recorrências sem contidos e intercalados
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
            print(f'\rQuaSegUnicos: {len(semcont)} ', end='')
    stop = time.perf_counter()
    QSR = 0
    for SegPos in semcont:
        for Pos in SegPos[1]:
            QSR = QSR + len(Pos)
    print(f'\nQuaSegRep: {QSR}')
    print(f'{stop-start} segundos\n')
    return semcont

def sem_cont_inte(listarecorrencias, distancia=0):
    listarecorrencias = sort_recorrencias(listarecorrencias)
    print(f'sem cont inte:')
    start = time.perf_counter()
    semcontinte = []
    quepassaram = []
    for segmento, posicoes in listarecorrencias:
        posicoessegmento = []
        for posicao in posicoes:
            if not contida(quepassaram, posicao) and not intercalada(posicoessegmento, posicao, distancia=distancia) and not intercalada(quepassaram, posicao, distancia=distancia):
                posicoessegmento.append(posicao)
        if len(posicoessegmento) > 1:
            for v in posicoessegmento:
                quepassaram.append(v)
            semcontinte.append((segmento,posicoessegmento))
            print(f'\rQuaSegUnicos: {len(semcontinte)} ', end='')
    stop = time.perf_counter()
    QSR = 0
    for SegPos in semcontinte:
        for Pos in SegPos[1]:
            QSR = QSR + len(Pos)
    print(f'\nQuaSegRep: {QSR}')
    print(f'{stop-start} segundos\n')
    return semcontinte

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
    return quepassaram