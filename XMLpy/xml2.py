import dirinp as f_d
import xmldict as f_xd
import analises as f_a

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
    xmlD = f_xd.xml_dict(xml)
    musD = f_xd.mus_dict(xmlD)
    musD.setdefault('nome',nome)
    f_d.escreve_pickle(diD, musD, nome)

caminhosdict = f_d.caminhos_extensao(diD, '.p')
nomes = [f_d.caminho_nome(caminho, '.p') for caminho in caminhosdict]
quantidade = len(nomes)

parametrosanalises = [{'keys': [('intDia','p1p2'),('duracao','p1p2')], 'atribs': [('Ncompasso','p1'),('Pcompasso','p1')],
             'filtroQT': {'posicao': 2},
             'filtroTP': [{'nome': ['k363']},True]}]
n = len(f_d.caminhos_extensao(diA, '.txt'))+1
for parametros in parametrosanalises:
    print('Analise:\n', parametrosanalises.index(parametros)+1, 'de', len(parametrosanalises))
    nomeanalise = f'analise {n}'
    log = {'nomes': nomes, 'quantidade': len(nomes), 'parametros': parametros}
    aDict = {}
    print('segmentacao:')
    for caminho in caminhosdict:
        print(caminhosdict.index(caminho)+1, 'de', len(caminhosdict),'      ')
        musD = f_d.le_pickle(caminho)
        analise = f_a.segmentacao_(parametros['keys'], parametros['atribs'], musD, aDict)
    print('filtros:     ')
    analise = f_a.filtro_quantidade(analise, parametros['filtroQT'])
    analise = f_a.filtro_contém(analise, parametros['filtroTP'])
    analise = f_a.sort_tamKquanV(analise)
    analise = f_a.filtro_nested(analise)
    f_d.escreve_txt(diA,log, nomeanalise)
    f_d.escreve_txt(diA,analise, nomeanalise)
    n += 1

'''
levantar erros ao ler xml quando:
    a primeira tag não for <score-part-wise>
    quando encontrar as mensagens <backward> <forward> <chord>

Fazer inputs com numeração para as opções
Ligar inputs a análise e salvar arquivos de parâmetros
pensar num jeito de automatizar a atualização das listas de input,
talvez algo que me mostra todas as def no modulo e permita executar todas
assim posso criar uma chave para def no dicionário pedindo os valores das def

somente segmentos que ocorrem pelomenos em n músicas (quantidade de nomes)
Tipos de carácteristica inclusivo e exclusivo
ou que ocorrem pelo menos n vezes (quantidade de posições)
tamanho do segmento (p2-p1)
duração do segmento

Fazer uma análise com os exclusivos de cada música, marcando os contidos e encavalados
Fazer uma análise com os exclusivos de cada música, retirando os contidos e encavalados

Posições em tuples contidas em listas pode ser útil para dar append nas informações de truncado e contido
o truncado de acontece antes é o que tem p1<, ver whatzapp do Flávio

homogeneidade dos valores:
    ver distribuição dos valores agredgados as posições
    quantas categorias e quantas vezes em cada categoria, quantos% em cada categoria
    música, posição tempo e posicao compasso
'''
'''
parametrosanalises = [{'keys': [('intDia','p1p2'),('duracao','p1p2')], 'atribs': [('Ncompasso','p1'),('Pcompasso','p1')],
             'filtroQT': {'nome':2},
             'filtroTP': {None}},
            {'keys': [('intDia','p1p2'),('duracao','p1p2')], 'atribs': [('Ncompasso','p1'),('Pcompasso','p1')],
             'filtroQT': {'nome':2},
             'filtroTP': {None}}]
'''
'''
[[[],[]], [[],[]], [[],[]]],[[][][]]
[0] = primeira analise
[1] = segunda analise...
[0][0] = parametros da analise
[0][1] = parametros filtro 1
[0][2] = parametros filtro 2
para cada análise salvar o arquivo log e acrescentar o txt da análise

log:
quantas musicas
quais musicas
parametros da análise
filtros

trazer fitro nested para o .xml
filtro de segmentos
filtro de quantidade de vezes independente da música em que aparece
'''
'''
formas de pesquisa:

0= p1 = só o primeiro valor do trecho
1= p1:p2 = trecho completo
2= p1:(p2-1) = trecho completo menos o último valor, como para intervalos e graus
3= set p1:p2 = somente valores unicos do trecho
4= set p2-1 = somente valores unicos do trecho menos o último
5= setdict somente valores únicos de TODOS os trechos

tudo - True, todos os valores que não estão na chave aparecem no resultado
'''
'''
1.input usuário (diretório com xml)
2.se diretório existe e contém xml
    faz uma lista com o caminho de todos os arquivos xml
    se no diretório existe pasta 'dicts'
        se na pasta 'dicts' existem arquivos com o mesmo nome dos arquivos da lista de caminhos
            remove nomes da lista caminhos que existem na pasta 'dicts'
3.se sobrarem caminhos na lista caminhos
    converte caminhos para dicts e salva na pasta dicts
    para cada caminho
        abre, limpa, counter, xml, dict, mus, salva, próximo
4.para cada arquivo na pasta 'Dicts'
    funções de recorrência
salva resultados em .dict e .txt 
'''
'''
def diretório de input:
    se contiver xml
        cria pastas 'dict', 'análise'
    se não:
        print ('diretorio não contem xml')
        return (diretório de input)

Caixa de diálogo
    certifique-se de que os arquivos xml só contém uma melodia por parte,
    (sem layers, chord, backup, foward, ou voices diferentes)

    botão ok

Caixa diálogo:
características para recorrência        outros atribs para mostrar no momento   
tipo                                    tipo

Filtros:
característica      quantidade      tipo

log de progresso
Total de xml :
verificando convertidos: nome do arquivo, posicao na lista de nomes, de, tamanho da lista de nomes
convertendo novos: nome do arquivo, . dict, salvo, posicao na lista de nomes, de, tamanho da lista de nomes
análise 1:
analisando: nome do arquivo, posicao na lista de nomes, de, tamanho da lista de nomes
filtrando por quantidade de músicas
filtrando por tipo ou quantidade de:
filtrando por tipo ou quantidade de:
Orgalizando por tamanho da chave quantidade de valores por chave
análise 1 salvo
análise 2:
analisando: nome do arquivo, posicao na lista de nomes, de, tamanho da lista de nomes
filtrando por quantidade de músicas
filtrando por tipo ou quantidade de:
filtrando por tipo ou quantidade de:
Orgalizando por tamanho da chave quantidade de valores por chave
análise 2 salvo
análise ...:
Pronto
'''
debug = 0