import dirEinp as f_d
import xmldict as f_xd
import insp as f_i

<<<<<<< HEAD
<<<<<<< HEAD
#pede diretorio do usuário e cria pastas e caminhos que vão ser usados
=======
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
=======
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
di = f_d.diretorio_ler('.xml')
diD = di+'\\Dicts'
diA = di+'\\Analises'
f_d.cria_pasta(diD)
f_d.cria_pasta(diA)

#converte xmls que não existem na pasta Dicts e salva usando pickle
caminhosxml = f_d.xml_sem_dict(f_d.caminhos_extensao(di, '.xml'), f_d.caminhos_extensao(diD, '.p'))
for xml in caminhosxml:
    nome = f_d.caminho_nome(xml, '.xml')
    xml = f_d.entrada_xml(xml)
    xml = f_xd.ad_counter(xml)
    xmlDicio = f_xd.xml_dict(xml)
    mDicio = f_xd.mus_dict(xmlDicio)
    mDicio.setdefault('nome',nome)
    f_d.escreve_pickle(diD, mDicio, nome)

caminhosdict = f_d.caminhos_extensao(diD, '.p')
mDicio = f_d.le_pickle(caminhosdict[0])
nomesmusicas = [f_d.caminho_nome(caminho, '.p') for caminho in caminhosdict]
caracteristicas = [k for k in mDicio['P1'].keys()]
prontas = ['asdf']
analisesPar = f_i.analisesPar_(caracteristicas, prontas, [])

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
for analisePar in analisesPar:
    aDicio = {}
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
    for caminho in caminhosdict:
        mDicio = f_d.le_pickle(caminho)
<<<<<<< HEAD
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
=======
=======
for analisePar in analisesPar:
    aDicio = {}
    for caminho in caminhosdict:
        mDicio = f_d.le_pickle(caminho)
>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
        analise = analisePar['segmentacao'][0](mDicio, aDicio)
    for nome, funcao in analisePar.items():
        if nome != 'segmentacao':
            analise = funcao[0](aDicio)

    numeroanalise = len(f_d.caminhos_extensao(diA, '.txt'))+1
    nomeanalise = f'analise {numeroanalise}'
    loganalise = {'nomes': nomesmusicas, 'quantidade': len(nomesmusicas), 'parametros': analisePar}
    f_d.escreve_txt(diA,loganalise, numeroanalise)
    f_d.escreve_txt(diA,analise, numeroanalise)

>>>>>>> parent of a10ca0a... salvando parametros criados e criando a partir de criados
'''
verificar lógica das funcoes uma a uma

'''
'''
levantar erros ao ler xml quando:
    a primeira tag não for <score-part-wise>
    quando encontrar as mensagens <backward> <forward> <chord>


Fazer uma análise com os exclusivos de cada música, marcando os contidos e encavalados
Fazer uma análise com os exclusivos de cada música, retirando os contidos e encavalados

homogeneidade dos valores:
    ver distribuição dos valores agredgados as posições
    quantas categorias e quantas vezes em cada categoria, quantos% em cada categoria
    música, posição tempo e posicao compasso
'''
