import dirEinp as f_d
import xmldict as f_xd
import insp as f_i

#pede diretorio do usuário e cria pastas e caminhos que vã oser usados
di = f_d.diretorio_ler('.xml')
diD = di+'\\Dicts'
diA = di+'\\Analises'
diP = di+'\\Parametros'
cPar = diP+'\\parametros.p'
f_d.cria_pasta(diD)
f_d.cria_pasta(diA)
f_d.cria_pasta(diP)

#converte xmls que não existem na pasta Dicts e salva usando pickle
caminhosxml = f_d.xml_sem_dict(f_d.caminhos_extensao(di, '.xml'), f_d.caminhos_extensao(diD, '.p'))
for xml in caminhosxml:
    print('convertendo xml', caminhosxml.index(xml)+1,' de ', len(caminhosxml))
    nome = f_d.caminho_nome(xml, '.xml')
    xml = f_d.entrada_xml(xml)
    xml = f_xd.ad_counter(xml)
    xmlDicio = f_xd.xml_dict(xml)
    mDicio = f_xd.mus_dict(xmlDicio)
    mDicio.setdefault('nome',nome)
    f_d.escreve_pickle(diD, mDicio, nome)
print()

#lista com todos os dicionarios
caminhosdict = f_d.caminhos_extensao(diD, '.p')
#puxa as caracteristicas do primeiro dicionario e confere para que todos tenham as mesmas
mDicio = f_d.le_pickle(caminhosdict[0])
caracteristicas = [k for k in mDicio['P1'].keys()]
for caminho in caminhosdict:
    mDicio = f_d.le_pickle(caminho)
    assert(caracteristicas == [k for k in mDicio['P1'].keys()])

#abre o arquivo de parametros criados, caso exista
#pede inputs de parametros do usuário (precisa das caracteristicas e parametros criados)
try:
    prontosPar = f_d.le_pickle(cPar)
except FileNotFoundError:
    prontosPar = []
analisesPar = f_i.analisesPar_(caracteristicas, prontosPar, [])
analisesLog = [dict([(x,y[1]) for x,y in a.items()]) for a in analisesPar]

#atualiza o arquivo de parametros com novos criados, caso existam
try:
    f_d.escreve_pickle(diP, analisesLog, 'parametros')
except FileExistsError:
    prontosPar = f_d.le_pickle(cPar)
    for analise in analisesLog:
        if analise not in prontosPar:
            prontosPar.append(analise)
    f_d.escreve_pickle(diP, prontosPar, 'parametros', trunca=True)

#executa as analises criadas
for analisePar in analisesPar:
    analiseLog = dict([(x,y[1]) for x,y in analisePar.items()])
    aDicio = {}
    #segmentacao
    for caminho in caminhosdict:
        print('segmentando ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
        mDicio = f_d.le_pickle(caminho)
        analise = analisePar['segmentacao'][0](mDicio, aDicio)
    analisePar.pop('segmentacao')
    #filtros e ordenacoes
    for nome, funcao in analisePar.items():
        print(nome, [x for x in analisePar.keys()].index(nome)+1,' de ', len(analisePar.keys()))
        if nome != 'segmentacao':
            analise = funcao[0](aDicio)
    #salva o log e a analise
    #nomes de todos os arquivos, que é o nome da música
    numeroanalise = len(f_d.caminhos_extensao(diA, '.txt'))+1
    nomeanalise = f'analise {numeroanalise}'
    nomesmusicas = [f_d.caminho_nome(caminho, '.p') for caminho in caminhosdict]
    loganalise = {'nomes': nomesmusicas, 'quantidade': len(nomesmusicas), 'parametros': analiseLog}
    f_d.escreve_txt(diA,loganalise, nomeanalise)
    f_d.escreve_txt(diA,analise, nomeanalise)

'''
verificar lógica das funcoes uma a uma
descobrir porque o dicionario na posicoes[0] nao esta sendo retirado
descobrir porque novas analises não estão sendo salvas no arquivo parametros
talvez porque o dicionario mesmo em outra ordem deja considerado o mesmo?

'''
'''
levantar erros ao ler xml quando:
    a primeira tag não for <score-part-wise>
    quando encontrar as mensagens <backward> <forward> <chord>

homogeneidade dos valores:
    ver distribuição dos valores agredgados as posições
    quantas categorias e quantas vezes em cada categoria, quantos% em cada categoria
    música, posição tempo e posicao compasso
'''
