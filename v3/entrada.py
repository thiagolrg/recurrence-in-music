#______________________________________________________
#limpa o arquivo de entrada e extrai as listas e constantes necessarias
import f_limpaextrai

caminhosmidi = f_limpaextrai.caminhos_midi('C:\\Users\\Thiago.DESKTOP-13409IC\\Desktop\\Midicsv\\MIDIs')

for caminhomidi in caminhosmidi:
    entrada = f_limpaextrai.midi_csv(caminhomidi)
    entradalimpa = f_limpaextrai.limpeza(entrada)
    nomemusica = f_limpaextrai.tira_nome(caminhomidi)

complista = f_limpaextrai.comp_lista(entradalimpa)
templista = f_limpaextrai.temp_lista(entradalimpa)
templimp = f_limpaextrai.templimp(templista)
notaslista = f_limpaextrai.notas_lista(entradalimpa)
vozeslista = f_limpaextrai.vozes_lista(notaslista)

ppq = f_limpaextrai.tira_ppq(entradalimpa)

#tom
#primeira mensagem no midi

#modo
#primeira mensagem no midi

#______________________________________________________
#chega ate o mapa usado para calcular as caracteristicas de qualquer linha da entrada limpa
import f_mapa

#conversao da lista tempo em mapa de bpm
mapabpm = []
for linha in templimp:
    compref = f_mapa.temp_comp(linha,complista)
    bpm = f_mapa.bpmf(linha,compref)
    mapabpm.append([linha[1], bpm])
 
#conversao da lista compasso em mapa de formulas localizações e durações
if complista[0][1] == 0:
    mapacomplocdur = []
    mapacomplocdur.append([0, 1, 0.0])
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
 
mapa = [mapacomplocdur, mapabpm]

 #estou pensando seriamente se tiro o locT dai e sempre assumo ele como 1.0
            #afinal mudancas de compasso estao obrigatoriamente no inicio do compasso
            
            #fiz diferente
            #estou apostando que locT nao precisa de somar posicao anteror para dar certo porque locT vem de um mod1
            #e as posicoes anteriores nunca eram fracoes
            #locR = localizacao relativa a formula de compasso ref.
            #locT = posicao dentro do compasso em tempos de compasso
            #locC = localizacao absolusta em compassos
            #durR = duracao em tempos relativa a formula de compasso ref.
            #durI = duracao em tempos desde o inicio em tempos de compasso
#a lista mapa é usada por f_ref calcular as carácteristicas de qualquer linha da entrada limpa usando
#formula de compasso, bpm, localização e duração de qualquer linha do arquivo

#entrada
#entradalimpa
#complista
#templimp

#ppq
#nome
#tom
#modo

#complista para loc dur e comp
#templimp para bpm [deltat, nota, vel]

#linha da entrada limpa com locs e bpms