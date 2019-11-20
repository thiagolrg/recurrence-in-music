import conversoes as f_c
import xmltodict

def ad_counter(arquivo):
    counter = 0
    xml = []
    chord = False
    for p in range(len(arquivo)):
        assert 'score-timewise' not in arquivo[p], NotImplementedError('XML é score-timewise')
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
            if 'attributes' in measure and measure['attributes'] != None:
                for attributes in to_list(measure['attributes']):

                    #divisions
                    if 'divisions' in attributes:
                        divisions = int(attributes['divisions'])
                        try:
                            assert divisions == xmlD['divisions']
                        except KeyError:
                            xmlD.setdefault('divisions', divisions)

                    #keys
                    if 'key' in attributes:
                        for k in to_list(attributes['key']):
                            assert 'mode' in k, '"key" sem "mode" no XML'
                            assert 'fifths' in k, '"key" sem "fifths" no XML'
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
                    tie = to_list(note['tie'])[-1]['@type']
                for pitch in to_list(note['pitch']): 
                    step = pitch['step']
                    octave = int(pitch['octave'])
                    if 'alter' in pitch:
                        alter = int(pitch['alter'])
                if 'chord' in note:
                    if isinstance(xmlD['notes'][partID][voice][-1], list) == False:
                        xmlD['notes'][partID][voice][-1] = [xmlD['notes'][partID][voice][-1]]
                    counter = xmlD['notes'][partID][voice][-1][0][0][0]
                    note = ((counter, measureN), (step,octave,alter,tie))
                    counter = xmlD['notes'][partID][voice][-1].append(note)
                else:
                    assert 'voice' in note, '"note" sem "voice"'
                    voice = int(note['voice'])
                    note = ((counter, measureN), (step,octave,alter,tie))
                    xmlD.setdefault('notes',{}).setdefault(partID, {}).setdefault(voice, []).append(note)
    xmlD['times'] = f_c.times_com_duracoes(xmlD['times'])
    assert 'metronomes' in xmlD,'algo faltando no xml?, nao foram extraidos metronomos'
    assert 'keys' in xmlD,'algo faltando no xml?, nao foram extraidas armaduras'
    assert 'times' in xmlD,'algo faltando no xml?, nao foram extraidas formulas de compasso'
    assert 'notes' in xmlD,'algo faltando no xml?, nao foram extraidas notas'
    return xmlD

