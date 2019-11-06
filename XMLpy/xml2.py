import conversoes as f_c
import xmltodict

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
with open(r'arquivos teste\MusicXML\k341k363\k363.xml') as f:
    arquivo = []
    for l in f.readlines():
        arquivo.append(l.strip().replace('\n', ''))

nome = 'nome'

def counter_arq_xml(arquivo):
    counter = 0
    xml = []
    for p in range(len(arquivo)):
        xml.append(arquivo[p])
        if p > 2 and p < len(arquivo):
            if '</' not in xml[p] and '/>' not in xml[p] and '<!' not in xml[p]:
                xml[p] = xml[p].rstrip('>')+' counter ='+'"'+str(counter)+'"'+'>'
        if '<duration>' in arquivo[p]:
            duration = int(arquivo[p].replace('<duration>','').replace('</duration>',''))
            counter = counter + duration
        if '</part>' in arquivo[p]:
            counter = 0
    return xmltodict.parse(''.join(xml))

def to_list(node):
    if isinstance(node, list) == True:
        return node
    else:
        return [node]

def xml_dict(xml):
    xmlDict = {}
    for part in to_list(xml['score-partwise']['part']):
        partID = part['@id']
        #numero do compasso
        for measure in to_list(part['measure']):
            measureN = int(measure['@number'])

            #atributos do compasso
            if 'attributes' in measure.keys():
                for attributes in to_list(measure['attributes']):

                    #divisions
                    if 'divisions' in attributes.keys():
                        divisions = int(attributes['divisions'])
                        try:
                            if divisions != xmlDict['divisions']:
                                raise ValueError ('divisions diferente')
                        except KeyError:
                            xmlDict.setdefault('divisions', divisions)

                    #keys
                    if 'key' in attributes.keys():
                        for k in to_list(attributes['key']):
                            key = ((int(k['@counter']), measureN) , f_c.key_(int(k['fifths']), k['mode']))
                            try:
                                if key not in xmlDict['keys']:
                                    keylocs = [f_c.loc(x) for x in xmlDict['keys']]
                                    if f_c.loc(key) in keylocs:
                                        raise ValueError ('keys diferentes')
                                    xmlDict.setdefault('keys', []).append(key)
                            except KeyError:
                                xmlDict.setdefault('keys', []).append(key)
                    
                    #times
                    if 'time' in attributes.keys():
                        for t in to_list(attributes['time']):
                            time = [[int(t['@counter']), measureN], (int(t['beats']), int(t['beat-type']))]
                            try:
                                if time not in xmlDict['times']:
                                    timelocs = [f_c.loc(x) for x in xmlDict['times']]
                                    if f_c.loc(time) in timelocs:
                                        raise ValueError ('times diferentes')
                                    xmlDict.setdefault('times', []).append(time)
                            except:
                                xmlDict.setdefault('times', []).append(time)
            
            #metronomes
            if 'direction' in measure.keys():
                for direction in to_list(measure['direction']):
                    if 'direction-type' in direction.keys():
                        for directionType in to_list(direction['direction-type']):
                            if 'metronome' in directionType.keys():
                                for m in to_list(directionType['metronome']):
                                    metronome = ((int(m['@counter']), measureN), (m['beat-unit'], int(m['per-minute'])))
                                    try:
                                        if metronome not in xmlDict['metronomes']:
                                            metronomelocs = [f_c.loc(x) for x in xmlDict['metronomes']]
                                            if f_c.loc(metronome) in metronomelocs:
                                                raise ValueError ('metronomes diferentes')
                                            xmlDict.setdefault('metronomes', []).append(metronome)
                                    except KeyError:
                                        xmlDict.setdefault('metronomes', []).append(metronome)
            
            #notas
            for note in to_list(measure['note']):
                counter = int(note['@counter'])
                step = None
                octave = None
                alter = None 
                tie = None
                if 'rest' in note.keys():
                    note = ((counter, measureN), (step,octave,alter,tie))
                    continue
                if 'tie' in note.keys():
                    tie = note['tie']['@type']
                for pitch in to_list(note['pitch']): 
                    step = pitch['step']
                    octave = int(pitch['octave'])
                    if 'alter' in pitch.keys():
                        alter = int(pitch['alter'])
                note = ((counter, measureN), (step,octave,alter,tie))
                xmlDict.setdefault('notes',{}).setdefault(partID, []).append(note)
    xmlDict['times'] = f_c.times_com_duracoes(xmlDict['times'])
    return xmlDict

