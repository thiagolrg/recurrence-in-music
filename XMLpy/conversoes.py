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

def int_diatonic(nota1,nota2):
    step_string = 'CDEFGABCDEFGABCDEFGABC'
    oit = -1
    int_lista = [-7,-6,-5,-4,-3,-2,1,2,3,4,5,6,7]

    for p in range(len(step_string)):
        if step_string[p] == nota1[0]:
            step_string =  step_string[p+1:p+14]
            break
    
    oit_list = []
    for nota in step_string:
        if nota == 'C':
            oit += 1
        oit_list.append(oit)
    return step_string

int_diatonic(('C',3),('B',3))