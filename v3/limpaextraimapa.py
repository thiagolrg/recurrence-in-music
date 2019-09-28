#______________________________________________________
#limpa o arquivo de entrada e extrai as listas e constantes necessarias
import f_limpaextrai as f_l
import f2_mapa as f2_m
import f2_segmenta

final = []

userinput = input('diretorio com arquivos midi de entrada: ')
diretorio = f_l.caminhos_midi(userinput)

for caminhos in diretorio:
    entrada = f_l.midi_csv(diretorio[0])
    entradalimpa = f_l.limpeza(entrada)

    nomemusica = f_l.tira_nome(diretorio[0])
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

    final = f2_segmenta.tabela_final(vozeslista,mapacomplocdur, mapabpm, ppq, final)
    for linha in final:
        linha.insert(0,modo)
        linha.insert(0,tom)
        linha.insert(0,nomemusica)

debug = final

