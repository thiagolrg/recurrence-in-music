'''from limpaextraimapa import final as finali

segintelista = tuple()
for posicao in finali:
    segintelista = tuple(append(posicao[10])
    segdurlista.append(posicao[11])
    segintedurlista.append([posicao[10],posicao[11]])




inteunico = []
intequant = {}

for posicao in segintstr:
    if intequant.get(segintstr[posicao]) == None:
        intequant.setdefault(segintstr[posicao], posicao)
    else:
        intequant.setdefault(segintstr[posicao], intequant.get(segintstr[posicao]).append(posicao))

        if segintstr[posicao1] == segintstr[posicao2]:
            indices.append(posicao2)
        if posicao2+1 == len(segintstr):
            inteunico.append(segintstr[posicao1])
            for i in indices:
                finali[i].append(len(indices))

import csv
with open("contagemdeintervalos.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(intequant)

debug = intequant'''