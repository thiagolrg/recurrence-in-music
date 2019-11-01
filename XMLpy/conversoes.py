#encontra o compasso, tonalidade ou andamento da nota
#a partir da nota e da lista de compassos,andamentos ou tonalidades
def referencia(nota,listaref):
    for p in range(len(listaref)):
        if p+1 == len(listaref):
            return listaref[p]
        if listaref[p+1][0][0] > nota[0][0]:
            return listaref[p]

#posicao de inicio dentro do compasso
#counter da nota
def posicao_fracaodetempo(divisions,time,nota):
    return duracao_R(divisions,time,nota[0][0])%1

def posicao_tempodecompasso(divisions,time,nota):
    uc = uc_(divisions,time)
    duracaoR = duracao_R(divisions,time,nota[0][0])
    while duracaoR//uc > 0:
        duracaoR = duracaoR - uc
    return int(duracaoR)

#duracao em temos desde o inicio
#counter da nota
def duracao_desdeinicio(divisions,time,nota):
    return duracao_R(divisions,time,nota[0][0])+time[0][2]

#graus de escala a partir do tom, modo e nota
def grau_escala(key,note):
    step = note[0]
    if step == None:
        return None
    stepBase = step_base(key[0])
    degrees = ['I','II','III','IV','V','VI','VII']
    for p in range(len(stepBase)):
        if stepBase[p] == step:
            return degrees[p]

#intervalo diatonico a partir do nome e oitava de duas notas
def int_diatonico(noteOld,note):
    nOldstep = noteOld[0]
    nOldocta = noteOld[1]
    nstep = note[0]
    nocta = note[1]
    if nOldstep == None or nstep == None:
        return None
    octa = nocta - nOldocta
    stepBase = step_base(nOldstep)
    octaBase = octa_base(nOldstep)
    int_base = [1,2,3,4,5,6,7]
    for p in range(len(stepBase)):
        if stepBase[p] == nstep:
            intDiatonic = int_base[p]
            if octa >= octaBase[p]:
                return intDiatonic+((octa - octaBase[p])*7)
            else:
                return (intDiatonic-9)+(((octa - octaBase[p]) + 1)*7)

#intevalos cromaticos a partir de duas notas(converte para midi antes)
def int_cromatico(note1,note2):
    if note1[0] == None or note2[0] == None:
        return None
    return note_to_midi(note2) - note_to_midi(note1) 

#qualidades dos intervalos em 'd m M A'
#partir do intervalo cromatico e intervalo diatonico
def int_qualidade(intDiatonic,intCromatic):
    if intDiatonic == None or intCromatic == None:
        return None
    intDiatonic = abs(intDiatonic)
    intCromatic = abs(intCromatic)
    while intDiatonic > 7:
        intDiatonic = intDiatonic -7
    if intDiatonic == 1:
        return intP(intDiatonic,intCromatic, 0)
    if intDiatonic == 2:
         return intMm(intDiatonic,intCromatic, 2)
    if intDiatonic == 3:
        return intMm(intDiatonic,intCromatic, 4)
    if intDiatonic == 4:
        return intP(intDiatonic,intCromatic, 5)
    if intDiatonic == 5:
        return intP(intDiatonic,intCromatic, 7)
    if intDiatonic == 6:
        return intMm(intDiatonic,intCromatic, 9)
    if intDiatonic == 7:
        return intMm(intDiatonic,intCromatic, 11)

def times_com_tempos(times):
    if times[0][0][0] == 0:
        times[0][0].append(0)
        times[0][0] = tuple(times[0][0])
        times[0] = tuple(times[0])
        for p in range(len(times)):
            if p+1 < len(times):
                tempos = ((times[p+1][0][1]-times[p][0][1])*times[p][1][0])+times[p][0][2]
                times[p+1][0].append(tempos)
                times[p+1][0] = tuple(times[p+1][0])
                times[p+1] = tuple(times[p+1])
    return times

#tom e modo a partir de fifths e mode
def key(fifths,mode):
    if mode == 'major':
        if fifths == 0:
            return tuple(['C',mode])
        if fifths == 1:
            return tuple(['G',mode])
        if fifths == -1:
            return tuple(['F',mode])
        if fifths == 2:
            return tuple(['D',mode])
        if fifths == -2:
            return tuple(['Bb',mode])
        if fifths == 3:
            return tuple(['A',mode])
        if fifths == -3:
            return tuple(['Eb',mode])
        if fifths == 4:
            return tuple(['E',mode])
        if fifths == -4:
            return tuple(['Ab',mode])
        if fifths == 5:
            return tuple(['B',mode])
        if fifths == -5:
            return tuple(['Db',mode])
        if fifths == 6:
            return tuple(['F#',mode])
        if fifths == -6:
            return tuple(['Gb',mode])
        if fifths == 7:
            return tuple(['C#',mode])
        if fifths == -7:
            return tuple(['Cb',mode])
    if mode == 'minor':
        if fifths == 0:
            return tuple(['a',mode])
        if fifths == 1:
            return tuple(['E',mode])
        if fifths == -1:
            return tuple(['D',mode])
        if fifths == 2:
            return tuple(['B',mode])
        if fifths == -2:
            return tuple(['G',mode])
        if fifths == 3:
            return tuple(['F#',mode])
        if fifths == -3:
            return tuple(['C',mode])
        if fifths == 4:
            return tuple(['C#',mode])
        if fifths == -4:
            return tuple(['F',mode])
        if fifths == 5:
            return tuple(['G#',mode])
        if fifths == -5:
            return tuple(['Bb',mode])
        if fifths == 6:
            return tuple(['D#',mode])
        if fifths == -6:
            return tuple(['Eb',mode])
        if fifths == 7:
            return tuple(['A#',mode])
        if fifths == -7:
            return tuple(['Ab',mode])

#usadas pelas outras funcoes
def intMm(intDiatonic, intCromatic, M):
        m = M-1
        if intCromatic < m:
            return 'd'*(m-intCromatic)
        if intCromatic == m:
            return 'm'
        if intCromatic == M:
            return 'M'
        if intCromatic > M:
            return 'A'*(intCromatic-M)
def intP(intDiatonic, intCromatic, P):
        if intCromatic < P:
            return 'd'*(P-intCromatic)
        if intCromatic == P:
            return 'P'
        if intCromatic > P:
            return 'A'*(intCromatic-P)
def ut_(divisions,time):
    return (divisions*4)/time[1][1]
def uc_(divisions,time):
    return ut_(divisions,time)*time[1][0]
def duracao_R(divisions,time,counter):
    ut = ut_(divisions,time)
    return (counter - time[0][0])/ut
def octa_base(step):
    p = base(step)
    octa_base = [0,0,0,0,0,0,0,1,1,1,1,1,1]
    return octa_base[p:p+7]
def step_base(step):
    p = base(step)
    stepBase = 'CDEFGABCDEFGA'
    return stepBase[p:p+7]
def base(step):
    stepBase = 'CDEFGABCDEFGA'
    for p in range(len(stepBase)):
        if stepBase[p] == step:
            return p
def note_to_midi(note):
    step = note[0]
    octave = note[1]
    alter = note[2]
    if step == 'C':
        midiN = 60
    elif step == 'D':
        midiN = 62
    elif step == 'E':
        midiN = 64
    elif step == 'F':
        midiN = 65
    elif step == 'G':
        midiN = 67
    elif step == 'A':
        midiN = 69
    elif step == 'B':
        midiN = 71
    if alter == None:
        alter = 0
    if step == None and octave == None:
        return None
    return (midiN+((octave - 4)*12))+alter