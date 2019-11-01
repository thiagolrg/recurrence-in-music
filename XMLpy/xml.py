import conversoes as f_c

with open(r'arquivos teste\MusicXML\localizacaocompassobpm.xml') as f:
    xml = []
    for l in f.readlines():
        if '<!' in l:
            continue
        xml.append(l.strip().replace('"', '').replace('\n', ''))

def xml2dict(xml):
    p = 0
    dicio = {}
    while p < len(xml):
        if '<part id=' in xml[p]:
            partID = str(xml[p].replace('<part id=', '').replace('>',''))
            dicio.setdefault(partID,{})
            counter = 0
            duration = 0
            tie = False
            p += 1
        
        elif '<divisions>' in xml[p]:
            divisions = int(xml[p].replace('<divisions>','').replace('</divisions>',''))
            dicio[partID].setdefault('divisions', divisions)
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
            countermeasure = tuple([counter,measureNumber])
            key = f_c.key(fifths,mode)
            key = tuple([countermeasure, key]) 
            dicio[partID].setdefault('keys', []).append(key)
    
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
            countermeasure = [counter,measureNumber]
            time = tuple([beats, beatType])
            time = [countermeasure,time]
            dicio[partID].setdefault('times', []).append(time)

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
            countermeasure = tuple([counter,measureNumber])
            metronome = tuple([beatUnit, perMinute])
            metronome = tuple([countermeasure,metronome])
            dicio[partID].setdefault('metronomes', []).append(metronome)

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
                    duration = int(l.replace('<duration>','').replace('</duration>',''))
                elif '<tie type=start />' in l:
                    tie = True
                elif '<tie type=stop />' in l:
                    tie = False
            countermeasure = tuple([counter,measureNumber])
            note = tuple([step,octave,alter,tie])
            note = tuple([countermeasure, note])
            dicio[partID].setdefault('notes', []).append(note)
            counter = counter + duration
        else:
            p += 1

    for parte, elem in dicio.items():
        elem['times'] = f_c.times_com_tempos(elem['times'])   
    for parte, elem in dicio.items():
        for p in range(len(elem['notes'])):

            divisions = elem['divisions']
            nota1 = elem['notes'][p]
            nota2 = elem['notes'][p+1]

            timeRef = f_c.referencia(nota1,elem['times'])
            keyRef = f_c.referencia(nota1,elem['keys'])
            metroRef = f_c.referencia(nota1,elem['metronomes'])

            posicaotempo = f_c.posicao_tempodecompasso(divisions,timeRef,nota1)
            posicaofracao = f_c.posicao_fracaodetempo(divisions,timeRef,nota1)
            duracaodesdeinicio = f_c.duracao_desdeinicio(divisions,timeRef,nota1)
            

    return dicio

dicio = xml2dict(xml)

debug = 0