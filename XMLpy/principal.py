import dirEinp as f_d
import xmldict as f_xd
import algoritmonovo as f_a


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
    print(f'convertendo {nome}, ', caminhosconverter.index(caminho)+1,' de ', len(caminhosconverter))
    if '.xml' in caminho:
        xml = f_d.entrada_xml(caminho)
    elif '.mxl' in caminho:
        xml = f_d.entrada_mxl(caminho, nome)
    xml = f_xd.ad_counter(xml)
    musDict = f_xd.xml_mus(xml, metronomes=False)
    musDict.setdefault('nome',nome)
    f_d.escreve_pickle(diD, musDict, nome)

#lista com todos os dicionarios
caminhosdict = f_d.caminhos_extensoes(diD, ['.p'])
print()

#cria resgata ou atualiza tamanho minimo necessário para pegar todas as recorrencias
#no conjunto de músicas
if len(caminhosconverter) > 0:
    TamMax = False
else:
    try:
        TamMax = f_d.le_pickle(diA+'\\_tamanho_.p')
    except FileNotFoundError:
        TamMax = False

LocalizacoesCaracteristicas = [('Ncompasso', 'p1'), ('Pcompasso', 'p1'), ('Ncompasso', 'p2'), ('Pcompasso', 'p2')]
"""
SegmentosCaracteristicas = [('intDia', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1'), ('Ptempo', 'p1')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ptempo', 'p1p2')]
SegmentosCaracteristicas = [('intDia', 'p1p2'), ('duracao', 'p1p2'), ('Ntempo', 'p1p2'), ('Ptempo', 'p1p2')]
"""

# Segmentacao IntDia
SegmentosCaracteristicas = [('intDia', 'p1p2')]
segmentacao = f_a.Segmentacao(SegmentosCaracteristicas, LocalizacoesCaracteristicas, caminhosdict, TamMax, diA)

iguaiouigualemaior = '=='
for quantidade in range(1,len(caminhosdict)):
    print(f'{iguaiouigualemaior} a {quantidade} de {len(caminhosdict)}')
    emquantidade = f_a.porquantidade(segmentacao, quantidade, iguaiouigualemaior)
    if emquantidade == None:
        break

    emquantidadeSemCont = f_a.sem_cont(emquantidade)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'{SegmentosCaracteristicas} {iguaiouigualemaior} {quantidade} SemCont')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    emquantidadeSemContInter = f_a.sem_cont_inter(emquantidade)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'{SegmentosCaracteristicas} {iguaiouigualemaior} {quantidade} SemContInter')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

"""
iguaiouigualemaior = '>='
for quantidade in range(1,len(caminhosdict)):
    print(f'{iguaiouigualemaior} a {quantidade} de {len(caminhosdict)}')
    emquantidade = f_a.porquantidade(segmentacao, quantidade, iguaiouigualemaior)
    if emquantidade == None:
        break
    emquantidadeSemCont = f_a.sem_cont(emquantidade)
    emquantidadeSemContInter = f_a.sem_cont_inter(emquantidade)
"""

