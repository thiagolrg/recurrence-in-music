#prepara o arquivo csv para ter as listas de notas duracoes e localizações extraidas
#o resultado sera arquivo com algumas colunas a mais contendo informações simbolicas de músicas
#ainda estou mexendo nesse

import funcoes
import csv
entrada = funcoes.entrada_csv("localizacaocompassobpm3.csv")

entradalimpa = funcoes.limpeza(entrada)

ppq = int(entrada[0][-1])
combpm = funcoes.com_bpm(entrada)
timesig = funcoes.timesig_filtra(entrada)

for linha in entrada:
   compasso_referencia = funcoes.compasso_referencia(linha,timesig)
   Unidade_compasso = funcoes.timesig_uc(int(compasso_referencia[1]),int(compasso_referencia[2]),ppq)
   linha[1] - compasso_referencia[0]