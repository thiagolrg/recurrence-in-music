import f_limpaextrai as f_l 
import f2_mapa as f2_m
import f2_segmenta as f2_s

diretorio = input('diretorio com arquivos midi de entrada: ')
nomecsv = input('nome do arquivo csv de saida: ')
diretoriosaida = diretorio + '\\' + nomecsv +'.csv'
listacaminhos = f_l.caminhos_midi(diretorio)

for caminho in listacaminhos:
    entrada = f_l.entrada_midi(caminho)
    entradalimpa = f_l.limpeza(entrada)
    nomemusica = f_l.tira_nome(caminho)
    
    mapabpm = f2_m.mapa_bpm(tempos,compassos)
    mapacomploc = f2_m.mapa_locdur(compassos,ppq)
    #as formulas do mappcomploc e do mapaseg são muito similares,
    #talvez tenha um jeito de fazer formulas unicas ou reduzir a quantidade de formulas
    mapaseg = f2_s.mapa_seg(notas, mapacomploc, mapabpm, ppq)

    for locCvoz, locTvoz, intevoz, durvoz, compvoz, tempvoz in mapaseg:
         debug = locCvoz
