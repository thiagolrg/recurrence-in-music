#encontra a Fcompasso, tonalidade ou andamento da nota
#a partir da nota e da lista de compassos,andamentos ou tonalidades
def referencia(nota,listaref):
    for p in range(len(listaref)):
        if p+1 == len(listaref):
            return listaref[p]
        if counter(listaref[p+1]) > counter(nota):
            return listaref[p]

#graus de escala a partir da tonalidade e nota
def grau_escala(key,note):
    s = step(note)
    if s == None:
        return None
    stepBase = step_base(tom(key)[0])
    graus = ['I','II','III','IV','V','VI','VII']
    for p in range(len(stepBase)):
        if stepBase[p] == s:
            return graus[p]

#intervalo diatonico a partir do nome e oitava de duas notas
def int_diatonico(nota1,nota2):
    n1step = step(nota1)
    n1octa = octave(nota1)
    n2step = step(nota2)
    n2octa = octave(nota2)
    if n1step == None or n2step == None:
        return None
    octa = n2octa - n1octa
    stepBase = step_base(n1step)
    octaBase = octa_base(n1step)
    int_base = [1,2,3,4,5,6,7]
    for p in range(len(stepBase)):
        if stepBase[p] == n2step:
            intDiatonic = int_base[p]
            if octa >= octaBase[p]:
                return intDiatonic+((octa - octaBase[p])*7)
            else:
                return (intDiatonic-9)+(((octa - octaBase[p]) + 1)*7)

#intevalos cromaticos a partir de duas notas(converte para midi para isso)
def int_cromatico(note1,note2):
    if step(note1) == None or step(note2) == None:
        return None
    return note_to_midi(note2) - note_to_midi(note1) 

#qualidades dos intervalos em 'd m M A'
#partir do intervalo cromatico e intervalo diatonico
def int_qualidade(intDiatonic,intCromatic):
    if intDiatonic == None or intCromatic == None:
        return None
    intDiatonic = abs(intDiatonic)
    intCromatic = abs(intCromatic)
    while intDiatonic//8 > 0:
        intDiatonic = intDiatonic -7
    while intCromatic//12 > 0:
        intCromatic = intCromatic - 12
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

#recebe todas as Fcompasso e coloca seu inicio em duracoes
def times_com_duracoes(times):
    if counter(times[0]) == 0:
        val(times[0]).append(0)
        times[0][1] = tuple(val(times[0]))
        times[0] = tuple(times[0])
        for p in range(len(times)):
            if p+1 < len(times):
                tempos = ((Ncompasso(times[p+1])-Ncompasso(times[p]))*num(times[p]))+duracao(times[p])
                val(times[p+1]).append(tempos)
                times[p+1][1] = tuple(val(times[p+1]))
                times[p+1] = tuple(times[p+1])
    return times

#tom e modo a partir de fifths e mode
def key_(fifths,mode):
    if mode == None:
        return fifths
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
            return tuple(['A',mode])
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

def m_soundtempo(soundtempo, time):
    d = den(time)
    if num(time)%3 == 0:
        c = 3
    else:
        c = 1
    return ( (d/ (d/4*d) ) *c, ( (soundtempo/4) *d) / c)

def m_metronome(m):
    if m['beat-unit'] == 'quarter':
        bu = 1
    elif m['beat-unit'] == 'eighth':
        bu = 0.5
    elif m['beat-unit'] == 'half':
        bu = 2
    elif m['beat-unit'] == 'whole':
        bu = 4
    elif m['beat-unit'] == '16th':
        bu = 0,25
    else:
        raise NotImplementedError('{} não implementado'.format(m['beat-unit']))
    if 'beat-unit-dot' in m:
        bu = bu+(bu/2)
    return (bu, int(m['per-minute']))

#duracao desde o inicio da musica
def duracao_inicio(divisions,time,nota):
    return duracao_Fcompasso(divisions,time,nota)+duracao(time)

#posicao dentro do compasso (tempo.fracaodetempo)
def P_compasso(divisions,time,nota):
    d = duracao_Fcompasso(divisions,time,nota)
    n = num(time)
    while d//n > 0:
        d = d - n
    return d+1

#posicao dentro tempo (resto de Pcompasso)
def P_tempo(divisions,time,nota):
    return P_compasso(divisions,time,nota)%1

#numero do tempo (inteiro de Pcompasso)
def N_tempo(divisions,time,nota):
    return int(P_compasso(divisions,time,nota))

#usadas pelas outras funcoes
def val(mensagem):
    return mensagem[1]
def loc(mensagem):
    return mensagem[0]

def counter(mensagem):
    return loc(mensagem)[0]
def Ncompasso(mensagem):
    return loc(mensagem)[1]
def division(mensagem):
    return loc(mensagem)[2]

def step(nota):
    return val(nota)[0]
def octave(nota):
    return val(nota)[1]
def alter(nota):
    return val(nota)[2]
def tie(nota):
    return val(nota)[3]

def tom(key):
    return val(key)[0]
def modo(key):
    val(key)[1]

def num(time):
    return val(time)[0]
def den(time):
    return val(time)[1]
def duracao(time):
    return val(time)[2]

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
        
def note_to_midi(note):
    s = step(note)
    a = alter(note)
    o = octave(note)
    if s == 'C':
        midiN = 60
    elif s == 'D':
        midiN = 62
    elif s == 'E':
        midiN = 64
    elif s == 'F':
        midiN = 65
    elif s == 'G':
        midiN = 67
    elif s == 'A':
        midiN = 69
    elif s == 'B':
        midiN = 71
    if a == None:
        a = 0
    if s == None and o == None:
        return None
    return (midiN+((o - 4)*12))+a

def ut_duration(divisions,time):
    return (divisions*4)/den(time)

def duracao_Fcompasso(divisions,time,note):
    return (counter(note) - counter(time))/ut_duration(divisions,time)

def duration_time(divisions,time,counter):
    ut = (divisions*4)/time[1][1]
    uc = ut*time[1][0]
    durationTime = counter - time[0]
    while durationTime//uc > 0:
        durationTime = durationTime - uc
    return durationTime/ut