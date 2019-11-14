import segmentacao as m_segmentacao
import filtrosord as m_filtrosord
import dirEinp as f_d

def dicio_funcoes(modulo):
    dicio = {}
    import inspect
    inspectmodulo = inspect.getmembers(modulo, inspect.isfunction)
    for k,v in inspectmodulo:
        dicio.setdefault(k,v)
    return dicio

segmentacao = dicio_funcoes(m_segmentacao)
filtrosord = dicio_funcoes(m_filtrosord)

def filtrordenacao(parametrosanalise):
    op = f_d.inp('adicionar filtros ou ordenacoes?', ('s','n'))
    if op == 's':
        fo = f_d.inp('qual?', [x for x in filtrosord.keys()])
        parametrosanalise.setdefault(fo, filtrosord[fo](parametrosanalise))
        return filtrordenacao(parametrosanalise)
    if op == 'n':
        return parametrosanalise

def criaranalise(caracteristicas, salvosPar, parametrosgerais):
    parametrosanalise = {}
    parametrosanalise.setdefault('segmentacao', segmentacao['segmentacao'](caracteristicas))
    parametrosanalise = filtrordenacao(parametrosanalise)
    op = f_d.inp(dict([(x,y[1]) for x,y in parametrosanalise.items()]), ('confirmar analise', 'refazer analise'))
    if op == 'confirmar analise':
        if dict([(x,y[1]) for x,y in parametrosanalise.items()]) not in [dict([(x,y[1]) for x,y in a.items()]) for a in parametrosgerais]:
            parametrosgerais.append(parametrosanalise)
            return parametrosgerais
        else:
            print('outra analise com os mesmos parametros ja existe')
    return analisesPar_(caracteristicas, salvosPar, parametrosgerais)

def usarsalvas(parametrosgerais, caracteristicas, salvosPar):
    parametrosanalise = {}
    op = f_d.inp('escolha uma analise:',(salvosPar))
    parametrosanalise.setdefault('segmentacao', segmentacao['segmentacao'](caracteristicas, parametros=op['segmentacao']))
    op.pop('segmentacao')
    for func, par in op.items():
            parametrosanalise.setdefault(func, filtrosord[func](parametrosanalise, parametros=par))
    op = f_d.inp(dict([(x,y[1]) for x,y in parametrosanalise.items()]), ('confirmar analise', 'refazer analise'))
    if op == 'confirmar analise':
        if dict([(x,y[1]) for x,y in parametrosanalise.items()]) not in [dict([(x,y[1]) for x,y in a.items()]) for a in parametrosgerais]:
            parametrosgerais.append(parametrosanalise)
            return parametrosgerais
        else:
            print('outra analise com os mesmos parametros ja existe')
    return analisesPar_(caracteristicas, salvosPar, parametrosgerais)

def analisesPar_(caracteristicas, salvosPar, parametrosgerais):
    op = f_d.inp('opcoes de analise:', ('criar nova', 'usar salva'))
    if op == 'criar nova':
        parametrosgerais = criaranalise(caracteristicas, salvosPar, parametrosgerais)
        op = f_d.inp([dict([(x,y[1]) for x,y in a.items()]) for a in parametrosgerais], ('confirmar analises', 'refazer analises'))
        if op == 'confirmar analises':    
            op = f_d.inp('outra analise?', ('s', 'n'))
            if op == 's':
                return analisesPar_(caracteristicas,salvosPar,parametrosgerais)
            if op == 'n':
                return parametrosgerais
        if op == 'refazer analises':
            return analisesPar_(caracteristicas, salvosPar, [])
    if op == 'usar salva':
        if salvosPar == []:
            print('não existem analises salvas')
            return analisesPar_(caracteristicas, salvosPar, parametrosgerais)
        else:
            parametrosgerais = usarsalvas(parametrosgerais,caracteristicas , salvosPar)
            op = f_d.inp([dict([(x,y[1]) for x,y in a.items()]) for a in parametrosgerais], ('confirmar analises', 'refazer analises'))
            if op == 'confirmar analises':    
                op = f_d.inp('outra analise?', ('s', 'n'))
                if op == 's':
                    return analisesPar_(caracteristicas,salvosPar,parametrosgerais)
                if op == 'n':
                    return parametrosgerais
            if op == 'refazer analises':
                return analisesPar_(caracteristicas, salvosPar, [])