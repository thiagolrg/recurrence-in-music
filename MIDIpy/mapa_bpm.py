#usa o restante das formulas desse modulo para chegar ao mapa_bpm
def mapa_bpm(templimp,complista):
    mapabpm = []
    for linha in templimp:
        compref = temp_compref(linha,complista)
        bpm = bpm_(linha,compref)
        mapabpm.append([linha[1], bpm])
    return mapabpm

#retorna o compass ref. na complista
def temp_compref(linha,lista):
    for posicaot in range(len(lista)):
        if posicaot+1 == len(lista):
            return lista[posicaot]
        elif lista[posicaot+1][1] > linha[1]:
            return lista[posicaot]

#retorna o valor de metronomo e o bpm
def bpm_(templinha,complinha):
    m = metro(complinha)
    return (m, round(bpm_seg(templinha)/m,2))

#valor de tempo para calculo do bpm final
#seminima = 1, colcheia = 2 etc...
def metro(complinha):
    return complinha[5]/24

#bpm em seminima
def bpm_seg(tempolinha):
    return 60000000/tempolinha[3]