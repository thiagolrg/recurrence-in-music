import dirEinp as f_d
import xmldict as f_xd
import SegmentacaoFiltros as f_sf
import time

#pede diretorio do usuário e cria pastas e caminhos que vão ser usados
extensoes = ['.xml','.mxl']
di = f_d.diretorio_ler(extensoes)
diD = di+'\\Dicts'
diA = di+'\\Analises'
f_d.cria_pasta(diD)
f_d.cria_pasta(diA)

#converte xmls que não existem na pasta Dicts e salva usando pickle
caminhosconverter = f_d.xml_sem_dict(di, extensoes, diD, ['.p'])

t = 0
for caminho in caminhosconverter:
    start = time.perf_counter()
    nome = f_d.caminho_nome(caminho, extensoes)
    print(f'\rconvertendo {nome}, {caminhosconverter.index(caminho)+1} de {len(caminhosconverter)} '  , end='')
    if '.xml' in caminho:
        xml = f_d.entrada_xml(caminho)
    elif '.mxl' in caminho:
        xml = f_d.entrada_mxl(caminho, nome)
    xml = f_xd.ad_counter(xml)
    musDict = f_xd.xml_mus(xml, metronomes=False)
    musDict.setdefault('nome',nome)
    f_d.escreve_pickle(diD, musDict, nome)
    stop = time.perf_counter()
    t = t + stop-start
print(f'\n{t} segundos\n')

#lista com todos os dicionarios
caminhosdict = f_d.caminhos_extensoes(diD, ['.p'])

#Características usadas nas localizações:
LocalizacoesCaracteristicas = [('Ncompasso', 'p1'), ('Pcompasso', 'p1'), ('Ncompasso', 'p2'), ('Pcompasso', 'p2')]
"""
Exemplos de Combinações de caracteristicas:

SegmentosCaracteristicas = [('intDia', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]


def quantidades(segmentacao, SegmentosCaracteristicas, quantidade, diA, nomes, iguaiouigualemaior='=='):
    for quantidade in range(1,quantidade+1):
        emquantidade = f_sf.porquantidade(segmentacao, quantidade, iguaiouigualemaior)
        if len(emquantidade) == 0:
            break
        print(f'{iguaiouigualemaior} a {quantidade} de {len(caminhosdict)} ')
        
        emquantidadeFiltro = f_sf.sem_cont3(copy.deepcopy(emquantidade))
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', [len(nomes)])
        parametros.setdefault('analise', [f'{SegmentosCaracteristicas} {iguaiouigualemaior} {quantidade} SemCont'])
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt(diA, {x:y for x,y in emquantidadeFiltro}, nomeanalise)
        
        distancia = 0
        emquantidadeFiltro = f_sf.sem_cont_inte3(emquantidade,distancia=distancia)
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', [len(nomes)])
        parametros.setdefault('analise', [f'{SegmentosCaracteristicas} {iguaiouigualemaior} {quantidade} SemContInte distancia: {distancia}'])
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt(diA, {x:y for x,y in emquantidadeFiltro}, nomeanalise)
    return None

def emumasozinha(segmentacao, diA, caminho, SegmentosCaracteristicas):
    segmentacaoFiltro = f_sf.sem_cont3(copy.deepcopy(segmentacao))
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', [1])
    parametros.setdefault('analise', f'{SegmentosCaracteristicas} SemCont')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in segmentacaoFiltro}, nomeanalise)

    distancia = 0
    segmentacaoFiltro = f_sf.sem_cont_inte3(copy.deepcopy(segmentacao), distancia=distancia)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', [1] )
    parametros.setdefault('analise', f'{SegmentosCaracteristicas} SemContInte distancia {distancia}')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in segmentacaoFiltro}, nomeanalise)
    return None

#Em cada música em várias combinações de característisticas
print('por musica:\n')
for i in range(len(caminhosdict)):
    print(f'{i+1} de {len(caminhosdict)}\n')
    caminho = caminhosdict[i]

    SegmentosCaracteristicas = [('intDia', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, [caminho], diA, defaultdict(list))
    emumasozinha(segmentacao, diA, caminho,SegmentosCaracteristicas)

    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, [caminho], diA, defaultdict(list))
    emumasozinha(segmentacao, diA, caminho,SegmentosCaracteristicas)

    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, [caminho], diA, defaultdict(list))
    emumasozinha(segmentacao, diA, caminho,SegmentosCaracteristicas)

    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, [caminho], diA, defaultdict(list))
    emumasozinha(segmentacao, diA, caminho,SegmentosCaracteristicas)

    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, [caminho], diA, defaultdict(list))
    emumasozinha(segmentacao, diA, caminho,SegmentosCaracteristicas)

    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, [caminho], diA, defaultdict(list))
    emumasozinha(segmentacao, diA, caminho,SegmentosCaracteristicas)


print('por quantidade:\n')
SegmentosCaracteristicas = [('intDia', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
#quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))

nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA,defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='>=')

"""
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, dict(), diA)
time.sleep(10)
#segmentacao = f_sf.sem_cont_inte3(segmentacao)

#nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
#quantidades(segmentacao, SegmentosCaracteristicas, len(caminhosdict), diA, nomes, iguaiouigualemaior='==')
#quantidades(segmentacao, SegmentosCaracteristicas, 1, diA, nomes, iguaiouigualemaior='>=')
