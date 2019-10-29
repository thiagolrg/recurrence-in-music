def mapa_mus(notas, mapacomplocdur, mapabpm, ppq):
    nv = 0
    mapamus = {'vozes': {}}
    for voz in notas:
        mapamus['vozes'].setdefault(nv, {})
        for linha in range(len(voz)):
            if linha+1 < len(voz): 
                reflocdur = ref_locdur(voz[linha][0],mapacomplocdur)
                n = voz[linha+1][0]
                ndur = durA(voz[linha][0],ppq,reflocdur)
                nondur = durA(n,ppq,reflocdur)
                #noff = voz[linha][1]
                #noffdur = durA(noff,ppq,reflocdur)

                mapamus['vozes'][nv].setdefault('locC', []).append(locC(voz[linha][0],ppq,reflocdur))
                mapamus['vozes'][nv].setdefault('locT', []).append(locT(voz[linha][0],ppq,reflocdur))
                mapamus['vozes'][nv].setdefault('inte', []).append(n[4]-voz[linha][0][4])
                mapamus['vozes'][nv].setdefault('dur', []).append(nondur-ndur)
                mapamus['vozes'][nv].setdefault('comp', []).append(comp_bpm(voz[linha][0],mapacomplocdur))
                mapamus['vozes'][nv].setdefault('bpm', []).append(comp_bpm(voz[linha][0],mapabpm))
                #mapamus['vozes'][nv].setdefault('durp', []).append([nondur-ndur, nondur-noffdur])
            else:
                nv = nv + 1
    return mapamus

#retorna a linha referencia para calculo das loc e dur
def ref_locdur(linha,mapa):
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            ref = mapa[posicaot]
        elif mapa[posicaot+1][0] >= linha[1]:
            ref = mapa[posicaot]
            break
    return  ref

#localização desde a ultima mudança de compasso em compassos e frações de compassos
#localização relativa - locR
def locR(linha,ppq,ref):
    return (linha[1] - ref[0])/uc(ref,ppq)

#localização de inicio dentro do compasso em tempos e frações de tempos
#localização em tempos - locT
def locT(linha,ppq,ref):
    return round(((locR(linha,ppq,ref)%1)*ref[1][0]),2)

#localização em número do compasso - locC
def locC(linha,ppq,ref):
    return int(locR(linha,ppq,ref) + ref[2])

#duracao em tempos desde a ultima mudança de compasso
#duração relativa - durR
def durR(linha,ppq,ref):
    return locR(linha,ppq,ref)*ref[1][0]

#duração em tempos desde o inicio
#duração absoluta - durA
def durA(linha,ppq,ref):
    return durR(linha,ppq,ref) + ref[3]

#unidade de compasso em ppq
def uc(linha,ppq):
    return ((ppq*4)/linha[1][1])*linha[1][0]

#retorna o compasso ou o tempo referente a linha
#para retoornar compasso recebe o mapacomplocdur
#para retornar tempo recebe o mapabpm
def comp_bpm(linha,mapa): 
    for posicaot in range(len(mapa)):
        if posicaot+1 == len(mapa):
            return mapa[posicaot][1]
        elif mapa[posicaot+1][0] > linha[1]:
            return mapa[posicaot][1]
