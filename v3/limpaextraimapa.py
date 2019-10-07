import f_limpaextrai as f_l
import f2_mapa as f2_m
import f2_segmenta as f2_s

final = []

diretorio = input('diretorio com arquivos midi de entrada: ')
nomecsv = input('nome do arquivo csv de saida: ')
diretoriosaida = diretorio + '\\' + nomecsv +'.csv'
listacaminhos = f_l.caminhos_midi(diretorio)

for caminho in listacaminhos:
    entrada = f_l.midi_csv(caminho)
    entradalimpa = f_l.limpeza(entrada)

    nomemusica = f_l.tira_nome(caminho)
    tom = f_l.tira_tom(entradalimpa)
    modo = f_l.tira_modo(entradalimpa)
    ppq = f_l.tira_ppq(entradalimpa)

    complista = f_l.comp_lista(entradalimpa)
    templista = f_l.temp_lista(entradalimpa)
    templimp = f_l.templimp(templista)
    notaslista = f_l.notas_lista(entradalimpa)
    vozeslista = f_l.vozes_lista(notaslista)

    mapabpm = f2_m.mapa_bpm(templimp,complista)
    mapalocdur= f2_m.mapa_locdur(complista,ppq)
    mapacomplocdur = f2_m.mapa_complocdur(mapalocdur, complista)

    final = f2_s.tabela_final(nomemusica,tom, modo, vozeslista, mapacomplocdur, mapabpm, ppq, final)

debug = final

import csv
with open(diretoriosaida, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(final)