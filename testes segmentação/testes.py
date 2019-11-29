from collections import defaultdict
import pickle
caminho = r'C:\Users\Thiago.DESKTOP-13409IC\Documents\TesteChordVoiceLayer\k5 principais voice1\Dicts\K5.p'
with open(caminho, 'rb') as f:
    arquivo = pickle.loads(f.read())
seq = arquivo['P1'][1]['intDia']

aDic = defaultdict(list)
for caminho in caminhos: 
    musD = defaultdict(list)
    for p1 in range(len(seq)):
        for p2 in range(p1 + 1, len(seq) + 1):
            musD[tuple(seq[p1:p2])].append((p1, p2))

    for val in musD.values():
        for v in val:
            if len(val) > 1:
                slices.append(val)
            else:
                usclices.append(val)

    slices = sorted(slices, key=lambda item: item[1] - item[0], reverse=True) #longest to shortest
    slices = sorted(slices, key=lambda item: item[0]) #imitial number small to big inside the longest to shortest

    def subset_of(longest_slices, slise):
        return any(slise[0] >= ls[0] and slise[1] <= ls[1] for ls in longest_slices)

    def part_of(longest_slices, slise):
        return any(slise[0] > ls[0] and slise[0] <= ls[1] and slise[1] > ls[1] for ls in longest_slices)

    longest_slices = []
    for slise in slices:
        if not subset_of(longest_slices, slise) or part_of(longest_slices, slise):
            longest_slices.append(slise)

    for v in uslices:
        longest_slices.append(v)

    for sli in longest_slices:
        aDic[tuple(seq[sli[0]:sli[1]])].append(sli)

aDic = dict(sorted(((k, v) for k, v in aDic.items() if len(v) > 1), key=lambda x: (len(x[0], lenx[1])), reverse=True))
print(aDic)