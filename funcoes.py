#loop que monta lista_intervalo a partir de lista_nota
def lista_intervalo(lista_nota):
    lista_intervalo = []
    for posicao in range(len(lista_nota)):
	    if posicao <= len(lista_nota)-2:
		    lista_intervalo.append(lista_nota[posicao+1] - lista_nota[posicao])

#segmenta e localiza lista_intervalo e lista_duracao
def SegLoc(lista_localizacao, lista_intervalo, lista_duracao):
    if len(lista_localizacao) == len(lista_intervalo) == len(lista_duracao):
        for posicao1 in range(len(lista_intervalo)):
            for posicao2 in range(posicao1, len(lista_intervalo)):
                print(lista_localizacao[posicao1], (posicao2+1) - posicao1, lista_intervalo[posicao1:posicao2+1], lista_duracao[posicao1:posicao2+1])
    else:
        print("listas de tamanhos diferentes")
        print("len(lista_localizacao) ==", len(lista_localizacao), "len(lista_intervalo) ==", len(lista_intervalo), "len(lista_duracao) ==", len(lista_duracao)) 
