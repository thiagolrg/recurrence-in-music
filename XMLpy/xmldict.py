import conversoes as f_c
import xmltodict

def ad_counter(xmlIn):
    counter = 0
    xmlCounter = []
    chord = False
    for p in range(len(xmlIn)):
        assert 'score-timewise' not in xmlIn[p], NotImplementedError('conversao XML score-timewise')
        xmlCounter.append(xmlIn[p])
        if p > 2 and p < len(xmlIn):
            if '</' not in xmlCounter[p] and '/>' not in xmlCounter[p] and '<!' not in xmlCounter[p]:
                xmlCounter[p] = xmlCounter[p].rstrip('>')+' counter ='+'"'+str(counter)+'"'+'>'       
        if 'chord' in xmlIn[p]:
            chord = True
        if '<duration>' in xmlIn[p]:
            duration = int(xmlIn[p].replace('<duration>','').replace('</duration>',''))
            if '<backup>' in xmlIn[p-1]:
                counter = counter - duration
            elif chord == True:
                chord = False
            else:
                counter = counter + duration
        if '</part>' in xmlIn[p]:
            counter = 0
    return xmltodict.parse(''.join(xmlCounter))

def to_list(node):
    if isinstance(node, list) == True:
        return node
    else:
        return [node]

def xml_dict(xmlIn):
    xmlDict = {}
    for part in to_list(xmlIn['score-partwise']['part']):
        partID = part['@id']
        #numero do compasso
        for measure in to_list(part['measure']):
            if measure['@number'] == 'X1':
                pass
            else:
                measureN = int(measure['@number'])

            #atributos do compasso
            if 'attributes' in measure and measure['attributes'] != None:
                for attributes in to_list(measure['attributes']):

                    #divisions
                    if 'divisions' in attributes:
                        divisions = int(attributes['divisions'])
                        try:
                            assert divisions == xmlDict['divisions']
                        except KeyError:
                            xmlDict.setdefault('divisions', divisions)

                    #keys
                    if 'key' in attributes:
                        for k in to_list(attributes['key']):
                            assert 'mode' in k, '"key" sem "mode" no XML'
                            assert 'fifths' in k, '"key" sem "fifths" no XML'
                            key = ((int(k['@counter']), measureN) , f_c.key_(int(k['fifths']), k['mode']))
                            try:
                                if key not in xmlDict['keys']:
                                    keylocs = [f_c.loc(x) for x in xmlDict['keys']]
                                    assert(f_c.loc(key) not in keylocs)
                                    xmlDict.setdefault('keys', []).append(key)
                            except KeyError:
                                xmlDict.setdefault('keys', []).append(key)
                    
                    #times
                    if 'time' in attributes:
                        for t in to_list(attributes['time']):
                            time = [[int(t['@counter']), measureN], (int(t['beats']), int(t['beat-type']))]
                            try:
                                if time not in xmlDict['times']:
                                    timelocs = [f_c.loc(x) for x in xmlDict['times']]
                                    assert(f_c.loc(time) not in timelocs)
                                    xmlDict.setdefault('times', []).append(time)
                            except:
                                xmlDict.setdefault('times', []).append(time)
            
            #metronomes
            if 'direction' in measure:
                for direction in to_list(measure['direction']):
                    if 'sound' in direction:
                        for sound in to_list(direction['sound']):
                            if '@tempo' in sound:
                                metronome = ((int(direction['@counter']), measureN), f_c.m_soundtempo(int(sound['@tempo']),time))
                    elif 'direction-type' in direction:
                        for directionType in to_list(direction['direction-type']):
                            if 'metronome' in directionType:
                                for m in to_list(directionType['metronome']):
                                    metronome = ((int(m['@counter']), measureN), f_c.m_metronome(m))
                    try:
                        if metronome not in xmlDict['metronomes']:
                            metronomelocs = [f_c.loc(x) for x in xmlDict['metronomes']]
                            assert(f_c.loc(metronome) not in metronomelocs)
                            xmlDict.setdefault('metronomes', []).append(metronome)
                    except KeyError:
                        xmlDict.setdefault('metronomes', []).append(metronome)
            
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
                    xmlDict.setdefault('notes',{}).setdefault(partID, {}).setdefault(voice, []).append(note)
                    continue
                if 'tie' in note:
                    tie = to_list(note['tie'])[-1]['@type']
                for pitch in to_list(note['pitch']): 
                    step = pitch['step']
                    octave = int(pitch['octave'])
                    if 'alter' in pitch:
                        alter = int(pitch['alter'])
                if 'chord' in note:
                    if isinstance(xmlDict['notes'][partID][voice][-1], list) == False:
                        xmlDict['notes'][partID][voice][-1] = [xmlDict['notes'][partID][voice][-1]]
                    counter = xmlDict['notes'][partID][voice][-1][0][0][0]
                    note = ((counter, measureN), (step,octave,alter,tie))
                    counter = xmlDict['notes'][partID][voice][-1].append(note)
                else:
                    assert 'voice' in note, '"note" sem "voice"'
                    voice = int(note['voice'])
                    note = ((counter, measureN), (step,octave,alter,tie))
                    xmlDict.setdefault('notes',{}).setdefault(partID, {}).setdefault(voice, []).append(note)
    xmlDict['times'] = f_c.times_com_duracoes(xmlDict['times'])
    assert 'metronomes' in xmlDict,'algo faltando no xml?, nao foram extraidos metronomos'
    assert 'keys' in xmlDict,'algo faltando no xml?, nao foram extraidas armaduras'
    assert 'times' in xmlDict,'algo faltando no xml?, nao foram extraidas formulas de compasso'
    assert 'notes' in xmlDict,'algo faltando no xml?, nao foram extraidas notas'
    return xmlDict

