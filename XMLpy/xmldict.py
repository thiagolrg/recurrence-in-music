import conversoes as f_c
import xmltodict

def ad_counter(arquivo):
    counter = 0
    xml = []
    chord = False
    for p in range(len(arquivo)):
        #assert 'score-timewise' not in arquivo[p], 'XML é score-timewise, não implementado'
        #assert 'chord' not in arquivo[p], 'tag "chord" no XML. Não podem existir notas simultâneas na mesma parte'
        #assert '<backup>' not in arquivo[p], 'tag "backup" no XML. Não podem existir notas simultâneas na mesma parte'
        #assert '<forward>' not in arquivo[p], 'tag "forward" no XML. Não podem existir notas simultâneas na mesma parte'
        xml.append(arquivo[p])
        if p > 2 and p < len(arquivo):
            if '</' not in xml[p] and '/>' not in xml[p] and '<!' not in xml[p]:
                xml[p] = xml[p].rstrip('>')+' counter ='+'"'+str(counter)+'"'+'>'       
        if 'chord' in arquivo[p]:
            chord = True
        if '<duration>' in arquivo[p]:
            duration = int(arquivo[p].replace('<duration>','').replace('</duration>',''))
            if '<backup>' in arquivo[p-1]:
                counter = counter - duration
            elif chord == True:
                chord = False
            else:
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
    xmlD = {}
    for part in to_list(xml['score-partwise']['part']):
        partID = part['@id']
        #numero do compasso
        for measure in to_list(part['measure']):
            measureN = int(measure['@number'])

            #atributos do compasso
            if measure['attributes'] != None:
                for attributes in to_list(measure['attributes']):

                    #divisions
                    if 'divisions' in attributes:
                        divisions = int(attributes['divisions'])
                        try:
                            assert(divisions != xmlD['divisions'])
                        except KeyError:
                            xmlD.setdefault('divisions', divisions)

                    #keys
                    if 'key' in attributes:
                        for k in to_list(attributes['key']):
                            key = ((int(k['@counter']), measureN) , f_c.key_(int(k['fifths']), k['mode']))
                            try:
                                if key not in xmlD['keys']:
                                    keylocs = [f_c.loc(x) for x in xmlD['keys']]
                                    assert(f_c.loc(key) not in keylocs)
                                    xmlD.setdefault('keys', []).append(key)
                            except KeyError:
                                xmlD.setdefault('keys', []).append(key)
                    
                    #times
                    if 'time' in attributes:
                        for t in to_list(attributes['time']):
                            time = [[int(t['@counter']), measureN], (int(t['beats']), int(t['beat-type']))]
                            try:
                                if time not in xmlD['times']:
                                    timelocs = [f_c.loc(x) for x in xmlD['times']]
                                    assert(f_c.loc(time) not in timelocs)
                                    xmlD.setdefault('times', []).append(time)
                            except:
                                xmlD.setdefault('times', []).append(time)
            
            #metronomes
            if 'direction' in measure:
                for direction in to_list(measure['direction']):
                    if 'direction-type' in direction:
                        for directionType in to_list(direction['direction-type']):
                            if 'metronome' in directionType:
                                for m in to_list(directionType['metronome']):
                                    metronome = ((int(m['@counter']), measureN), (m['beat-unit'], int(m['per-minute'])))
                                    try:
                                        if metronome not in xmlD['metronomes']:
                                            metronomelocs = [f_c.loc(x) for x in xmlD['metronomes']]
                                            assert(f_c.loc(metronome) not in metronomelocs)
                                            xmlD.setdefault('metronomes', []).append(metronome)
                                    except KeyError:
                                        xmlD.setdefault('metronomes', []).append(metronome)
            
            #notas
            for note in to_list(measure['note']):
                step = None
                octave = None
                alter = None 
                tie = None
                counter = int(note['@counter'])
                if 'rest' in note:
                    voice = int(note['voice'])
                    note = ((counter, measureN), (step,octave,alter,tie))
                    xmlD.setdefault('notes',{}).setdefault(partID, {}).setdefault(voice, []).append(note)
                    continue
                if 'tie' in note:
                    for tipo in to_list(note['tie']):
                        tie = tipo['@type']
                for pitch in to_list(note['pitch']): 
                    step = pitch['step']
                    octave = int(pitch['octave'])
                    if 'alter' in pitch:
                        alter = int(pitch['alter'])
                if 'chord' not in note:
                    voice = int(note['voice'])
                    note = ((counter, measureN), (step,octave,alter,tie))
                    xmlD.setdefault('notes',{}).setdefault(partID, {}).setdefault(voice, []).append(note)
                else:
                    counter = xmlD['notes'][partID][voice][-1][0][0]
                    note = ((counter, measureN), (step,octave,alter,tie))
                    xmlD.setdefault('notes',{}).setdefault(partID, {}).setdefault(voice, []).append(note)
    xmlD['times'] = f_c.times_com_duracoes(xmlD['times'])
    return xmlD

def mus_dict(xmlD, tie='stop', rest=None):
    musD = {}
    divisions = xmlD['divisions']
    for part, notes in xmlD['notes'].items():
        p = 0
        fim = False
        while p < len(notes):
            while f_c.tie(notes[p]) == tie or f_c.step(notes[p]) == rest:
                p += 1
            note1 = notes[p]
            timeRefn1 = f_c.referencia(note1,xmlD['times'])
            keyRef = f_c.referencia(note1,xmlD['keys'])
            metronome = f_c.referencia(note1,xmlD['metronomes'])
            Pcompasso = f_c.P_compasso(divisions,timeRefn1,note1)
            grau = f_c.grau_escala(keyRef,note1)
            Ptempo = f_c.P_tempo(divisions,timeRefn1,note1)
            Ntempo = f_c.N_tempo(divisions,timeRefn1,note1)
            musD.setdefault(part, {})
            musD[part].setdefault('notaStep', []).append(note1[1][0])
            musD[part].setdefault('notaOitava', []).append(note1[1][1])
            musD[part].setdefault('notaAlter', []).append(note1[1][2])
            musD[part].setdefault('Ncompasso', []).append(f_c.Ncompasso(note1))
            musD[part].setdefault('tonalidade', []).append(f_c.val(keyRef))
            musD[part].setdefault('Fcompasso', []).append(f_c.val(timeRefn1))
            musD[part].setdefault('andamento', []).append(f_c.val(metronome))
            musD[part].setdefault('grau',[]).append(grau)
            musD[part].setdefault('Pcompasso',[]).append(Pcompasso)
            musD[part].setdefault('Ptempo', []).append(Ptempo)
            musD[part].setdefault('Ntempo', []).append(Ntempo)
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
                timeRefn2 = f_c.referencia(note2,xmlD['times'])      
                duracao = f_c.duracao_inicio(divisions,timeRefn2,note2) - f_c.duracao_inicio(divisions,timeRefn1,note1)
                intDia = f_c.int_diatonico(note1,note2)
                intCro = f_c.int_cromatico(note1,note2)
                intQua = f_c.int_qualidade(intDia,intCro)
                musD[part].setdefault('duracao', []).append(duracao)
                musD[part].setdefault('intDia', []).append(intDia)
                musD[part].setdefault('intCro', []).append(intCro)
                musD[part].setdefault('intQua', []).append(intQua)    
    return musD