def mus_dict(xmlD, tie=None, rest=None, chord=True):
    musD = {}
    divisions = xmlD['divisions'] 
    for part, voices in xmlD['notes'].items():
            for voice, notes in voices.items():
                musD.setdefault(part,{}).setdefault(voice,{})
                g = 0
                while g < len(notes):
                    note1 = notes[g]
                    if isinstance(note1, list):
                        if chord == True:
                            notaStepL = []
                            notaOitavaL = []
                            notaAlterL = []
                            grauL = []
                            duracaoL = []
                            intCroL = []
                            intDiaL = []
                            intQuaL = []
                            for p in range(len(note1)):
                                Fcompasso1 = f_c.referencia(note1[p],xmlD['times'])
                                tonalidade = f_c.referencia(note1[p],xmlD['keys'])
                                andamento = f_c.referencia(note1[p],xmlD['metronomes'])
                                Ncompasso = f_c.Ncompasso(note1[p])
                                Pcompasso = f_c.P_compasso(divisions,Fcompasso1,note1[p])
                                Ntempo = f_c.N_tempo(divisions,Fcompasso1,note1[p])
                                Ptempo = f_c.P_tempo(divisions,Fcompasso1,note1[p])
                                notaStep = note1[p][1][0]
                                notaOitava = note1[p][1][1]
                                notaAlter = note1[p][1][2]
                                grau = f_c.grau_escala(tonalidade,note1[p])
    
                                notaStepL.append(notaStep)
                                notaOitavaL.append(notaOitava)
                                notaAlterL.append(notaAlter)
                                grauL.append(grau)

                                if p+1 < len(note1):
                                    Fcompasso2 = f_c.referencia(note1[p+1],xmlD['times'])
                                    duracao = f_c.duracao_inicio(divisions,Fcompasso2,note1[p+1]) - f_c.duracao_inicio(divisions,Fcompasso1,note1[p])
                                    intCro = f_c.int_cromatico(note1[p],note1[p+1])
                                    intDia = f_c.int_diatonico(note1[p],note1[p+1])
                                    intQua = f_c.int_qualidade(intDia,intCro)
                                    
                                    duracaoL.append(duracao)
                                    intCroL.append(intCro)
                                    intDiaL.append(intDia)
                                    intQuaL.append(intQua)

                            musD[part][voice].setdefault('Fcompasso', []).append(Fcompasso1)
                            musD[part][voice].setdefault('tonalidade', []).append(tonalidade)
                            musD[part][voice].setdefault('andamento', []).append(andamento)
                            musD[part][voice].setdefault('Ncompasso', []).append(Ncompasso)
                            musD[part][voice].setdefault('Pcompasso', []).append(Pcompasso)
                            musD[part][voice].setdefault('Ntempo', []).append(Ntempo)
                            musD[part][voice].setdefault('Ptempo', []).append(Ptempo)
                            musD[part][voice].setdefault('notaStep', []).append(tuple(notaStepL))
                            musD[part][voice].setdefault('notaOitava', []).append(tuple(notaOitavaL))
                            musD[part][voice].setdefault('notaAlter', []).append(tuple(notaAlterL))
                            musD[part][voice].setdefault('grau', []).append(tuple(grauL))
                            musD[part][voice].setdefault('duracao', []).append(tuple(duracaoL))
                            musD[part][voice].setdefault('intCro', []).append(tuple(intCroL))
                            musD[part][voice].setdefault('intDia', []).append(tuple(intDiaL))
                            musD[part][voice].setdefault('intQua', []).append(tuple(intQuaL))
                            note1 = note1[0]

                            g += 1
                            if g >= len(notes):
                                continue
                            note2 = notes[g]
                            if isinstance(notes[g], list):
                                note2 = notes[g][0]
                            if f_c.tie(note2) != 'start':
                                while f_c.tie(note2) != tie or f_c.step(note2) == rest:
                                    g += 1
                                    if g >= len(notes):
                                        break
                                    note2 = notes[g]
                                    if isinstance(notes[g], list):
                                        note2 = notes[g][0]
                            if g >= len(notes):
                                continue

                            Fcompasso2 = f_c.referencia(note2,xmlD['times'])
                            duracao = f_c.duracao_inicio(divisions,Fcompasso2,note2) - f_c.duracao_inicio(divisions,Fcompasso1,note1)
                            intCro = f_c.int_cromatico(note1,note2)
                            intDia = f_c.int_diatonico(note1,note2)
                            intQua = f_c.int_qualidade(intDia,intCro)

                            duracaoL.append(duracao)
                            intCroL.append(intCro)
                            intDiaL.append(intDia)
                            intQuaL.append(intQua)

                            musD[part][voice]['duracao'][-1] = tuple(duracaoL)
                            musD[part][voice]['intCro'][-1] = tuple(intCroL)
                            musD[part][voice]['intDia'][-1] = tuple(intDiaL)
                            musD[part][voice]['intQua'][-1] = tuple(intQuaL)
                            continue
                        else:
                            note1 = note1[0]    
                    Fcompasso1 = f_c.referencia(note1,xmlD['times'])
                    tonalidade = f_c.referencia(note1,xmlD['keys'])
                    andamento = f_c.referencia(note1,xmlD['metronomes'])
                    Ncompasso = f_c.Ncompasso(note1)
                    Pcompasso = f_c.P_compasso(divisions,Fcompasso1,note1)
                    Ntempo = f_c.N_tempo(divisions,Fcompasso1,note1)
                    Ptempo = f_c.P_tempo(divisions,Fcompasso1,note1)
                    notaStep = note1[1][0]
                    notaOitava = note1[1][1]
                    notaAlter = note1[1][2]
                    grau = f_c.grau_escala(tonalidade,note1)

                    musD[part][voice].setdefault('Fcompasso', []).append(Fcompasso1)
                    musD[part][voice].setdefault('tonalidade', []).append(tonalidade)
                    musD[part][voice].setdefault('andamento', []).append(andamento)
                    musD[part][voice].setdefault('Ncompasso', []).append(Ncompasso)
                    musD[part][voice].setdefault('Pcompasso', []).append(Pcompasso)
                    musD[part][voice].setdefault('Ntempo', []).append(Ntempo)
                    musD[part][voice].setdefault('Ptempo', []).append(Ptempo)
                    musD[part][voice].setdefault('notaStep', []).append(notaStep)
                    musD[part][voice].setdefault('notaOitava', []).append(notaOitava)
                    musD[part][voice].setdefault('notaAlter', []).append(notaAlter)
                    musD[part][voice].setdefault('grau', []).append(grau)
                    
                    g += 1
                    if g >= len(notes):
                        continue
                    note2 = notes[g]
                    if isinstance(notes[g], list):
                        note2 = notes[g][0]
                    if f_c.tie(note2) != 'start':
                        while f_c.tie(note2) != tie or f_c.step(note2) == rest:
                            g += 1
                            if g >= len(notes):
                                break
                            note2 = notes[g]
                            if isinstance(notes[g], list):
                                note2 = notes[g][0]
                    if g >= len(notes):
                        continue
  
                    Fcompasso2 = f_c.referencia(note2,xmlD['times'])
                    duracao = f_c.duracao_inicio(divisions,Fcompasso2,note2) - f_c.duracao_inicio(divisions,Fcompasso1,note1)
                    intCro = f_c.int_cromatico(note1,note2)
                    intDia = f_c.int_diatonico(note1,note2)
                    intQua = f_c.int_qualidade(intDia,intCro)
    
                    musD[part][voice].setdefault('duracao', []).append(duracao)
                    musD[part][voice].setdefault('intCro', []).append(intCro)
                    musD[part][voice].setdefault('intDia', []).append(intDia)
                    musD[part][voice].setdefault ('intQua', []).append(intQua)
    for parte in musD:
        for voz in musD[parte]:
            assert len(musD[parte][voz]['Fcompasso']) == len(musD[parte][voz]['tonalidade']) == len(musD[parte][voz]['andamento']) == len(musD[parte][voz]['Ncompasso']) == len(musD[parte][voz]['Pcompasso']) == len(musD[parte][voz]['Ntempo']) == len(musD[parte][voz]['Ptempo']) == len(musD[parte][voz]['notaStep']) == len(musD[parte][voz]['notaOitava']) == len(musD[parte][voz]['notaAlter']) == len(musD[parte][voz]['grau'])
            assert len(musD[parte][voz]['duracao']) == len(musD[parte][voz]['intCro']) == len(musD[parte][voz]['intDia']) == len(musD[parte][voz]['intQua'])
            assert len(musD[parte][voz]['duracao']) == len(musD[parte][voz]['Fcompasso'])-1
    return musD
