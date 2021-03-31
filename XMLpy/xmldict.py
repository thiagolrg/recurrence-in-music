import conversoes as f_c

def time_certo(times,compasso):
    for p in range(len(times)):
        if times[p][0] >= compasso:
            return times[p-1]
    return times[-1]

def NoneText(element):
    if element == None:
        return element
    return element.text

def NoneTag(element):
    if element == None:
        return element
    return element.tag

def NoneInt(element):
    if element == None:
        return element
    return int(element.text)

def NoneAtr(element):
    if element == None:
        return element
    return element.attrib['type']

def xml_mus(xml):
    xmlDict = {}
    for part in xml.iter('part'):
        keys = []
        times = []
        metronomes = []
        compassos = []
        elements = {}
        partid = part.get('id')
        divisions = part.findall('.//divisions')
        assert len(divisions) == 1
        divisions = int(divisions[0].text)
        for measure in part:
            if measure.get('number') == 'X1':
                pass
            else:
                measureN = int(measure.get('number'))
                compassos.append(measureN)
            beats = measure.findall('.//beats')
            beatType = measure.findall('.//beat-type')
            assert len(beats) <= len(beatType) <= 1
            if len(beats) == len(beatType) == 1 and measureN not in [t[0] for t in times]:
                beats = int(beats[0].text)
                beatType = int(beatType[0].text)
                times.append([measureN,[beats, beatType]])
            for element in measure.iter():
                if element.tag == 'key' or element.tag == 'note' or element.tag == 'backup' or element.tag == 'forward' or  element.tag == 'metronome' or 'tempo' in element.attrib.keys():
                    elements.setdefault(measureN, []).append(element)
        for t in times:  
            t[1].append(int(divisions*4/t[1][1]*t[1][0]))

        compassoscounter = []
        if compassos[0] == 0:
            compasso0voice = {}
            counter = 0
            for compasso, elementosdocompasso in elements.items():
                for element in elementosdocompasso:
                    if element.tag == 'note':
                        counter = counter + int(element.find('.//duration').text)
                        voice = int(element.find('.//voice').text)
                    elif element.tag == 'backup':
                        compasso0voice.update({voice: times[0][1][2] - counter})
                        counter = counter - int(element.find('duration').text)
                    elif element.tag == 'forward':
                        counter = counter + int(element.find('duration').text)
                compasso0voice.update({voice: times[0][1][2] - counter})
                counter = counter - int(element.find('duration').text)
                break
        compassoscounter.append([compassos[0], 0])
        for compasso in compassos[1:]:
            timecerto = time_certo(times, compasso)
            compassoscounter.append([compasso, compassoscounter[-1][1]+timecerto[1][2]])
        compassoscounter = {c : v for c, v in compassoscounter}

        
        xmlDict.setdefault(partid, {}).setdefault('notes', {})
        for compasso, elementosdocompasso in elements.items():
            counter = compassoscounter[compasso]
            for element in elementosdocompasso:
                if element.tag == 'note':
                    grace = NoneTag(element.find('.//grace'))
                    if grace == 'grace':
                        continue
                    step = NoneText(element.find('.//step'))
                    octave =  NoneInt(element.find('.//octave'))
                    alter = NoneInt(element.find('.//alter'))
                    tie =  NoneAtr(element.find('.//tie'))
                    chord =  NoneTag(element.find('.//chord'))
                    voice = int(element.find('.//voice').text)

                    if chord == 'chord':
                        if isinstance(xmlDict[partid]['notes'][voice][-1], list):
                            counter = xmlDict[partid]['notes'][voice][-1][0][0][0]
                        else:
                            counter = xmlDict[partid]['notes'][voice][-1][0][0]
                            xmlDict[partid]['notes'][voice][-1] = [xmlDict[partid]['notes'][voice][-1]]
                        note = ((counter,compasso), (step,octave,alter,tie))
                        xmlDict[partid]['notes'][voice][-1].append(note)
                    else:
                        if compasso == 0:
                            counter = compasso0voice[voice]
                        note = ((counter,compasso), (step,octave,alter,tie))
                        xmlDict[partid]['notes'].setdefault(voice, []).append(note)
                    counter = counter + int(element.find('.//duration').text)
                    if compasso == 0: 
                        compasso0voice[voice] = counter

                elif element.tag == 'backup':
                    counter = counter - int(element.find('duration').text)
                elif element.tag == 'forward':
                    counter = counter + int(element.find('duration').text)
                elif element.tag == 'key':
                    fifths = int(element.find('fifths').text)
                    mode = element.find('mode').text
                    key = ((counter,compasso), f_c.key_(fifths, mode))
                    if key[0][0] in [k[0][0] for k in keys]:
                        keys[[k[0][0] for k in keys].index(key[0][0])] = key
                    else:
                        keys.append(key)
                elif element.tag == 'metronome':
                    beatUnit = NoneText(element.find('.//beat-unit'))
                    beatUnitiDot = NoneTag(element.find('.//beat-unit-dot'))
                    perMinute = NoneInt(element.find('.//per-minute'))
                    metronome = ((counter,compasso), (f_c.m_metronome(beatUnit, beatUnitiDot), perMinute))
                    if metronome[0][0] not in [m[0][0] for m in metronomes]:
                        metronomes.append(metronome)
                elif element.tag == 'sound':
                    tempo = int(element.attrib['tempo'])
                    metronome = ((counter,compasso), f_c.m_soundtempo(tempo, time_certo(times, compasso)))
                    if metronome[0][0] not in [m[0][0] for m in metronomes]:
                        metronomes.append(metronome)
        for p in range(len(times)):
            times[p] = [(compassoscounter[times[p][0]], times[p][0]), times[p][1][0:2]]
        times = f_c.times_com_duracoes(times)
        xmlDict[partid].update({'keys': keys})
        xmlDict[partid].update({'times': times})
        xmlDict[partid].update({'metronomes': metronomes})
        xmlDict[partid].update({'divisions': divisions})

        for voice in xmlDict[partid]['notes'].items():
            for note in voice[1]:
                print(voice[0], note)
        return musDict(xmlDict)

