import dirEinp as f_d
import xmldict as f_xd
import segmentacaoFiltros as f_sf
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
    musDict = f_xd.xml_mus(xml)
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

#Combinações de caracteristicas nos segmentos:
ListaSegmentosCaracteristicas = [[('intDia', 'p1p2')],
                                [('intDia', 'p1p2'), ('duracao', 'p1p2')],
                                [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1')],
                                [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')],
                                [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]]


def porquantidade_conj(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, diatancia):
    print('por quantidade conjuntos:\n')

    quantidadeT = len(caminhosdict)
    nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
    igualouigualemaior = '>='
    for quantidade in range(1,quantidadeT+1):
        emquantidade = f_sf.porquantidade2(segmentacao, quantidade, igualouigualemaior)
        if len(emquantidade) == 0:
            q = quantidade
            break
        print(f'{igualouigualemaior} a {quantidade} de {quantidadeT} ')
        
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', [quantidadeT])
        parametros.setdefault('analise', [f'{SegmentosCaracteristicas} em {igualouigualemaior} {quantidade} SemContInte Distancia: {distancia}'])
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt_grupos(diA, emquantidade, nomeanalise)
    else:
        q = quantidadeT+1
    
    igualouigualemaior = '=='
    for quantidade in range(1,q):
        emquantidade = f_sf.porquantidade2(segmentacao, quantidade, igualouigualemaior)
        if len(emquantidade) == 0:
            continue
        print(f'{igualouigualemaior} a {quantidade} de {quantidadeT} ')
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', [quantidadeT])
        parametros.setdefault('analise', [f'{SegmentosCaracteristicas} em {igualouigualemaior} {quantidade} SemContInte Distancia: {distancia}'])
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt_grupos(diA, emquantidade, nomeanalise)
    print()

def porquantidade_geral(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, distancia):
    print('por quantidade geral:\n')
    quantidadeT = len(caminhosdict)
    nomes = [f_d.caminho_nome(x, ['.p']) for x in caminhosdict]
    igualouigualemaior = '>='
    for quantidade in range(1,quantidadeT+1):
        emquantidade = f_sf.porquantidade(segmentacao, quantidade, igualouigualemaior)
        if len(emquantidade) == 0:
            q = quantidade
            break
        print(f'{igualouigualemaior} a {quantidade} de {quantidadeT} ')
        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)

        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', [quantidadeT])
        parametros.setdefault('analise', [f'{SegmentosCaracteristicas} em {igualouigualemaior} {quantidade} SemContInte Distancia: {distancia}'])
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt(diA, {c:v for c,v in emquantidade}, nomeanalise)
    else:
        q = quantidadeT+1
    
    igualouigualemaior = '=='
    for quantidade in range(1,q):
        emquantidade = f_sf.porquantidade(segmentacao, quantidade, igualouigualemaior)
        if len(emquantidade) == 0:
            continue
        print(f'{igualouigualemaior} a {quantidade} de {quantidadeT} ')

        nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
        parametros = {'nomes': nomes}
        parametros.setdefault('quantidade', [quantidadeT])
        parametros.setdefault('analise', [f'{SegmentosCaracteristicas} em {igualouigualemaior} {quantidade} SemContInte Distancia: {distancia}'])
        f_d.escreve_txt(diA, parametros, nomeanalise)
        f_d.escreve_txt(diA, {c:v for c,v in emquantidade}, nomeanalise)
    print()

for SegmentosCaracteristicas in ListaSegmentosCaracteristicas:
    segmentacao = f_sf.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, diA)
    distancia = 0
    segmentacao = f_sf.sem_cont_inte_conj(segmentacao, distancia=distancia, conj=1)
    porquantidade_conj(f_sf.dictConj(segmentacao, 1), caminhosdict, diA, SegmentosCaracteristicas, distancia)
    porquantidade_geral(segmentacao, caminhosdict, diA, SegmentosCaracteristicas, distancia)