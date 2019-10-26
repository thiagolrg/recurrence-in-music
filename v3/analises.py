import diretorios as f_d

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
    print(nomemapamus+' analisado por interdurunicos_loc')
    return (interdurunicoloc)

def interdurunicos_maisoumenos_loc(interdurunicoloc, mapamus, nomemapamus):
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

                for seginte in interdurunicoloc.keys():
                    if len(seginte[0]) == len(inteseg):
                        maisoumenos = mais_ou_menos(inteseg, seginte[0])
                        if maisoumenos == False:
                            continue
                        elif maisoumenos != 0 and seginte[1] == durseg:
                            valor = (mapamus['nome'], v, locC, locT, tamanho, locA, maisoumenos)
                            interdurunicoloc[seginte].append(valor)
                
                interdurunicoloc.setdefault(intedurseg, []).append(valor)
                if type(interdurunicoloc[intedurseg][0]) != dict:
                    interdurunicoloc[intedurseg].insert(0 ,{'name' : set()})
                interdurunicoloc[intedurseg][0]['name'].add(mapamus['nome'])
    print(nomemapamus+' analisado por interdurunicos_loc')
    return (interdurunicoloc)

def mais_ou_menos(seginte1, seginte2):
    i = 0
    for p in range(len(seginte1)):
        if seginte1[p] == seginte2[p]:
            continue
        elif seginte1[p] + 1 == seginte2[p] or seginte1[p] - 1 == seginte2[p]:
            i = i + 1
        else:
            return False
    return i


def filtro_maisde1musica(entrada):
    pronto = {}
    for chave, valor in entrada.items():
        if len(valor[0]['name']) > 1:
            pronto.setdefault(chave,valor[1:])
    print('filtro_maisde1musica ok')
    return pronto

def sort_tamSIquanLOC(entrada):
    pronto = {}
    for chave, valor in sorted(entrada.items(), key=lambda item: (len(item[0][0]), len(item[1])), reverse=True):
        pronto.setdefault(chave, valor)
    print('sort_tamSIquanLOC ok')
    return pronto

def nested_identificados(entrada):
    for chave1, valores1 in (entrada.copy()).items():
        if 'caso 1' in valores1[0][0]:
            continue 
        for chave2, valores2 in (entrada.copy()).items():
            if len(chave2[0]) < len(chave1[0]) and lista_in(chave2, chave1) == True:
                a=0
                for valor1 in valores1:
                    if 'caso' in valor1[0]:
                        continue
                    p=0
                    while p < len(valores2):
                        if 'caso' in valores2[p][0]:
                            p += 1
                            continue
                        if valores2[p][5][0] >= valor1[5][0] and valores2[p][5][1] <= valor1[5][1] and valores2[p][0:2] == valor1[0:2]:
                            entrada[chave2].pop(entrada[chave2].index(valores2[p]))
                            a = 1
                        p += 1
                p = 0
                while p < len(valores2):
                    if 'caso' in valores2[p][0]:
                        p += 1
                    else:
                        break
                if a == 1  and p == len(valores2):
                    entrada.setdefault(chave2).insert(0, ('caso 1', chave1))
                    continue
                if a == 1 and len(set([x[0] for x in valores2[p:]])) == 1:
                    entrada.setdefault(chave2).insert(0, ('caso 2', chave1))
                    continue
                if a == 1:
                    entrada.setdefault(chave2).insert(0, ('caso 3', chave1))
                    continue
    print('nested_identificados ok')
    return entrada

def filtro_nested(entrada):
    for chave1, valores1 in (entrada.copy()).items():
        if valores1 == []:
            continue 
        for chave2, valores2 in (entrada.copy()).items():
            if len(chave2[0]) < len(chave1[0]) and lista_in(chave2, chave1) == True:
                a=0
                for valor1 in valores1:
                    p=0
                    while p < len(valores2):
                        if valores2[p][5][0] >= valor1[5][0] and valores2[p][5][1] <= valor1[5][1] and valores2[p][0:2] == valor1[0:2]:
                            entrada[chave2].pop(entrada[chave2].index(valores2[p]))
                            a = 1
                        p += 1
                if a == 1  and valores2 == []:
                    entrada.pop(chave2)
                elif a == 1 and len(set([x[0] for x in valores2])) == 1:
                    entrada.pop(chave2)
    print('filtro_nested ok')
    return entrada

def limpa_posicoes(entrada):
    for chave, valores in entrada.items():
        valoreslimpos = [valor[:-1] for valor in valores]
        entrada.setdefault(chave, valoreslimpos)
    print('limpa_posicoes ok')
    return entrada

def lista_in(menor, maior):
    for posicao in range(len(maior[0])):
        t1 = maior[0][posicao:(posicao+len(menor[0]))]
        t2 = maior[1][posicao:(posicao+len(menor[1]))]
        if t1 == menor[0] and t2 == menor[1]:
            return True
    return False

'''
def sort_tamanhoSI(item):
    return len(item[0][0])

def sort_quantidadeLOC(item):
    return len(item[1])  
                
def interunicos_loc(mapamus):
    interunicosloc = 
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
