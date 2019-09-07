#Do arquivo CSV vem as listas de nota duracao e localizacao


import csv

#faz uma lista contendo o arquivo de entrada completo
def entrada_csv(caminho_csv):
    entrada = []
    with open(camimnho_csv) as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            entrada.append(row)
    return entrada

#faz uma lista cópia do arquivo de entrada acrescentando as localizações em cada linha
def comloc_csv(entrada)
for posicaod in range(len(entrada)):
	for posicaot in range(len(timesignature)):
		if posicaot+1 == len(timesignature): #gambiarra
		        print(entrada[posicaod][1], timesignature[posicaot])
		elif int(timesignature[posicaot+1][0]) >= int(deltat[posicaod]):
			print(deltat[posicaod], timesignature[posicaot])
			break

#monta lista_intervalo a partir de lista_nota
def lista_intervalo(lista_nota):
    lista_int = []
    for posicao in range(len(lista_nota)):
	    if posicao <= len(lista_nota)-2:
		    lista_int.append(lista_nota[posicao+1] - lista_nota [posicao])
    return lista_int

#talvez tenha como juntar listaintervalo, listaduracao e listalocalizacao em um unico loop.
#na verdade o importante é que cada lista tenha o mesmo tamanho, desde que isso aconteça tanto faz qual lista eu puxo para medir o tamanho
#e posso colocar todas em um mesmo loop	
#o que o loop faz é:
#verifica se as 3 listas tem o mesmo tamanho antes do loop
#imprime a posição na listalocalozação
#imprime a diferença entre as posições dos subloop e do loop(equivalente a quantidade de notas)
#imprime os pedaços na listaintervalo e na listaduracao
#segmenta e localiza lista_intervalo e lista_duracao
def seg_loc(lista_localizacao, lista_intervalo, lista_duracao):
    if len(lista_localizacao) == len(lista_intervalo) == len(lista_duracao):
        for posicao1 in range(len(lista_intervalo)):
            for posicao2 in range(posicao1, len(lista_intervalo)):
                print(lista_localizacao[posicao1], (posicao2+1) - posicao1, lista_intervalo[posicao1:posicao2+1], lista_duracao[posicao1:posicao2+1])
    else:
        print("listas de tamanhos diferentes")
        print("len(lista_localizacao) ==", len(lista_localizacao), "len(lista_intervalo) ==", len(lista_intervalo), "len(lista_duracao) ==", len(lista_duracao)) 

#calcula unidade de compasso de um timesignature
def timesig_uc(num,den,ppq):
    if den == 0:
        UC = ppq*4*num
    elif den == 1:
	    UC = ppq*2*num
    elif den == 2:
        UC = ppq*num
    elif den == 3:
        UC = ppq/2*num
    elif den == 4:
        UC = ppq/4*num
    else:
        raise ValueError('Denominador nao encontrado')
    return UC


#calcula o numero de tempos de um timesignature
def timesig_nt(num,vuc):
    if num == 2 or 3 or 4:
        NT = num
    elif num == 6 or 9 or 12:
        NT = num/2
    else:
        raise ValueError('numerador nao encontrado')
    return NT

def timesig_filtra(camimnho_csv):
    timesignature = list()
    with open(camimnho_csv) as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            if ' Time_signature' in row:
                junta = row[1:2]+row[3:5]
                timesignature.append(junta)
                junta = []
    return timesignature

