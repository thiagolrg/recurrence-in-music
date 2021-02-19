import dirEinp as f_d

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
        for segmento1, localizacoes1 in aDicio.copy().items():
            contido = False
            for segmento2, localizacoes2 in aDicio.copy().items():
                for localizacao1 in localizacoes1[1]:
                    for localizacao2 in localizacoes2[1]:
                        if localizacao2[0][0:3] == localizacao1[0][0:3] and localizacao2[0][3] != localizacao1[0][3]:
                            if localizacao2[0][3][0] >= localizacao1[0][3][0] and localizacao2[0][3][1] <= localizacao1[0][3][1]:
                                aDicio[segmento2][1].pop(aDicio[segmento2][1].index(localizacao2))
                                contido = True
                        else:
                            continue
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
        for segmento1, localizacoes1 in aDicio.copy().items():
            amontoado = False
            for segmento2, localizacoes2 in aDicio.copy().items():
                for localizacao1 in localizacoes1[1]:
                    for localizacao2 in localizacoes2[1]:
                        if localizacao2[0][0:3] == localizacao1[0][0:3] and localizacao2[0][3] != localizacao1[0][3]:
                            if localizacao2[0][3][0] <= localizacao1[0][3][1] and localizacao2[0][3][1] > localizacao1[0][3][1]:
                                aDicio[segmento2][1].pop(aDicio[segmento2][1].index(localizacao2)) 
                                amontoado = True
                                if parametros == 'marcar segundo':
                                    aDicio[segmento2][0].setdefault('amontoado', tuple([localizacao1[0][3][1]-localizacao2[0][3][0], segmento1]))
                if amontoado == True and parametros == 'retirar vazios' and aDicio[segmento2][1] == []:
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
        parametros.setdefault(caracteristica, int(quantidade))
        op = f_d.inp(parametros, ('confirmar entrada', 'refazer entrada'))
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
        op = f_d.inp(parametros, ('confirmar filtro_quantidade', 'comecar novamente'))
        if op == 'confirmar filtro_quantidade':
            return parametros
        if op == 'comecar novamente':
            return Par(parametroanalise, {})
    
    if parametros == dict():
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

def filtroset_tipo(parametroanalise, parametros=list()):
    def filtroPar(parametroanalise, parametros):
        opcoes = [x[0] for x in parametroanalise[0][1][1]['posicoesPar'] if 'f' in x[1]]
        opcoes.append('nome')
        caracteristica = f_d.inp('por qual caracteristica filtrar?', opcoes)
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
        print( )
        parametros.append(({caracteristica: valores}, tipo))
        op = f_d.inp(parametros, ('confirmar entrada', 'refazer entrada'))
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
        op = f_d.inp(parametros, ('confirmar filtro_tipo', 'comecar novamente'))
        if op == 'confirmar filtro_tipo':
            return parametros
        if op == 'comecar novamente':
            return Par(parametroanalise, [])
    
    if parametros == list():
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

def ord_tamSegQantLoc(parametrosanalise, parametros=str()):
    def funcao_(aDicio):
        pronto = {}
        for chave, valor in sorted(aDicio.items(), key=lambda item: (len(item[0][0]), len(item[1][1])), reverse=True):
            pronto.setdefault(chave, valor)
        return pronto
    if parametros == str():    
        parametros = 's'
    return (funcao_,parametros)

#Sequencias sem contidos e intecalados
#Antigo e muito provavelmente precisa de ser refeito para funcionar, foi pouco testado
def sorts_sequencias(dicio):
    seq = sort_sequencias(dicio)
    seq = so_seq(seq)
    seq = sortsoseq(seq)
    return seq

def sort_sequencias(dicio):
    return sorted([(c, v) for c, v in dicio.items() if len(v) > 1 and len(c[0]) > 1], key=lambda item: (len(item[0][0]), len(item[1])), reverse=True)    

def so_seq(listarecorrencias):
    soseq = []
    for segmento, posicoes in listarecorrencias:
        posicoesseq = seq(posicoes)
        if len(posicoesseq) > 1:
            soseq.append((segmento,posicoesseq))
    return soseq

def seq(posicoes):
    posicoesseq = []
    p = 0
    while p+1 < len(posicoes):
        if posicoes[p+1][3][0] - posicoes[p][3][1] == 1 and posicoes[p+1][0:3] == posicoes[p][0:3]:
            s1 = p
            while posicoes[p+1][3][0] - posicoes[p][3][1] == 1 and posicoes[p+1][0:3] == posicoes[p][0:3]:
                p = p+1
                if p == len(posicoes)-1:
                    break
            s2 = p+1
            posicoesseq.append(posicoes[s1:s2])
        p = p+1
    return posicoesseq

def sortsoseq(listarecorrencias):
    listasort = []
    for segmento, posicoes in listarecorrencias:
        for posicao in posicoes:
            tamanhoseq = posicao[-1][3][1] - posicao[0][3][0]
            listasort.append((segmento,posicoes,tamanhoseq))
    listasort = sorted(listasort, key= lambda x: x[2], reverse=True)
    listasort = [(s,p) for s,p,t in listasort]
    return listasort

def sem_cont_inter_seq(listarecorrencias):
    semcontinter = []
    quepassaram = []
    for segmento, posicoes in listarecorrencias:
        posicoessegmento = []
        for posicao in posicoes:
            if not intercalada_seq(posicoessegmento, posicao) and not intercalada_seq(quepassaram, posicao) and not contida_seq(quepassaram, posicao):
                posicoessegmento.append(posicao)
        if len(posicoessegmento) > 0:
            for v in posicoessegmento:
                quepassaram.append(v)
            semcontinter.append((segmento,posicoessegmento))
    return semcontinter

def contida_seq(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0][0:3] == outra[0][0:3] and posicao[0][3][0] >= outra[0][3][0] and posicao[-1][3][1] <= outra[-1][3][1]:
            return True
    return False

def intercalada_seq(listaposicoes, posicao):
    for outra in listaposicoes:
        if posicao[0][0:3] == outra[0][0:3] and posicao[0][3][0] > outra[0][3][0] and posicao[0][3][0] < outra[-1][3][1] and posicao[-1][3][1] > outra[-1][3][1]:
            return True
        if posicao[0][0:3] == outra[0][0:3] and posicao[-1][3][1] > outra[0][3][0] and posicao[-1][3][1] < outra[0][3][1] and posicao[0][3][0] < outra[0][3][0]:
            return True
    return False
