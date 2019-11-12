import dirinp as f_d

def segmentacao(caracteristicas,tipos):

    #funcoes de input de parametros para a segmentação
    def segmentosPar_(caracteristicas, tipos, parametros):
        sc = f_d.inp('caracteristicas para segmentos:', (caracteristicas))
        st = f_d.inp('modos de segmentar:', (tipos))
        parametros['segmentosPar'].append((sc,st))
        op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
        if op == 'confirmar':
            op = f_d.inp('adicionar outra caracteristica para segmentos?', ('s','n'))
            if op == 's':
                return segmentosPar_(caracteristicas, tipos, parametros)
            if op == 'n':
                return parametros
        if op == 'repetir':
            parametros['segmentosPar'].pop()
            return segmentosPar_(caracteristicas, tipos, parametros)
    def posicoesPar_(caracteristicas, tipos, parametros):
        sc = f_d.inp('caracteristicas para posicoes:', (caracteristicas))
        st = f_d.inp('modos de segmentar:', (tipos))
        op = f_d.inp('usar para filtros?', ('s', 'n'))
        if op == 's':
            filtro = True
        elif op == 'n':
            filtro = False
        parametros['posicoesPar'].append((sc, st, filtro))
        op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
        if op == 'confirmar':
            op = f_d.inp('adicionar outra caracteristica para posicoes?', ('s','n'))
            if op == 's':
                return posicoesPar_(caracteristicas, tipos, parametros)
            if op == 'n':
                return parametros
        if op == 'repetir':
            parametros['posicoesPar'].pop()
            return posicoesPar_(caracteristicas, tipos, parametros)

    #montando parametros
    parametros = {'segmentosPar': [], 'posicoesPar': []}
    parametros = segmentosPar_(caracteristicas, tipos, parametros)
    op = f_d.inp('adicionar caracteristicas para posicoes?', ('s','n'))
    if op == 's':
        parametros = posicoesPar_(caracteristicas, tipos, parametros)

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

def sort_tamKquanV(entrada):
    pronto = {}
    for chave, valor in sorted(entrada.items(), key=lambda item: (len(item[0][0]), len(item[1])), reverse=True):
        pronto.setdefault(chave, valor[1:])
    return pronto

#acontecem >= que tantas vezes
#filtro ex:{'nome',1}
def filtro_quantidade(parametrosanalises):
    def filtroPar(parametrosanalises, parametros):
        opcoes = [x[0] for x in parametrosanalises['segmentacao'][1]['posicoesPar'] if x[2] == True]
        opcoes.append('nome')
        opcoes.append('posicoes')
        c = f_d.inp('por qual caracteristica filtrar', opcoes)
        q = input('que ocorrem pelo menos _ vezes: ')
        print( )
        parametros.setdefault(c,q)
        op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
        if op == 'confirmar':
            op = f_d.inp('adicionar outra caracteristica ao filtro_quantidade?', ('s','n'))
            if op == 's':
                return filtroPar(parametrosanalises, parametros)
            if op == 'n':
                return parametros
        if op == 'repetir':
            parametros['filtroQT'].pop()
            return filtroPar(parametrosanalises, parametros)
    
    parametros = filtroPar(parametrosanalises, {})

    def funcao_(aDict):
        filtrado = {}
        for segmento, posicoes in aDict.items():
            f = True
            for cf, vf in parametros.items():
                if len(posicoes[0][cf]) >= vf:
                    continue
                else:
                    f = False
                    break
            if f == True:
                filtrado.setdefault(segmento,posicoes)
        return filtrado
    return (funcao_, parametros)

'''
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
'''