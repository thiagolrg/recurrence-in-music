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


nomes = [f_d.caminho_nome(x, ['.xml', '.mxl']) for x in caminhosconverter]
print(f'MusicXMLs para conversao: {len(nomes)}')
start = time.perf_counter()
for caminho in caminhosconverter:
    nome = f_d.caminho_nome(caminho, extensoes)
    if '.xml' in caminho:
        xml = f_d.entrada_xml(caminho)
    elif '.mxl' in caminho:
        xml = f_d.entrada_mxl(caminho, nome)
    xml = f_xd.ad_counter(xml)
    musDict = f_xd.xml_mus(xml, metronomes=False)
    musDict.setdefault('nome',nome)
    f_d.escreve_pickle(diD, musDict, nome)
stop = time.perf_counter()
if len(nomes) > 0:
    print(f'{stop-start} segundos\n')
else:
    print()

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
"""

def semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, igualouigualemaior, distancia):
    quantidadeT = len(caminhosdict)
    nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
    for quantidade in range(1,quantidadeT+1):
        emquantidade = f_sf.porquantidade(segmentacao, quantidade, igualouigualemaior)
        if len(emquantidade) == 0:
            break
        print(f'{igualouigualemaior} a {quantidade} de {quantidadeT} ')
        
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', [quantidadeT])
        parametros.setdefault('analise', [f'{SegmentosCaracteristicas} em {igualouigualemaior} {quantidade} SemContInte Distancia: {distancia}'])
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt(diA, {x:y for x,y in emquantidade}, nomeanalise)

def emumasozinha(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, distancia):
    quantidadeT = len(caminhosdict)
    nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': nomes}
    parametros.setdefault('quantidade', [quantidadeT])
    parametros.setdefault('analise', [f'{SegmentosCaracteristicas} SemContInte Distancia: {distancia}'])
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in segmentacao}, nomeanalise)
    return None

#Em cada música em várias combinações de característisticas
print('por musica:\n')
for i in range(len(caminhosdict)):
    print(f'{i+1} de {len(caminhosdict)}\n')
    caminho = [caminhosdict[i]]
 
    SegmentosCaracteristicas = [('intDia', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminho, diA)
    distancia = 0
    segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
    emumasozinha(segmentacao, caminho, diA, SegmentosCaracteristicas, distancia)
  
    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminho, diA)
    distancia = 0
    segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
    emumasozinha(segmentacao, caminho, diA, SegmentosCaracteristicas, distancia)
  
    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminho, diA)
    distancia = 0
    segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
    emumasozinha(segmentacao, caminho, diA, SegmentosCaracteristicas, distancia)

    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminho, diA)
    distancia = 0
    segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
    emumasozinha(segmentacao, caminho, diA, SegmentosCaracteristicas, distancia)

    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminho, diA)
    distancia = 0
    segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
    emumasozinha(segmentacao, caminho, diA, SegmentosCaracteristicas, distancia)
   
    SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminho, diA)
    distancia = 0
    segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
    emumasozinha(segmentacao, caminho, diA, SegmentosCaracteristicas, distancia)

print('por quantidade:\n')
SegmentosCaracteristicas = [('intDia', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA)
distancia = 0
segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '==', distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '>=', distancia)

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA)
distancia = 0
segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '==', distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '>=', distancia)

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA)
distancia = 0
segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '==', distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '>=', distancia)

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA)
distancia = 0
segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '==', distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '>=', distancia)

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA)
distancia = 0
segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '==', distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '>=', distancia)

SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]
segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA)
distancia = 0
segmentacao = f_sf.sem_cont_inte3(segmentacao, distancia=distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '==', distancia)
semcontinte_porquantidade(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, '>=', distancia)