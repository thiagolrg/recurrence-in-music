import dirEinp as f_d

<<<<<<< HEAD
def filtroposicoes_quantidade(parametrosanalise, parametros=int()):
    def funcao_(aDicio):
        filtrado = {}
        for chave, valor in aDicio.items():
            if len(valor[1]) >= parametros:
                filtrado.setdefault(chave,valor)
        return filtrado
    if parametros == int():    
        parametros = f_d.quantidade_()
    return (funcao_,parametros)

def filtroposicoes_contidas(parametroanalise, parametros=str()):
    def Par():
        parametros = f_d.inp('o que fazer com os contidos?', ('marcar','retirar vazios'))
        op = f_d.inp(parametros, ('confirmar filtro_contidos', 'comecar novamente'))
        if op == 'confirmar filtro_contidos':
            return parametros
        if op == 'comecar novamente':
            return Par()
    
    if parametros == str():
        parametros = Par()

    def funcao_(aDicio):
        musica1 = aDicio.copy()
        for segmento1, localizacoes1 in musica1.items():
            contido = False
            for segmento2, localizacoes2 in aDicio.items():
                for localizacao1 in localizacoes1[1]:
                    for localizacao2 in localizacoes2[1]:
                        if localizacao2[0][0:2] != localizacao1[0][0:2]:
                            continue
                        if localizacao2[0][2][0] >= localizacao1[0][2][0] and localizacao2[0][2][1] <= localizacao1[0][2][1]:
                            aDicio[segmento2][1].pop(aDicio[segmento2][1].index(localizacao2)) 
                            contido = True
            if contido == True:
                if parametros == 'marcar':
                    aDicio[segmento2][0].setdefault('contido', segmento1)
                elif parametros == 'retirar vazios' and aDicio[segmento2][1] == []:
                    aDicio.pop(segmento2)
        return aDicio
    return (funcao_, parametros)

def filtroposicoes_amontoadas(parametroanalise, parametros=str()):
    def Par():
        parametros = f_d.inp('o que fazer com os amontados?', ('marcar segundo','retirar vazios'))
        op = f_d.inp(parametros, ('confirmar filtro_amontoados', 'comecar novamente'))
        if op == 'confirmar filtro_amontoados':
            return parametros
        if op == 'comecar novamente':
            return Par()
    if parametros == str():
        parametros = Par()

    def funcao_(aDicio):
        musica1 = aDicio.copy()
        for segmento1, localizacoes1 in musica1.items():
            amontado = False
            for segmento2, localizacoes2 in aDicio.items():
                for localizacao1 in localizacoes1[1]:
                    for localizacao2 in localizacoes2[1]:
                        if localizacao2[0][0:2] != localizacao1[0][0:2]:
                            continue
                        if localizacao2[0][2][0] <= localizacao1[0][2][1] and localizacao2[0][2][1] > localizacao1[0][2][1]:
                            aDicio[segmento2][1].pop(aDicio[segmento2][1].index(localizacao2)) 
                            amontado = True
            if amontado == True:
                if parametros == 'marcar segundo':
                    aDicio[segmento2][0].setdefault('amontoado', tuple([localizacao1[0][2][1]-localizacao2[0][2][0], segmento1]))
                elif parametros == 'retirar vazios' and aDicio[segmento2][1] == []:
                    aDicio.pop(segmento2)
        return aDicio
    return (funcao_, parametros)

def filtroset_quantidade(parametroanalise, parametros=dict()):
    def filtroPar(parametroanalise, parametros):
        opcoes = [x[0] for x in parametroanalise[0][1][1]['posicoesPar'] if 'f' in x[1]]
        opcoes.append('nome')
        opcoes.append('posicao')
        caracteristica = f_d.inp('por qual caracteristica filtrar?', opcoes)
        quantidade = f_d.quantidade_()
        print()
=======
def filtro_quantidade(parametroanalise):
    def filtroPar(parametroanalise, parametros):
        opcoes = [x[0] for x in parametroanalise['segmentacao'][1]['posicoesPar'] if 'f' in x[1]]
        opcoes.append('nome')
        opcoes.append('posicao')
        caracteristica = f_d.inp('por qual caracteristica filtrar?', opcoes)
        quantidade = input('que ocorrem pelo menos _ vezes: ')
        print( )
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
        parametros.setdefault(caracteristica, int(quantidade))
        op = f_d.inp(f'{parametros}', ('confirmar entrada', 'refazer entrada'))
        if op == 'confirmar entrada':
            op = f_d.inp('adicionar outra caracteristica ao filtro_quantidade?', ('s','n'))
            if op == 's':
                return filtroPar(parametroanalise, parametros)
            if op == 'n':
                return parametros
        if op == 'refazer entrada':
            parametros.pop(caracteristica)
            return filtroPar(parametroanalise, parametros)
    
    def Par(parametroanalise, parametros):
        parametros = filtroPar(parametroanalise, parametros)
        op = f_d.inp(f'{parametros}', ('confirmar filtro_quantidade', 'comecar novamente'))
        if op == 'confirmar filtro_quantidade':
            return parametros
        if op == 'comecar novamente':
            return Par(parametroanalise, {})
    parametros = Par(parametroanalise, {})

    def funcao_(aDicio):
        filtrado = {}
        for segmento, posicoes in aDicio.items():
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
<<<<<<< HEAD

def filtroset_tipo(parametroanalise, parametros=list()):
=======

    
    
