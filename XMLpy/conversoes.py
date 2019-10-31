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

def scale_degrees():
    degrees = ['I','II','III','IV','V','VI','VII']