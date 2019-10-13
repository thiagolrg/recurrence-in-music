#as formulas mapa_ chaman todas as outras desses arquivo de formas diferentes
#sao as unicas usadas diretamente pelo programa
#conversao da lista tempo em mapa de bpm
import f1_mapa as f1m

def mapa_bpm(templimp,complista):
    mapabpm = []
    for linha in templimp:
        compref = f1m.temp_comp(linha,complista)
        bpm = f1m.bpmf(linha,compref)
        mapabpm.append([linha[1], bpm])
    return mapabpm
 
#conversao da lista compasso em mapa de formulas localizações e durações
def mapa_comploc(complista,ppq):
    if complista[0][1] == 0:
        mapalocdur = [[0, f1m.comp(complista[0]), 0, 0.0]]
        for posicao in range(len(complista)):
            if posicao+1 < len(complista):
                comp = f1m.comp(complista[posicao+1])
                locRr = f1m.locR(complista[posicao+1],complista[posicao],ppq)
                durRr = f1m.durR(complista[posicao+1],complista[posicao],ppq)
                locCr = int(locRr + mapalocdur[posicao][2])
                durIr = durRr + mapalocdur[posicao][3]
                mapalocdur.append([complista[posicao+1][1], comp, locCr, durIr])
    else:
        raise ValueError('compasso nao comeca no 0')
    return mapalocdur