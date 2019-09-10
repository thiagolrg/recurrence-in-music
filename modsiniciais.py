#prepara o arquivo csv para ter as listas de notas duracoes e localizações extraidas
#o resultado sera arquivo com algumas colunas a mais contendo informações simbolicas de músicas
#esta e a primeira versao final

import funcoes
import copy

entrada = funcoes.entrada_csv("localizacaocompassobpm3.csv")
entradalimpa = funcoes.limpeza(entrada)
ppq = funcoes.tira_ppq(entradalimpa)
complista = funcoes.comp_lista(entradalimpa)
tempolista = funcoes.tempo_lista(entradalimpa)

#faz uma lista copia da tempolista acrescentando BPM
tempocombpm = []
for linha in tempolista:
   bpm = int(60000000/linha[3])
   junta = [[bpm], linha]
   tempocombpm.append(junta)

#faz uma lista copia da complista acrescendando localizacoes em cada compasso
if complista[0][1] == 0:
   compcomloc = []
   compcomloc.append([[1, 1.0], complista[0]])
   for posicao in range(len(complista)):
      if posicao+1 < len(complista):
         uc = funcoes.comp_uc(complista[posicao], ppq)
         nt = complista[posicao][3] #o numerador direto como o valor e mais tolerante a compassos diferentes, melhor do que tentar prever qual o tamanho do tempo
         loc = (complista[posicao+1][1] - complista[posicao][1])/uc + compcomloc[posicao][0][0]
         locc = int(loc)
         loct = ((loc%1)*nt)+1
         junta = [[locc, loct], complista[posicao+1]]
         compcomloc.append(junta)
else:
   raise ValueError('compasso nao comeca no inicio')

#faz uma lista copia da entrada acrescentando compasso bpm e localizacao em todas as linhas
entradacomloc = []
for linha in entradalimpa:
   comp = funcoes.comp_ref(linha, compcomloc)
   bpm = funcoes.comp_ref(linha, tempocombpm)
   uc = funcoes.comp_uc(comp[1], ppq)
   nt = funcoes.comp_nt(comp[1])
   loc = (linha[1] - comp[1][1])/uc + comp[0][0]
   locc = int(loc)
   loct = round(((loc%1)*nt)+1, 2)
   junta = [comp[1][3:5], bpm[0], [locc, loct], linha]
   entradacomloc.append(junta)


   #esse arquivo desse jeito está em sua primeira versão final.
   #faz uma lista
   #[[formula de compasso], [bpm], [locc], [loct], [mensagem]]

   #tenho que refletir se converto os denominadores dos compassos para os que se usa em musicas
      #para fazer isso teria que fazer um outro loop aqui e uma outra funcao no arquivo funcoes
   #tenho que refletir se converto os BPM para outros valores além da semínima
      #para fazer isso teria que rodar a funcao _ref na tempolista, fazer o BPM para cada mensagem e converter usando o 24 ou 36 da formula
      #acho que vale a pena tentar isso amanha antes de seguir adiante

   #tambem verificar se e possivel calcular as duracoes
   # ou se e necessario recalcular a partir dos deltaT