def mus_dict(xmlDict, tie='stop', rest=None):
    mDict = {}
    divisions = xmlDict['divisions']
    for part, notes in xmlDict['notes'].items():
        p = 0
        fim = False
        while p < len(notes):
            while f_c.tie(notes[p]) == tie or f_c.step(notes[p]) == rest:
                p += 1
            note1 = notes[p]
            timeRefn1 = f_c.referencia(note1,xmlDict['times'])
            keyRef = f_c.referencia(note1,xmlDict['keys'])
            metronome = f_c.referencia(note1,xmlDict['metronomes'])
            Pcompasso = f_c.P_compasso(divisions,timeRefn1,note1)
            grau = f_c.grau_escala(keyRef,note1)
            Ptempo = f_c.P_tempo(divisions,timeRefn1,note1)
            Ntempo = f_c.N_tempo(divisions,timeRefn1,note1)
            mDict.setdefault(part, {})
            mDict[part].setdefault('nota', []).append(note1[0:3][0])
            mDict[part].setdefault('Ncompasso', []).append(f_c.Ncompasso(note1))
            mDict[part].setdefault('tonalidade', []).append(f_c.val(keyRef))
            mDict[part].setdefault('Fcompasso', []).append(f_c.val(timeRefn1))
            mDict[part].setdefault('andamento', []).append(f_c.val(metronome))
            mDict[part].setdefault('grau',[]).append(grau)
            mDict[part].setdefault('Pcompasso',[]).append(Pcompasso)
            mDict[part].setdefault('Ptempo', []).append(Ptempo)
            mDict[part].setdefault('Ntempo', []).append(Ntempo)
            p += 1
            if p < len(notes):
                while f_c.tie(notes[p]) == tie or f_c.step(notes[p]) == rest:
                    p += 1
                    if p == len(notes):
                        fim = True
                        break      
                if fim == True:
                    break
                note2 = notes[p]
                timeRefn2 = f_c.referencia(note2,xmlDict['times'])      
                duracao = f_c.duracao_inicio(divisions,timeRefn2,note2) - f_c.duracao_inicio(divisions,timeRefn1,note1)
                intDia = f_c.int_diatonico(note1,note2)
                intCro = f_c.int_cromatico(note1,note2)
                intQua = f_c.int_qualidade(intDia,intCro)
                mDict[part].setdefault('duracao', []).append(duracao)
                mDict[part].setdefault('intDia', []).append(intDia)
                mDict[part].setdefault('intCro', []).append(intCro)
                mDict[part].setdefault('intQua', []).append(intQua)    
    return mDict

