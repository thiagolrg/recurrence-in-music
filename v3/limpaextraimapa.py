import f_limpaextrai as f_l
import f2_mapa as f2_m
import f2_segmenta as f2_s
import timeit

finaldic = {}
finalcsv = []

diretorio = input('diretorio com arquivos midi de entrada: ')
nomecsv = input('nome do arquivo csv de saida: ')
diretoriosaida = diretorio + '\\' + nomecsv +'.csv'
listacaminhos = f_l.caminhos_midi(diretorio)

for caminho in listacaminhos:
    entrada = f_l.midi_csv(caminho)
    entradalimpa = f_l.limpeza(entrada)
    nomemusica = f_l.tira_nome(caminho)

    voz = 0
    notas = [[]]
    compassos = []
    tempos = []
    tom = str()
    modo = str()
    ppq = int()

    for linha in entradalimpa:
        if 'Note_on_c' in linha:
            if notas == [[]]:
                notas[voz].append(linha)
            elif notas[voz][len(notas[voz])-1][1][0] == linha[0]:
                notas[voz].append(linha)
            else:
                notas.append([])
                voz = voz + 1
                notas[voz].append(linha)
        elif 'Note_off_c' in linha:
            if notas[voz][len(notas[voz])-1][4] == linha[4]:
                notas[voz][len(notas[voz])-1] = [notas[voz][len(notas[voz])-1], linha]
            else:
                raise ValueError('Note_on_c correspondente nao encontrado')
        elif 'Time_signature' in linha:
            compassos.append(linha)
        elif 'Tempo' in linha:
            if tempos == []:
                tempos.append(linha)
            elif tempos[len(tempos)-1][1] != linha[1]:
                tempos.append(linha)
            else:
                tempos[len(tempos)-1] = linha
        elif 'Key_signature' in linha:
            tom = f_l.tira_tom(linha)
            modo = linha[4]
        elif 'Header' in linha:
            ppq = int(linha[5])

    mapabpm = f2_m.mapa_bpm(tempos,compassos)
    mapacomploc = f2_m.mapa_locdur(compassos,ppq)
    finalcsv, finaldic = f2_s.musica_final(nomemusica, tom, modo, notas, mapacomploc, mapabpm, ppq, finalcsv, finaldic)
    print(nomemusica, listacaminhos.index(caminho)+1, "de", len(listacaminhos), ((listacaminhos.index(caminho)+1)/(len(listacaminhos)))*100)

debug = finaldic

'''
with open(diretoriosaida, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(final)'''