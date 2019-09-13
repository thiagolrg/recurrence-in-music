#___________________________________________________
#entrada limpeza e extracao das listas e variaveis importante
#essas sao lista de compassos, lista de tempo e ppq

#faz uma lista contendo o arquivo de entrada completo
def entrada_csv(caminho_csv):
    import csv
    entrada = []
    with open(caminho_csv) as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            entrada.append(row)
    return entrada

#tira todos os espacos e transforma numeros em int na lista de entrada
def limpeza(lista):
    listalimpa = []
    for linha in lista:
        linhalimpa = []
        for valor in linha:
            valor = valor.strip()
            if valor.isdigit():
                valor = int(valor)
            linhalimpa.append(valor)
        listalimpa.append(linhalimpa)
    return listalimpa

#faz lista com os compassos filtrados da lista de entrada
def comp_lista(lista):
    complista = []
    for linha in lista:
         if 'Time_signature' in linha:
            complista.append(linha)
    return complista

#faz lista com os tempos filtrados da lista de entrada
def temp_lista(lista):
    tempolista = []
    for row in lista:
         if 'Tempo' in row:
            tempolista.append(row)
    return tempolista

#tira repeticoes da templimp
def templimp(templista):
    templimp = []
    for posicao in range(len(templista)):
        if posicao+1 == len(templista):
            if templista[posicao][1] == templista[posicao-1][1]:
                templimp.append(templista[posicao])
            break
        elif templista[posicao+1][1] == templista[posicao][1]:
            continue
        else:
            templimp.append(templista[posicao])
    return(templimp)

#def tira_nome fazer
#def tira_tom fazer
#def tira_modo fazer
#tira ppq da lista
def tira_ppq(lista):
    if 'Header' in lista[0]:
        ppq = int(lista[0][5])
        return ppq
    else:
        raise ValueError("Header nao identificado")