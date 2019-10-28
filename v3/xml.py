import xmltodict

with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Análise\MusicXML\Teste4.xml') as f:
    musica = str()
    for linha in f.readlines():
        linha = linha.strip()
        linha = linha.replace('\n', '')
        musica = musica+linha
    xmldict = xmltodict.parse(musica)

def ut(divisions, beatType):
    return (divisions*4)/beatType

def duration_por_tempo(duration, division, beatType):
    return duration/ut(divisions, beatType)

def duration_no_compasso(duration,beats):
    while duration//beats > 0:
        duration = duration - beats
    return duration

def node_iter(node):
    if isinstance(node, dict) == True:
        return node.items()
    if isinstance(node, tuple) == True:
        return node_iter(node[1])
    if isinstance(node, list) == True:
        node = [valor2 for valor1 in node for valor2 in valor1.items()]
        return node
    raise ValueError('tipo de node não classificado')

mapamus = {}
for scorePartwise_item in node_iter(xmldict['score-partwise']):
    if 'part' in scorePartwise_item:
        for part_item in node_iter(scorePartwise_item):
            if '@id' in part_item:
                partID = part_item[1]
            if 'measure' in part_item:
                for measure_item in node_iter(part_item):
                    if '@number' in measure_item:
                        measure_number = int(measure_item[1])
                    if 'attributes' in measure_item:
                        for attributes_item in node_iter(measure_item):
                            if 'divisions' in attributes_item:
                                divisions = int(attributes_item[1])
                            elif 'time' in attributes_item:
                                for time_item in node_iter(attributes_item):
                                    if 'beat-type' in time_item:
                                        beatType = int(time_item[1])
                                    elif 'beats' in time_item:
                                        beats = int(time_item[1])
                    if 'note' in measure_item:
                        for note_item in node_iter(measure_item):
                            if 'rest' in note_item:
                                rest = note_item[1]
                                octave = rest
                                step = rest
                            elif 'duration' in note_item:
                                duration = int(note_item[1])
                            elif 'pitch' in note_item:
                                for pitch_item in note_item[1].items():
                                    if 'octave' in pitch_item:
                                        octave = int(pitch_item[1])
                                    elif 'step' in pitch_item:
                                        step = pitch_item[1]
                        
                        durationPorTempo = duration_por_tempo(duration, divisions, beatType)
                        compasso = tuple([beats,beatType])

                        mapamus.setdefault(partID, {})
                        mapamus[partID].setdefault('durationPorTempo', []).append(durationPorTempo)
                        mapamus[partID].setdefault('measure_number', []).append(measure_number)
                        mapamus[partID].setdefault('step', []).append(step)
                        mapamus[partID].setdefault('octave', []).append(octave)
                        mapamus[partID].setdefault('compasso', []).append(compasso)

debug = 0

'''
    for measure in part['measure']:
        if 'time' in measure['attributes']:
            den = int(measure['attributes']['time']['beat-type'])
        if 'divisions' in measure['attributes']:
            divisions = int(measure['attributes']['divisions'])
        if 'pitch' in measure['note']:
            note = measure['note']
        else:

            for note in measure['note']:
                if mapamus['duration'] == []:
                    duration_desdeinicio = duration_por_tempo(note['duration'],divisions,den)
                    continue
                else:
                    t1 = mapamus['duration'][-1:]
                    duration_desdeinicio = mapamus['duration'][-1:][0] + duration_por_tempo(note['duration'],divisions,den)
                mapamus['duration'].append(duration_desdeinicio)
                continue

        if mapamus['duration'] == []:
            duration_desdeinicio = duration_por_tempo(note['duration'],divisions,den)
        else:
            duration_desdeinicio = mapamus['duration'][-1:][0] + duration_por_tempo(note['duration'],divisions,den)
        mapamus['duration'].append(duration_desdeinicio)

            mapamus['voice'].append(note['voice'])
            mapamus['partid'].append(part['@id'])
            mapamus['step'].append(note['pitch']['step'])
            mapamus['octave'].append(note['pitch']['octave'])
            mapamus['duration'].append(note['duration'])
            mapamus['measureNumber'].append(measure['@number'])
            mapamus['beats'].append(measure['attributes']['time']['beats'])
            mapamus['beat-type'].append(measure['attributes']['time']['beat-type'])

((segint), (segdur)): (nome,posição,compasso,tempo)

debug=0
'''

