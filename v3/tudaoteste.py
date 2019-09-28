#______________________________________________________
#limpa o arquivo de entrada e extrai as listas e constantes necessarias
import f_limpaextrai
import f_mapa
import f_segmenta

userinput = input('diretorio com arquivos midi de entrada: ')
diretorio = f_limpaextrai.caminhos_midi(userinput)

entrada = f_limpaextrai.midi_csv(diretorio[0])
entradalimpa = f_limpaextrai.limpeza(entrada)

nomemusica = f_limpaextrai.tira_nome(diretorio[0])
tom = f_limpaextrai.tira_tom(entradalimpa)
modo = f_limpaextrai.tira_modo(entradalimpa)
ppq = f_limpaextrai.tira_ppq(entradalimpa)

complista = f_limpaextrai.comp_lista(entradalimpa)
templista = f_limpaextrai.temp_lista(entradalimpa)
templimp = f_limpaextrai.templimp(templista)
notaslista = f_limpaextrai.notas_lista(entradalimpa)
vozeslista = f_limpaextrai.vozes_lista(notaslista)

#______________________________________________________
#chega ate o mapa usado para calcular as caracteristicas de qualquer linha da entrada limpa

#conversao da lista tempo em mapa de bpm
mapabpm = []
for linha in templimp:
    compref = f_mapa.temp_comp(linha,complista)
    bpm = f_mapa.bpmf(linha,compref)
    mapabpm.append([linha[1], bpm])
 
#conversao da lista compasso em mapa de formulas localizações e durações
if complista[0][1] == 0:
    mapacomplocdur = []
    mapacomplocdur = [[0, 1, 0.0]]
    for posicao in range(len(complista)):
        comp = f_mapa.comp(complista[posicao])
        mapacomplocdur[posicao].insert(1,comp)
        if posicao+1 < len(complista):
            locR = f_mapa.locR(complista[posicao+1],complista[posicao],ppq)
            durR = f_mapa.durR(complista[posicao+1],complista[posicao],ppq)
            locC = int(locR + mapacomplocdur[posicao][2])
            durI = durR + mapacomplocdur[posicao][3]
            mapacomplocdur.append([complista[posicao+1][1], locC, durI])
else:
    raise ValueError('compasso nao comeca no 0')

#____________________________________________________________________
#Segmenta

p = 0
lcomp = [[]]
lbpm = [[]]
llocC = [[]]
llocT = [[]]
inte = [[]]
dur = [[]]

for voz in vozeslista:
    for linha in range(len(voz)):
        if linha+1 < len(voz):
            
            #idealmente todos os compassos e bpms do segmento devem ser impressos
            #nao so os de inicio
            #talvez montar funcoes separadas com cada dessas
            #ou uma funcao com varios argumentos para ativar e desativar partes dessa
            if 'Note_on_c' in voz[linha]:
                comp = f_segmenta.comp_bpm(voz[linha],mapacomplocdur)
                bpm = f_segmenta.comp_bpm(voz[linha],mapabpm)
                reflocdur = f_segmenta.ref_locdur(voz[linha],mapacomplocdur)
                locC = f_segmenta.locC(voz[linha],ref=reflocdur)
                locT = f_segmenta.locT(voz[linha],ref=reflocdur)
                lcomp[p].append(comp)
                lbpm[p].append(bpm)
                llocC[p].append(locC)
                llocT[p].append(locT)

                non = []
                noff = []
                for busca in range(linha+1,len(voz)):
                    if noff == [] or non == []:
                        if 'Note_off_c'  in voz[busca]:
                            noff = voz[busca]
                        if 'Note_on_c' in voz[busca]:
                            non = voz[busca]
                    else:
                        linhadur = f_segmenta.durI(voz[linha],ref=reflocdur)
                        nondur = f_segmenta.durI(non)
                        noffdur = f_segmenta.durI(noff)
                        inte[p].append(non[4]-voz[linha][4])
                        dur[p].append(nondur-linhadur)
                        #dur[p].append([nondur-linhadur, nondur-noffdur])
                        break
    
        else:
            if len(llocC) != len(vozeslista):
                lcomp.append([])
                lbpm.append([])
                llocC.append([])
                llocT.append([])
                inte.append([])
                dur.append([])
                p = p + 1

final = []
for compvoz, bpmvoz, locCvoz, locTvoz, intevoz, durvoz in zip(lcomp, lbpm, llocC, llocT, inte, dur):
    for posicao1 in range(len(intevoz)):
        for posicao2 in range(posicao1, len(intevoz)):
            comppronto = []
            bpmpronto = []

            for valorcomp, valorbpm in zip(compvoz[posicao1:posicao2+1], bpmvoz[posicao1:posicao2+1]):
                if valorcomp not in comppronto:
                    comppronto.append(valorcomp)
                if valorbpm not in bpmpronto:
                    bpmpronto.append(valorbpm)
            final.append([nomemusica, tom, modo, comppronto, bpmpronto, locCvoz[posicao1], locTvoz[posicao1], (posicao2+1)-posicao1, sum(durvoz[posicao1:posicao2+1]), intevoz[posicao1:posicao2+1], durvoz[posicao1:posicao2+1]])
            #preiso acrescentar a duração do segmento em compassos alem de tempos
            #para isso preciso acrescentar no mapa complocdur a duracao em compassos
            #mudar as formulas f_ref para dar a duracao em compassos

debug = final