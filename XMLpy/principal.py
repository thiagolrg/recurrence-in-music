import dirEinp as f_d
import xmldict as f_xd
import analises2 as f_a
import timeit
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
    xmlDict = f_xd.xml_dict(xml)
    musDict = f_xd.mus_dict(xmlDict)
    musDict.setdefault('nome',nome)
    f_d.escreve_pickle(diD, musDict, nome)
#lista com todos os dicionarios
caminhosdict = f_d.caminhos_extensoes(diD, ['.p'])
print()

#cria resgata ou atualiza tamanho minimo necessário para pegar todas as recorrencias
#no conjunto de músicas
if len(caminhosconverter) > 0:
    tamanho = f_a.tam_min(caminhosdict)
    f_d.escreve_pickle(diA,tamanho, '_tamanho_', trunca=True)
else:
    try:
        tamanho = f_d.le_pickle(diA+'\\_tamanho_.p')
    except FileNotFoundError:
        tamanho = f_a.tam_min(caminhosdict, tamanho=100)
        f_d.escreve_pickle(diA,tamanho, '_tamanho_')

'''
for caminho in caminhosdict:
    seg = f_a.segmentacao([caminho], tamanho=tamanho)

    rec = f_a.recorrencias(seg)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, recorrências')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

    seq = f_a.sequencias(seg)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': f_d.caminho_nome(caminho, ['.p'])}
    parametros.setdefault('quantidade', len([caminho]))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, sequências')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in seq}, nomeanalise)
'''


seg = f_a.segmentacao(caminhosdict, tamanho=tamanho)
rec = f_a.sort_recorrencias(seg)

'''
print('rec em tudo')
rec = f_a.recorrencias(seg)
nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
parametros.setdefault('quantidade', len(caminhosdict))
parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, recorrências')
f_d.escreve_txt(diA, parametros, nomeanalise)
f_d.escreve_txt(diA, {x:y for x,y in rec}, nomeanalise)

print('seq em tudo')
seq = f_a.sequencias(seg)
nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
parametros.setdefault('quantidade', len(caminhosdict))
parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, sequências')
f_d.escreve_txt(diA, parametros, nomeanalise)
f_d.escreve_txt(diA, {x:y for x,y in seq}, nomeanalise)
'''

for quantidade in range(1,len(caminhosdict)):
    print(f'rec em {quantidade}')
    recq = []
    for item in rec:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0])
        if len(nomes) == quantidade:
            recq.append(item)
    if len(recq) == 0:
        break
    recq = f_a.sem_cont_rec(recq)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto, recorrências sem cont')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in recq}, nomeanalise)

'''
for quantidade in range(1,len(caminhosdict)):
    print(f'sec em {quantidade}')
    seqq = []
    for item in seq:
        nomes = set()
        for valor in item[1]:
            nomes.add(valor[0][0])
        if len(nomes) == quantidade:
            seqq.append(item)
    if len(seqq) == 0:
        break
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]}
    parametros.setdefault('quantidade', len(caminhosdict))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, que acontecem em {quantidade} músicas do conjunto, sequências')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA, {x:y for x,y in seqq}, nomeanalise)
'''