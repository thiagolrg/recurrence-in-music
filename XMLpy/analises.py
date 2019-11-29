from collections import defaultdict
import dirEinp as f_d

def segdur(caminhosdict):
    '''
    seguimento de intervalo e durações únicos que repetem pelo menos uma vez,
    sem contidos e amontoados
    '''
    aDicio = defaultdict(list)
    for caminho in caminhosdict:
        print('analisando, ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
        musD = f_d.le_pickle(caminho)
        musA = defaultdict(list)
        nome = musD.pop('nome')
        for parte in musD:
            for voz in parte:
                for p1 in range(len(voz['grau'])):
                    for p2 in range(p1 + 1, len(voz['grau']) + 1):
                        musA[tuple(tuple(voz['intDia'][p1:p2]),tuple(voz['dur'][p1:p2]))].append([tuple(nome, parte, voz, (p1, p2)), [voz['Ncompasso'], voz['Pcompasso']]])

        slices = []
        uslices = []
        for val in musA.values():
            for v in val:
                if len(val) > 1:
                    slices.append(val)
                else:
                    uslices.append(val)

        slices = sorted(slices, key=lambda item: item[1] - item[0], reverse=True) #longest to shortest
        slices = sorted(slices, key=lambda item: item[0]) #imitial number small to big inside the longest to shortest

        def subset_of(longest_slices, slise):
            return any(slise[0] >= ls[0] and slise[1] <= ls[1] for ls in longest_slices)

        def part_of(longest_slices, slise):
            return any(slise[0] > ls[0] and slise[0] <= ls[1] and slise[1] > ls[1] for ls in longest_slices)

        longest_slices = []
        for slise in slices:
            if not subset_of(longest_slices, slise) or part_of(longest_slices, slise):
                longest_slices.append(slise)

        for v in uslices:
            longest_slices.append(v)

        #for sli in longest_slices:
            #aDicio[tuple(seq[sli[0]:sli[1]])].append(sli)
    aDicio = dict(sorted(((k, v) for k, v in aDicio.items() if len(v) > 1), key=lambda x: (len(x[0]), len(x[1])), reverse=True))
    return aDicio