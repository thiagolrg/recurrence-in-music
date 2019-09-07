#loop que monta ListaIntervalo a partir de ListaNota
def lista_intervalo(listaNota):
    lista_int = []
    for posicao in range(len(listaNota)):
	    if posicao <= len(listaNota)-2:
		    lista_int.append(listaNota[posicao+1] - listaNota[posicao])
    return lista_int

#segmenta e localiza ListaIntervalo e ListaDuracao
def SegLoc(ListaLocalizacao, ListaIntervalo, ListaDuracao):
    if len(ListaLocalizacao) == len(ListaIntervalo) == len(ListaDuracao):
        for posicao1 in range(len(ListaIntervalo)):
            for posicao2 in range(posicao1, len(ListaIntervalo)):
                print(ListaLocalizacao[posicao1], (posicao2+1) - posicao1, ListaIntervalo[posicao1:posicao2+1], ListaDuracao[posicao1:posicao2+1])
    else:
        print("listas de tamanhos diferentes")
        print("len(ListaLocalizacao) ==", len(ListaLocalizacao), "len(listaintervalo) ==", len(ListaIntervalo), "len(listaduracao) ==", len(ListaDuracao)) 


def compasso_uc(num,den,ppq):
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



def compasso_nt(num,vuc):
    if num == 2 or 3 or 4:
        NT = UC/num
    elif num == 6 or 9 or 12:
        NT = UC/num/2
    else:
        raise ValueError('numerador nao encontrado')
    return NT

import csv
def filtra_timesig(camimnho_csv):
    timesignature = list()
    with open(camimnho_csv) as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            if ' Time_signature' in row:
                timesignature.append(row)
    return timesignature

