#prepara o arquivo csv para ter as listas de notas duracoes e localizações extraidas
#o resultado sera arquivo com algumas colunas a mais contendo informações simbolicas de músicas
#ainda estou mexendo nesse

import funcoes
import copy

entrada = funcoes.entrada_csv("localizacaocompassobpm3.csv")
entradalimpa = funcoes.limpeza(entrada)
ppq = funcoes.tira_ppq(entradalimpa)
complista = funcoes.comp_lista(entradalimpa)
tempolista = funcoes.tempo_lista(entradalimpa)

#faz uma lista copia da complista acrescendando localizacoes em cada compasso
if complista[0][1] == 0:
   compcomloc = []
   compcomloc.append([[1, 1.0], complista[0]])
   for posicao in range(len(complista)):
      if posicao+1 < len(complista):
         uc = funcoes.comp_uc(complista[posicao], ppq)
         nt = funcoes.comp_nt(complista[posicao])
         loc = (complista[posicao+1][1] - complista[posicao][1])/uc + compcomloc[posicao][0][0]
         locc = int(loc)
         loct = ((loc%1)*nt)+1
         junta = [locc, loct]
         junta = [junta, complista[posicao+1]]
         compcomloc.append(junta)
else:
   raise ValueError('compasso nao comeca no inicio')

entradacomloc = []
 for linha in entradalimpa:
   comp = funcoes.comp_ref(linha, compcomloc)
   uc = funcoes.comp_uc(comp[1], ppq)
   nt = funcoes.comp_nt(comp[1])
   loc = (linha[1] - comp[1][1])/uc + comp[0][0]
   locc = int(loc)
   loct = ((loc%1)*nt)+1
   junta = [locc, loct]
   junta = [junta, linha]
   entradacomloc.append(junta)