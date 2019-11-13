from dirEinp import dirEinp as f_d

def segmentacao(caracteristicas):

    #funcoes de input de parametros para a segmentação
    def segmentosPar_(caracteristicas, parametros):
        sc = f_d.inp('caracteristicas para segmentos:', (caracteristicas))
        st = f_d.inp('modos de segmentar:', ('p1','p1p2','p2m1','p1p2set','p2m1set'))
        parametros['segmentosPar'].append((sc,st))
        op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
        if op == 'confirmar':
            op = f_d.inp('adicionar outra caracteristica para segmentos?', ('s','n'))
            if op == 's':
                return segmentosPar_(caracteristicas, parametros)
            if op == 'n':
                return parametros
        if op == 'repetir':
            parametros['segmentosPar'].pop()
            return segmentosPar_(caracteristicas, parametros)
    def posicoesPar_(caracteristicas, parametros):
        sc = f_d.inp('caracteristicas para posicoes:', (caracteristicas))
        st = f_d.inp('modos de segmentar:', ('p1','p1p2','p2m1','p1p2set','p2m1set'))
        parametros['posicoesPar'].append((sc, st))
        op = f_d.inp('usar para filtros?', ('s', 'n'))
        if op == 's':
            ft = f_d.inp('modos de segmentar para filtrar:', ('p1f,','p1p2f','p2m1f'))
            parametros['posicoesPar'].append((sc, ft))
        op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
        if op == 'confirmar':
            op = f_d.inp('adicionar outra caracteristica para posicoes?', ('s','n'))
            if op == 's':
                return posicoesPar_(caracteristicas, parametros)
            if op == 'n':
                return parametros
        if op == 'repetir':
            parametros['posicoesPar'].pop()
            return posicoesPar_(caracteristicas, parametros)

    #montando parametros
    parametros = {'segmentosPar': [], 'posicoesPar': []}
    parametros = segmentosPar_(caracteristicas, parametros)
    op = f_d.inp('adicionar caracteristicas para posicoes?', ('s','n'))
    if op == 's':
        parametros = posicoesPar_(caracteristicas, parametros)

    def funcao_(mDict, aDict):
        musica = mDict.copy()
        nome = musica.pop('nome')
        for parte, caracteristicas in musica.items():
            for p1 in range(len(caracteristicas['grau'])):
                print(nome, parte, round((p1*100)/len(caracteristicas['grau'])+0.5),'%   ', end='\r')
                for p2 in range(p1+1,len(caracteristicas['grau'])):
                    keyAnalise = []
                    posicao = (nome, parte, (p1,p2))
                    valueAnalise = [posicao]
                    for segmentoPar in parametros['segmentosPar']:
                        segmentop1 = caracteristicas[segmentoPar[0]][p1]
                        segmentop1p2 = tuple(caracteristicas[segmentoPar[0]][p1:p2])
                        segmentop2m1 = tuple(caracteristicas[segmentoPar[0]][p1:p2-1])
                        if segmentoPar[1] == 'p1':
                            keyAnalise.append(segmentop1)
                        elif segmentoPar[1] =='p1p2':
                            keyAnalise.append(segmentop1p2)
                        elif segmentoPar[1] == 'p2m1':
                            keyAnalise.append(segmentop2m1)
                        elif segmentoPar[1] == 'p1p2set':
                            keyAnalise.append(set(segmentop1p2))
                        elif segmentoPar[1] == 'p2m1set':
                            keyAnalise.append(set(segmentop2m1))
                    if isinstance(keyAnalise, tuple) == False:
                        keyAnalise = tuple(keyAnalise)
                    aDict.setdefault(keyAnalise, [{'nome': set()}])[0]['nome'].add(nome)
                    aDict[keyAnalise][0].setdefault('posicao', set()).add(posicao)
                    for posicaoPar in parametros['posicoesPar']:
                        if posicaoPar != []:
                            posicaop1 = caracteristicas[posicaoPar[0]][p1]
                            posicaop1p2 = tuple(caracteristicas[posicaoPar[0]][p1:p2])
                            posicaop2m1 = tuple(caracteristicas[posicaoPar[0]][p1:p2-1])
                            if posicaoPar[1] == 'p1':
                                valueAnalise.append(posicaop1)
                            elif posicaoPar[1] == 'p1p2':
                                valueAnalise.append(posicaop1p2)
                            elif posicaoPar[1] == 'p2m1':
                                valueAnalise.append(posicaop2m1)
                            elif posicaoPar[1] == 'p1p2set':
                                valueAnalise.append(set(posicaop1p2))
                            elif posicaoPar[1] == 'p2m1set':
                                valueAnalise.append(set(posicaop2m1))
                            elif posicaoPar[1] == 'p1f':
                                aDict[keyAnalise][0].setdefault(posicaoPar[0], set()).add(posicaop1)
                            elif posicaoPar[1] == 'p1p2f':
                                for a in posicaop1p2:
                                    aDict[keyAnalise][0].setdefault(posicaoPar[0], set()).add(a)
                            elif posicaoPar[1] == 'p2m1f':
                                for a in posicaop2m1:
                                    aDict[keyAnalise][0].setdefault(posicaoPar[0], set()).add(a)
                        aDict[keyAnalise].append(valueAnalise)
        return aDict
    return (funcao_, parametros)