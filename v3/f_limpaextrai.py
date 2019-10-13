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

#rece o caminho de um arquivo midi
#cria uma lista em csv a partir do midi correspondente ao caminho
#substitui o entrada_csv
def entrada_midi(nome):
    import subprocess
    entrada = []
    listacsv = subprocess.run(['Midicsv.exe', nome], text=True, capture_output=True, shell=True)
    # o midicsv.exe é executado externamente e não pode estar em outro diretório
    separalinha = listacsv.stdout.splitlines()
    for linha in separalinha: #separa por virgula
        entrada.append(linha.split(','))
    return entrada

#tira todos os espacos e transforma numeros em int na lista de entrada
def limpeza(lista):
    listalimpa = []
    for linha in lista:
        linhalimpa = []
        for valor in linha:
            valor = valor.strip()
            valor = valor.replace('\"','')
            if valor.lstrip('-').isdigit():
                valor = int(valor)
            linhalimpa.append(valor)
        listalimpa.append(linhalimpa)
    return listalimpa

#tira da lista o tom em letras: c = dó d = ré...
def tira_tom(row):
    if 'major' in row:
        if row[3] == 0:
            tom = 'C'
        elif row[3] == 1:
            tom = 'G'
        elif row[3] == -1:
            tom = 'F'
        elif row[3] == 2:
            tom = 'D'
        elif row[3] == -2:
            tom = 'Bb'
        elif row[3] == 3:
            tom = 'A'
        elif row[3] == -3:
            tom = 'Eb'
        elif row[3] == 4:
            tom = 'E'
        elif row[3] == -4:
            tom = 'Ab'
        elif row[3] == 5:
            tom = 'B'
        elif row[3] == -5:
            tom = 'Db'
        elif row[3] == 6:
            tom = 'F#'
        elif row[3] == -6:
            tom = 'Gb'
        elif row[3] == 7:
            tom = 'C#'
        elif row[3] == -7:
            tom = 'Cb'
    if 'minor' in row:
        if row[3] == 0:
            tom = 'a'
        elif row[3] == 1:
            tom = 'e'
        elif row[3] == -1:
            tom = 'd'
        elif row[3] == 2:
            tom = 'b'
        elif row[3] == -2:
            tom = 'g'
        elif row[3] == 3:
            tom = 'f#'
        elif row[3] == -3:
            tom = 'c'
        elif row[3] == 4:
            tom = 'c#'
        elif row[3] == -4:
            tom = 'f'
        elif row[3] == 5:
            tom = 'g#'
        elif row[3] == -5:
            tom = 'bb'
        elif row[3] == 6:
            tom = 'd#'
        elif row[3] == -6:
            tom = 'eb'
        elif row[3] == 7:
            tom = 'a#'
        elif row[3] == -7:
            tom = 'ab'
    return tom

def limpa_extrai(entradalimpa):
    voz = 0
    notas = [[]]
    compassos = []
    tempos = []
    tom = str()
    modo = str()
    ppq = int()
    for linha in entradalimpa:
        if 'Note_on_c' in linha:
            if notas == [[]]:
                notas[voz].append(linha)
            elif notas[voz][len(notas[voz])-1][1][0] == linha[0]:
                notas[voz].append(linha)
            else:
                notas.append([])
                voz = voz + 1
                notas[voz].append(linha)
        elif 'Note_off_c' in linha:
            if notas[voz][len(notas[voz])-1][4] == linha[4]:
                notas[voz][len(notas[voz])-1] = [notas[voz][len(notas[voz])-1], linha]
            else:
                raise ValueError('Note_on_c correspondente nao encontrado')
        elif 'Time_signature' in linha:
            compassos.append(linha)
        elif 'Tempo' in linha:
            if tempos == []:
                tempos.append(linha)
            elif tempos[len(tempos)-1][1] != linha[1]:
                tempos.append(linha)
            else:
                tempos[len(tempos)-1] = linha
        elif 'Key_signature' in linha:
            tom = tira_tom(linha)
            modo = linha[4]
        elif 'Header' in linha:
            ppq = int(linha[5])
    return(tom, modo, ppq, compassos, tempos, notas)

#faz uma lista contendo o arquivo csv de entrada completo
#substituido pela midi_csv
def entrada_csv(caminho_csv):
    import csv
    entrada = []
    with open(caminho_csv) as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            entrada.append(row)
    return entrada