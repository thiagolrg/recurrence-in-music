#loop que monta ListaIntervalo a partir de ListaNota
def listaIntervalo(listaNota):
    listaIntervalo = []
    for posicao in range(len(listaNota)):
	    if posicao <= len(listaNota)-2:
		    listaIntervalo.append(listaNota[posicao+1] - listaNota[posicao])


#segmenta e localiza ListaIntervalo e ListaDuracao
def SegLoc(ListaLocalizacao, ListaIntervalo, ListaDuracao):
    if len(ListaLocalizacao) == len(ListaIntervalo) == len(ListaDuracao):
        for posicao1 in range(len(ListaIntervalo)):
            for posicao2 in range(posicao1, len(ListaIntervalo)):
                print(ListaLocalizacao[posicao1], (posicao2+1) - posicao1, ListaIntervalo[posicao1:posicao2+1], ListaDuracao[posicao1:posicao2+1])
    else:
        print("listas de tamanhos diferentes")
        print("len(ListaLocalizacao) ==", len(ListaLocalizacao), "len(listaintervalo) ==", len(ListaIntervalo), "len(listaduracao) ==", len(ListaDuracao)) 
