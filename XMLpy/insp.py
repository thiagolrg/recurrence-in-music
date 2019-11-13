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

def analisesPar_(caracteristicas, prontas, parametrosgerais):
    if prontas != []:
        op = f_d.inp('criar analise ou usar prontas?', ('criar', 'prontas',))
        if op == 'criar':
            parametrosanalise = {}
            parametrosanalise.setdefault('segmentacao', segmentacao['segmentacao'](caracteristicas))
            parametrosanalise = filtrordenacao(parametrosanalise)
            parametrosgerais.append(parametrosanalise)
            op = f_d.inp(f'{parametrosanalise}', ('confirmar parametros', 'refazer parametros'))
            if op == 'confirmar parametros':
                op = f_d.inp('acrescentar outra analise?', ('s','n'))
                if op == 's':
                    return analisesPar_(caracteristicas, prontas, parametrosgerais)
                if op == 'n':
                    op = f_d.inp(f'{parametrosgerais}', ('confirmar analises', 'refazer analises'))
                    if op == 'confirmar analises':
                        return parametrosgerais
                    if op ==  'refazer analises':
                        return analisesPar_(caracteristicas, prontas, [])
            if op == 'refazer parametros':
                parametrosgerais.pop()
                return analisesPar_(caracteristicas, prontas, parametrosgerais)
        elif op == 'prontas':
            print('nao implementado')
            return analisesPar_(caracteristicas, prontas, parametrosgerais)