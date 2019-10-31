def note_to_miniN(step,alter,octave):
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
    return (midiN+((octave - 4)*12))+alter

def duration_time(divisions,time,counter):
    ut = (divisions*4)/time[1][1]
    uc = ut*time[1][0]
    durationTime = counter - time[0]
    while durationTime//uc > 0:
        durationTime = durationTime - uc
    return durationTime/ut

def int_diatonic(n1,n2):
    n1step = n1[0]
    n1octa = n1[1]
    n2step = n2[0]
    n2octa = n2[1]
    octa = n2octa - n1octa
    octa_base = [0,0,0,0,0,0,0,1,1,1,1,1,1]
    int_base = [1,2,3,4,5,6,7]
    step_base = 'CDEFGABCDEFGA'
    for p in range(len(step_base)):
        if step_base[p] == n1step:
            step_base =  step_base[p:p+7]
            octa_base =  octa_base[p:p+7]
            break
    for p in range(len(step_base)):
        if step_base[p] == n2step:
            int_diatonic = int_base[p]
            if octa >= octa_base[p]:
                int_diatonic = int_diatonic+((octa - octa_base[p])*7)
                break
            else:
                int_diatonic = (int_diatonic-9)+(((octa - octa_base[p]) + 1)*7)
                break
    return int_diatonic

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

#graus de escala a partir do tom modo e nota
def scale_degrees():
    degrees = ['I','II','III','IV','V','VI','VII']

#intevalos em semi-tons a partir do número MIDI
def int_cromatic():
    pass

#intervalos em M m d a partir do int cromatico e int diatonico
def int_qual(diat,cromat):
    pass