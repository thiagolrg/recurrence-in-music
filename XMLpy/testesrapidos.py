import xmldict as f_xd
import dirEinp as f_d
import xmltodict

xml = f_d.entrada_xml(r'C:\Users\Thiago.DESKTOP-13409IC\Documents\testeChordVoiceLayer.xml')
xmldict = xmltodict.parse(''.join(xml))
debug = 0

def to_list(node):
    if isinstance(node, list) == True:
        return node
    else:
        return [node]

dicionotas = {}
for parte in to_list(xmldict['score-partwise']['part']):
    for measure in to_list(parte['measure']):
        for note in to_list(measure['note']):
            if 'chord' not in note:
                voice = note['voice']
                dicionotas.setdefault(voice, []).append([note])
            else:
                dicionotas[voice][-1].append(note)

debug = 0
'''
counter = 0
for p in range(len(arquivo)):
    assert 'score-timewise' not in arquivo[p], 'XML é score-timewise, não implementado'
    assert 'chord' not in arquivo[p], 'tag "chord" no XML. Não podem existir notas simultâneas na mesma parte'
    assert '<backup>' not in arquivo[p], 'tag "backup" no XML. Não podem existir notas simultâneas na mesma parte'
    assert '<forward>' not in arquivo[p], 'tag "forward" no XML. Não podem existir notas simultâneas na mesma parte'
    xml.append(arquivo[p])
    if p > 2 and p < len(arquivo):
        if '</' not in xml[p] and '/>' not in xml[p] and '<!' not in xml[p]:
            xml[p] = xml[p].rstrip('>')+' counter ='+'"'+str(counter)+'"'+'>'
    if '<duration>' in arquivo[p]:
        duration = int(arquivo[p].replace('<duration>','').replace('</duration>',''))
        counter = counter + duration
    if '</part>' in arquivo[p]:
        counter = 0
    xmltodict.parse(''.join(xml))

debug = 0
'''