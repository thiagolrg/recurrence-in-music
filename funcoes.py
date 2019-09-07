#monta lista_intervalo a partir de lista_nota
def lista_intervalo(lista_nota):
    lista_int = []
    for posicao in range(len(lista_nota)):
	    if posicao <= len(lista_nota)-2:
		    lista_int.append(lista_nota[posicao+1] - lista_nota [posicao])
    return lista_int

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

import csv
def timesig_filtra(camimnho_csv):
    ppq = int()
    timesignature = list()
    with open(camimnho_csv) as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            if ' Header' in row:
                ppq = row[-1:-1]
            if ' Time_signature' in row:
                timesignature.append(row[3:4], ppq)
    return timesignature

