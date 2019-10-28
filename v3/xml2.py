with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Análise\MusicXML\Teste4.xml') as f:
    xmllista = []
    for linha in f.readlines():
        linha = linha.strip()
        linha = linha.replace('\n', '')
        xmllista.append(linha)

dicio = {}
counter = 0
duration = 0
for l in xmllista:
    if '<part id=' in l:
        l = l.lstrip('<part id="') 
        l = l.rstrip('">')
        partID = str(l)
        dicio.setdefault(partID,{})

    elif '</part>' in l:
        counter = 0

    elif '<divisions>' in l:
        l = l.lstrip('<divisions>') 
        l = l.rstrip('</divisions>')
        divisions = int(l)

    elif '<duration>' in l:
        l = l.lstrip('<duration>') 
        l = l.rstrip('</duration>')
        duration = int(l)
        counter = counter + duration

    elif '<measure number= "' in l:
        l = l.lstrip('<measure number= "') 
        l = l.rstrip('" width="694">')
        measureNumber = int(l)

    elif '<beats>' in l:
        l = l.lstrip('<beats>') 
        l = l.rstrip('</beats>')
        beats = int(l)

    elif '<beat-unit>' in l:
        l = l.lstrip('<beat-unit>') 
        l = l.rstrip('</beat-unit>')
        beatsUnit = str(l)

    elif '<per-minute>' in l:
        l = l.lstrip('<per-minute>') 
        l = l.rstrip('</per-minute>')
        perMinute = int(l)

    elif '<beat-type>' in l:
        l = l.lstrip('<beat-type>') 
        l = l.rstrip('</beat-type>')
        beatType = int(l)

    elif '<step>' in l:
        l = l.lstrip('<step>') 
        l = l.rstrip('</step>')
        step = str(l)
        dicio[partID].setdefault('step',[]).append(tuple([counter,step]))

    elif '<alter>' in l:
        l = l.lstrip('<alter>') 
        l = l.rstrip('</alter>')
        alter = int(l)

    elif '<octave>' in l:
        l = l.lstrip('<octave>') 
        l = l.rstrip('</octave>')
        octave = int(l)


debug = 0