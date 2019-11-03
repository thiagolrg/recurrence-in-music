import conversoes as f_c

with open(r'arquivos teste\MusicXML\k341k363\k363.xml') as f:
    xml = []
    for l in f.readlines():
        if '<!' in l:
            continue
        xml.append(l.strip().replace('"', '').replace('\n', ''))

def xml_dict(xml):
    p = 0
    musica = {}
    while p < len(xml):
        if '<part id=' in xml[p]:
            partID = str(xml[p].replace('<part id=', '').replace('>',''))
            musica.setdefault('notes',{}).setdefault(partID, [])
            Cduration = 0
            duration = 0
            tie = False
            p += 1    
        elif '<divisions>' in xml[p]:
            divisions = int(xml[p].replace('<divisions>','').replace('</divisions>',''))
            p += 1
            try:
                if divisions != musica['divisions']:
                    raise ValueError ('divisions diferente')
            except KeyError:
                musica.setdefault('divisions', divisions) 
        elif '<measure number=' in xml[p]:
            measureNumber = int(xml[p].replace('<measure number=','').split(' ')[0])
            p += 1
        elif '<key ' in xml[p]:
            keyList = []
            while '</key>' not in xml[p]:
                keyList.append(xml[p])
                p += 1
            for l in keyList:
                if '<fifths>' in l:
                    fifths = int(l.replace('<fifths>','').replace('</fifths>',''))
                elif '<mode>' in l:
                    mode = str(l.replace('<mode>','').replace('</mode>',''))
            key = ((Cduration, measureNumber), f_c.key(fifths,mode))
            try:
                if key not in musica['keys']:
                    keylocs = [f_c.loc(x) for x in musica['keys']]
                    if f_c.loc(key) in keylocs:
                        raise ValueError ('keys diferentes')
                    musica.setdefault('keys', []).append(key)
            except KeyError:
                musica.setdefault('keys', []).append(key)
        elif '<time ' in xml[p]:
            timeList = []
            while '</time>' not in xml[p]:
                timeList.append(xml[p])
                p += 1
            for l in timeList:
                if '<beats>' in l:
                    beats = int(l.replace('<beats>','').replace('</beats>',''))
                elif '<beat-type>' in l:
                    beatType = int(l.replace('<beat-type>','').replace('</beat-type>',''))
            time = [[Cduration,measureNumber],(beats, beatType)]
            try:
                if time not in musica['times']:
                    timelocs = [f_c.loc(x) for x in musica['times']]
                    if f_c.loc(time) in timelocs:
                        raise ValueError ('times diferentes')
                    musica.setdefault('times', []).append(time)
            except:
                musica.setdefault('times', []).append(time)
        elif '<metronome ' in xml[p]:
            metronomeList = []
            while '</metronome>' not in xml[p]:
                metronomeList.append(xml[p])
                p += 1
            for l in metronomeList:
                if '<beat-unit>' in l:
                    beatUnit = str(l.replace('<beat-unit>','').replace('</beat-unit>',''))
                elif '<per-minute>' in l:
                    perMinute = int(l.replace('<per-minute>','').replace('</per-minute>',''))
            metronome = ((Cduration,measureNumber),(beatUnit, perMinute))
            try:
                if metronome not in musica['metronomes']:
                    metronomelocs = [f_c.loc(x) for x in musica['metronomes']]
                    if f_c.loc(metronome) in metronomelocs:
                        raise ValueError ('metronomes diferentes')
                    musica.setdefault('metronomes', []).append(metronome)
            except KeyError:
                musica.setdefault('metronomes', []).append(metronome)
        elif '<note ' in xml[p]:
            noteList = []
            alter = None
            tie = None
            while '</note>' not in xml[p]:
                noteList.append(xml[p])
                p += 1
            for l in noteList:
                if '<rest />' in l:
                    step = None
                    octave = None
                elif '<step>' in l:
                    step = str(l.replace('<step>','').replace('</step>',''))
                elif '<alter>' in l:
                    alter = int(l.replace('<alter>','').replace('</alter>',''))
                elif '<octave>' in l:
                    octave = int(l.replace('<octave>','').replace('</octave>',''))
                elif '<duration>' in l:
                    duration = int(l.replace('<duration>','').replace('</duration>',''))
                elif '<tie type=start />' in l:
                    tie = True
                elif '<tie type=stop />' in l:
                    tie = False
            note = ((Cduration,measureNumber),(step,octave,alter,tie))
            musica['notes'][partID].append(note)
            Cduration = Cduration + duration
        else:
            p += 1
    musica['times'] = f_c.times_com_duracoes(musica['times'])
    return musica

def musica_dict(xmlDict, tie=False, rest=None):
    musicaDict = {}
    divisions = xmlDict['divisions']
    for parte, notes in xmlDict['notes'].items():
        p = 0
        fim = False
        while p < len(notes):
            while f_c.tie(notes[p]) == tie or f_c.step(notes[p]) == rest:
                p += 1
            note1 = notes[p]
            timeRefn1 = f_c.referencia(note1,xmlDict['times'])
            keyRef = f_c.referencia(note1,xmlDict['keys'])
            metronome = f_c.referencia(note1,xmlDict['metronomes'])
            Ptempo = f_c.Ptempo(divisions,timeRefn1,note1)
            Ntempo = f_c.Ntempo(divisions,timeRefn1,note1)
            grau = f_c.grau_escala(keyRef,note1)
            musicaDict.setdefault(parte, {})
            musicaDict[parte].setdefault('Ncompasso', []).append(f_c.Ncompasso(note1))
            musicaDict[parte].setdefault('tonalidade', []).append(f_c.val(keyRef))
            musicaDict[parte].setdefault('Fcompasso', []).append(f_c.val(timeRefn1))
            musicaDict[parte].setdefault('andamento', []).append(f_c.val(metronome))
            musicaDict[parte].setdefault('grau',[]).append(grau)
            musicaDict[parte].setdefault('Ptempo', []).append(Ptempo)
            musicaDict[parte].setdefault('Ntempo', []).append(Ntempo)
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
                musicaDict[parte].setdefault('duracao', []).append(duracao)
                musicaDict[parte].setdefault('intDia', []).append(intDia)
                musicaDict[parte].setdefault('intCro', []).append(intCro)
                musicaDict[parte].setdefault('intQua', []).append(intQua)    
    return musicaDict

xmlDict = xml_dict(xml)
musicaDict = musica_dict(xmlDict)
debug = 0 