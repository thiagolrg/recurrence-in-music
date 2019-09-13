#____________________________________________________________________________________
#formulas Ref.
# recebem a linha e o mapa, retornam o compasso, bpm, localizacao e duracao

#esse arquivo precisa melhorar porque as funcoes locdur e compbpm sao chamadas
#varias vezes desnecessariamente

def locdur(linha,mapa):
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            ref = mapa[posicaot]
        elif mapa[posicaot+1][0] >= linha[1]:
            ref = mapa[posicaot]
            break
    return  ref

def compbpm(linha,mapa):
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            ref = mapa[posicaot]
        elif mapa[posicaot+1][0] > linha[1]:
            ref = mapa[posicaot]
            break
    return  ref

def comp(linha,mapa):
    ref = compbpm(linha,mapa[0])[1]
    return ref

def bpm(linha,mapa):
    bpmref = compbpm(linha,mapa[1])[1]
    return bpmref

def uc(linha,ppq):
    uc = ((ppq*4)/linha[1][1])*linha[1][0]
    return uc

#essas funcoes chamam locdur e compbpm mais vezes que o necessário
def locR(linha,mapa,ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    locR = (linha[1] - ref[0])/uc(ref,ppq)
    return locR

def locT(linha,mapa,ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    locT = ((locR(linha,mapa,ppq,ref)%1)*ref[1][0])+1
    return locT

def locC(linha,mapa,ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    locC = int(locR(linha,mapa,ppq,ref) + ref[2][0])
    return locC

def durR(linha,mapa,ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    durR = locR(linha,mapa,ppq,ref)*ref[1][0]
    return durR

def durI(linha,mapa,ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    durI = durR(linha,mapa,ppq,ref) + ref[3]
    return durI

def tudo(linha,mapa,ppq)
    refcomp = compbpm(linha[0],mapa)
    refbpm = compbpm(linha[1],mapa)
    reflocdur = locdur(linha,mapa)
    comp = refcomp[1]
    bpm = refbpm[1]
    locR
    locC
    locT
    durR
    durI
    return