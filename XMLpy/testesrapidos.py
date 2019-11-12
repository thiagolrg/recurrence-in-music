prontas = ['a','b','c','d']
caracteristicas = ['a','b','c','d']
tipos = ['p1', 'p1p2', 'p2m1']

def inp(texto, opcoes):
    print(f'{texto}')
    for o in range(len(opcoes)):
        print(f'{o+1}. {opcoes[o]}')
    ip = input('escolha uma opcao: ')
    if ip.isdigit() and int(ip) <= len(opcoes):
        print( )
        return opcoes[int(ip)-1]
    else:
        print(f'{ip} não é uma ooção\n')
        return inp(texto, opcoes)

teste = inp('titulo:', ('s','n','t'))
debug = 0
def Csegmentos_(caracteristicas, tipos, parametros):
    sc = inp('caracteristicas para segmentos:', (caracteristicas))
    st = inp('tipos para segmentos:', (tipos))
    parametros['segmentos'].append((sc,st))
    sn = inp(f'{parametros}', ('confirmar', 'repetir'))
    if sn == 'confirmar':
        sn = inp('adicionar outra caracteristica para segmentos?', ('s','n'))
        if sn == 's':
            return Csegmentos_(caracteristicas, tipos, parametros)
        if sn == 'n':
            return parametros
    if sn == 'repetir':
        parametros['segmentos'].pop()
        return Csegmentos_(caracteristicas, tipos, parametros)

def Cposicoes_(caracteristicas, tipos, parametros):
    sc = inp('caracteristicas para posicoes:', (caracteristicas))
    st = inp('tipos para segmentos:', (tipos))
    sn = inp('usar para filtros?', ('s', 'n'))
    if sn == 's':
        filtro = True
    elif sn == 'n':
        filtro = False
    parametros['posicoes'].append((sc, st, filtro))
    sn = inp(f'{parametros}', ('confirmar', 'repetir'))
    if sn == 'confirmar':
        sn = inp('adicionar outra caracteristica para posicoes?', ('s','n'))
        if sn == 's':
            return Cposicoes_(caracteristicas, tipos, parametros)
        if sn == 'n':
            return parametros
    if sn == 'repetir':
        parametros['posicoes'].pop()
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

def parametros_(caracteristicas, tipos, prontas, analises):
                parametros = {'segmentos': [], 'posicoes': []}
                parametros = Csegmentos_(caracteristicas, tipos, parametros)
                sn = inp('adicionar caracteristicas para posicoes?', ('s','n'))
                if sn == 's':
                    parametros = Cposicoes_(caracteristicas, tipos, parametros)
                sn = inp('filtro quantidade?', ('s','n'))
                if sn == 's':
                    parametros = Cfiltro_quantidade(parametros)
                analises.append(parametros)
                return analises_(caracteristicas, tipos, prontas, analises)
                
def analises_(caracteristicas, tipos, prontas, analises):
            sn = inp(f'Analises:\n{analises}', ('confirmar e seguir para analises', 'adiciona nova analise', 'repetir', 'apagar e começar novamente'))
            if sn == 'adiciona nova analise':
                return inpMaster(caracteristicas, tipos, prontas, analises)
            if sn == 'repetir':
                analises.pop()
                return inpMaster(caracteristicas, tipos, prontas, analises)
            if sn == 'apagar e começar novamente':
                analises = []
                return inpMaster(caracteristicas, tipos, prontas, analises)
            if sn == 'confirmar e seguir para analises':
                return analises

def inpMaster(caracteristicas, tipos, prontas, analises):
    if prontas != []:
        sn = inp('criar ou usar prontas?', ('criar','prontas'))
        if sn == 'criar':
            return parametros_(caracteristicas, tipos,prontas, analises)
        if sn == 'prontas':
            analise = inp('escolha a análise:', (prontas))
            analises.append(analise)
            return analises_(caracteristicas, tipos, prontas, analises)
    elif prontas == []:
        return parametros_(caracteristicas, tipos,prontas, analises)

analises = inpMaster(caracteristicas, tipos, prontas, [])
debug = 0
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