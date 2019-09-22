import entrada, f_ref

vozeslista = entrada.vozeslista
p = 0
loc = [[]]
inte = [[]]
dur = [[]]

for voz in vozeslista:
    for linha in range(len(voz)):
        if linha+1 < len(voz):

            if 'Note_on_c' in voz[linha]:
                comp = f_ref.comp(voz[linha])
                bpm =  f_ref.bpm(voz[linha])
                locC = f_ref.locC(voz[linha])
                locT = f_ref.locT(voz[linha])
                loc[p].append([comp, bpm, locC, locT])

                non = []
                noff = []
                for busca in range(linha+1,len(voz)):
                    if noff == [] or non == []:
                        if 'Note_off_c'  in voz[busca]:
                            noff = voz[busca]
                        if 'Note_on_c' in voz[busca]:
                            non =voz[busca]
                    else:
                        linhadur = f_ref.durI(voz[linha])
                        nondur = f_ref.durI(non)
                        noffdur = f_ref.durI(noff)
                        inte[p].append(non[4]-voz[linha][4])
                        dur[p].append(nondur-linhadur)
                        #dur[p].append([nondur-linhadur, nondur-noffdur])
                        break
    
        else:
            if len(loc) != len(vozeslista):
                loc.append([])
                inte.append([])
                dur.append([])
                p = p + 1

final = []
for locvoz, intevoz, durvoz in zip(loc,inte,dur):
    for posicao1 in range(len(intevoz)):
        for posicao2 in range(posicao1, len(intevoz)):
            final.append([locvoz[posicao1], intevoz[posicao1:posicao2+1], durvoz[posicao1:posicao2+1]])
