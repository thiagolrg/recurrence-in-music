#___________________________________________________
#funcoes para transformar o arquivo de entrada em uma lista
#tirar espacos dessas listas e reconhecer os dígitos como int

#extrair da lista de entra as constantes e listas:
#nome da música
#tom
#modo
#resolusao (ppq)

#compassos
#tempos
#vozes

#retorna uma lista com o caminho de todos os arquivos midi de um diretório
def caminhos_midi(diretorio):
    import os
    path = diretorio
    caminhos = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.mid' in file:
                caminhos.append(os.path.join(r, file))
    return caminhos

#rece o caminho de um arquivo midi
#cria uma lista em csv a partir do midi correspondente ao caminho
#substitui o entrada_csv
def midi_csv(nome):
    import subprocess
    entrada = []
    listacsv = subprocess.run(['Midicsv.exe', nome], text=True, capture_output=True, shell=True)
    # o midicsv.exe é executado externamente e não pode estar em outro diretório
    separalinha = listacsv.stdout.splitlines()
    for linha in separalinha: #separa por virgula
        entrada.append(linha.split(','))
    return entrada

#faz uma lista contendo o arquivo de entrada completo
#substituido pela midi_csv
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

#recebe o caminho midi e tira o nome do arquivo
#o usuário tem que colocar o nome do arquivo como nome da música 
def tira_nome(caminhomidi):
    for linha in caminhomidi.split('\\'):
        if '.mid' in linha:
            nome = linha.replace('.mid','')
            break
    return nome

#def tira_tom fazer
#primeira mensagem no midi

#def tira_modo fazer
#primeira mensagem no midi

#tira ppq da lista
def tira_ppq(lista):
    if 'Header' in lista[0]:
        ppq = int(lista[0][5])
        return ppq
    else:
        raise ValueError("Header nao identificado")

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

#faz lista com as notas filtradas da lista de entrada
def notas_lista(lista):
    notaslista = []
    for linha in lista:
        if 'Note_on_c' in linha or 'Note_off_c' in linha:
            notaslista.append(linha)
    return notaslista

#separa a lista notas por vozes(cada voz deve estar em uma track diferente do MIDI)
def vozes_lista(lista):
    voz = 0
    vozes = [[]]
    lista = lista
    for posicao in range(len(lista)):
        vozes[voz].append(lista[posicao])
        if posicao+1 < len(lista):
            if lista[posicao+1][0] != lista[posicao][0]:
                vozes.append([])
                voz = voz + 1
    return vozes