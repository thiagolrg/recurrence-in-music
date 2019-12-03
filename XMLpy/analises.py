from collections import defaultdict
import dirEinp as f_d

'''
contidos = True
partes = True
Segmentos = caracteristicas e p1 p1p2 p2m1 p1p2set p2m1set
posicoes = caractetisticas localizacao p1 p1p2 p2m1 p1p2set p2m1set
filtrosset = caractetisticas p1f p1p2f p2m1f

(segmento1,sgmento2): [{car1: set(), car2: set()}, [nome, parte, voz, (p1,p2),{}]]
'''

def subset_of(longest_slices, slise):
    for item in longest_slices:
        for ls in item[1]:
            if slise[3][0] >= ls[3][0] and slise[3][1] <= ls[3][1] and slise[0:3] == ls[0:3]:
                return True
    return False

def part_of(longest_slices, slise):
    for item in longest_slices:
        for ls in item[1]:
            if slise[3][0] > ls[3][0] and slise[3][0] <= ls[3][1] and slise[3][1] > ls[3][1] and slise[0:3] == ls[0:3]:
                return True
    return False



def segdur(caminhosdict):
    '''
    seguimento de intervalo e durações únicos que repetem pelo menos uma vez,
    sem contidos e amontoados
    '''
    aDicio = defaultdict(list)
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        musA = defaultdict(list)
        nome = musD.pop('nome')
        print(f'analisando {nome}, ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
    
        for parte in musD:
            for voz, caracteristicas in musD[parte].items():
                if 'intDia' in caracteristicas:
                    p1 = -1
                    p2 = 0
                    while p2 <= len(caracteristicas['intDia']):
                        p1 += 1
                        p2 = p1+1
                        while p2-p1 <= len(caracteristicas['intDia'])/2:
                            musA[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]))].append((nome, parte, voz, (p1, p2)))
                            p2 += 1

        slices = []
        uslices = []
        for val in musA.values():
            if len(val) > 1:
                for v in val:
                    slices.append(v) 
            else:
                for v in val:
                    uslices.append(v)

        slices = sorted(slices, key=lambda item: item[3][1] - item[3][0], reverse=True) #longest to shortest
        uslices = sorted(uslices, key=lambda item: item[3][1] - item[3][0], reverse=True)

        longest_slices = []
        for slise in slices:
            if subset_of(longest_slices, slise) or part_of(longest_slices, slise):
                continue
            else:
                longest_slices.append(slise)
        for slise in uslices:
            if subset_of(longest_slices, slise) or part_of(longest_slices, slise):
                continue
            else:
                longest_slices.append(slise)
        

        for sli in longest_slices:
            aDicio[(tuple(musD[sli[1]][sli[2]]['intDia'][sli[3][0]:sli[3][1]]),tuple(musD[sli[1]][sli[2]]['duracao'][sli[3][0]:sli[3][1]]))].append(sli)
    aDicio = dict(sorted(((k, v) for k, v in aDicio.items() if len(v) > 1), key=lambda x: (len(x[0]), len(x[1])), reverse=True))
    return aDicio

def segdur2(caminhosdict):
    '''seguimento de intervalo e durações únicos que repetem pelo menos uma vez, contidos e amontoados retirados e somente os que continuam repetindo ficam, janela de analise colocada a mão em 133'''
    aDicio = defaultdict(list)
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        print(f'analisando {nome}, ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
    
        for parte in musD:
            for voz, caracteristicas in musD[parte].items():
                if 'intDia' in caracteristicas:
                    p1 = 0
                    while p1 < len(caracteristicas['intDia']):
                        p2 = p1+1
                        while p2-p1 <= 133 and p2 <= len(caracteristicas['intDia']):
                            aDicio[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]))].append((nome, parte, voz, (p1, p2),(caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1])))
                            p2 += 1
                        p1 += 1
    print(len(aDicio))
    aDicio = sorted([(k, v) for k, v in aDicio.items() if len(v) > 1], key=lambda x: (len(x[0][0]), len(x[1])), reverse=True)
    print(len(aDicio))
    semconteamont = []
    for seg, pos in aDicio:
        posp = []
        for loc in pos:
            if not subset_of(semconteamont, loc) and not part_of(semconteamont, loc):
                posp.append(loc)
        if len(posp) > 1:
            semconteamont.append((seg,posp))
    print(len(aDicio))
    return {x:y for x,y in semconteamont}

def tamanho_seg(caminhosdict, n=1, t1=0):
    print(n)
    t2 = len(segdur2(caminhosdict))
    if t2 == t1:
        print(n-1)
        return n-1
    else:
        tamanho_seg(caminhosdict, n=n+1, t1=t2)