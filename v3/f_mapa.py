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
    bpmf = [m, bpm1(templinha)/m]
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