def mus_dict(xmlDict, tie=None, rest=None, chord=True, keys=True, metronomes=True):
    musDict = {}
    for partvalues in xmlDict.items():
        divisions = partvalues[1]['divisions']
        for voice, notes in partvalues[1]['notes'].items():
            musDict.setdefault(partvalues[0],{}).setdefault(voice,{})
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
                            Fcompasso1 = f_c.referencia(note1[p],partvalues[1]['times'])
                            if keys == True:
                                tonalidade = f_c.referencia(note1[p],partvalues[1]['keys'])
                                grau = f_c.grau_escala(tonalidade,note1[p])
                            if metronomes == True:
                                andamento = f_c.referencia(note1[p],partvalues[1]['metronomes'])
                            Ncompasso = f_c.Ncompasso(note1[p])
                            Pcompasso = round(f_c.P_compasso(divisions,Fcompasso1,note1[p]),2)
                            Ntempo = f_c.N_tempo(divisions,Fcompasso1,note1[p])
                            Ptempo = round(f_c.P_tempo(divisions,Fcompasso1,note1[p]),2)
                            notaStep = note1[p][1][0]
                            notaOitava = note1[p][1][1]
                            notaAlter = note1[p][1][2]
                            

                            notaStepL.append(notaStep)
                            notaOitavaL.append(notaOitava)
                            notaAlterL.append(notaAlter)
                            if keys == True:
                                grauL.append(grau)

                            if p+1 < len(note1):
                                Fcompasso2 = f_c.referencia(note1[p+1],partvalues[1]['times'])
                                duracao = round(f_c.duracao_inicio(divisions,Fcompasso2,note1[p+1]) - f_c.duracao_inicio(divisions,Fcompasso1,note1[p]),2)
                                intCro = f_c.int_cromatico(note1[p],note1[p+1])
                                intDia = f_c.int_diatonico(note1[p],note1[p+1])
                                intQua = f_c.int_qualidade(intDia,intCro)
                                
                                duracaoL.append(duracao)
                                intCroL.append(intCro)
                                intDiaL.append(intDia)
                                intQuaL.append(intQua)

                        if keys == True:
                            musDict[partvalues[0]][voice].setdefault('tonalidade', []).append(tonalidade)
                            musDict[partvalues[0]][voice].setdefault('grau', []).append(tuple(grauL))
                        if metronomes == True:
                            musDict[partvalues[0]][voice].setdefault('andamento', []).append(andamento)
                        musDict[partvalues[0]][voice].setdefault('Fcompasso', []).append(Fcompasso1)
                        musDict[partvalues[0]][voice].setdefault('Ncompasso', []).append(Ncompasso)
                        musDict[partvalues[0]][voice].setdefault('Pcompasso', []).append(Pcompasso)
                        musDict[partvalues[0]][voice].setdefault('Ntempo', []).append(Ntempo)
                        musDict[partvalues[0]][voice].setdefault('Ptempo', []).append(Ptempo)
                        musDict[partvalues[0]][voice].setdefault('notaStep', []).append(tuple(notaStepL))
                        musDict[partvalues[0]][voice].setdefault('notaOitava', []).append(tuple(notaOitavaL))
                        musDict[partvalues[0]][voice].setdefault('notaAlter', []).append(tuple(notaAlterL))
                        musDict[partvalues[0]][voice].setdefault('duracao', []).append(tuple(duracaoL))
                        musDict[partvalues[0]][voice].setdefault('intCro', []).append(tuple(intCroL))
                        musDict[partvalues[0]][voice].setdefault('intDia', []).append(tuple(intDiaL))
                        musDict[partvalues[0]][voice].setdefault('intQua', []).append(tuple(intQuaL))
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

                        Fcompasso2 = f_c.referencia(note2,partvalues[1]['times'])
                        duracao = round(f_c.duracao_inicio(divisions,Fcompasso2,note2) - f_c.duracao_inicio(divisions,Fcompasso1,note1),2)
                        intCro = f_c.int_cromatico(note1,note2)
                        intDia = f_c.int_diatonico(note1,note2)
                        intQua = f_c.int_qualidade(intDia,intCro)

                        duracaoL.append(duracao)
                        intCroL.append(intCro)
                        intDiaL.append(intDia)
                        intQuaL.append(intQua)

                        musDict[partvalues[0]][voice]['duracao'][-1] = tuple(duracaoL)
                        musDict[partvalues[0]][voice]['intCro'][-1] = tuple(intCroL)
                        musDict[partvalues[0]][voice]['intDia'][-1] = tuple(intDiaL)
                        musDict[partvalues[0]][voice]['intQua'][-1] = tuple(intQuaL)
                        continue
                    else:
                        note1 = note1[0]
                if keys == True:
                    tonalidade = f_c.referencia(note1,partvalues[1]['keys'])
                    grau = f_c.grau_escala(tonalidade,note1)
                if metronomes == True:
                    andamento = f_c.referencia(note1,partvalues[1]['metronomes'])
                Fcompasso1 = f_c.referencia(note1,partvalues[1]['times'])
                Ncompasso = f_c.Ncompasso(note1)
                Pcompasso = round(f_c.P_compasso(divisions,Fcompasso1,note1),2)
                Ntempo = f_c.N_tempo(divisions,Fcompasso1,note1)
                Ptempo = round(f_c.P_tempo(divisions,Fcompasso1,note1),2)
                notaStep = note1[1][0]
                notaOitava = note1[1][1]
                notaAlter = note1[1][2]

                if keys == True:
                    musDict[partvalues[0]][voice].setdefault('tonalidade', []).append(tonalidade)
                    musDict[partvalues[0]][voice].setdefault('grau', []).append(grau)
                if metronomes == True:
                    musDict[partvalues[0]][voice].setdefault('andamento', []).append(andamento)
                musDict[partvalues[0]][voice].setdefault('Fcompasso', []).append(Fcompasso1)
                musDict[partvalues[0]][voice].setdefault('Ncompasso', []).append(Ncompasso)
                musDict[partvalues[0]][voice].setdefault('Pcompasso', []).append(Pcompasso)
                musDict[partvalues[0]][voice].setdefault('Ntempo', []).append(Ntempo)
                musDict[partvalues[0]][voice].setdefault('Ptempo', []).append(Ptempo)
                musDict[partvalues[0]][voice].setdefault('notaStep', []).append(notaStep)
                musDict[partvalues[0]][voice].setdefault('notaOitava', []).append(notaOitava)
                musDict[partvalues[0]][voice].setdefault('notaAlter', []).append(notaAlter)
                
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

                Fcompasso2 = f_c.referencia(note2,partvalues[1]['times'])
                duracao = round(f_c.duracao_inicio(divisions,Fcompasso2,note2) - f_c.duracao_inicio(divisions,Fcompasso1,note1),2)
                intCro = f_c.int_cromatico(note1,note2)
                intDia = f_c.int_diatonico(note1,note2)
                intQua = f_c.int_qualidade(intDia,intCro)

                musDict[partvalues[0]][voice].setdefault('duracao', []).append(duracao)
                musDict[partvalues[0]][voice].setdefault('intCro', []).append(intCro)
                musDict[partvalues[0]][voice].setdefault('intDia', []).append(intDia)
                musDict[partvalues[0]][voice].setdefault ('intQua', []).append(intQua)
    return musDict