'''
#({caracteristica: valores}, op)
# onde op == inclusivo ou exclusivo
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

def filtro_tipo(parametroanalise):
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
    def filtroPar(parametroanalise, parametros):
        opcoes = [x[0] for x in parametroanalise[0][1][1]['posicoesPar'] if 'f' in x[1]]
        opcoes.append('nome')
        opcoes.append('posicao')
        caracteristica = f_d.inp('por qual caracteristica filtrar?', opcoes)
<<<<<<< HEAD
        def valores_():
            valores = input('que contenha quais valores? ')
            try:
                valores = [float(v) for v in valores.split(',')]
            except ValueError:
                valores = [v.strip() for v in valores.split(',')]
            print((caracteristica, valores))
            op = f_d.inp('certifique-se que digitou valores correspondentes a caracteristica:', ('confirmar', 'repetir'))
            if op == 'confirmar':
                return valores
            if op == 'repetir':
                return valores_()
        valores = valores_()
        tipo = f_d.inp('como filtrar?', ('inclusivo qualquer','inclusivo todos','exclusivo qualquer','exclusivo todos'))
=======
        valores = input('que contenha quais valores? ')
        valores = [float(v) for v in valores.split(',')]
        tipo = f_d.inp('como filtrar?', ['inclusivo qualquer','inclusivo todos','exclusivo qualquer','exclusivo todos'])
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
        print( )
        parametros.append(({caracteristica: valores}, tipo))
        op = f_d.inp(f'{parametros}', ('confirmar entrada', 'refazer entrada'))
        if op == 'confirmar entrada':
            op = f_d.inp('adicionar outra caracteristica ao filtro_tipo?', ('s','n'))
            if op == 's':
                return filtroPar(parametroanalise, parametros)
            if op == 'n':
                return parametros
        if op == 'refazer entrada':
            parametros.pop()
            return filtroPar(parametroanalise, parametros)

    def Par(parametroanalise, parametros):
        parametros = filtroPar(parametroanalise, parametros)
        op = f_d.inp(f'{parametros}', ('confirmar filtro_tipo', 'comecar novamente'))
        if op == 'confirmar filtro_tipo':
            return parametros
        if op == 'comecar novamente':
            return Par(parametroanalise, [])
    parametros = Par(parametroanalise, [])

    def funcao_(aDicio):
        filtrado = {}
        for segmento, localizacoes in aDicio.items():
            filtro = True
            for parametro in parametros:
                for caracteristica, valoresf in parametro[0].items():
                    if parametro[1] == 'inclusivo qualquer': #True se qualquer valor no filtro estiver no set, podem ter valores no set que nao estao no filtro
                        if any(True if valorf in localizacoes[0][caracteristica] else False for valorf in valoresf):
                            continue
                        else:
                            filtro = False
                            break
                    elif parametro[1] == 'inclusivo todos': #True se todos os valores do filtro estiverem no set, podem ter valores no set que nao estao no filtro
                        if all(True if valorf in localizacoes[0][caracteristica] else False for valorf in valoresf):
                            continue
                        else:
                            filtro = False
                            break
                    elif parametro[1] == 'exclusivo qualquer': #True se todos os valores do set estiverem no filtro, podem ter valores no filtro que nao estao no set
                        if all(True if valorseg in valoresf else False for valorseg in localizacoes[0][caracteristica]):
                            continue
                        else:
                            filtro = False
                            break
                    elif parametro[1] == 'exclusivo todos': #True se todos os valores do set estiverem no filtro e todos do filtro estiverem no set, não valores diferentes
                        if all(True if valorf in localizacoes[0][caracteristica] else False for valorf in valoresf):
                            if all(True if valorseg in valoresf else False for valorseg in localizacoes[0][caracteristica]):
                                continue
                            else:
                                filtro = False
                                break
            if filtro == True:
                filtrado.setdefault(segmento, localizacoes)
        return filtrado
    return (funcao_, parametros)

<<<<<<< HEAD
def ord_tamSegQantLoc(parametrosanalise, parametros=str()):
    def funcao_(aDicio):
        pronto = {}
        for chave, valor in sorted(aDicio.items(), key=lambda item: (len(item[0][0]), len(item[1][1])), reverse=True):
            pronto.setdefault(chave, valor)
=======

def filtro_contidos(parametroanalise):
    def Par():
        parametros = f_d.inp('o que fazer com os contidos?', ('marcar','retirar vazios'))
        op = f_d.inp(f'{parametros}', ('confirmar filtro_contidos', 'comecar novamente'))
        if op == 'confirmar filtro_contidos':
            return parametros
        if op == 'comecar novamente':
            return Par()
    parametros = Par()

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
                if parametros == 'marcar':
                    aDicio[segmento2].insert(0, segmento1)
                elif parametros == 'retirar vazios' and aDicio[segmento2] == []:
                    aDicio.pop(segmento2)
        return aDicio
    return (funcao_, parametros)

def filtro_amontoados(parametroanalise):
    def Par():
        parametros = f_d.inp('o que fazer com os amontados?', ('marcar segundo','retirar vazios'))
        op = f_d.inp(f'{parametros}', ('confirmar filtro_amontoados', 'comecar novamente'))
        if op == 'confirmar filtro_amontoados':
            return parametros
        if op == 'comecar novamente':
            return Par()
    parametros = Par()

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
                if parametros == 'marcar segundo':
                    aDicio[segmento2].insert(0, segmento1)
                elif parametros == 'retirar vazios' and aDicio[segmento2] == []:
                    aDicio.pop(segmento2)
        return aDicio
    return (funcao_, parametros)

def ord_tamSegQantLoc(parametrosanalise):
    def funcao_(aDicio):
        pronto = {}
        for chave, valor in sorted(aDicio.items(), key=lambda item: (len(item[0][0]), len(item[1])), reverse=True):
            pronto.setdefault(chave, valor[1:])
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
        return pronto
    op = f_d.inp('confirmar ord_tamSegQantLoc?', ('s','n'))
    if op == 's':
        return (funcao_,op)