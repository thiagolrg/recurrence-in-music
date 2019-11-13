import dirEinp.dirEinp as f_d
def filtro_quantidade(parametrosanalises):
    def filtroPar(parametrosanalises, parametros):
        opcoes = [x[0] for x in parametrosanalises['segmentacao'][1]['posicoesPar'] if x[2] == True]
        opcoes.append('nome')
        opcoes.append('posicoes')
        caracteristica = f_d.inp('por qual caracteristica filtrar?', opcoes)
        quantidade = input('que ocorrem pelo menos _ vezes: ')
        print( )
        parametros.setdefault(caracteristica, quantidade)
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
            for caracteristica, quantidade in parametros.items():
                if len(posicoes[0][caracteristica]) >= quantidade:
                    continue
                else:
                    f = False
                    break
            if f == True:
                filtrado.setdefault(segmento,posicoes)
        return filtrado
    return (funcao_, parametros)

    
    #({caracteristica: valores}, op)
    # onde op == inclusivo ou exclusivo
    '''
    inclusivo qualquer:
    passa se qualquer um dos valores existir nas caracteristicas do total de localizacoes do segmento
    as caracteristicas do segmento podem ter outros valores diferentes do filtro

    inclusivo todos:
    passa se todos os valores existires nas caracteristicas do total de localizacoes do segmento
    as caracteristicas do segmento podem ter outros valores diferentes do filtro

    exclusivo qualquer:
    passa se qualquer valor existir nas caracteristicas do total de localizacoes do segmento
    as caracteristicas do segmento só podem conter valores do filtro

    exclusica qualquer:
    passa se todos os valores existires nas caracteristicas do total de localizacoes do segmento
    as caracteristicas do segmento só podem conter valores do filtro
    '''
def filtro_tipo(parametrosanalises):
    def filtroPar(parametrosanalises, parametros):
        opcoes = [x[0] for x in parametrosanalises['segmentacao'][1]['posicoesPar'] if x[2] == True]
        opcoes.append('nome')
        opcoes.append('posicoes')
        caracteristica = f_d.inp('por qual caracteristica filtrar?', opcoes)
        valores = input('que contenha quais valores? ')
        tipo = f_d.inp('como filtrar?', ['inclusivo qualquer','inclusivo todos','exclusivo qualquer','exclusivo todos'])
        print( )
        parametros.append(({caracteristica: valores}, tipo))
        op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
        if op == 'confirmar':
            op = f_d.inp('adicionar outra caracteristica ao filtro_quantidade?', ('s','n'))
            if op == 's':
                return filtroPar(parametrosanalises, parametros)
            if op == 'n':
                return parametros
        if op == 'repetir':
            parametros.pop()
            return filtroPar(parametrosanalises, parametros)
    parametros = filtroPar(parametrosanalises, [])

    def funcao_(aDicio):
        filtrado = {}
        for segmento, localizacoes in aDicio.items():
            for valorf in valoresf:
                for caracteristica, valoresf in parametros[0].items():
                    if parametros[1] == 'inclusivo qualquer': 
                        if any((True for valorf in valoresf if valorf in localizacoes[0][caracteristica])):
                            continue
                        else:
                            break
                    elif parametros[1] == 'inclusivo todos': 
                        if all((True for valorf in valoresf if valorf in localizacoes[0][caracteristica])):
                            continue
                        else:
                            break
                    elif parametros[1] == 'exclusivo qualquer':
                        if all((True for valorseg in localizacoes[0][caracteristica] if valorseg in valoresf)):
                            continue
                        else:
                            break
                    elif parametros[1] == 'exclusivo todos':
                        if all((True for valorf in valoresf if valorf in localizacoes[0][caracteristica])) and all((True for valorseg in localizacoes[0][caracteristica] if valorseg in valoresf)):
                            continue
                        else:
                            break
                    else:
                        break
            filtrado.setdefault(segmento, localizacoes)
        return filtrado
    return (funcao_, parametros)


def filtro_contidos():
    op = f_d.inp('o que fazer com os contidos?', ('marcar','retirar vazios'))
    def funcao_(aDicio):
        for segmento1, localizacoes1 in (aDicio.copy()).items():
            contido = False
            for segmento2, localizacoes2 in (aDicio.copy()).items():
                for localizacao1 in localizacoes1:
                    for localizacao2 in localizacoes2:
                        if localizacao2[0:2] != localizacao1[0:2]:
                            continue
                        if localizacao2[2][0] >= localizacao1[2][0] and localizacao2[2][1] <= localizacao2[2][1]:
                            aDicio[segmento2].pop(aDicio[segmento2].index(localizacao2)) 
                            contido = True
            if contido == True:
                if op == 'marcar':
                    aDicio[segmento2].insert(0, segmento1)
                elif op == 'retirar vazios' and aDicio[segmento2] == []:
                    aDicio.pop(segmento2)
        return aDicio
    return (funcao_, op)

def filtro_amontoados():
    op = f_d.inp('o que fazer com os amontados?', ('marcar segundo','retirar vazios'))
    def funcao_(aDicio):
        for segmento1, localizacoes1 in (aDicio.copy()).items():
            amontado = False
            for segmento2, localizacoes2 in (aDicio.copy()).items():
                for localizacao1 in localizacoes1:
                    for localizacao2 in localizacoes2:
                        if localizacao2[0:2] != localizacao1[0:2]:
                            continue
                        if localizacao2[2][0] <= localizacao1[2][1] and localizacao2[2][1] > localizacao1[2][1]:
                            aDicio[segmento2].pop(aDicio[segmento2].index(localizacao2)) 
                            amontado = True
            if amontado == True:
                if op == 'marcar segundo':
                    aDicio[segmento2].insert(0, segmento1)
                elif op == 'retirar vazios' and aDicio[segmento2] == []:
                    aDicio.pop(segmento2)
        return aDicio
    return (funcao_, op)