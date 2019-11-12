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

#acontecem também nessas (explusivamente ou não)
#filtro ex:[{'nome': ['k341','k363']}, False]
def filtro_tipo(parametrosanalises):
    def filtro_tipo(aDict, filtro):
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