import f_diretorios as f_d

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

def interdurunicos_loc(mapamus, arquivoanalise):
    import pickle
    try:
        with open(arquivoanalise, 'rb') as arquivo:
            analise = pickle.loads(arquivo.read())
    except FileNotFoundError:
        analise = {}
    for v, voz in mapamus['vozes'].items():
        for posicao1 in range(len(voz['inte'])):
            for posicao2 in range(posicao1, len(voz['inte'])):
                inteseg = tuple(voz['inte'][posicao1:posicao2+1])
                durseg = tuple(voz['dur'][posicao1:posicao2+1])
                intedurseg = (inteseg, durseg)
                locC = voz['locC'][posicao1]
                locT = voz['locT'][posicao1]
                tamanho = ((posicao2 + 1) - posicao1)
                valor = (mapamus['nome'], v, locC, locT, tamanho)

                analise.setdefault(intedurseg, []).append(valor)
    f_d.grava_arquivo(arquivoanalise, analise, 'w+b')
    return (arquivoanalise+' atualizado')

def filtro_maisde1musica(arquivo):
    arquivopronto = {}
    for chave, valor in sorted(arquivo.items(), key=sort_tamanhoSI, reverse=True):
        musicas = set()
        if len(valor) > 1:
            for v in valor:
                musicas.add(v[0])
            if len(musicas) > 1:
                arquivopronto.setdefault(chave,valor)
    return arquivopronto    

'''                musica.setdefault((v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1), 
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
