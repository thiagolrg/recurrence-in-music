import dirEinp as f_d
import xmldict as f_xd
import SegmentacaoFiltros as f_sf
from collections import defaultdict
import copy
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
for caminho in caminhosconverter:
    nome = f_d.caminho_nome(caminho, extensoes)
    print(f'\rconvertendo {nome}, {caminhosconverter.index(caminho)+1} de {len(caminhosconverter)} '  , end='')
    if '.xml' in caminho:
        start = time.perf_counter()
        xml = f_d.entrada_xml(caminho)
        stop = time.perf_counter()
        print(f'{stop-start} segundos')
    elif '.mxl' in caminho:
        xml = f_d.entrada_mxl(caminho, nome)
    xml = f_xd.ad_counter(xml)
    musDict = f_xd.xml_mus(xml, metronomes=False)
    musDict.setdefault('nome',nome)
    f_d.escreve_pickle(diD, musDict, nome)
print()

#lista com todos os dicionarios
caminhosdict = f_d.caminhos_extensoes(diD, ['.p'])

LocalizacoesCaracteristicas = [('Ncompasso', 'p1'), ('Pcompasso', 'p1'), ('Ncompasso', 'p2'), ('Pcompasso', 'p2')]
"""
SegmentosCaracteristicas = [('intDia', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]
"""

#verificar se a quantidade mantém depois de Sem_Cont_Inte
def quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='=='):
    for quantidade in range(1,len(caminhosdict)):
        print(f'{iguaiouigualemaior} a {quantidade} de {len(caminhosdict)} ')
        emquantidade = f_sf.porquantidade(segmentacao, quantidade, iguaiouigualemaior)
        if emquantidade == None:
            break

        emquantidadeCopy = copy.deepcopy(emquantidade)
        emquantidadeFiltro = f_sf.sem_cont(emquantidadeCopy)
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', len(nomes))
        parametros.setdefault('analise', f'{SegmentosCaracteristicas} {iguaiouigualemaior} {quantidade} SemCont')
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt(diA, {x:y for x,y in emquantidadeFiltro}, nomeanalise)

        emquantidadeCopy = copy.deepcopy(emquantidade)
        emquantidadeFiltro = f_sf.sem_cont_inte(emquantidadeCopy)
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', len(nomes))
        parametros.setdefault('analise', f'{SegmentosCaracteristicas} {iguaiouigualemaior} {quantidade} SemContInter')
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt(diA, {x:y for x,y in emquantidadeFiltro}, nomeanalise)
    return None

def emumasozinha(segmentacao, diA, caminho, SegmentosCaracteristicas):
    segmentacaoCopy = copy.deepcopy(segmentacao)
    segmentacaoFiltro = f_sf.sem_cont(segmentacaoCopy)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', 1)
    parametros.setdefault('analise', f'{SegmentosCaracteristicas} SemCont')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in segmentacaoFiltro}, nomeanalise)

    segmentacaoCopy = copy.deepcopy(segmentacao)
    segmentacaoFiltro = f_sf.sem_cont_inte(segmentacaoCopy)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', 1 )
    parametros.setdefault('analise', f'{SegmentosCaracteristicas} SemContInter')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in segmentacaoFiltro}, nomeanalise)
    return None

"""
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


print('por tamanho:\n')
SegmentosCaracteristicas = [('intDia', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='>=')
"""
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
"""
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA,defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='>=')

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA, defaultdict(list))
nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='==')
quantidades(segmentacao, SegmentosCaracteristicas, caminhosdict, diA, nomes, iguaiouigualemaior='>=')
"""