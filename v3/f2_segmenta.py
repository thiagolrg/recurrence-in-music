#____________________________________________________________________
#Segmenta
import f1_segmenta as f1_s

def mapa_seg(notas, mapacomploc, mapabpm, ppq):
    p = 0
    mapaseg = [[]]
    for voz in notas:
        locCvoz = []
        locTvoz = []
        intevoz = []
        durvoz = []
        compvoz = []
        tempvoz = []
        for linha in range(len(voz)):
            if linha+1 < len(voz): 
                reflocdur = f1_s.ref_locdur(voz[linha][0],mapacomploc)
                non = voz[linha+1][0]
                noff = voz[linha][1]
                linhadur = f1_s.durI(voz[linha][0],mapacomploc,ppq,ref=reflocdur)
                nondur = f1_s.durI(non,mapacomploc,ppq)
                noffdur = f1_s.durI(noff,mapacomploc,ppq)

                locCvoz.append(f1_s.locC(voz[linha][0], mapacomploc, ppq, ref=reflocdur))
                locTvoz.append(f1_s.locT(voz[linha][0], mapacomploc, ppq, ref=reflocdur))
                intevoz.append(non[4]-voz[linha][0][4])
                durvoz.append(nondur-linhadur)
                compvoz.append(f1_s.comp_bpm(voz[linha][0],mapacomploc))
                tempvoz.append(f1_s.comp_bpm(voz[linha][0],mapabpm))
                #durvozes.append([nondur-linhadur, nondur-noffdur])
            else:
                mapaseg[p].append(tuple(locCvoz))
                mapaseg[p].append(tuple(locTvoz))
                mapaseg[p].append(tuple(intevoz))
                mapaseg[p].append(tuple(durvoz))
                mapaseg[p].append(tuple(compvoz))
                mapaseg[p].append(tuple(tempvoz))
                if len(mapaseg) != len(notas):
                    mapaseg.append([])
                    p = p + 1
    return mapaseg
'''
    for compvoz, bpmvoz, locCvoz, locTvoz, intevoz, durvoz in zip(compvozes, tempvozes, locCvozes, locTvozes, intevozes, durvozes):
        v = v+1
        for posicao1 in range(len(intevoz)):
            for posicao2 in range(posicao1, len(intevoz)):

                musica.setdefault((v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1), 
                                 (tuple(intevoz[posicao1:posicao2+1]),
                                 tuple(durvoz[posicao1:posicao2+1]),
                                 tuple(compvoz[posicao1:posicao2+1]),
                                 tuple(bpmvoz[posicao1:posicao2+1])))

                if tuple(intevoz[posicao1:posicao2+1]) in teste.values(): 
                    teste.setdefault(tuple(intevoz[posicao1:posicao2+1]),
                                    (teste.get(tuple(intevoz[posicao1:posicao2+1])),
                                    (v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1)))
                else:
                    teste.setdefault(tuple(intevoz[posicao1:posicao2+1]),
                                    (v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1))
                                    
                
                comppronto = []
                bpmpronto = []
                for valorcomp, valorbpm in zip(compvoz[posicao1:posicao2+1], bpmvoz[posicao1:posicao2+1]):
                    if valorcomp not in comppronto:
                        comppronto.append(valorcomp)
                    if valorbpm not in bpmpronto:
                        bpmpronto.append(valorbpm)

                finalcsv.append([nome, tom, modo,
                                (v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1),
                                tuple(intevoz[posicao1:posicao2+1]), tuple(durvoz[posicao1:posicao2+1]),
                                comppronto, bpmpronto])
    testet = teste.items()
    finaldic.setdefault(nome, musica)
    return (finalcsv, finaldic)'''
