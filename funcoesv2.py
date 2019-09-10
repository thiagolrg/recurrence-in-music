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
    lista = lista
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

#tira ppq da lista
def tira_ppq(lista):
    ppq = int(lista[0][5])
    return ppq

 #faz lista com os compassos filtrados da lista de entrada
def comp_lista(lista):
    complista = []
    for row in lista:
         if 'Time_signature' in row:
            complista.append(row)
    return complista

#faz uma lista com os tempos filtrados da lista de entrada
def temp_lista(lista):
    tempolista = []
    for row in lista:
         if 'Tempo' in row:
            tempolista.append(row)
    return tempolista

#_______________________________________________
#Refs.
#sao funcoes parecidas usadas em momentos diferentes para
#encontrar um compasso ou tempo de ref. para calculo de
#localizacoes duracoes e BPM

#recebe a templista e retorna o compasso.ref
def temp_comp(linha,lista):
    comp = []
    for posicaot in range(len(lista)):
        if posicaot+1 == len(lista):
            comp = lista[posicaot]
        elif lista[posicaot+1][1] > linha[1]:
            comp = lista[posicaot]
            break
    return  comp

#recebe a entrada limpa e a lista de compcomloc, retorna o compasso.ref
def comp_ref(linha,lista):
    comp = []
    for posicaot in range(len(lista)):
        if posicaot+1 == len(lista):
            comp = lista[posicaot]
        elif lista[posicaot+1][2][1] >= linha[1]:
            comp = lista[posicaot]
            break
    return  comp

#recebe a entrada limpa e a lista de complista, retorna a formula de compasso ref.
def fcomp_ref(linha,lista):
    comp = []
    for posicaot in range(len(lista)):
        if posicaot+1 == len(lista):
            comp = [lista[posicaot][3], 2**lista[posicaot][4]]
        elif lista[posicaot+1][1] > linha[1]:
            comp = [lista[posicaot][3], 2**lista[posicaot][4]]
            break
    return  comp

#recebe a entrada limpa e a lista de tempos, retorna o tempo ref.
def temp_ref(linha,lista):
    temp = []
    for posicaot in range(len(lista)):
        if posicaot+1 == len(lista):
            temp = lista[posicaot]
        elif lista[posicaot+1][1][1] > linha[1]:
            temp = lista[posicaot]
            break
    return  temp

#______________________________________________
#Auxiliares no calculo de localizacao duracao e bpm

# unidade de compasso = ((ppq*4)/(2**den))*num
def uc(complinha,ppq):
    uc = ((ppq*4)/(2**complinha[4]))*complinha[3]
    return uc

# numero de tempo sempre vai ser o numerador
def nt(complinha):
    nt = complinha[3]
    return nt

# BPM = (60000000/usec)/(MClock/24)
# BPM = bpm_1/metron
def bpm_1(tempolinha):
    bpm1 = 60000000/tempolinha[3]
    return bpm1

def metron(complinha):
    metron = complinha[5]/24
    return metron