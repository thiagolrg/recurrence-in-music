def segmentacao_(keys, atribs, mDict, aDict, tudo=False):
    musica = mDict.copy()
    nome = musica.pop('nome')
    for part, atribsP in musica.items():
        if tudo == True:
            atribs = [key for key in atribsP.keys()]
            for key in keys:
                atribs.pop(atribs.index(key))
            abribs = [(x, 'p1p2') for x in abribs]
        for p1 in range(len(atribsP['grau'])):
            print(nome, part, round((p1*100)/len(atribsP['grau'])+0.5),'%   ', end='\r')
            for p2 in range(p1+1,len(atribsP['grau'])):
                keyAnalise = []
                posicao = (nome, part, (p1,p2))
                valueAnalise = [posicao]
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
                    elif key[1] == 'p1p2set':
                        keyAnalise.append(set(keyp1p2))
                    elif key[1] == 'p2m1set':
                        keyAnalise.append(set(keyp1p2m1))
                if isinstance(keyAnalise, tuple) == False:
                    keyAnalise = tuple(keyAnalise)
                aDict.setdefault(keyAnalise, [{'nome': set()}])[0]['nome'].add(nome)
                aDict[keyAnalise][0].setdefault('posicao', set()).add(posicao)
                for atrib in atribs:
                    atribp1 = atribsP[atrib[0]][p1]
                    atribp1p2 = tuple(atribsP[atrib[0]][p1:p2])
                    atribp2m1 = tuple(atribsP[atrib[0]][p1:p2-1])
                    if atrib[1] == 'p1':
                        valueAnalise.append(atribp1)
                    elif atrib[1] == 'p1p2':
                        valueAnalise.append(atribp1p2)
                    elif atrib[1] == 'p2m1':
                        valueAnalise.append(atribp2m1)
                    elif atrib[1] == 'p1p2set':
                        valueAnalise.append(set(atribp1p2))
                    elif atrib[1] == 'p2m1set':
                        valueAnalise.append(set(atribp2m1))
                    elif atrib[1] == 'p1f':
                        aDict[keyAnalise][0].setdefault(atrib[0], set()).add(atribp1)
                    elif atrib[1] == 'p1p2f':
                        for a in atribp1p2:
                            aDict[keyAnalise][0].setdefault(atrib[0], set()).add(a)
                    elif atrib[1] == 'p2m1f':
                        for a in atribp2m1:
                            aDict[keyAnalise][0].setdefault(atrib[0], set()).add(a)
                aDict[keyAnalise].append(valueAnalise)
    return aDict

#acontecem >= que tantas vezes
#filtro ex:{'nome',1}
def filtro_quantidade(aDict, filtro):
    if filtro == {None}:
        return aDict
    filtrado = {}
    for chave, valor in aDict.items():
        f = True
        for cf, vf in filtro.items():
            if len(valor[0][cf]) >= vf:
                continue
            else:
                f = False
                break
        if f == True:
            filtrado.setdefault(chave,valor)
    print('filtro QT ok')
    return filtrado
#acontecem também nessas (explusivamente ou não)
#filtro ex:[{'nome': ['k341','k363']}, False]
def filtro_contém(aDict, filtro):
    if filtro == {None}:
        return aDict
    filtrado = {}
    if filtro[1] == False:
        for chave, valor in aDict.items():
            f = True
            for cf, vf in filtro[0].items():
                for vf in filtro[0][cf]:
                    if vf in valor[0][cf]:
                        continue
                    else:
                        f = False
                        break
            if f == True:
                filtrado.setdefault(chave,valor)
        print('filtro TP ok')
        return filtrado
    elif filtro[1] == True:
        for chave, valor in aDict.items():
            f = True
            for cf, vf in filtro[0].items():
                for vset in valor[0][cf]:
                    if vset in vf:
                        continue
                    else:
                        f = False
                        break
            if f == True:
                filtrado.setdefault(chave,valor)
        print('filtro TP ok')
        return filtrado

def lista_in(menor, maior):
    for posicao in range(len(maior[0])):
        t1 = maior[0][posicao:(posicao+len(menor[0]))]
        t2 = maior[1][posicao:(posicao+len(menor[1]))]
        if t1 == menor[0] and t2 == menor[1]:
            return True
    return False
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
                        if valores2[p][0][2][0] >= valor1[0][2][0] and valores2[p][0][2][1] <= valor1[0][2][1] and valores2[p][0][0:2] == valor1[0][0:2]:
                            entrada[chave2].pop(entrada[chave2].index(valores2[p]))
                            a = 1
                        p += 1
                if a == 1  and valores2 == []:
                    entrada.pop(chave2)
                elif a == 1 and len(set([x[0] for x in valores2])) == 1:
                    entrada.pop(chave2)
    print('filtro_nested ok')
    return entrada

def sort_tamKquanV(entrada):
    pronto = {}
    for chave, valor in sorted(entrada.items(), key=lambda item: (len(item[0][0]), len(item[1])), reverse=True):
        pronto.setdefault(chave, valor[1:])
    return pronto