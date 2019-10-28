import xmltodict
from xml.dom import minidom

with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\MusicXML\MIDIStressTest.xml') as f:
    musica = str()
    for linha in f.readlines():
        linha = linha.strip()
        linha = linha.replace('\n', '')
        musica = musica+linha
    xmldict = xmltodict.parse(musica)
    xmldom = minidom.parseString(musica)

mapamus = {'voice': [],
           'partid': [],
           'step': [],
           'octave': [],
           'duration': [],
           'measureNumber': [],
           'beats': [],
           'beat-type': []}

'''
listanotas = xmldom.documentElement.getElementsByTagName('note')
for nota in listanotas:
    if 'division' in nota.parentNode.getElementsByTagName('attribues').childNodes.
    divisions = int(nota.parentNode.getElementsByTagName('attributes')[0].getElementsByTagName('divisions')[0].childNodes[0].data)
    duration = int(nota.getElementsByTagName('duration')[0].childNodes[0].data)
    compDen = int(nota.parentNode.getElementsByTagName('attributes')[0].getElementsByTagName('time')[0].getElementsByTagName('beat-type')[0].childNodes[0].data)
    duration_por_tempo = duration/((divisions*4)/compDen)
    if mapamus['duration'] == []:
        duration_desdeinicio = duration_por_tempo
    else:
        duration_desdeinicio = mapamus['duration'][:-1][0]+duration_por_tempo
    mapamus['duration'].append(duration_desdeinicio)
'''
debug = 0

def division_por_tempo(divisions, den):
    return (int(divisions)*4)/den

def duration_por_tempo(duration,division,den):
    return int(duration)/division_por_tempo(divisions, den)

duration_desdeinicio = float()
for part in xmldict['score-partwise']['part']:

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

'''
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