"""

for caminho in caminhosdict:

    
    segIntDiaDur = f_a.segmentacao_IntDia_Dur([caminho], tamanho=tamanho)

    rec = f_a.sort_recorrencias(segIntDiaDur)
    rec = f_a.sem_cont_inter(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'recorrências IntDiaDur sem contidos e intercalados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    rec = f_a.sorts_sequencias(segIntDiaDur)
    rec = f_a.sem_cont_inter_seq(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'sequências IntDiaDur sem contidos e intercalados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    del segIntDiaDur

    segIntDiaDurPtempo = f_a.segmentacao_IntDia_Dur_Ptempo([caminho], tamanho=tamanho)

    rec = f_a.sort_recorrencias(segIntDiaDurPtempo)
    rec = f_a.sem_cont_inter(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'recorrências IntDiaDurPtempo sem contidos e intercalados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    rec = f_a.sorts_sequencias(segIntDiaDurPtempo)
    rec = f_a.sem_cont_inter_seq(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'sequências IntDiaDurPtempo sem contidos e intercalados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    del segIntDiaDurPtempo
    
    segIntDiaDurPcompasso = f_a.segmentacao_IntDia_Dur_Pcompasso([caminho], tamanho=tamanho)

    rec = f_a.sort_recorrencias(segIntDiaDurPcompasso)
    rec = f_a.sem_cont_inter(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'recorrências IntDiaDurPcompasso sem contidos e intercalados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    rec = f_a.sorts_sequencias(segIntDiaDurPcompasso)
    rec = f_a.sem_cont_inter_seq(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'sequências IntDiaDurPcompasso sem contidos e intercalados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    del segIntDiaDurPcompasso

segIntDiaDur = f_a.segmentacao_IntDia_Dur(caminhosdict, tamanho=tamanho)
recIntDiaDur = f_a.sort_recorrencias(segIntDiaDur)
seqIntDiaDur = f_a.sorts_sequencias(segIntDiaDur)
del segIntDiaDur

rec = f_a.sem_cont_inter(recIntDiaDur)
nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
parametros.setdefault('quantidade', len(caminhosdict))
parametros.setdefault('analise', f'recorrências IntDiaDur sem cont e inter em tudo')
f_d.escreve_txt(diA, parametros, nomeanalise)
f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

rec = f_a.sem_cont_inter_seq(seqIntDiaDur)
nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
parametros.setdefault('quantidade', len(caminhosdict))
parametros.setdefault('analise', f'sequências IntDiaDur sem cont e inter em tudo')
f_d.escreve_txt(diA, parametros, nomeanalise)
f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

for quantidade in range(1,len(caminhosdict)):
    print(f'rec em {quantidade}')
    rec = []
    for item in recIntDiaDur:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0])
        if len(nomes) == quantidade:
            rec.append(item)
    if len(rec) == 0:
        break
    rec = f_a.sem_cont_inter(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'recorrências IntDiaDur sem cont e inter, tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

for quantidade in range(1,len(caminhosdict)):
    print(f'sec em {quantidade}')
    rec = []
    for item in seqIntDiaDur:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0][0])
        if len(nomes) == quantidade:
            rec.append(item)
    if len(rec) == 0:
        break
    rec = f_a.sem_cont_inter_seq(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'sequências IntDiaDur sem cont e inter, tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)
del recIntDiaDur, seqIntDiaDur

for quantidade in range(1,len(caminhosdict)):
    print(f'rec em {quantidade}')
    rec = []
    for item in recIntDiaDurPtempo:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0])
        if len(nomes) == quantidade:
            rec.append(item)
    if len(rec) == 0:
        break
    rec = f_a.sem_cont_inter(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'recorrências IntDiaDurPtempo sem cont e inter, tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

for quantidade in range(1,len(caminhosdict)):
    print(f'sec em {quantidade}')
    rec = []
    for item in SeqIntDiaDurPtempo:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0][0])
        if len(nomes) == quantidade:
            rec.append(item)
    if len(rec) == 0:
        break
    rec = f_a.sem_cont_inter_seq(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'sequências IntDiaDurPtempo sem cont e inter, int e dur de tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

for quantidade in range(1,len(caminhosdict)):
    print(f'rec em {quantidade}')
    rec = []
    for item in recIntDiaDurPcompasso:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0])
        if len(nomes) == quantidade:
            rec.append(item)
    if len(rec) == 0:
        break
    rec = f_a.sem_cont_inter(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'recorrências IntDiaDurPcompasso sem cont e inter, tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

for quantidade in range(1,len(caminhosdict)):
    print(f'sec em {quantidade}')
    rec = []
    for item in SeqIntDiaDurPcompasso:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0][0])
        if len(nomes) == quantidade:
            rec.append(item)
    if len(rec) == 0:
        break
    rec = f_a.sem_cont_inter_seq(rec)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'sequências IntDiaDurPcompasso sem cont e inter, int e dur de tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

"""