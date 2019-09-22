#preciso acessar, nome, tom, modo, ppq,entradalimpa e mapa de qualquer arquivo
#preciso que o proprio python crie novas variaveis sob demanda para acomodar as diferentes melodias
#para cada melodia tem que existir uma lista de intervalos e duracoes, com deltat para cada posicao
#o deltat sera usado para as refs depois da segmentacao
#aceitar melodias com pausas!
import entrada, f_ref

#__________________________________________
#tira todas as mensagens note on e note off da entrada
melo = []
for linha in entrada.entrada:
    if 'Note_on_c' in linha or 'Note_off_c' in linha:
        melo.append(linha)

# coloca as caracteristicas em cada mensagem
melodi = []
for linha in melo:
    comp = f_ref.comp(linha)
    bpm =  f_ref.bpm(linha)
    locC = f_ref.locC(linha)
    locT = f_ref.locT(linha)
    durI = f_ref.durI(linha)
    melodi.append([comp,bpm,locC,locT,durI,linha])

#separa cada melodia em uma posicao na lista
melodias = [[]]
p = 0
for posicao in range(len(melodi)):
    melodias[p].append(melodi[posicao])
    if posicao+1 < len(melodi):
        if melodi[posicao+1][0] != melodi[posicao][0]:
            melodias.append([])
            p = p + 1

# monta a lista loc inte, dur e segmenta cada melodia
final = []
loc = []
inte = []
dur = []
for posicao1 in range(len(melodias)):
    for posicao2 in range(len(melodias[posicao1])):
        if 'Note_on_c' in melodias[posicao1][posicao2][5]:
            noff = []
            non = []
            for posicao3 in range(posicao2+1, len(melodias[posicao1])):
                if noff == [] or non == []:
                    if 'Note_off_c'  in melodias[posicao1][posicao3][5]:
                        noff = melodias[posicao1][posicao3]
                    if 'Note_on_c' in melodias[posicao1][posicao3][5]:
                        non = melodias[posicao1][posicao3]
                else:
                    loc.append(melodias[posicao1][posicao2][0:5])
                    inte.append(non[5][4] - melodias[posicao1][posicao2][5][4])
                    dur.append(non[4] - melodias[posicao1][posicao2][4])
                    #dur.append([non[4] - melodia[posicao1][posicao2][4], non[4] - noff[4]])
                    break
    if len(loc) == len(inte) == len(dur):
        for posicao2 in range(len(loc)):
            for posicao3 in range(posicao2, len(loc)):
                final.append(loc[posicao2][0:2] + [posicao1] + loc[posicao2][2:4]  + [sum(dur[posicao2:posicao3+1])] + [(posicao3+1) - posicao2] + [inte[posicao2:posicao3+1]] + [dur[posicao2:posicao3+1]])
    else:
        print("listas de tamanhos diferentes")
        print("len(loc) ==", len(loc), "len(inte) ==", len(inte), "len(dur) ==", len(dur))
    loc = []
    inte = []
    dur = []

import csv
with open('saidev2.2.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(final)

#melodia = []
#for linha in saidateste:
#    if linha[5][0] == 2 and ('Note_on_c' in linha[5] or 'Note_off_c' in linha[5]):
#        melodia.append(linha[0:5] + [linha[5][2]] + [linha[5][4]])

#for posicao1 in range(len(melodiap)):
#    for posicao2 in range(posicao1, len(melodiap)):
#        durseg.append(melodiap[posicao1][6]:posicao2+1][6])
#        inteseg.append(inte[posicao1][5]:posicao2+1][5])
#else:
#        print("listas de tamanhos diferentes")
#        print("len(listalocalizacao) ==", len(listalocalizacao), "len(listaintervalo) ==", len(listaintervalo), "len(listaduracao) ==", len(listaduracao)) 