#chama um subprocesso para converer o midi em CSV
def midi_csv(nome):
    import subprocess
    return subprocess.run(['Midicsv.exe', nome], text=True, capture_output=True, shell=True).stdout.splitlines()
    # o midicsv.exe é executado externamente e não pode estar em outro diretório

#tira todos os espacos e transforma numeros em int na lista de entrada
def limpa(lista):
    listalimpa = []
    for linha in lista:
        linhalimpa = []
        for valor in linha.split(','):
            valor = (valor.strip()).replace('\"','')
            if valor.lstrip('-').isdigit():
                valor = int(valor)
            linhalimpa.append(valor)
        listalimpa.append(linhalimpa)
    return listalimpa

#em um unico loop pelo arquivo de entrada, monta essas listas e extrais as constantes
def extrai(entradalimpa):
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
            if linha[4] == notas[voz][len(notas[voz])-1][4]:
                notas[voz][len(notas[voz])-1] = [notas[voz][len(notas[voz])-1], linha]
            else:
                raise ValueError('Note_off_c correspondente nao encontrado')
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