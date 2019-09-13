#______________________________________________________
#limpa o arquivo de entrada e extrai as listas e constantes necessarias
import f_limpaextrai

entrada = f_limpaextrai.entrada_csv("localizacaocompassobpm3.csv")
entradalimpa = f_limpaextrai.limpeza(entrada)

complista = f_limpaextrai.comp_lista(entradalimpa)
templista = f_limpaextrai.temp_lista(entradalimpa)
templimp = f_limpaextrai.templimp(templista)

ppq = f_limpaextrai.tira_ppq(entradalimpa)
#nome
#tom
#modo

#______________________________________________________
#chega ate o mapa usado para calcular as caracteristicas de qualquer linha da entrada limpa
import f_mapa

#mapa da conversao da lista tempo em bpm
mapabpm = []
for linha in templimp:
    compref = f_mapa.temp_comp(linha,complista)
    bpm = f_mapa.bpmf(linha,compref)
    mapabpm.append([linha[1], bpm])

#mapa da conversao da lista compasso em formulas localizações e durações
if complista[0][1] == 0:
    mapacomplocdur = []
    mapacomplocdur.append([0, [1, 1.0],0.0])
    for posicao in range(len(complista)):
        comp = f_mapa.comp(complista[posicao])
        mapacomplocdur[posicao].insert(1,comp)
        if posicao+1 < len(complista):
            locR = f_mapa.locR(complista[posicao+1],complista[posicao],ppq)
            locT = f_mapa.locT(complista[posicao+1],complista[posicao],ppq)
            durR = f_mapa.durR(complista[posicao+1],complista[posicao],ppq)
            locC = int(locR + mapacomplocdur[posicao][2][0])
            durI = durR + mapacomplocdur[posicao][3]
            mapacomplocdur.append([complista[posicao+1][1], [locC, locT], durI])
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
else:
    raise ValueError('compasso nao comeca no 0')
mapa = [mapacomplocdur, mapabpm]

#______________________________________________________________________________
#a lista mapa é usada para calcular todas as carácteristicas de qualquer linha da entrada limpa
#formula de compasso, bpm, localização e duração de qualquer linha do arquivo
import f_ref

entradapronta = []
for linha in entradalimpa:
    comp = f_ref.comp(linha,mapa)
    bpm = f_ref.bpm(linha, mapa)
    loct = f_ref.locT(linha,mapa,ppq)
    locc = f_ref.locC(linha,mapa,ppq)
    duri = f_ref.durI(linha,mapa,ppq)
    entradapronta.append([comp,bpm,locc,loct,duri,linha])



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