#____________________________________________________________________
#Segmenta
import f1_segmenta

def musica_final(nome, tom, modo, vozeslista, mapacomplocdur, mapabpm, ppq, finalcsv, finaldic):
    p = 0
    v = 0
    lcomp = [[]]
    lbpm = [[]]
    llocC = [[]]
    llocT = [[]]
    inte = [[]]
    dur = [[]]
    musica = {'tom' : tom, 'modo' : modo}
    for voz in vozeslista:
        for linha in range(len(voz)):
            if linha+1 < len(voz): 
                comp = f1_segmenta.comp_bpm(voz[linha][0],mapacomplocdur)
                bpm = f1_segmenta.comp_bpm(voz[linha][0],mapabpm)
                reflocdur = f1_segmenta.ref_locdur(voz[linha][0],mapacomplocdur)
                locC = f1_segmenta.locC(voz[linha][0], mapacomplocdur, ppq, ref=reflocdur)
                locT = f1_segmenta.locT(voz[linha][0], mapacomplocdur, ppq, ref=reflocdur)
                lcomp[p].append(comp)
                lbpm[p].append(bpm)
                llocC[p].append(locC)
                llocT[p].append(locT)
                non = voz[linha+1][0]
                noff = voz[linha][1]
                linhadur = f1_segmenta.durI(voz[linha][0],mapacomplocdur,ppq,ref=reflocdur)
                nondur = f1_segmenta.durI(non,mapacomplocdur,ppq)
                noffdur = f1_segmenta.durI(noff,mapacomplocdur,ppq)
                inte[p].append(non[4]-voz[linha][0][4])
                dur[p].append(nondur-linhadur)
                #dur[p].append([nondur-linhadur, nondur-noffdur])
            else:
                if len(llocC) != len(vozeslista):
                    lcomp.append([])
                    lbpm.append([])
                    llocC.append([])
                    llocT.append([])
                    inte.append([])
                    dur.append([])
                    p = p + 1

    for compvoz, bpmvoz, locCvoz, locTvoz, intevoz, durvoz in zip(lcomp, lbpm, llocC, llocT, inte, dur):
        v = v+1
        for posicao1 in range(len(intevoz)):
            for posicao2 in range(posicao1, len(intevoz)):
                musica.setdefault((v, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1), 
                                 (tuple(intevoz[posicao1:posicao2+1]),
                                 tuple(durvoz[posicao1:posicao2+1]),
                                 tuple(compvoz[posicao1:posicao2+1]),
                                 tuple(bpmvoz[posicao1:posicao2+1])))
                
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
    finaldic.setdefault(nome, musica)
    return (finalcsv, finaldic)
