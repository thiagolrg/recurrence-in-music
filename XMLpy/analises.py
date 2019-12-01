from collections import defaultdict
import dirEinp as f_d

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
                            musA[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]))].append((nome, parte, voz, (p1, p2), (caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1])))
                            p2 += 1

        def subset_of(longest_slices, slise):
            for ls in longest_slices:
                if slise[3][0] >= ls[3][0] and slise[3][1] <= ls[3][1] and slise[0:3] == ls[0:3]:
                    return True
            return False

        def part_of(longest_slices, slise):
            for ls in longest_slices:
                if slise[3][0] > ls[3][0] and slise[3][0] <= ls[3][1] and slise[3][1] > ls[3][1] and slise[0:3] == ls[0:3]:
                    return True
            return False

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
        uslices = sorted(slices, key=lambda item: item[3][1] - item[3][0], reverse=True)

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
            intdia = musD[sli[1]][sli[2]]['intDia'][sli[3][0]:sli[3][1]]
            duracao = musD[sli[1]][sli[2]]['duracao'][sli[3][0]:sli[3][1]]
            aDicio[(tuple(musD[sli[1]][sli[2]]['intDia'][sli[3][0]:sli[3][1]]),tuple(musD[sli[1]][sli[2]]['duracao'][sli[3][0]:sli[3][1]]))].append(sli)
        n = 0
        for key, value in aDicio.items():
            if len(value) == 1:
                n += 1
                debug = 0
        debug = 0
    aDicio = dict(sorted(((k, v) for k, v in aDicio.items() if len(v) > 1), key=lambda x: (len(x[0]), len(x[1])), reverse=True))
    return aDicio