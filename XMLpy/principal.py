import dirEinp as f_d
import xmldict as f_xd
import analises as f_a
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
    xmlDicio = f_xd.xml_dict(xml)
    mDicio = f_xd.mus_dict(xmlDicio)
    mDicio.setdefault('nome',nome)
    f_d.escreve_pickle(diD, mDicio, nome)
#lista com todos os dicionarios
caminhosdict = f_d.caminhos_extensoes(diD, ['.p'])
print()

#cria resgata ou atualiza tamanho minimo necessário para pegar todas as recorrencias
#no conjunto de músicas
if len(caminhosconverter) > 0:
    tamanho = f_a.tamanho_todasrecorrencias (caminhosdict)
    f_d.escreve_pickle(diA,tamanho, '_tamanho_', trunca=True)
else:
    try:
        tamanho = f_d.le_pickle(diA+'\\_tamanho_.p')
    except FileNotFoundError:
        tamanho = f_a.tamanho_todasrecorrencias(caminhosdict)
        f_d.escreve_pickle(diA,tamanho, '_tamanho_')

for caminhodict in caminhosdict:
    caminhodict = [caminhodict]

    tamanho = f_a.tamanho_todasrecorrencias(caminhodict)

    le = 0
    aDicio = f_a.analise1(caminhodict, tamanho, le)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhodict]}
    parametros.setdefault('quantidade', len(caminhodict))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, > {le} continuam depois de contidos e amontoados retirados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA,aDicio, nomeanalise)

    le = 1
    aDicio = f_a.analise1(caminhodict, tamanho, le)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhodict]}
    parametros.setdefault('quantidade', len(caminhodict))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, > {le} continuam depois de contidos e amontoados retirados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA,aDicio, nomeanalise)

    tamanho = f_a.tamanho_maiorquantidade(caminhodict)

    le = 0
    aDicio = f_a.analise1(caminhodict, tamanho, le)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhodict]}
    parametros.setdefault('quantidade', len(caminhodict))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, > {le} continuam depois de contidos e amontoados retirados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA,aDicio, nomeanalise)

    le = 1
    aDicio = f_a.analise1(caminhodict, tamanho, le)
    nomeanalise = 'analise'+str(len(f_d.caminhos_extensoes(diA, ['.txt']))+1)
    parametros = {'nomes': [f_d.caminho_nome(caminho, ['.p']) for caminho in caminhodict]}
    parametros.setdefault('quantidade', len(caminhodict))
    parametros.setdefault('analise', f'int e dur de tamanhomax {tamanho}, > {le} continuam depois de contidos e amontoados retirados')
    f_d.escreve_txt(diA, parametros, nomeanalise)
    f_d.escreve_txt(diA,aDicio, nomeanalise)

'''
tamanhomaior deixa 1
tamanhomaior nao deixa 1
tamanho quantidadedeixa 1
tamanoquantidade naodeixa 1
'''


'''
testar um tirando todos os que acontecem <=1 vezes
testar um marcando os contidos e amontoados
testar um organizando por quantidade de músicas em que aparece, do maior para o menor.
colocar numeros e posicoes de compassos

intDia duração e Pcompasso: Loc....


'''

'''
#executa as analises criadas
for analisePar, analiseLog in zip(analisesPar, analisesLog):
    analise = {}
    #segmentacao
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
'''
testar função part_of

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
