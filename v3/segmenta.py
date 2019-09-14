#preciso acessar, nome, tom, modo, ppq,entradalimpa e mapa de qualquer arquivo
#preciso que o proprio python crie novas variaveis sob demanda para acomodar as diferentes melodias
#para cada melodia tem que existir uma lista de intervalos e duracoes, com deltat para cada posicao
#o deltat sera usado para as refs depois da segmentacao
#aceitar melodias com pausas!
import entrada, f_ref

saidateste = []
for linha in entrada.entrada:
    comp = f_ref.comp(linha)
    bpm =  f_ref.bpm(linha)
    locC = f_ref.locC(linha)
    locT = f_ref.locT(linha)
    durI = f_ref.durI(linha)
    saidateste.append([comp,bpm,locC,locT,durI,linha])

import csv
with open('saidateste3.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(saidateste)
