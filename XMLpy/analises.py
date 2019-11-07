def analise(keys, atribs, mDict, aDict, tudo=False):
    musica = mDict.copy()
    nome = musica.pop('nome')
    for part, atribsP in musica.items():
        if tudo == True:
            atribs = [key for key in atribsP.keys()]
            for key in keys:
                atribs.pop(atribs.index(key))
            abribs = [(x, 'p1p2') for x in abribs]
        for p1 in range(len(atribsP['grau'])):
            for p2 in range(p1+1,len(atribsP['grau'])):
                keyAnalise = []
                valueAnalise = [(nome, part, (p1,p2))]
                for key in keys:
                    keyp1 = atribsP[key[0]][p1]
                    keyp1p2 = tuple(atribsP[key[0]][p1:p2])
                    keyp1p2m1 = tuple(atribsP[key[0]][p1:p2-1])
                    if key[1] == 'p1':
                        keyAnalise.append(keyp1)
                    elif key[1] =='p1p2':
                        keyAnalise.append(keyp1p2)
                    elif key[1] == 'p2m1':
                        keyAnalise.append(keyp1p2m1)
                    elif key[1] == 'p1set':
                        keyAnalise.append(set(keyp1))
                    elif key[1] == 'p1p2set':
                        keyAnalise.append(set(keyp1p2))
                    elif key[1] == 'p2m1set':
                        keyAnalise.append(set(keyp1p2m1))
                if isinstance(keyAnalise, tuple) == False:
                    keyAnalise = tuple(keyAnalise)
                aDict.setdefault(keyAnalise, [{'nome': set()}])[0]['nome'].add(nome)
                for atrib in atribs:
                    atribp1 = atribsP[atrib[0]][p1]
                    atribp1p2 = tuple(atribsP[atrib[0]][p1:p2])
                    atribp2m1 = tuple(atribsP[atrib[0]][p1:p2-1])
                    if atrib[1] == 'p1':
                        valueAnalise.append(atribp1)
                    elif atrib[1] == 'p1p2':
                        valueAnalise.append(atribp1p2)
                    elif atrib[1] == 'p1p2m1':
                        valueAnalise.append(atribp2m1)
                    elif atrib[1] == 'p1set':
                        valueAnalise.append(set(atribp1))
                    elif atrib[1] == 'p1p2set':
                        valueAnalise.append(set(atribp1p2))
                    elif atrib[1] == 'p2m1set':
                        valueAnalise.append(set(atribp2m1))
                    elif atrib[1] == 'p1setg':
                        aDict[keyAnalise][0].setdefault(atrib[0], set()).add(atribp1)
                    elif atrib[1] == 'p1p2setg':
                        aDict[keyAnalise][0].setdefault(atrib[0], set()).add(atribp1p2)
                    elif atrib[1] == 'p2m1setg':
                        aDict[keyAnalise][0].setdefault(atrib[0], set()).add(atribp2m1)
    return aDict

def filtro_quantidade(aDict, atribslen):
    filtrado = {}
    for chave, valor in aDict.items():
        for atriblen in atribslen:
            if len(valor[0][atriblen[0]]) > atriblen[1]:
                filtrado.setdefault(chave,valor[1:])
    return filtrado

def filtro_tipo(aDict, atribs):
    filtrado = {}
    for chave, valor in aDict.items():
        for atrib in atribs:
            if all(valor[0][atrib[0]]) == atrib[1]:
                filtrado.setdefault(chave,valor[1:])
    return filtrado

def sort_tamKquanV(entrada):
    pronto = {}
    for chave, valor in sorted(entrada.items(), key=lambda item: (len(item[0][0]), len(item[1])), reverse=True):
        pronto.setdefault(chave, valor)
    return pronto