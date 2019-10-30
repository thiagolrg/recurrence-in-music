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