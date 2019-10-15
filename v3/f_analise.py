import f_diretorios as f_d

def interdurunicos_loc(interdurunicoloc, mapamus, nomemapamus):
    for v, voz in mapamus['vozes'].items():
        for posicao1 in range(len(voz['inte'])):
            for posicao2 in range(posicao1, len(voz['inte'])):
                locA = (posicao1, posicao2+1)
                inteseg = tuple(voz['inte'][posicao1:posicao2+1])
                durseg = tuple(voz['dur'][posicao1:posicao2+1])
                intedurseg = (inteseg, durseg)
                locC = voz['locC'][posicao1]
                locT = voz['locT'][posicao1]
                tamanho = ((posicao2 + 1) - posicao1)
                valor = (mapamus['nome'], v, locC, locT, tamanho, locA)

                interdurunicoloc.setdefault(intedurseg, []).append(valor)
                if type(interdurunicoloc[intedurseg][0]) != dict:
                    interdurunicoloc[intedurseg].insert(0 ,{'name' : set()})
                interdurunicoloc[intedurseg][0]['name'].add(mapamus['nome'])
    print(nomemapamus+' analisado')
    return (interdurunicoloc)

def filtro_maisde1musica(dicio):
    pronto = {}
    for chave, valor in sorted(dicio.items(), key=sort_tamanhoSI, reverse=True):
        if len(valor[0]['name']) > 1:
            pronto.setdefault(chave,valor[1:])

    for chave1, valores1 in (pronto.copy()).items():
        for chave2, valores2 in (pronto.copy()).items():
            if len(chave2[0]) < len(chave1[0]) and str(chave2[0]).strip('()') in str(chave1[0]) and str(chave2[1]).strip('()') in str(chave1[1]):
                a=0
                for valor1 in valores1:
                    p=0
                    while p < len(valores2):
                        if valores2[p][5][0] >= valor1[5][0] and valores2[p][5][1] <= valor1[5][1] and valores2[p][0:2] == valor1[0:2]:
                            pronto[chave2].pop(pronto[chave2].index(valores2[p]))
                            a = 1
                        p += 1
                if a == 1  and valores2 == []:
                    pronto.pop(chave2)
                elif a == 1 and len(set([x[0] for x in valores2])) == 1:
                    pronto.pop(chave2)
    print('filtro_maisde1musica ok')
    return pronto  

def sort_tamanhoSI(item):
    return len(item[0][0])

def sort_quantidadeLOC(item):
    return len(item[1])  

'''                
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