def mus_dict(xmlDict, tie=None, rest=None, chord=True):
    musDict = {}
    divisions = xmlDict['divisions'] 
    for part, voices in xmlDict['notes'].items():
            for voice, notes in voices.items():
                musDict.setdefault(part,{}).setdefault(voice,{})
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
                                Fcompasso1 = f_c.referencia(note1[p],xmlDict['times'])
                                tonalidade = f_c.referencia(note1[p],xmlDict['keys'])
                                andamento = f_c.referencia(note1[p],xmlDict['metronomes'])
                                Ncompasso = f_c.Ncompasso(note1[p])
                                Pcompasso = round(f_c.P_compasso(divisions,Fcompasso1,note1[p]),2)
                                Ntempo = f_c.N_tempo(divisions,Fcompasso1,note1[p])
                                Ptempo = round(f_c.P_tempo(divisions,Fcompasso1,note1[p]),2)
                                notaStep = note1[p][1][0]
                                notaOitava = note1[p][1][1]
                                notaAlter = note1[p][1][2]
                                grau = f_c.grau_escala(tonalidade,note1[p])
    
                                notaStepL.append(notaStep)
                                notaOitavaL.append(notaOitava)
                                notaAlterL.append(notaAlter)
                                grauL.append(grau)

                                if p+1 < len(note1):
                                    Fcompasso2 = f_c.referencia(note1[p+1],xmlDict['times'])
                                    duracao = round(f_c.duracao_inicio(divisions,Fcompasso2,note1[p+1]) - f_c.duracao_inicio(divisions,Fcompasso1,note1[p]),2)
                                    intCro = f_c.int_cromatico(note1[p],note1[p+1])
                                    intDia = f_c.int_diatonico(note1[p],note1[p+1])
                                    intQua = f_c.int_qualidade(intDia,intCro)
                                    
                                    duracaoL.append(duracao)
                                    intCroL.append(intCro)
                                    intDiaL.append(intDia)
                                    intQuaL.append(intQua)

                            musDict[part][voice].setdefault('Fcompasso', []).append(Fcompasso1)
                            musDict[part][voice].setdefault('tonalidade', []).append(tonalidade)
                            musDict[part][voice].setdefault('andamento', []).append(andamento)
                            musDict[part][voice].setdefault('Ncompasso', []).append(Ncompasso)
                            musDict[part][voice].setdefault('Pcompasso', []).append(Pcompasso)
                            musDict[part][voice].setdefault('Ntempo', []).append(Ntempo)
                            musDict[part][voice].setdefault('Ptempo', []).append(Ptempo)
                            musDict[part][voice].setdefault('notaStep', []).append(tuple(notaStepL))
                            musDict[part][voice].setdefault('notaOitava', []).append(tuple(notaOitavaL))
                            musDict[part][voice].setdefault('notaAlter', []).append(tuple(notaAlterL))
                            musDict[part][voice].setdefault('grau', []).append(tuple(grauL))
                            musDict[part][voice].setdefault('duracao', []).append(tuple(duracaoL))
                            musDict[part][voice].setdefault('intCro', []).append(tuple(intCroL))
                            musDict[part][voice].setdefault('intDia', []).append(tuple(intDiaL))
                            musDict[part][voice].setdefault('intQua', []).append(tuple(intQuaL))
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

                            Fcompasso2 = f_c.referencia(note2,xmlDict['times'])
                            duracao = round(f_c.duracao_inicio(divisions,Fcompasso2,note2) - f_c.duracao_inicio(divisions,Fcompasso1,note1),2)
                            intCro = f_c.int_cromatico(note1,note2)
                            intDia = f_c.int_diatonico(note1,note2)
                            intQua = f_c.int_qualidade(intDia,intCro)

                            duracaoL.append(duracao)
                            intCroL.append(intCro)
                            intDiaL.append(intDia)
                            intQuaL.append(intQua)

                            musDict[part][voice]['duracao'][-1] = tuple(duracaoL)
                            musDict[part][voice]['intCro'][-1] = tuple(intCroL)
                            musDict[part][voice]['intDia'][-1] = tuple(intDiaL)
                            musDict[part][voice]['intQua'][-1] = tuple(intQuaL)
                            continue
                        else:
                            note1 = note1[0]    
                    Fcompasso1 = f_c.referencia(note1,xmlDict['times'])
                    tonalidade = f_c.referencia(note1,xmlDict['keys'])
                    andamento = f_c.referencia(note1,xmlDict['metronomes'])
                    Ncompasso = f_c.Ncompasso(note1)
                    Pcompasso = round(f_c.P_compasso(divisions,Fcompasso1,note1),2)
                    Ntempo = f_c.N_tempo(divisions,Fcompasso1,note1)
                    Ptempo = round(f_c.P_tempo(divisions,Fcompasso1,note1),2)
                    notaStep = note1[1][0]
                    notaOitava = note1[1][1]
                    notaAlter = note1[1][2]
                    grau = f_c.grau_escala(tonalidade,note1)

                    musDict[part][voice].setdefault('Fcompasso', []).append(Fcompasso1)
                    musDict[part][voice].setdefault('tonalidade', []).append(tonalidade)
                    musDict[part][voice].setdefault('andamento', []).append(andamento)
                    musDict[part][voice].setdefault('Ncompasso', []).append(Ncompasso)
                    musDict[part][voice].setdefault('Pcompasso', []).append(Pcompasso)
                    musDict[part][voice].setdefault('Ntempo', []).append(Ntempo)
                    musDict[part][voice].setdefault('Ptempo', []).append(Ptempo)
                    musDict[part][voice].setdefault('notaStep', []).append(notaStep)
                    musDict[part][voice].setdefault('notaOitava', []).append(notaOitava)
                    musDict[part][voice].setdefault('notaAlter', []).append(notaAlter)
                    musDict[part][voice].setdefault('grau', []).append(grau)
                    
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
  
                    Fcompasso2 = f_c.referencia(note2,xmlDict['times'])
                    duracao = round(f_c.duracao_inicio(divisions,Fcompasso2,note2) - f_c.duracao_inicio(divisions,Fcompasso1,note1),2)
                    intCro = f_c.int_cromatico(note1,note2)
                    intDia = f_c.int_diatonico(note1,note2)
                    intQua = f_c.int_qualidade(intDia,intCro)
    
                    musDict[part][voice].setdefault('duracao', []).append(duracao)
                    musDict[part][voice].setdefault('intCro', []).append(intCro)
                    musDict[part][voice].setdefault('intDia', []).append(intDia)
                    musDict[part][voice].setdefault ('intQua', []).append(intQua)
    return musDict 