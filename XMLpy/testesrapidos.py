prontas = ['a','b','c','d']
caracteristicas = ['a','b','c','d']
tipos = ['p1', 'p1p2', 'p2m1']

def inp(texto, opcoes):
    print(f'{texto}\n')
    for o in opcoes:
        print(o)
    ip = input('escolha uma opcao: ')
    if ip in opcoes:
        return ip
    else:
        print(f'{ip} não é uma ooção')
        return inp(texto, opcoes)

if prontas != []:
    inp('criar ou usar prontas?', ('criar','prontas'))
    if 'criar':
        def analise_(caracteristicas, tipos, analise):
            def parametros_(caracteristicas, tipos):
                def Csegmentos_(caracteristicas, tipos, parametros):
                    sc = inp('caracteristicas para segmentos:', (caracteristicas))
                    st = inp('tipos para segmentos:', (tipos))
                    parametros['segmentos'].append((sc,st))
                    print(parametros)
                    sn = inp('adicionar carácteristica para segmentos?', ('s','n'))
                    if sn == 's':
                        return Csegmentos_(caracteristicas, tipos, parametros)
                    if sn == 'n':
                        return parametros
                def Cposicoes_(caracteristicas, tipos, parametros):
                    sc = inp('caracteristicas para posicoes:', (caracteristicas))
                    st = inp('tipos para segmentos:', (tipos))
                    sn = inp('usar para filtros?', ('s', 'n'))
                    if sn == 's':
                        filtro = True
                    elif sn == 'n':
                        filtro = False
                    parametros['posicoes'].append((sc, st, filtro))
                    print(parametros)
                    sn = inp('adicionar carácteristica para posicoes?', ('s','n'))
                    if sn == 's':
                        return Cposicoes_(caracteristicas, tipos, parametros)
                    if sn == 'n':
                        return parametros
                def Cfiltro_quantidade(parametros):
                    opcoes = [x[0] for x in parametros['posicoes'] if x[2] == True]
                    opcoes.append('nome')
                    opcoes.append('posicoes')
                    c = inp('por qual caracteristica filtrar', opcoes)
                    q = input('que ocorrem pelo menos _ vezes: ')
                    parametros.setdefault('filtroQT', []).append((c,q))
                    print(parametros)
                    sn = inp('adicionar outro filtro_quantidade?', ('s','n'))
                    if sn == 's':
                        return Cfiltro_quantidade(parametros)
                    if sn == 'n':
                        return parametros
                parametros = {'segmentos': [], 'posicoes': []}
                parametros = Csegmentos_(caracteristicas, tipos, parametros)
                sn = inp('caracteristicas para posicoes?', ('s','n'))
                if sn == 's':
                    parametros = Cposicoes_(caracteristicas, tipos, parametros)
                sn = inp('filtro quantidade?', ('s','n'))
                if sn == 's':
                    parametros = Cfiltro_quantidade(parametros)
                return parametros
            analise.append(parametros_(caracteristicas, tipos))
            sn = inp(f'Analises:\n{analise}', ('outra nova', 'apagar e começar novamente', 'confirmar e seguir para analise'))
            if sn == 'outra nova':
                return analise_(caracteristicas, tipos, analise)
            elif sn == 'apagar e começar novamente':
                analise = []
                return analise_(caracteristicas, tipos, analise)
            elif sn == 'confirmar e seguir para analise':
                return analise
        analise = analise_(caracteristicas, tipos, [])

#fazer input de opções por número e não por texto...
'''
    elif 'prontas'
        inp('escolha os parâmetros:', (prontas))
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