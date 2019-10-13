def interunicos_loc(mapamus):
    interunicosloc = {}
    v = 0
    for locCvoz, locTvoz, intevoz, durvoz, compvoz, bpmvoz in mapamus:
        v = v+1
        for posicao1 in range(len(intevoz)):
            for posicao2 in range(posicao1, len(intevoz)):
                if interunicosloc.get(tuple(intevoz[posicao1:posicao2+1])) == None: 
                    interunicosloc.setdefault(tuple(intevoz[posicao1:posicao2+1]),
                                    [(v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1)])
                else:
                     interunicosloc.setdefault(tuple(intevoz[posicao1:posicao2+1]),
                                    interunicosloc.get(tuple(intevoz[posicao1:posicao2+1])).append((v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1)))
    for chave, valor in sorted(interunicosloc.items(), key=sort_tamanhoSI, reverse=True):
        if len(valor) > 2 and valor[0][3] > 2:
            interunicosloc2.setdefault(chave,valor)
    return interunicosloc

def sort_tamanhoSI(item):
    return item[1][0][3]

def sort_quantidadeLOC(item):
    return len(item[1])

def interdurunicos_loc(mapamus):
    interdurunicosloc = {}
    interdurunicosloc2 = {}
    v = 0
    for v, voz in mapamus['vozes'].items():
        for posicao1 in range(len(voz['inte'])):
            for posicao2 in range(posicao1, len(voz['inte'])):
                interdurunicosloc.setdefault(
                    (tuple(voz['inte'][posicao1:posicao2+1]), tuple(voz['dur'][posicao1:posicao2+1])), []).append(
                    [(v, voz['locC'][posicao1], voz['locT'][posicao1], (posicao2+1)-posicao1)])
                    
               
    for chave, valor in sorted(interdurunicosloc.items(), key=sort_quantidadeLOC, reverse=True):
        if len(valor) > 1:
            interdurunicosloc2.setdefault(chave,valor)
    return interdurunicosloc2

'''         
                musica.setdefault((v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1), 
                                 (tuple(intevoz[posicao1:posicao2+1]),
                                 tuple(durvoz[posicao1:posicao2+1]),
                                 tuple(compvoz[posicao1:posicao2+1]),
                                 tuple(bpmvoz[posicao1:posicao2+1])))                    
                
                comppronto = []
                bpmpronto = []
                for valorcomp, valorbpm in zip(compvoz[posicao1:posicao2+1], bpmvoz[posicao1:posicao2+1]):
                    if valorcomp not in comppronto:
                        comppronto.append(valorcomp)
                    if valorbpm not in bpmpronto:
                        bpmpronto.append(valorbpm)

                finalcsv.append([nome, tom, modo,
                                (v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1),
                                tuple(intevoz[posicao1:posicao2+1]), tuple(durvoz[posicao1:posicao2+1]),
                                comppronto, bpmpronto])
    testet = teste.items()
    finaldic.setdefault(nome, musica)
    return (finalcsv, finaldic)
'''
