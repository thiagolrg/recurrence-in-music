listalocalizacao = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4]]
listanota = [13, 15, 18, 10, 8, 20, 14]
listaintervalo = list()

# Gera a listaintervalo a partir da listanota

for posicao in range(len(listanota)):
	if posicao <= len(listanota)-2:
		listaintervalo.append(listanota[posicao+1] - listanota[posicao])

# monta todos os segmentos a partir da lista intervalo, imprime a posição corresponde na listalocalização e tamanho

for posicao1 in range(len(listaintervalo)):
	for posicao2 in range(posicao1, len(listaintervalo)):
		print(listalocalizacao[posicao1], (posicao2+1) - posicao1, listaintervalo[posicao1:posicao2+1])
