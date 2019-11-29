import dirEinp as f_d
import xmldict as f_xd
import insp as f_i

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
    print(f'convertendo {nome}', caminhosconverter.index(caminho)+1,' de ', len(caminhosconverter))
    if '.xml' in caminho:
        xml = f_d.entrada_xml(caminho)
    elif '.mxl' in caminho:
        xml = f_d.entrada_mxl(caminho, nome)
    xml = f_xd.ad_counter(xml)
    xmlDicio = f_xd.xml_dict(xml)
    mDicio = f_xd.mus_dict(xmlDicio)
    mDicio.setdefault('nome',nome)
    f_d.escreve_pickle(diD, mDicio, nome)
print()

#lista com todos os dicionarios
caminhosdict = f_d.caminhos_extensoes(diD, ['.p'])
#puxa as caracteristicas do primeiro dicionario e confere para que todos tenham as mesmas
mDicio = f_d.le_pickle(caminhosdict[0])
caracteristicas = [k for k in mDicio['P1'].keys()]
for caminho in caminhosdict:
    mDicio = f_d.le_pickle(caminho)
    assert(caracteristicas == [k for k in mDicio['P1'].keys()])


#executa as analises criadas
for analisePar, analiseLog in zip(analisesPar, analisesLog):
    analise = {}
    #segmentacao
    for caminho in caminhosdict:
        print('segmentando ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
        mDicio = f_d.le_pickle(caminho)
        analise = analisePar[0][1][0](mDicio, analise)
    #filtros e ordenacoes
    for filtroord in analisePar[1:]:
        print(filtroord[0], analisePar[1:].index(filtroord)+1,' de ', len(analisePar[1:]))
        analise = filtroord[1][0](analise)
    #salva o log e a analise
    #nomes de todos os arquivos, que é o nome da música
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    nomesmusicas = [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhosdict]
    loganalise = {'nomes': nomesmusicas, 'quantidade': len(nomesmusicas), 'parametros': analiseLog}
    f_d.escreve_txt(diA,loganalise, nomeanalise)
    f_d.escreve_txt(diA,analise, nomeanalise)

'''

Pensar em um jeito de igualar sound tempo e metronome

fazer inputs de parametros do modulo
OK testar e refinar funcoes de analise:
OK    melhorar eficiencia dos contidos e amontoados ordenando antes de fazer o loop


limpar inputs, não é prioridade mas é o que falta

talvez seja melhor fazer várias condições já na função de segmentação em vez de funções filtros depois da segmentação.
tamanho do segmento <= que, (ou a mesma condicao vista pera diferença de p1p2)
por alguma outra caracteristica da posição (inicio do compasso, duração == tamanho do compasso)
para os que acontecem também na música ou também no compasso ou também no andamento é possível filtrar direto
para os que acontecem exclusivamente nessas carácteristicas é necessário ver todos e filtrar depois

homogeneidade dos valores:
    ver distribuição dos valores agredgados as posições
    quantas categorias e quantas vezes em cada categoria, quantos% em cada categoria
    música, posição tempo e posicao compasso
'''
