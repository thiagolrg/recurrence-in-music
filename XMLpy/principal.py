import dirEinp as f_d
import xmldict as f_xd
import insp as f_i

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

for analisePar in analisesPar:
    aDicio = {}
    for caminho in caminhosdict:
        mDicio = f_d.le_pickle(caminho)
        analise = analisePar['segmentacao'][0](mDicio, aDicio)
    for nome, funcao in analisePar.items():
        if nome != 'segmentacao':
            analise = funcao[0](aDicio)

    numeroanalise = len(f_d.caminhos_extensao(diA, '.txt'))+1
    nomeanalise = f'analise {numeroanalise}'
    loganalise = {'nomes': nomesmusicas, 'quantidade': len(nomesmusicas), 'parametros': analisePar}
    f_d.escreve_txt(diA,loganalise, numeroanalise)
    f_d.escreve_txt(diA,analise, numeroanalise)
'''
levantar erros ao ler xml quando:
    a primeira tag não for <score-part-wise>
    quando encontrar as mensagens <backward> <forward> <chord>

Fazer inputs com numeração para as opções OK
Ligar inputs a análise e salvar arquivos de parâmetros
pensar num jeito de automatizar a atualização das listas de input
definir entradas para segmentação e filtros
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