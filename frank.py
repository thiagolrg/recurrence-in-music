#Do arquivo CSV vem as listas de nota duracao e localizacao
listanota = [1,2,4,7,11,16]
listalocalizacao = [[1,1],[2,1],[3,1],[4,1],[5,1]]
listaduracao = [1,2,3,4,5]

#loop que monta listaintervalo a partir de listanota
listaintervalo = []
for posicao in range(len(listanota)):
	if posicao <= len(listanota)-2:
		listaintervalo.append(listanota[posicao+1] - listanota[posicao])

#loop que imprime localizacao tamanho e segmentos de intervalo
		
##for posicao1 in range(len(listaintervalo)):
##	for posicao2 in range(posicao1, len(listaintervalo)):
##		print(listalocalizacao[posicao1], (posicao2+1) - posicao1, listaintervalo[posicao1:posicao2+1])

#talvez tenha como juntar listaintervalo, listaduracao e listalocalizacao em um unico loop.
#na verdade o importante é que cada lista tenha o mesmo tamanho, desde que isso aconteça tanto faz qual lista eu puxo para medir o tamanho
#e posso colocar todas em um mesmo loop
		
#o que o loop faz é:
#verifica se as 3 listas tem o mesmo tamanho antes do loop
#imprime a posição na listalocalozação
#imprime a diferença entre as posições dos subloop e do loop(equivalente a quantidade de notas)
#imprime os pedaços na listaintervalo e na listaduracao
		
if len(listalocalizacao) == len(listaintervalo) == len(listaduracao):
        for posicao1 in range(len(listaintervalo)):
                for posicao2 in range(posicao1, len(listaintervalo)):
                        print(listalocalizacao[posicao1], (posicao2+1) - posicao1, listaintervalo[posicao1:posicao2+1], listaduracao[posicao1:posicao2+1])
else:
        print("listas de tamanhos diferentes")
        print("len(listalocalizacao) ==", len(listalocalizacao), "len(listaintervalo) ==", len(listaintervalo), "len(listaduracao) ==", len(listaduracao)) 

#a tabela final tem que ter:
#nome da musica (nome do arquivo)
#modo da musica
#formula de compasso
#bpm
#posicao de inicio (compasso e tempo)
#duracao total (em tempos de compasso)
#quantidade de notas
#segmento de intervalo
#segmento de duracao

#desses os que a lógica acima resovle são:
#posicao de inicio (compasso e tempo)
#quantidade de notas
#segmento de intervalo
#segmento de duracao

#preciso trabalhar um pouco agora na matemática para converter os milissegundos do CSV em compassos e tempos de compasso
#para fazer isso e necessario converter e usar o valor da formula de compasso no header do midi e fazer tudo com base nele
#alem disso no arquivo de teste de stress ele tem que ser capaz de identificar que a formula de compasso mudou e fazer as contas na nova formula.

#o valor na mensagem tempo e sempre a duracao de uma seminina em microsegundos
#para calcular o BPM e preciso levar em conta a formula de conpasso
#se o BPM for marcado em seminima pontuada ou minina ou colcheia, qualquer outra duracao que nao seminima
#o valor tempo tem que passar por alguma formula tipo, *0,5 * 1,5 * 2 depois /1000000*60
        
# o valor tempo tem que ser /2(valor da seminima) *pelodenominador, depois /1000000 para conversão em segundos e *60 para minutos
# isso resolve para as formulas comuns 2/2 3/2 4/2 2/4 3/4 4/4 3/8 6/8 9/8 12/8, 3/8 seria um 1/4 com tercina
# essas decisão de interpretar compassos também envolve andamentos o que significa que envolve análise perceptiva
# quando um 4/4 deve ser marcado como um binário? quando um 3/8 deve ser marcado como unário?
# de qualquer forma essa formula seria um padrão eficiente
# marca semínima pontuada quando o denominador e colcheia
# marca seminima quando o denominador e seminima
# marca minima quando o denominador e minima
# sera um problema para compassos irregulares

tempo = 666666
denominador = 3
bpm = round((((tempo/2)*denominador)/1000000)*60)
print(bpm)

#a dificuldade e que o denominador de referencia muda a depender do deltaT
#a dificuldade e que o DeltaT sempre deve ser expresso em compassos e fracoes de compasso
# quando a formula de compasso muda as conversoes devem mudar de acordo

# Parece ser uma boa ideia fazer uma lista convertento TODOS os DeltaT para compasso/tempo
# nao sei bem se e possivel fazer as duracoes dos segmentos e a duração total com isso mas vou tentar mesmo assim

# a ideia e comparar uma lista de deltaT extraídos do CSV com uma uma de time_signatures extraidos do CSV
# a lista deltat  deve usar o denominador do primeiro time signature de deltat >= valor da lista deltat

#extrai todos os deltat para a lista deltat
#extrai todos os Time_signature com seus deltat para a lista timesignature
timesignature = list()
deltat = list()

import csv
with open(r'localizacaocompassobpm3.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        deltat.append(row[1])
        if ' Time_signature' in row:
                timesignature.append(row)

print(timesignature)
print(deltat)

# para calcular a posicao em compassos de um deltat
# (((deltat atual - deltat da time signature anterior)/U.C. da anterior)+ valor em compassos da anterior)
# para a posição em tempo com partes de tempo em sao os decimais de compasso * numero de tempos

#Identifica as timesignatures referencias para cada deltat
for posicaod in range(len(deltat)):
	for posicaot in range(len(timesignature)):
		if posicaot+1 == len(timesignature): #gambiarra
		       print(deltat[posicaod], timesignature[posicaot])
		elif int(timesignature[posicaot+1][0]) >= int(deltat[posicaod]):
			print(deltat[posicaod], timesignature[posicaot])
			break
		
#passei um tempao tentando resolver a logica desse loop e ainda parece ruim,
#o problema e que a conta e feita com na posicao seguinte de timesignature
#nao sei tambem se essa abordagem de transformar tudo em listas para fazer as contas a partir delas e a melhor de qualquer forma...



