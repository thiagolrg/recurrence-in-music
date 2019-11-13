from analise import segmentacao as m_segmentacao
from analise import filtros as m_filtros
from analise import ordenacoes as m_ordenacoes
from dirEinp import dirEinp as f_d

prontas = ['a','b','c','d']
caracteristicas = ['a','b','c','d']

def dicio_funcoes(modulo):
    dicio = {}
    import inspect
    inspectmodulo = inspect.getmembers(modulo, inspect.isfunction)
    for k,v in inspectmodulo:
        dicio.setdefault(k,v)
    return dicio

segmentacao = dicio_funcoes(m_segmentacao)
filtros = dicio_funcoes(m_filtros)
ordenacoes = dicio_funcoes(m_ordenacoes)

parametrosanalise = {}
if prontas != []:
    op = f_d.inp('criar ou usar prontas?', ('criar','prontas'))
    if op == 'criar':
        parametrosanalise.setdefault('segmentacao', segmentacao['segmentacao'](caracteristicas))
        op = f_d.inp('adicionar filtros:', ('s','n'))
        if op == 's':
            filtro = f_d.inp('qual filtro?', [x for x in filtros.keys()])
            parametrosanalise.setdefault(filtro, filtros[filtro]())
            t = 0
        #if op == 'n':
    '''
    if op == 'prontas':
        para cada chave da prontas buscar a função de mesma chave na funcoesAnalise
        e passar os parametros da prontas para a função
        '''
'''

teste = inp('titulo:', ('s','n','t'))
debug = 0
def Csegmentos_(caracteristicas, tipos, parametros):
    sc = f_d.inp('caracteristicas para segmentos:', (caracteristicas))
    st = f_d.inp('tipos para segmentos:', (tipos))
    parametros[0]['segmentos'].append((sc,st))
    op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
    if op == 'confirmar':
        op = f_d.inp('adicionar outra caracteristica para segmentos?', ('s','n'))
        if op == 's':
            return Csegmentos_(caracteristicas, tipos, parametros)
        if op == 'n':
            return parametros
    if op == 'repetir':
        parametros[0]['segmentos'].pop()
        return Csegmentos_(caracteristicas, tipos, parametros)

def Cposicoes_(caracteristicas, tipos, parametros):
    sc = f_d.inp('caracteristicas para posicoes:', (caracteristicas))
    st = f_d.inp('tipos para segmentos:', (tipos))
    op = f_d.inp('usar para filtros?', ('s', 'n'))
    if op == 's':
        filtro = True
    elif op == 'n':
        filtro = False
    parametros[0]['posicoes'].append((sc, st, filtro))
    op = f_d.inp(f'{parametros}', ('confirmar', 'repetir'))
    if op == 'confirmar':
        op = f_d.inp('adicionar outra caracteristica para posicoes?', ('s','n'))
        if op == 's':
            return Cposicoes_(caracteristicas, tipos, parametros)
        if op == 'n':
            return parametros
    if op == 'repetir':
        parametros[0]['posicoes'].pop()
        return Cposicoes_(caracteristicas, tipos, parametros)

def Cfiltro_quantidade(parametros):
    opcoes = [x[0] for x in parametros['posicoes'] if x[2] == True]
    opcoes.append('nome')
    opcoes.append('posicoes')
    c = inp('por qual caracteristica filtrar', opcoes)
    q = input('que ocorrem pelo menos _ vezes: ')
    print( )
    parametros.setdefault('filtroQT', []).append((c,q))
    sn = inp(f'{parametros}', ('confirmar', 'repetir'))
    if sn == 'confirmar':
        sn = inp('adicionar outro filtro_quantidade?', ('s','n'))
        if sn == 's':
            return Cfiltro_quantidade(parametros)
        if sn == 'n':
            return parametros
    if sn == 'repetir':
        parametros['filtroQT'].pop()
        return Cfiltro_quantidade(parametros)

def parametros_(caracteristicas, tipos, prontas, analises, filtros):
                parametros = [{'segmentos': [], 'posicoes': []},[]]
                parametros = Csegmentos_(caracteristicas, tipos, parametros)
                op = f_d.inp('adicionar caracteristicas para posicoes?', ('s','n'))
                if op == 's':
                    parametros = Cposicoes_(caracteristicas, tipos, parametros)
                op = f_d.inp('adicionar filtros?', ('s','n'))
                if op == 's':
                    parametros = Cfiltros(parametros, filtros)
                analises.append(parametros)
                return outMaster_(caracteristicas, tipos, prontas, analises)
                
def outMaster_(caracteristicas, tipos, prontas, analises):
            op = f_d.inp(f'Analises:\n{analises}', ('confirmar e seguir para analises', 'adiciona nova analise', 'repetir', 'apagar e começar novamente'))
            if op == 'adiciona nova analise':
                return inMaster_(caracteristicas, tipos, prontas, analises)
            if op == 'repetir':
                analises.pop()
                return inMaster_(caracteristicas, tipos, prontas, analises)
            if op == 'apagar e começar novamente':
                analises = []
                return inMaster_(caracteristicas, tipos, prontas, analises)
            if op == 'confirmar e seguir para analises':
                return analises

def inMaster_(caracteristicas, tipos, prontas, analises):
    if prontas != []:
        op = f_d.inp('criar ou usar prontas?', ('criar','prontas'))
        if op == 'criar':
            return parametros_(caracteristicas, tipos,prontas, analises, filtros)
        if op == 'prontas':
            analise = f_d.inp('escolha a análise:', (prontas))
            analises.append(analise)
            return outMaster_(caracteristicas, tipos, prontas, analises)
    elif prontas == []:
        return parametros_(caracteristicas, tipos,prontas, analises, filtros)

analises = inMaster_(caracteristicas, tipos, prontas, [])
debug = 0
'''
'''
def Criar análise ou usar prontas?
    criar
    prontas

se 'prontas' verifica se existem arquivos de parametros:
    se existirem:
        (análises prontas)
        (confirmar refazer)
        (Editar ou confirmar?)
    se não:
        'não existem análises prontas'
        (criar análise?)

se 'criar':
    (processo de criação)
    (confirmar refazer)
    (Editar ou confirmar?)
        se 'nome da análise':
            (processo de criação com nome da análise)
                se confirmar:


def análises prontas:
    análise 1
    análise 2
    análise 3

Confirmar análise {análise}?
s
n

Editar ou confirmar? {lista de análisees}?
análise 1
análise 2
análise 3
Confirmar

Para cada parâmetros:
    OK ou Editar {parametro}?
    Ok
    Editar

    Parametro {parametro}:
    opções

Editar {lista de análisees}?
análise 1
análise 2
análise 3
Não

Acresntar análise?
s
n

Análises {lista de análises}:
Confirmar
Editar
Refazer


'''