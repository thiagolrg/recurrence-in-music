'''import limpaextraimapa

#____________________________________________________________________________________
#formulas Ref.
# recebem a linha e o mapa, retornam o compasso, bpm, localizacao e duracao

#esse arquivo precisa melhorar porque as funcoes locdur e compbpm sao chamadas
#varias vezes desnecessariamente
#do jeito que esta aqui cada def funciona independentemente, o que e legal
#mas quando se chama uma atras da outra no arquivo geral as locdur e compbpm
#sao chamadas varias vezes para o mesmo resultado

#retorna a linha referencia para calculo das loc e dur
def ref_locdur(linha,mapa):
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            ref = mapa[posicaot]
        elif mapa[posicaot+1][0] >= linha[1]:
            ref = mapa[posicaot]
            break
    return  ref

#retorna o compasso ou o tempo referente a linha
#para compasso recebe o mapacomplocdur
#para tempo recebe o mapabpm
def comp_bpm(linha,mapa): 
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            ref = mapa[posicaot]
        elif mapa[posicaot+1][0] > linha[1]:
            ref = mapa[posicaot][1]
            break
    return  ref

def uc(linha,ppq=limpaextraimapa.ppq):
    uc = ((ppq*4)/linha[1][1])*linha[1][0]
    return uc

#funcoes que usam mapacomplocdur
def locR(linha,mapa=limpaextraimapa.mapacomplocdur,ppq=limpaextraimapa.ppq,ref=list()):
    if ref == []:
        ref = ref_locdur(linha,mapa)
    locR = (linha[1] - ref[0])/uc(ref,ppq)
    return locR

def locT(linha,mapa=limpaextraimapa.mapacomplocdur,ppq=limpaextraimapa.ppq,ref=list()):
    if ref == []:
        ref = ref_locdur(linha,mapa)
    locT = round(((locR(linha,mapa,ppq,ref)%1)*ref[1][0])+1,2)
    return locT

def locC(linha,mapa=limpaextraimapa.mapacomplocdur,ppq=limpaextraimapa.ppq,ref=list()):
    if ref == []:
        ref = ref_locdur(linha,mapa)
    locC = int(locR(linha,mapa,ppq,ref) + ref[2])
    return locC

def durR(linha,mapa=limpaextraimapa.mapacomplocdur,ppq=limpaextraimapa.ppq,ref=list()):
    if ref == []:
        ref = ref_locdur(linha,mapa)
    durR = locR(linha,mapa,ppq,ref)*ref[1][0]
    return durR

def durI(linha,mapa=limpaextraimapa.mapacomplocdur,ppq=limpaextraimapa.ppq,ref=list()):
    if ref == []:
        ref = ref_locdur(linha,mapa)
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
#        return durI'''