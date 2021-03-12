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
    print('segmentacao:')
    print('lTV:')
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        for parte in musD:
            for voz, caracteristicas in musD[parte].items():
                if 'intDia' in caracteristicas:
                    print([nome, parte, voz, 'IntDia', len(caracteristicas["intDia"])])

    start = time.perf_counter()
    print(f'\ncaracteristicas: {SegmentosCaracteristicas}')
    nomes = tuple([f_d.caminho_nome(x, ['.p']) for x in caminhosdict])
    chavearquivo = (nomes,tuple(SegmentosCaracteristicas))
    segmentacoes = dict()
    try:
        tamanhos = f_d.le_pickle(diA+'\\_tamanhos_.p')
        try:
            TamMax = tamanhos[(nomes,tuple(SegmentosCaracteristicas))]
        except KeyError:
            TamMax = False
    except FileNotFoundError:
        f_d.escreve_pickle(diA,dict(), '_tamanhos_')
        tamanhos = f_d.le_pickle(diA+'\\_tamanhos_.p')
        TamMax = False        

    if TamMax == False:
        print('verificando tamanho máximo:')
        def verificandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho=1):
            print(f'\rgerando segmentos de tamanho: {tamanho}', end='')
            SegmentosDoTam = Segmentos_do_tam(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho)
            for localizacoes in SegmentosDoTam.values():
                if len(localizacoes) > 1:
                    SegmentosLocalizacoes.update(SegmentosDoTam)
                    return verificandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho+1)
            TamMax = tamanho-1
            tamanhos.setdefault((nomes,tuple(SegmentosCaracteristicas)),TamMax)
            f_d.escreve_pickle(diA,tamanhos, '_tamanhos_', trunca=True)
            print(f'\ntamanho máximo salvo: {TamMax}')
            sorecorrencias = [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]
            stop = time.perf_counter()

            QSU = len(SegmentosLocalizacoes)
            QSR = 0
            for seg, loc in SegmentosLocalizacoes.items():
                QSR = QSR + len(loc)

            QSUr = len(sorecorrencias)
            QSRr = 0
            for seg, loc in sorecorrencias:
                QSRr = QSRr + len(loc)
            
            print(f'\nQuaSegRep: {QSR}')
            print(f'QuaSegUnicos: {QSU}')
            print(f'QuaSegRepRec: {QSRr}')
            print(f'QuaSegUnicosRec: {QSUr}')
            print(f'{stop-start} segundos\n')

            return sorecorrencias
        return verificandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict)

    print(f'tamanho máximo armanezado: {TamMax}')
    for tam in range(1,TamMax+1):
        print(f'\rgerando segmentos de tamanho: {tam}', end='')
        SegmentosDoTam = Segmentos_do_tam(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho=tam)
        SegmentosLocalizacoes.update(SegmentosDoTam)
    sorecorrencias = [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]
    stop = time.perf_counter()

    QSU = len(SegmentosLocalizacoes)
    QSR = 0
    for seg, loc in SegmentosLocalizacoes.items():
        QSR = QSR + len(loc)

    QSUr = len(sorecorrencias)
    QSRr = 0
    for seg, loc in sorecorrencias:
        QSRr = QSRr + len(loc)

    print(f'\nQuaSegRep: {QSR}')        
    print(f'QuaSegUnicos: {QSU}')
    print(f'QuaSegRepRec: {QSRr}')
    print(f'QuaSegUnicosRec: {QSUr}')
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
            print(f'\rQSu: {len(dictrecorrencias)} ', end='')
    listarecorrenciaspronta = []
    for chave, valor in dictrecorrencias.items():
        if len(valor) > 1:
            setv = set()
            for v in valor:
                setv.add(v[0:3])
            if tuple(sorted(setv)) == chave[1]:
                listarecorrenciaspronta.append((chave[0], valor))
    stop = time.perf_counter()
    dadosseg(listarecorrenciaspronta)
    print(f'{stop-start} segundos\n')
    return listarecorrencias

def sem_cont_inte(listarecorrencias):
    listarecorrencias = sort_recorrencias(listarecorrencias)
    start = time.perf_counter()
    print(f'sem cont inte:\nquantidade de segmentos: {len(listarecorrencias)}')
    semcontinte = []
    quepassaram = []
    for segmento, posicoes in listarecorrencias:
        posicoessegmento = []
        for posicao in posicoes:
            if not intercalada(posicoessegmento, posicao) and not intercalada(quepassaram, posicao) and not contida(quepassaram, posicao):
                posicoessegmento.append(posicao)
        if len(posicoessegmento) > 1:
            for v in posicoessegmento:
                quepassaram.append(v)
            semcontinte.append((segmento,posicoessegmento))
            print(f'\rquantidade de segmentos: {len(semcontinte)} ', end='')
        stop = time.perf_counter()
    print(f'\n{stop-start} segundos')
    print()
    dadosseg(listarecorrenciaspronta)
    print(f'{stop-start} segundos\n')
    return listarecorrenciaspronta

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