from collections import defaultdict
import dirEinp as f_d

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
    print(f'caracteristicas: {SegmentosCaracteristicas}')
    nomes = tuple([f_d.caminho_nome(x, ['.p']) for x in caminhosdict])
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
            TamMax = tamanho
            print(f'\nsalvando tamanho máximo: {TamMax}')
            tamanhos.setdefault((nomes,tuple(SegmentosCaracteristicas)),TamMax)
            f_d.escreve_pickle(diA,tamanhos, '_tamanhos_', trunca=True)
            sorecorrencias = [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]
            print(f'quantidade de segmentos: {len(sorecorrencias)}\n')
            return sorecorrencias
        return verificandotamanhos(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict)

    print(f'tamanho máximo armanezado: {TamMax}')
    for tam in range(1,TamMax+1):
        print(f'\rgerando segmentos de tamanho: {tam}', end='')
        SegmentosDoTam = Segmentos_do_tam(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, tamanho=tam)
        SegmentosLocalizacoes.update(SegmentosDoTam)
    sorecorrencias = [(c, v) for c, v in SegmentosLocalizacoes.items() if len(v) > 1]
    print(f'\nquantidade de segmentos: {len(sorecorrencias)}\n')
    return sorecorrencias

#Recorrências sem contidos e intercalados
def sort_recorrencias(segmentacao):
    return sorted([(c, v) for c, v in segmentacao], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)

def contido(maior, menor):
    if maior[0:3] == menor[0:3] and menor[3][0] > maior[3][0] and menor[3][1] <= maior[3][1]:
        return True
    if maior[0:3] == menor[0:3] and menor[3][0] >= maior[3][0] and menor[3][1] < maior[3][1]:
        return True
    return False

def intercalado(antes, depois, distancia=0):
    if antes[0:3] == depois[0:3] and depois[3][0] > antes[3][0] and depois[3][0] < antes[3][1]+distancia and depois[3][1] > antes[3][1]:
        return True
    return False

def Sem_Cont_Inte(listarecorrencias, SemCont=True, SemInte=True):
    listarecorrencias = sort_recorrencias(listarecorrencias)
    print(f'SemCont: {SemCont}, SemInte: {SemInte}')
    listarecorrencias = sort_recorrencias(listarecorrencias)
    print(f'\rquantidade de segmentos: {len(listarecorrencias)} ')

    SegIni = 0
    LocIni = 0
    SegComp = SegIni
    LocComp = LocIni + 1

    while SegIni < len(listarecorrencias):
        nomesSegIni = set()
        for v in listarecorrencias[SegComp][1]:
            nomesSegIni.add(v[0:3])
        while SegComp < len(listarecorrencias):
            nomesSegComp = set()
            for v in listarecorrencias[SegComp][1]:
                nomesSegComp.add(v[0:3])

            if nomesSegIni.issubset(nomesSegComp):
                while LocIni < len(listarecorrencias[SegIni][1]):
                    Ini = listarecorrencias[SegIni][1][LocIni]
                    while LocComp < len(listarecorrencias[SegComp][1]):
                        Comp = listarecorrencias[SegComp][1][LocComp]
                        if SemCont and contido(Ini, Comp):
                            listarecorrencias[SegComp][1].pop(LocComp)
                            LocComp -= 1
                        elif SemInte and (intercalado(Ini, Comp) or intercalado(Comp, Ini)):
                            listarecorrencias[SegComp][1].pop(LocComp)
                            LocComp -= 1
                        LocComp += 1
                    LocIni += 1
                    LocComp = 0
                if len(listarecorrencias[SegComp][1]) <= 1:
                    listarecorrencias.pop(SegComp)
                    SegComp -= 1
            SegComp += 1
            LocIni = 0

        SegIni += 1
        SegComp = SegIni
        LocComp = LocIni + 1
        print(f'\rquantidade de segmentos: {len(listarecorrencias)} ',end='')
    print()
    return listarecorrencias

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
    if len(quepassaram) > 0:
        return quepassaram