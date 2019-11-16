import conversoes as f_c

with open(r'arquivos teste\MusicXML\MIDIStressTest.xml') as f:
    xml = []
    for linha in f.readlines():
        linha = linha.strip()
        if '<!' in linha:
            continue
        linha = linha.replace('"', '')
        linha = linha.replace('\n', '')
        xml.append(linha)

dicio = {}
counter = 0
duration = 0
tie = 0
p = 0
while p < len(xml):
    if '<part id=' in xml[p]:
        l = xml[p].lstrip('<part id=')
        l = l.rstrip('>')
        partID = str(l)
        dicio.setdefault(partID,{})
        p += 1
        
    elif '</part>' in xml[p]:
        counter = 0
        p += 1
        
    elif '<divisions>' in xml[p]:
        l = xml[p].lstrip('<divisions>') 
        l = l.rstrip('</divisions>')
        divisions = int(l)
        p += 1
        
    elif '<measure number=' in xml[p]:
        l = xml[p].lstrip('<measure number=') 
        l = l.split(' ')[0]
        measureNumber = int(l)
        p += 1

    elif '<time ' in xml[p]:
        timeList = []
        for p2 in range(p,len(xml)):
            if '</time>' in xml[p2]:
                timeList.append(xml[p2])
                p += 1
                break
            timeList.append(xml[p2])
            p += 1
        for linha in timeList:
            if '<beats>' in linha:
                l = linha.lstrip('<beats>') 
                l = l.rstrip('</beats>')
                beats = int(l)
            elif '<beat-type>' in linha:
                l = linha.lstrip('<beat-type>') 
                l = l.rstrip('</beat-type>')
                beatType = int(l)
        time = tuple([counter,(beats, beatType)])

    elif '<metronome ' in xml[p]:
        metronomeList = []
        for p2 in range(p,len(xml)):
            if '</metronome>' in xml[p2]:
                metronomeList.append(xml[p2])
                p += 1
                break
            metronomeList.append(xml[p2])
            p += 1
        for linha in metronomeList:
            if '<beat-unit>' in linha:
                l = linha.lstrip('<beat-unit>') 
                l = l.rstrip('</beat-unit>')
                beatUnit = str(l)
            elif '<per-minute>' in linha:
                l = linha.lstrip('<per-minute>') 
                l = l.rstrip('</per-minute>')
                perMinute = int(l)
        metronome = tuple([beatUnit, perMinute])

    elif '<note ' in xml[p]:
        noteList = []
        alter = None
        for p2 in range(p,len(xml)):
            if '</note>' in xml[p2]:
                noteList.append(xml[p2])
                p += 1
                break
            noteList.append(xml[p2])
            p += 1
        for linha in noteList:
            if '<rest />' in linha:
                step = None
                octave = None
            elif '<step>' in linha:
                l = linha.lstrip('<step>') 
                l = l.rstrip('</step>')
                step = str(l)
            elif '<alter>' in linha:
                l = linha.lstrip('<alter>') 
                l = l.rstrip('</alter>')
                alter = int(l)
            elif '<octave>' in linha:
                l = linha.lstrip('<octave>') 
                l = l.rstrip('</octave>')
                octave = int(l)
            elif '<duration>' in linha:
                l = linha.lstrip('<duration>') 
                l = l.rstrip('</duration>')
                if tie == True:
                    duration = int(l) + duration
                else:
                    duration = int(l)
            elif '<tie type=start />' in linha:
                tie = 1
            elif '<tie type=stop />' in linha:
                tie = 0

        if tie == 1:
            tie = True
        elif tie == 0:
            tie = False

        if tie == False:
            
            durationTime = f_c.duration_time(divisions,time,counter)
            midiN = f_c.note_to_miniN(step,alter,octave)

            dicio[partID].setdefault('step', []).append(step)
            dicio[partID].setdefault('alter', []).append(alter)
            dicio[partID].setdefault('octave', []).append(octave)
            dicio[partID].setdefault('metronome', []).append(metronome)
            dicio[partID].setdefault('time', []).append(time)
            dicio[partID].setdefault('counter', []).append(counter)
            dicio[partID].setdefault('measureNumber', []).append(measureNumber)
            dicio[partID].setdefault('durationTime',[]).append(durationTime)
            dicio[partID].setdefault('midiN',[]).append(midiN)
            counter = counter + duration
    else:
        p += 1

debug = 0