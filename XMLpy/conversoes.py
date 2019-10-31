#posicao de inicio dentro do compasso
def position_measure(divisions,time,counter):
    ut = ut_(divisions,time)
    uc = uc_(divisions,time)
    positionMeasure = counter - time[0][0]
    while positionMeasure//uc > 0:
        positionMeasure = positionMeasure - uc
    return (positionMeasure/ut)+1

def time_number(timeOld,time):
    return ((time[0][1]-timeOld[0][1])*timeOld[1][0])+timeOld[0][2]


#graus de escala a partir do tom modo e nota
def scale_degree(key,note):
    step = note[0]
    if step == None:
        return None
    stepBase = step_base(key[0])
    degrees = ['I','II','III','IV','V','VI','VII']
    for p in range(len(stepBase)):
        if stepBase[p] == step:
            return degrees[p]

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

#numero MIDI a partir do step alter e octave da nota
def note_to_miniN(note):
    step = note[0]
    alter = note[1]
    octave = note[2]
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

#intervalo diatonico a partir do step e octave de 2 notas
def int_diatonic(noteOld,note):
    nOldstep = noteOld[0]
    nOldocta = noteOld[2]
    nstep = note[0]
    nocta = note[2]
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

#intevalos cromaticos a partir do número MIDI
def int_cromatic(midiNOld,midiN):
    return midiN-midiNOld

#qualidades dos intervalos em 'd m M A'
#partir do intervalo cromatico e intervalo diatonico
def int_quality(intDiatonic,intCromatic):
    intDiatonic = abs(intDiatonic)
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

a = int_quality(-15,-2)
a = int_quality(-8,-1)
a = int_quality(1,0)
a = int_quality(8,1)
a = int_quality(15,2)

a = int_quality(-16,-1)
a = int_quality(-9,0)
a = int_quality(-2,1)
a = int_quality(2,2)
a = int_quality(9,3)
a = int_quality(16,4)

a = int_quality(-17,1)
a = int_quality(-10,2)
a = int_quality(-3,3)
a = int_quality(3,4)
a = int_quality(10,5)
a = int_quality(17,6)

a = int_quality(4,3)
a = int_quality(4,4)
a = int_quality(4,5)
a = int_quality(4,6)
a = int_quality(4,7)

a = int_quality(5,5)
a = int_quality(5,6)
a = int_quality(5,7)
a = int_quality(5,8)
a = int_quality(5,9)

a = int_quality(6,6)
a = int_quality(6,7)
a = int_quality(6,8)
a = int_quality(6,9)
a = int_quality(6,10)
a = int_quality(6,11)

a = int_quality(7,8)
a = int_quality(7,9)
a = int_quality(7,10)
a = int_quality(7,11)
a = int_quality(7,12)
a = int_quality(7,13)