import limpaextraimapa, f_segmenta

vozeslista = limpaextraimapa.vozeslista
nome = limpaextraimapa.nomemusica
tom = limpaextraimapa.tom
modo = limpaextraimapa.modo
mapacomplocdur = limpaextraimapa.mapacomplocdur
mapabpm = limpaextraimapa.mapabpm

p = 0
lcomp = [[]]
lbpm = [[]]
llocC = [[]]
llocT = [[]]
inte = [[]]
dur = [[]]

for voz in vozeslista:
    for linha in range(len(voz)):
        if linha+1 < len(voz):
            
            #idealmente todos os compassos e bpms do segmento devem ser impressos
            #nao so os de inicio
            #talvez montar funcoes separadas com cada dessas
            #ou uma funcao com varios argumentos para ativar e desativar partes dessa
            if 'Note_on_c' in voz[linha]:
                comp = f_segmenta.comp_bpm(voz[linha],mapacomplocdur)
                bpm = f_segmenta.comp_bpm(voz[linha],mapabpm)
                reflocdur = f_segmenta.ref_locdur(voz[linha],mapacomplocdur)
                locC = f_segmenta.locC(voz[linha],ref=reflocdur)
                locT = f_segmenta.locT(voz[linha],ref=reflocdur)
                lcomp[p].append(comp)
                lbpm[p].append(bpm)
                llocC[p].append(locC)
                llocT[p].append(locT)

                non = []
                noff = []
                for busca in range(linha+1,len(voz)):
                    if noff == [] or non == []:
                        if 'Note_off_c'  in voz[busca]:
                            noff = voz[busca]
                        if 'Note_on_c' in voz[busca]:
                            non = voz[busca]
                    else:
                        linhadur = f_segmenta.durI(voz[linha],ref=reflocdur)
                        nondur = f_segmenta.durI(non)
                        noffdur = f_segmenta.durI(noff)
                        inte[p].append(non[4]-voz[linha][4])
                        dur[p].append(nondur-linhadur)
                        #dur[p].append([nondur-linhadur, nondur-noffdur])
                        break
    
        else:
            if len(llocC) != len(vozeslista):
                lcomp.append([])
                lbpm.append([])
                llocC.append([])
                llocT.append([])
                inte.append([])
                dur.append([])
                p = p + 1

final = []
for compvoz, bpmvoz, locCvoz, locTvoz, intevoz, durvoz in zip(lcomp, lbpm, llocC, llocT, inte, dur):
    for posicao1 in range(len(intevoz)):
        for posicao2 in range(posicao1, len(intevoz)):
            comppronto = []
            bpmpronto = []

            for valorcomp, valorbpm in zip(compvoz[posicao1:posicao2+1], bpmvoz[posicao1:posicao2+1]):
                if valorcomp not in comppronto:
                    comppronto.append(valorcomp)
                if valorbpm not in bpmpronto:
                    bpmpronto.append(valorbpm)
            final.append([nome, tom, modo, comppronto, bpmpronto, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1, sum(durvoz[posicao1:posicao2+1]), intevoz[posicao1:posicao2+1], durvoz[posicao1:posicao2+1]])
            #preiso acrescentar a duração do segmento em compassos alem de tempos
            #para isso preciso acrescentar no mapa complocdur a duracao em compassos
            #mudar as formulas f_ref para dar a duracao em compassos

debug = final