def analise(keys, atribs, mDict, aDict, tudo=False):
    musica = mDict.copy()
    nome = musica.pop('nome')
    for part, atribsP in musica.items():
        if tudo == True:
            atribs = [key for key in atribsP.keys()]
            for key in keys:
                atribs.pop(atribs.index(key))
            abribs = [(x, 'p1p2') for x in abribs]
        for p1 in range(len(atribsP['grau'])):
            for p2 in range(p1+1,len(atribsP['grau'])):
                keyAnalise = []
                valueAnalise = [(nome, part, (p1,p2))]
                for key in keys:
                    keyp1 = atribsP[key[0]][p1]
                    keyp1p2 = tuple(atribsP[key[0]][p1:p2])
                    keyp1p2m1 = tuple(atribsP[key[0]][p1:p2-1])
                    if key[1] == 'p1':
                        keyAnalise.append(keyp1)
                    elif key[1] =='p1p2':
                        keyAnalise.append(keyp1p2)
                    elif key[1] == 'p2m1':
                        keyAnalise.append(keyp1p2m1)
                    elif key[1] == 'p1set':
                        keyAnalise.append(set(keyp1))
                    elif key[1] == 'p1p2set':
                        keyAnalise.append(set(keyp1p2))
                    elif key[1] == 'p2m1set':
                        keyAnalise.append(set(keyp1p2m1))
                if isinstance(keyAnalise, tuple) == False:
                    keyAnalise = tuple(keyAnalise)
                aDict.setdefault(keyAnalise, [{'nome': set()}])[0]['nome'].add(nome)
                for atrib in atribs:
                    atribp1 = atribsP[atrib[0]][p1]
                    atribp1p2 = tuple(atribsP[atrib[0]][p1:p2])
                    atribp2m1 = tuple(atribsP[atrib[0]][p1:p2-1])
                    if atrib[1] == 'p1':
                        valueAnalise.append(atribp1)
                    elif atrib[1] == 'p1p2':
                        valueAnalise.append(atribp1p2)
                    elif atrib[1] == 'p1p2m1':
                        valueAnalise.append(atribp2m1)
                    elif atrib[1] == 'p1set':
                        valueAnalise.append(set(atribp1))
                    elif atrib[1] == 'p1p2set':
                        valueAnalise.append(set(atribp1p2))
                    elif atrib[1] == 'p2m1set':
                        valueAnalise.append(set(atribp2m1))
                    elif atrib[1] == 'p1setg':
                        aDict[keyAnalise][0].setdefault(atrib[0], set()).add(atribp1)
                    elif atrib[1] == 'p1p2setg':
                        aDict[keyAnalise][0].setdefault(atrib[0], set()).add(atribp1p2)
                    elif atrib[1] == 'p2m1setg':
                        aDict[keyAnalise][0].setdefault(atrib[0], set()).add(atribp2m1)
                aDict.setdefault(keyAnalise,[]).append(valueAnalise)
    return aDict

def filtro_quantidade(aDict, atribslen):
    filtrado = {}
    for chave, valor in aDict.items():
        for atriblen in atribslen:
            if len(valor[0][atriblen[0]]) > atriblen[1]:
                filtrado.setdefault(chave,valor[1:])
    return filtrado

def filtro_tipo(aDict, atribs):
    filtrado = {}
    for chave, valor in aDict.items():
        for atrib in atribs:
            if all(valor[0][atrib[0]]) == atrib[1]:
                filtrado.setdefault(chave,valor[1:])
    return filtrado

def sort_tamKquanV(entrada):
    pronto = {}
    for chave, valor in sorted(entrada.items(), key=lambda item: (len(item[0][0]), len(item[1])), reverse=True):
        pronto.setdefault(chave, valor)
    return pronto

xml = counter_arq_xml(arquivo)
xmlDict = xml_dict(xml)
mDict = mus_dict(xmlDict)
mDict.setdefault('nome',nome)

aDict = {}
intDia_dur__Ncomp_Pcomp = analise([('intDia','p1p2'),('duracao','p1p2')],[('Ncompasso','p1'),('Pcompasso','p1')], mDict, aDict)
grau_intDia_dur__Ncompasso_Pcompasso = analise([('grau', 'p1p2'), ('intDia', 'p2m1'), ('duracao', 'p2m1')],[('Ncompasso', 'p1'),('Pcompasso', 'p1'),('tonalidade', 'p1p2set')], mDict, aDict)

'''
duracao_intDia = analise(mDict,['duracao'],[1],['intDia'],[1])
intDia_duracao = analise(mDict,['intDia'],[1],['duracao'],[1])
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
carácteristicas para recorrência        outros atribs para mostrar no momento   
tipo                                    tipo

log de progresso
Total de xml :
verificando convertidos: nome do arquivo, posicao na lista de nomes, de, tamanho da lista de nomes
convertendo novos: nome do arquivo, . dict, salvo, posicao na lista de nomes, de, tamanho da lista de nomes
análise 1:
analisando: nome do arquivo, posicao na lista de nomes, de, tamanho da lista de nomes
filtrando por quantidade de músicas
organizando por tamanho e quantidade de vezes que aparece
análise 1 salvo
análise 2:
analisando: nome do arquivo, posicao na lista de nomes, de, tamanho da lista de nomes
filtrando por quantidade de músicas
organizando por tamanho e quantidade de vezes que aparece
análise 2 salvo
análise ...:
Pronto
'''
debug = 0