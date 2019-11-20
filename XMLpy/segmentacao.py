import dirEinp as f_d

def segmentacao(caracteristicas, parametros=dict()):
    #parametros = {'segmentosPar': (caracteristica, forma de extrair),... 'posicoesPar':(caracteristica, forma de extrair),...}
    #funcoes de input de parametros para a segmentação
    def segmentosPar_(caracteristicas, parametros):
        sc = f_d.inp('caracteristicas para segmentos:', (caracteristicas))
        st = f_d.inp('modos de segmentar:', ('p1','p1p2','p2m1','p1p2set','p2m1set'))
        parametros['segmentosPar'].append((sc,st))
        op = f_d.inp(parametros, ('confirmar entrada', 'refazer entrada'))
        if op == 'confirmar entrada':
            op = f_d.inp('adicionar outra caracteristica para segmentos?', ('s','n'))
            if op == 's':
                return segmentosPar_(caracteristicas, parametros)
            if op == 'n':
                return parametros
        if op == 'refazer entrada':
            parametros['segmentosPar'].pop()
            return segmentosPar_(caracteristicas, parametros)
    def posicoesPar_(caracteristicas, parametros):
        sc = f_d.inp('caracteristicas para posicoes:', (caracteristicas))
        st = f_d.inp('modos de segmentar:', ('p1','p1p2','p2m1','p1p2set','p2m1set'))
        parametros['posicoesPar'].append((sc, st))
        op = f_d.inp(parametros, ('confirmar entrada', 'refazer entrada'))
        if op == 'confirmar entrada':
            op = f_d.inp('adicionar outra caracteristica para posicoes?', ('s','n'))
            if op == 's':
                return posicoesPar_(caracteristicas, parametros)
            if op == 'n':
                return parametros
        if op == 'refazer entrada':
            parametros['posicoesPar'].pop()
            return posicoesPar_(caracteristicas, parametros)
    def filtrosPar_(caracteristicas, parametros):
        sc = f_d.inp('caracteristicas para filtros:', (caracteristicas))
        st = f_d.inp('modos de segmentar:', ('p1f','p1p2f','p2m1f'))
        parametros['posicoesPar'].append((sc, st))
        op = f_d.inp(parametros, ('confirmar entrada', 'refazer entrada'))
        if op == 'confirmar entrada':
            op = f_d.inp('adicionar outra caracteristica para filtros?', ('s','n'))
            if op == 's':
                return filtrosPar_(caracteristicas, parametros)
            if op == 'n':
                return parametros
        if op == 'refazer entrada':
            parametros['posicoesPar'].pop()
            return filtrosPar_(caracteristicas, parametros)

    #montando parametros
    def Par(caracteristicas):
        parametros = {'segmentosPar': [], 'posicoesPar': []}
        parametros = segmentosPar_(caracteristicas, parametros)
        op = f_d.inp('adicionar caracteristicas para posicoes?', ('s','n'))
        if op == 's':
            parametros = posicoesPar_(caracteristicas, parametros)
        op = f_d.inp('adicionar caracteristicas para filtros?', ('s','n'))
        if op == 's':
            parametros = filtrosPar_(caracteristicas, parametros)
        op = f_d.inp(parametros, ('confirmar segmentacao', 'comecar novamente'))
        if op == 'confirmar segmentacao':
            return parametros
        if op == 'comecar novamente':
            return Par(caracteristicas)
    
    if parametros == dict():
        parametros = Par(caracteristicas)

    def funcao_(mDicio, aDicio):
        musica = mDicio.copy()
        nome = musica.pop('nome')
        for parte in musica:
            for voz, caracteristicas in parte.items():
                for p1 in range(len(caracteristicas['grau'])):
                    for p2 in range(p1+1,len(caracteristicas['grau'])):

                        #caracteristicas nos segmentos
                        keyAnalise = []
                        for segmentoPar in parametros['segmentosPar']:
                            if segmentoPar[1] == 'p1':
                                keyAnalise.append(caracteristicas[segmentoPar[0]][p1])
                            elif segmentoPar[1] =='p1p2':
                                keyAnalise.append(tuple(caracteristicas[segmentoPar[0]][p1:p2]))
                            elif segmentoPar[1] == 'p2m1':
                                if (p2-1)-p1 == 0:
                                    continue
                                keyAnalise.append(tuple(caracteristicas[segmentoPar[0]][p1:p2-1]))
                            elif segmentoPar[1] == 'p1p2set':
                                keyAnalise.append(tuple(set(caracteristicas[segmentoPar[0]][p1:p2])))
                            elif segmentoPar[1] == 'p2m1set':
                                if (p2-1)-p1 == 0:
                                    continue
                                keyAnalise.append(tuple(set(caracteristicas[segmentoPar[0]][p1:p2-1])))
                        if keyAnalise == []:
                            continue
                        keyAnalise = tuple(keyAnalise)

                        #esse set criado no index 0 do valor permite ver valores unicos para
                        #todas as caracteristicas do segmentos em qualquer posicao
                        aDicio.setdefault(keyAnalise, [{'nome': set()},[]])[0]['nome'].add(nome)

                        #caracteristicas nas posicoes
                        carposicao = {}
                        locposicao = (nome, parte, voz, (p1,p2))
                        for posicaoPar in parametros['posicoesPar']:
                            if posicaoPar != []:
                                if posicaoPar[1] == 'p1':
                                    carposicao.setdefault(posicaoPar[0], caracteristicas[posicaoPar[0]][p1])
                                elif posicaoPar[1] == 'p1p2':
                                    carposicao.setdefault(posicaoPar[0], tuple(caracteristicas[posicaoPar[0]][p1:p2]))
                                elif posicaoPar[1] == 'p2m1':
                                    if (p2-1)-p1 == 0:
                                        continue
                                    carposicao.setdefault(posicaoPar[0],tuple(caracteristicas[posicaoPar[0]][p1:p2-1]))
                                elif posicaoPar[1] == 'p1p2set':
                                    carposicao.setdefault(posicaoPar[0], set(caracteristicas[posicaoPar[0]][p1:p2]))
                                elif posicaoPar[1] == 'p2m1set':
                                    if (p2-1)-p1 == 0:
                                        continue
                                    carposicao.setdefault(posicaoPar[0], set(caracteristicas[posicaoPar[0]][p1:p2-1]))

                                #acrescenta ao set no index 0 do valor
                                elif posicaoPar[1] == 'p1f':
                                    aDicio[keyAnalise][0].setdefault(posicaoPar[0], set()).add(caracteristicas[posicaoPar[0]][p1])
                                elif posicaoPar[1] == 'p1p2f':
                                    aDicio[keyAnalise][0].setdefault(posicaoPar[0], set()).update(caracteristicas[posicaoPar[0]][p1:p2])
                                elif posicaoPar[1] == 'p2m1f':
                                    if (p2-1)-p1 == 0:
                                        continue
                                    aDicio[keyAnalise][0].setdefault(posicaoPar[0], set()).update(caracteristicas[posicaoPar[0]][p1:p2-1])
                        
                        #localizao sempre é index 0 e as outras caracteristicas vem no index 1 
                        aDicio[keyAnalise][1].append((locposicao,carposicao))
        return aDicio
    return (funcao_, parametros)

#print(nome, parte, round((p1*100)/len(caracteristicas['grau'])+0.5),'%   ', end='\r')