#todas as funcoes desse arquivos estão relacionadas com o arquivo modsiniciais
#tirei algumas funcoes que vão usar o resultado do modsiniciais como entrada e coloquei no frank
#ainda nao debuguei e nao fiz o unitTest dessas funções

#faz uma lista contendo o arquivo de entrada completo
def entrada_csv(caminho_csv):
    entrada = []
    with open(caminho_csv) as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            entrada.append(row)
    return entrada

#tira todos os espacos e transforma numeros em int na lista de entrada
def limpeza_entrada(list):
    listalimpa = []
    linhalimpa = []
    for linha in lista:
        for valor in linha:
            valor = valor.strip()
            if valor.isdigit():
                valor = int(valor)
            linhalimpa.append(valor)
        listalimpa.append(linhalimpa)
    return listalimpa

#tira ppq da lista
def tira_ppq(lista)
    ppq = lista[0][-1:]
    return ppq

#faz lista com os compassos filtrados da lista de entrada
def comp_lista(list):
    complista = list()
    for row in lista:
         if ' Time_signature' in row:
            junta = row[1:2]+row[3:5]
            complista.append(junta)
    return complista

#recebe uma linha e a lista de compassos filtrados
#devolve o compasso referencia para a linha
def comp_ref(linha,listacomp):
    comp = []
    for posicaot in range(len(timesig)):
        if posicaot+1 == len(timesig):
            comp = timesig[posicaot]
        elif int(timesig[posicaot+1][0]) >= int(linha[1]):
            comp = timesig[posicaot]
            break
    return comp

#calcula unidade de compasso em ppq
def comp_uc(num,den,ppq):
    if den == 0:
        uc = ppq*4*num
    elif den == 1:
	    uc = ppq*2*num
    elif den == 2:
        uc = ppq*num
    elif den == 3:
        uc = ppq/2*num
    elif den == 4:
        UC = ppq/4*num
    else:
        raise ValueError('Denominador nao encontrado')
    return UC

#calcula o numero de tempos de um compasso
def comp_nt(num,vuc):
    if num == 2 or 3 or 4:
        nt = num
    elif num == 6 or 9 or 12:
        nt = num/2
    else:
        raise ValueError('numerador nao encontrado')
    return nt

#faz uma lista cópia da lista de entrada acrescentando colunas localizações(compasso e tempo de compasso) em cada linha
    def com_loc(list):
        """aqui vao ser usadas as funções comp_"""

#faz uma lista cópia da lista de entrada acrescentando coluna BPM nas mensagens tempo
def com_bpm(list):
    bpm = int()
    combpm = []
    for linha in lista[:]:
        if ' Tempo' in linha:
            temp = linha
            bpm = int(60000000/int(linha[3]))
            temp.insert(4,bpm)
            combpm.append(temp)
        else:
            combpm.append(linha)
    return combpm