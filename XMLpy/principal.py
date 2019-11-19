import dirEinp as f_d
import xmldict as f_xd
import insp as f_i

#pede diretorio do usuário e cria pastas e caminhos que vão ser usados
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

#abre o arquivo de parametros salvos, caso exista
#pede inputs de parametros do usuário (precisa das caracteristicas e parametros salvos)
try:
    salvosPar = f_d.le_pickle(cPar)
except FileNotFoundError:
    salvosPar = []
analisesPar = f_i.analisesPar_(caracteristicas, salvosPar, [])
analisesLog = f_i.analisesLog_(analisesPar)

#atualiza o arquivo de parametros com novos criados, caso existam
try:
    f_d.escreve_pickle(diP, analisesLog, 'parametros')
except FileExistsError:
    salvosPar = f_d.le_pickle(cPar)
    for analiseLog in analisesLog:
        if analiseLog not in salvosPar:
            salvosPar.append(analiseLog)
    f_d.escreve_pickle(diP, salvosPar, 'parametros', trunca=True)


#executa as analises criadas
for analisePar, analiseLog in zip(analisesPar, analisesLog):
    analise = {}
    #segmentacao
    for caminho in caminhosdict:
        print('segmentando ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
        mDicio = f_d.le_pickle(caminho)
        analise = analisePar[0][1][0](mDicio, analise)
        debug = 0
    #filtros e ordenacoes
    for filtroord in analisePar[1:]:
        print(filtroord[0], analisePar[1:].index(filtroord)+1,' de ', len(analisePar[1:]))
        analise = filtroord[1][0](analise)
    #salva o log e a analise
    #nomes de todos os arquivos, que é o nome da música
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensao(diA, '.txt'))+1)
    nomesmusicas = [f_d.caminho_nome(caminho, '.p') for caminho in caminhosdict]
    loganalise = {'nomes': nomesmusicas, 'quantidade': len(nomesmusicas), 'parametros': analiseLog}
    f_d.escreve_txt(diA,loganalise, nomeanalise)
    f_d.escreve_txt(diA,analise, nomeanalise)

'''
refazer condicao de ti e rest na funcao xml_dict...
Se tie(nota1) == 'start', busca nota2 até que tie de nota2 seja None e Nota2 não seja pausa 

'''


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
