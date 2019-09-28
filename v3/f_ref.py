<<<<<<< HEAD:v3/f_ref.py
<<<<<<< HEAD:v3/f_segmenta.py
'''import limpaextraimapa
=======
import limpaextraimapa
>>>>>>> parent of 7cc848b... zuei tudo e vou voltar para outro commit:v3/f_segmenta.py

=======
>>>>>>> parent of 767f250... baguncei tudo e ajeitei tudo de novo tentando fazer o loop no programa todo:v3/f_ref.py
#____________________________________________________________________________________
#formulas Ref.
# recebem a linha e o mapa, retornam o compasso, bpm, localizacao e duracao

#esse arquivo precisa melhorar porque as funcoes locdur e compbpm sao chamadas
#varias vezes desnecessariamente
#do jeito que esta aqui cada def funciona independentemente, o que e legal
#mas quando se chama uma atras da outra no arquivo geral as locdur e compbpm
#sao chamadas varias vezes para o mesmo resultado
import entrada

def locdur(linha,mapa):
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            ref = mapa[posicaot]
        elif mapa[posicaot+1][0] >= linha[1]:
            ref = mapa[posicaot]
            break
    return  ref

def comp_bpm(linha,mapa,compbpm):
    if compbpm == 'comp':
        mapa = mapa[0]
    elif compbpm == 'bpm':
        mapa = mapa[1]
    else:
        raise ValueError('escolha comp ou bpm')  
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            ref = mapa[posicaot]
        elif mapa[posicaot+1][0] > linha[1]:
            ref = mapa[posicaot][1]
            break
    return  ref

def uc(linha,ppq=entrada.ppq):
    uc = ((ppq*4)/linha[1][1])*linha[1][0]
    return uc

#essas funcoes chamam locdur e compbpm mais vezes que o necessário
def locR(linha,mapa=entrada.mapa,ppq=entrada.ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    locR = (linha[1] - ref[0])/uc(ref,ppq)
    return locR

def locT(linha,mapa=entrada.mapa,ppq=entrada.ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    locT = round(((locR(linha,mapa,ppq,ref)%1)*ref[1][0])+1,2)
    return locT

def locC(linha,mapa=entrada.mapa,ppq=entrada.ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    locC = int(locR(linha,mapa,ppq,ref) + ref[2])
    return locC

def durR(linha,mapa=entrada.mapa,ppq=entrada.ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    durR = locR(linha,mapa,ppq,ref)*ref[1][0]
    return durR

def durI(linha,mapa=entrada.mapa,ppq=entrada.ppq,ref=list()):
    if ref == []:
        ref = locdur(linha,mapa[0])
    durI = durR(linha,mapa,ppq,ref) + ref[3]
    return durI

#nao prestou
#def tudo(linha,mapa,lista,ppq):
#    refcomp = compbpm(linha,mapa[0])
#    refbpm = compbpm(linha,mapa[1])
#    reflocdur = locdur(linha,mapa[0])
#    locR = (linha[1] - reflocdur[0])/uc(reflocdur,ppq)
#    durR = locR*reflocdur[1][0]
#    if 'comp' in lista:
#        comp = refcomp[1]
#        return comp
#    if 'bpm' in lista:
#       bpm = refbpm[1]
#        return bpm
#    if 'locC' in lista:
#        locC = int(locR + reflocdur[2][0])
#        return locC
#    if 'locT' in lista:
#        locT = ((locR%1)*reflocdur[1][0])+1
#        return locT
#    if 'durI' in lista:
#        durI = durR + reflocdur[3]
#        return durI