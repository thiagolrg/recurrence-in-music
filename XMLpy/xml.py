import conversoes as f_c

with open(r'arquivos teste\MusicXML\k341k363\k363.xml') as f:
    xml = []
    for l in f.readlines():
        if '<!' in l:
            continue
        xml.append(l.strip().replace('"', '').replace('\n', ''))

nome = 'nome'
def xml_dict(xml):
    p = 0
    xmlDict = {}
    while p < len(xml):
        if '<part id=' in xml[p]:
            partID = str(xml[p].replace('<part id=', '').replace('>',''))
            xmlDict.setdefault('notes',{}).setdefault(partID, [])
            Cduration = 0
            duration = 0
            tie = False
            p += 1    
        elif '<divisions>' in xml[p]:
            divisions = int(xml[p].replace('<divisions>','').replace('</divisions>',''))
            p += 1
            try:
                if divisions != xmlDict['divisions']:
                    raise ValueError ('divisions diferente')
            except KeyError:
                xmlDict.setdefault('divisions', divisions) 
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
            key = ((Cduration, measureNumber), f_c.key_(fifths,mode))
            try:
                if key not in xmlDict['keys']:
                    keylocs = [f_c.loc(x) for x in xmlDict['keys']]
                    if f_c.loc(key) in keylocs:
                        raise ValueError ('keys diferentes')
                    xmlDict.setdefault('keys', []).append(key)
            except KeyError:
                xmlDict.setdefault('keys', []).append(key)
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
                if time not in xmlDict['times']:
                    timelocs = [f_c.loc(x) for x in xmlDict['times']]
                    if f_c.loc(time) in timelocs:
                        raise ValueError ('times diferentes')
                    xmlDict.setdefault('times', []).append(time)
            except:
                xmlDict.setdefault('times', []).append(time)
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
                if metronome not in xmlDict['metronomes']:
                    metronomelocs = [f_c.loc(x) for x in xmlDict['metronomes']]
                    if f_c.loc(metronome) in metronomelocs:
                        raise ValueError ('metronomes diferentes')
                    xmlDict.setdefault('metronomes', []).append(metronome)
            except KeyError:
                xmlDict.setdefault('metronomes', []).append(metronome)
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
            xmlDict['notes'][partID].append(note)
            Cduration = Cduration + duration
        else:
            p += 1
    xmlDict['times'] = f_c.times_com_duracoes(xmlDict['times'])
    return xmlDict

def musica_dict(xmlDict, tie=False, rest=None):
    musicaDict = {}
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
            #Ptempo = f_c.P_tempo(divisions,timeRefn1,note1)
            #Ntempo = f_c.N_tempo(divisions,timeRefn1,note1)
            musicaDict.setdefault(part, {})
            musicaDict[part].setdefault('Ncompasso', []).append(f_c.Ncompasso(note1))
            musicaDict[part].setdefault('tonalidade', []).append(f_c.val(keyRef))
            musicaDict[part].setdefault('Fcompasso', []).append(f_c.val(timeRefn1))
            musicaDict[part].setdefault('andamento', []).append(f_c.val(metronome))
            musicaDict[part].setdefault('grau',[]).append(grau)
            musicaDict[part].setdefault('Pcompasso',[]).append(Pcompasso)
            #musicaDict[part].setdefault('Ptempo', []).append(Ptempo)
            #musicaDict[part].setdefault('Ntempo', []).append(Ntempo)
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
                musicaDict[part].setdefault('duracao', []).append(duracao)
                musicaDict[part].setdefault('intDia', []).append(intDia)
                musicaDict[part].setdefault('intCro', []).append(intCro)
                musicaDict[part].setdefault('intQua', []).append(intQua)    
    return musicaDict

def analise(musicaDict, keys, keystype, atribs, atribstype, tudo=False):
    analiseDict = {}
    for part, atrib1 in musicaDict.items():
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
                        keyAnalise.append(tuple(atrib1[key][p1:p2]))
                    elif ktype == 1:
                        keyAnalise.append(tuple(atrib1[key][p1:p2-1]))
                    elif ktype == 2:
                        keyAnalise.append(atrib1[key][p1])
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
                analiseDict.setdefault(keyAnalise,[]).append(valueAnalise)
    return analiseDict

xmlDict = xml_dict(xml)
musicaDict = musica_dict(xmlDict)

intDia = analise(musicaDict,['intDia'],[0],['Ncompasso','Pcompasso'],[2,2])
grau = analise(musicaDict,['grau', 'intDia'],[0,1],['Ncompasso','Pcompasso','tonalidade'],[2,2,3])
debug = 0

'''
formas de pesquisa:

0= p1:p2 = trecho completo
1= p1:(p2-1) = trecho completo menos o último valor, como para intervalos e graus
2= p1 = só o primeiro valor do trecho
3= sp1 = set, somente valores unicos do trecho
4= sp2-1 = set, somente valores unicos do trecho menos o último

tudo - True, todos os valores que não estão na chave aparecem no resultado
'''

