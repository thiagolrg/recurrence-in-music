#loop que monta listaintervalo a partir de listanota
def listaIntervalo(listaNota):{
    listaIntervalo = []
    for posicao in range(len(listaNota)):
	    if posicao <= len(listaNota)-2:
		    listaIntervalo.append(listaNota[posicao+1] - listaNota[posicao])

}
