#conversao da lista compasso em mapa de formulas localizações e durações
def mapa_complocdur(complista,ppq):
    if complista[0][1] == 0:
        mapalocdur = [[0, comp(complista[0]), 0, 0.0]]
        for posicao in range(len(complista)):
            if posicao+1 < len(complista):
                locRa = locR(complista[posicao+1],complista[posicao],ppq)
                durRa = durR(complista[posicao+1],complista[posicao],ppq)
                mapalocdur.append([complista[posicao+1][1],
                                   comp(complista[posicao+1]),
                                   int(locRa + mapalocdur[posicao][2]),
                                   durRa + mapalocdur[posicao][3]])
    else:
        raise ValueError('compasso nao comeca no 0')
    return mapalocdur

#____________________________________________________________________________________
#recebe a mensagem de 'Time_signature' e retorna a formula de compasso como musicos conhecem
def comp(complinha):
    return (num(complinha), den(complinha))

#numerador do compasso
def num(complinha):
    return complinha[3]

#denominador do compasso
def den(complinha):
    return 2**complinha[4]

#_____________________________________________________________
#formulas para duracao e localizacao
#unidade de compasso em ppq
def uc(comp, ppq):
    return ((ppq*4)/(den(comp)))*num(comp)

#retorna a localizacao relativa desde a ultima formula de compasso
def locR(linha,compref,ppq):
    return (linha[1] - compref[1])/uc(compref,ppq)

#posicao dentro do compasso em tempos de compasso
def locT(linha,compref,ppq):
    return ((locR(linha,compref,ppq)%1)*num(compref))+1

#quantos tempos de compasso passaram desde o ultimo compasso
def durR(linha,compref,ppq):
    return locR(linha,compref,ppq)*num(compref)
