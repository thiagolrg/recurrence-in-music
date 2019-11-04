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
    musDict = {}
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
            musDict.setdefault(part, {})
            musDict[part].setdefault('Ncompasso', []).append(f_c.Ncompasso(note1))
            musDict[part].setdefault('tonalidade', []).append(f_c.val(keyRef))
            musDict[part].setdefault('Fcompasso', []).append(f_c.val(timeRefn1))
            musDict[part].setdefault('andamento', []).append(f_c.val(metronome))
            musDict[part].setdefault('grau',[]).append(grau)
            musDict[part].setdefault('Pcompasso',[]).append(Pcompasso)
            musDict[part].setdefault('Ptempo', []).append(Ptempo)
            musDict[part].setdefault('Ntempo', []).append(Ntempo)
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
                musDict[part].setdefault('duracao', []).append(duracao)
                musDict[part].setdefault('intDia', []).append(intDia)
                musDict[part].setdefault('intCro', []).append(intCro)
                musDict[part].setdefault('intQua', []).append(intQua)    
    return musDict

def analise(musicaDict, keys, keystype, atribs, atribstype, tudo=False):
    musica = musicaDict.copy()
    nome = musica.pop('nome')
    analiseDict = {}
    for part, atrib1 in musica.items():
        if tudo == True:
            atribs = [key for key in atrib1.keys()]
            for key in keys:
                atribs.pop(atribs.index(key))
        for p1 in range(len(atrib1['intDia'])):
            for p2 in range(p1+1,len(atrib1['intDia'])):
                valueAnalise = []
                keyAnalise = []
                loc = (nome, part, (p1,p2))
                valueAnalise.append(loc)
                for key, ktype in zip(keys, keystype):
                    if ktype == 0:
                        keyAnalise.append(atrib1[key][p1])
                    elif ktype == 1:
                        keyAnalise.append(tuple(atrib1[key][p1:p2]))
                    elif ktype == 2:
                        keyAnalise.append(tuple(atrib1[key][p1:p2-1]))
                    elif atype == 3:
                        valueAnalise.append(set(atrib1[atrib2][p1:p2]))
                    elif atype == 4:
                        valueAnalise.append(set(atrib1[atrib2][p1:p2-1]))
                keyAnalise = tuple(keyAnalise)
                for atrib2, atype in zip(atribs,atribstype):
                    if atype == 0:
                        valueAnalise.append(tuple(atrib1[atrib2][p1:p2]))
                    elif atype == 1:
                        valueAnalise.append(tuple(atrib1[atrib2][p1:p2-1]))
                    elif atype == 2:
                        valueAnalise.append(atrib1[atrib2][p1])
                    elif atype == 3:
                        valueAnalise.append(set(atrib1[atrib2][p1:p2]))
                    elif atype == 4:
                        valueAnalise.append(set(atrib1[atrib2][p1:p2-1]))
                analiseDict.setdefault(keyAnalise,[]).append(valueAnalise)
    return analiseDict

xml = counter_arq_xml(arquivo)
xmlDict = xml_dict(xml)
musDict = mus_dict(xmlDict)
musDict.setdefault('nome',nome)

intDia = analise(musDict,['intDia','duracao'],[1,1],['Ncompasso','Pcompasso'],[0,0])
grau = analise(musDict,['grau', 'intDia','duracao'],[1,2,2],['Ncompasso','Pcompasso','tonalidade'],[0,0,3])
duracao_intDia = analise(musDict,['duracao'],[1],['intDia'],[1])
intDia_duracao = analise(musDict,['intDia'],[1],['duracao'],[1])

'''
formas de pesquisa:

0= p1 = só o primeiro valor do trecho
1= p1:p2 = trecho completo
2= p1:(p2-1) = trecho completo menos o último valor, como para intervalos e graus
3= set p1 = somente valores unicos do trecho
4= set p2-1 = somente valores unicos do trecho menos o último

tudo - True, todos os valores que não estão na chave aparecem no resultado
'''

debug = 0