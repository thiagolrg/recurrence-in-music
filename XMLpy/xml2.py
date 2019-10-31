import conversoes as f_c

with open(r'arquivos teste\MusicXML\MIDIStressTest.xml') as f:
    xml = []
    for l in f.readlines():
        if '<!' in l:
            continue
        xml.append(l.strip().replace('"', '').replace('\n', ''))

dicio = {}
p = 0
while p < len(xml):
    if '<part id=' in xml[p]:
        partID = str(xml[p].replace('<part id=', '').replace('>',''))
        dicio.setdefault(partID,{})
        counter = 0
        duration = 0
        tie_old = False
        tie_new = False
        p += 1
        
    elif '<divisions>' in xml[p]:
        divisions = int(xml[p].replace('<divisions>','').replace('</divisions>',''))
        p += 1
        
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
        key = f_c.key(fifths,mode)
    
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
        time = [[counter,measureNumber],(beats, beatType)]
        if 'time' in dicio[partID].keys():
            time[0].append(f_c.time_number(dicio[partID]['time'][-1:][0],time))
            time[0] = tuple(time[0])
            time = tuple(time)
        else:
            time[0].append(1)
            time[0] = tuple(time[0])
            time = tuple(time)

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
        metronome = tuple([beatUnit, perMinute])

    elif '<note ' in xml[p]:
        noteList = []
        alter = None
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
                if tie_old == True:
                    duration = int(l.replace('<duration>','').replace('</duration>','')) + duration
                else:
                    duration = int(l.replace('<duration>','').replace('</duration>',''))
            elif '<tie type=start />' in l:
                tie_new = True
            elif '<tie type=stop />' in l:
                tie_new = False

        tie_old = tie_new
        if tie_old == False:

            positionMeasure = f_c.position_measure(divisions,time,counter)
            midiN = f_c.note_to_miniN(step,alter,octave)
            degree = f_c.scale_degree(key,step)

            dicio[partID].setdefault('degree', []).append(degree)
            dicio[partID].setdefault('midiN',[]).append(midiN)
            dicio[partID].setdefault('key', []).append(key)
            dicio[partID].setdefault('step', []).append(step)
            dicio[partID].setdefault('alter', []).append(alter)
            dicio[partID].setdefault('octave', []).append(octave)
            dicio[partID].setdefault('metronome', []).append(metronome)
            dicio[partID].setdefault('time', []).append(time)
            dicio[partID].setdefault('counter', []).append(counter)
            dicio[partID].setdefault('measureNumber', []).append(measureNumber)
            dicio[partID].setdefault('positionMeasure',[]).append(positionMeasure)
            counter = counter + duration
            
    elif '</part>' in xml[p]:


        p += 1

    else:
        p += 1

debug = 0