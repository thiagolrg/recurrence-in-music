import segmentacao as m_segmentacao
import filtrosord as m_filtrosord
import dirEinp as f_d
import inspect

segmentacao = inspect.getmembers(m_segmentacao, inspect.isfunction)
assert(len(segmentacao)==1)
filtrosord = dict([(x,y) for x,y in inspect.getmembers(m_filtrosord, inspect.isfunction)])
def analiseLog_(analisePar):
    return [(x[0],x[1][1]) for x in analisePar]
def analisesLog_(analisesPar):
    return [[(x[0],x[1][1]) for x in a] for a in analisesPar]

def filtrordenacao(analisePar):
    op = f_d.inp('adicionar filtros ou ordenacoes?', ('s','n'))
    if op == 's':
        fo = f_d.inp('qual?', [x for x in filtrosord.keys()])
        analisePar.append((fo, filtrosord[fo](analisePar)))
        return filtrordenacao(analisePar)
    if op == 'n':
        return analisePar

<<<<<<< HEAD
<<<<<<< HEAD
def criaranalise(caracteristicas, salvosPar, analisesPar):
    analisePar = []
    analisePar.append((segmentacao[0][0], segmentacao[0][1](caracteristicas)))
    analisePar = filtrordenacao(analisePar)
    op = f_d.inp(analiseLog_(analisePar), ('confirmar analise', 'refazer analise'))
    if op == 'confirmar analise':
        if analiseLog_(analisePar) not in analisesLog_(analisesPar):
            analisesPar.append(tuple(analisePar))
            return analisesPar
        else:
            print('outra analise com os mesmos parametros ja existe')
    return analisesPar_(caracteristicas, salvosPar, analisesPar)

def usarsalvas(analisesPar, caracteristicas, salvosPar):
    analisePar = []
    op = f_d.inp('escolha uma analise:',(salvosPar))
    assert(op[0][0]==segmentacao[0][0])
    analisePar.append((op[0][0], segmentacao[0][1](caracteristicas, parametros=op[0][1])))
    for filord in op[1:]:
        analisePar.append((filord[0], filtrosord[filord[0]](analisePar, parametros=filord[1]))) 
    op = f_d.inp(analiseLog_(analisePar), ('confirmar analise', 'refazer analise'))
    if op == 'confirmar analise':
        if analiseLog_(analisePar) not in analisesLog_(analisesPar):
            analisesPar.append(analisePar)
            return analisesPar
        else:
            print('outra analise com os mesmos parametros ja existe')
    return analisesPar_(caracteristicas, salvosPar, analisesPar)

def analisesPar_(caracteristicas, salvosPar, analisesPar):
    op = f_d.inp('opcoes de analise:', ('criar nova', 'usar salva'))
    if op == 'criar nova':
        analisesPar = criaranalise(caracteristicas, salvosPar, analisesPar)
        op = f_d.inp(analisesLog_(analisesPar), ('confirmar analises', 'refazer analises'))
        if op == 'confirmar analises':    
            op = f_d.inp('outra analise?', ('s', 'n'))
            if op == 's':
                return analisesPar_(caracteristicas,salvosPar,analisesPar)
            if op == 'n':
                return analisesPar
        if op == 'refazer analises':
            return analisesPar_(caracteristicas, salvosPar, [])
    if op == 'usar salva':
        if salvosPar == []:
            print('não existem analises salvas')
            return analisesPar_(caracteristicas, salvosPar, analisesPar)
        else:
            analisesPar = usarsalvas(analisesPar,caracteristicas , salvosPar)
            op = f_d.inp(analisesLog_(analisesPar), ('confirmar analises', 'refazer analises'))
            if op == 'confirmar analises':    
                op = f_d.inp('outra analise?', ('s', 'n'))
                if op == 's':
                    return analisesPar_(caracteristicas,salvosPar,analisesPar)
                if op == 'n':
                    return analisesPar
            if op == 'refazer analises':
                return analisesPar_(caracteristicas, salvosPar, [])
=======
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
=======
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
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
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
<<<<<<< HEAD
            return analisesPar_(caracteristicas, prontas, parametrosgerais)
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
=======
            return analisesPar_(caracteristicas, prontas, parametrosgerais)
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
