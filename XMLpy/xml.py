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
            dicio.setdefault(partID,[])
            counter = 0
            duration = 0
            tie = False
            p += 1
        
        elif '<divisions>' in xml[p]:
            divisions = int(xml[p].replace('<divisions>','').replace('</divisions>',''))
            p += 1
            try:
                if divisions not in dicio['division']:
                    dicio.setdefault('divisions', divisions)
            except KeyError:
                dicio.setdefault('divisions', divisions)
        
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
            try:
                if key not in dicio['keys']:
                    dicio.setdefault('keys', []).append(key)
            except KeyError:
                dicio.setdefault('keys', []).append(key)
    
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
            try:
                if time not in dicio['times']:
                    dicio.setdefault('times', []).append(time)
            except:
                dicio.setdefault('times', []).append(time)

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
            try:
                if metronome not in dicio['metronomes']:
                    dicio.setdefault('metronomes', []).append(metronome)
            except KeyError:
                dicio.setdefault('metronomes', []).append(metronome)

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
            dicio[partID].append(note)
            counter = counter + duration
        else:
            p += 1
    dicio['times'] = f_c.times_com_tempos(dicio['times'])
    return dicio

def dict_to_pronto(dicio):   
    for parte, elem in dicio.items():
        for p in range(len(elem['notes'])):
            divisions = elem['divisions']
            nota1 = elem['notes'][p]
            timeRefn1 = f_c.referencia(nota1,elem['times'])
            keyRef = f_c.referencia(nota1,elem['keys'])
            fracaoTempo = f_c.fracao_tempo(divisions,timeRefn1,nota1)
            tempoCompasso = f_c.tempo_compasso(divisions,timeRefn1,nota1)
            grau = f_c.grau_escala(keyRef,nota1)
            
            if p+1 < len(elem['notes']):
                
                nota2 = elem['notes'][p+1]
                timeRefn2 = f_c.referencia(nota2,elem['times'])
                metroRef = f_c.referencia(nota1,elem['metronomes'])      
                duracao = duracaoInicio_n2 = f_c.duracao_inicio(divisions,timeRefn2,nota2) - f_c.duracao_inicio(divisions,timeRefn1,nota1)
                intDia = f_c.int_diatonico(nota1,nota2)
                intCro = f_c.int_cromatico(nota1,nota2)
                intQua = f_c.int_qualidade(intDia,intCro)
    return dicio

dicio = xml2dict(xml)
dicio = dict_to_pronto(dicio)
debug = 0