import funcoesv2

entrada = funcoesv2.entrada_csv("localizacaocompassobpm3.csv")
entradalimpa = funcoesv2.limpeza(entrada)
ppq = funcoesv2.tira_ppq(entradalimpa)
complista = funcoesv2.comp_lista(entradalimpa)
templista = funcoesv2.temp_lista(entradalimpa)

#faz uma lista acrescendando locc loct e dur a complista
#localizacao compasso, localizacao tempo, duracao
if complista[0][1] == 0:
   compcomloc = []
   compcomloc.append([[1, 1.0], 0, complista[0]])
   for posicao in range(len(complista)):
        if posicao+1 < len(complista):
            uc = funcoesv2.uc(complista[posicao], ppq)
            nt = funcoesv2.nt(complista[posicao])
            locR = (complista[posicao+1][1] - complista[posicao][1])/uc
            locI = locR + compcomloc[posicao][0][0]
            locC = int(locI)
            locT = ((locI%1)*nt)+1
            durI = (locR*nt) + compcomloc[posicao][1]
            junta = [[locC, locT], durI, complista[posicao+1]]
            compcomloc.append(junta)
            #locR = localizacao relativa, desde a ultima formula de compasso
            #locI = localizacao desde o inicio
            #locC = localizacao em compasso
            #locT = localizacao em tempos por compasso
            #durI = duracao desde o inicio em tempos de compasso
else:
   raise ValueError('compasso nao comeca no inicio')

#faz uma lista acrescentando bpm e tamanho de tempo de ref para cada mensagem tempo
tempcombpm = []
for linha in templista:
    bpm1 = funcoesv2.bpm_1(linha)
    compref = funcoesv2.temp_comp(linha, complista)
    metron = funcoesv2.metron(compref)
    bpmf = bpm1/metron
    junta = [[metron, bpmf], linha]
    tempcombpm.append(junta)

entradapronta = []
for linha in entradalimpa:
    compref = funcoesv2.comp_ref(linha,compcomloc)
    tempref = funcoesv2.temp_ref(linha,tempcombpm)
    fcompref = funcoesv2.fcomp_ref(linha,complista)
    uc = funcoesv2.uc(compref[2],ppq)
    nt = funcoesv2.nt(compref[2])
    locR = (linha[1] - compref[2][1])/uc
    locI = locR + compref[0][0]
    locC = int(locI)
    locT = ((locI%1)*nt)+1
    durI = (locR*nt) + compref[1]
    junta = [fcompref, tempref[0],[locC, locT], durI, linha]
    entradapronta.append(junta)

import csv
with open('entradapronta.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(entradapronta)

#acho que é possivel usar a mesma funcao_ref para tempo ref e formula de compasso ref
#e a mesma funcao para localizacao e duracao total

#como vou juntar tudo a entradalimpa no fim as unicas informacoes que preciso manter das templist e complist são:
#complist [deltat, [locC, locT], durI]
#templist [deltat, [metron, bpmf]]

#preciso enxergar algum jeito de transformar esse monte de loc e dur em uma única funcao
#uma funcao que tem linha, listaref e ppq como entrada
#e devolve [[locC, locT], durI]
