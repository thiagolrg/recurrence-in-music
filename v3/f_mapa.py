#as formulas mapa_ chaman todas as outras desses arquivo de formas diferentes
#sao as unicas usadas diretamente pelo programa
#conversao da lista tempo em mapa de bpm
from tudaoteste import ppq as ppq


def mapa_bpm(templimp,complista):
    mapabpm = []
    for linha in templimp:
        compref = temp_comp(linha,complista)
        bpm = bpmf(linha,compref)
        mapabpm.append([linha[1], bpm])
    return mapabpm
 
#conversao da lista compasso em mapa de formulas localizações e durações
def mapa_locdur(complista):
    import f_mapa
    if complista[0][1] == 0:
        mapalocdur = [[0, 1, 0.0]]
        for posicao in range(len(complista)):
            if posicao+1 < len(complista):
                locRr = locR(complista[posicao+1],complista[posicao],ppq)
                durRr = durR(complista[posicao+1],complista[posicao],ppq)
                locCr = int(locRr + mapalocdur[posicao][2])
                durIr = durRr + mapalocdur[posicao][3]
                mapalocdur.append([complista[posicao+1][1], locCr, durIr])
    else:
        raise ValueError('compasso nao comeca no 0')
    return mapalocdur

def mapa_complocdur(mapalocdur, complista):
    for posicao in range(len(complista)):
        mapacomplocdur = []
        comp = comp(complista[posicao])
        mapacomplocdur = mapalocdur[posicao].insert(1,comp)
    return mapacomplocdur

#____________________________________________________________________________________
#recebe a mensagem de compasso e retorna a formula de compasso como musicos conhecem
def comp(complinha):
    complinha = [num(complinha), den(complinha)]
    return  complinha

#numerador do compasso
def num(complinha):
    num = complinha[3]
    return num

#denominador do compasso
def den(complinha):
    den = 2**complinha[4]
    return den

#unidade de compasso em ppq
#nao e usado diretamente, chamdo pelas funcoes localizacao e duracao
def uc(comp, ppq):
    uc = ((ppq*4)/(den(comp)))*num(comp)
    return uc

#_____________________________________________________________
#formulas para duracao e localizacao

#retorna a localizacao relativa desde a ultima formula de compasso
#nao e usado diretamente
#a parte inteira e a quantidade de compassos desde a ultima formula de compasso
#a parte fracionaria e usada para calcular a posicao dentro do compasso em que linha acontece
#ele todo e usado para calcucar a quantidade de tempos desde o compref.
def locR(linha,compref,ppq):
    locR = (linha[1] - compref[1])/uc(compref,ppq)
    return locR

#posicao dentro do compasso em tempos de compasso
def locT(linha,compref,ppq):
    locT = ((locR(linha,compref,ppq)%1)*num(compref))+1
    return locT

#quantos tempos de compasso passaram desde o ultimo compasso
def durR(linha,compref,ppq):
    durR = locR(linha,compref,ppq)*num(compref)
    return durR

#_____________________________________________
#formulas para bpm

#retorna o compass ref. na complista
def temp_comp(linha,lista):
    for posicaot in range(len(lista)):
        if posicaot+1 == len(lista):
            comp = lista[posicaot]
        elif lista[posicaot+1][1] > linha[1]:
            comp = lista[posicaot]
            break
    return  comp

#retorna o valor de metronomo e o bpm
def bpmf(templinha,complinha):
    m = metron(complinha)
    bpmf = [m, round(bpm1(templinha)/m,2)]
    return bpmf

#valor de tempo para calculo do bpm final
#seminima = 1, colcheia = 2 etc...
def metron(complinha):
    metron = complinha[5]/24
    return metron

#bpm em seminima
def bpm1(tempolinha):
    bpm1 = 60000000/tempolinha[3]
    return bpm1
