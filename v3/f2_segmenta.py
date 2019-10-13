#____________________________________________________________________
#Segmenta
import f1_segmenta as f1_s
import collections

def mapa_mus(nome, tom, modo, notas, mapacomploc, mapabpm, ppq):
    nv = 0
    mapamus = {'nome': nome, 'tom': tom, 'modo': modo, 'vozes': {}}
    for voz in notas:
        mapamus['vozes'].setdefault(nv, {})
        for linha in range(len(voz)):
            if linha+1 < len(voz): 
                reflocdur = f1_s.ref_locdur(voz[linha][0],mapacomploc)
                non = voz[linha+1][0]
                noff = voz[linha][1]
                linhadur = f1_s.durI(voz[linha][0],mapacomploc,ppq,ref=reflocdur)
                nondur = f1_s.durI(non,mapacomploc,ppq)
                noffdur = f1_s.durI(noff,mapacomploc,ppq)

                mapamus['vozes'][nv].setdefault('locC', []).append(f1_s.locC(voz[linha][0], mapacomploc, ppq, ref=reflocdur))
                mapamus['vozes'][nv].setdefault('locT', []).append(f1_s.locT(voz[linha][0], mapacomploc, ppq, ref=reflocdur))
                mapamus['vozes'][nv].setdefault('inte', []).append(non[4]-voz[linha][0][4])
                mapamus['vozes'][nv].setdefault('dur', []).append(nondur-linhadur)
                mapamus['vozes'][nv].setdefault('comp', []).append(f1_s.comp_bpm(voz[linha][0],mapacomploc))
                mapamus['vozes'][nv].setdefault('bpm', []).append(f1_s.comp_bpm(voz[linha][0],mapabpm))
                #mapamus['vozes'][nv].setdefault('durp', []).append([nondur-linhadur, nondur-noffdur])
            else:
                nv = nv + 1
    return mapamus