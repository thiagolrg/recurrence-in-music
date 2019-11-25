from collections import defaultdict
import pickle
from collections import defaultdict
caminho = r'C:\Users\Thiago.DESKTOP-13409IC\Documents\TesteChordVoiceLayer\k5 principais voice1\Dicts\K5.p'
with open(caminho, 'rb') as f:
    arquivo = pickle.loads(f.read())
seq = arquivo['P1'][1]['intDia']

dic = defaultdict(list)

for p1 in range(len(seq)):
    for p2 in range(p1 + 1, len(seq) + 1):
        dic[tuple(seq[p1:p2])].append((p1, p2))

slices = [ v for val in dic.values() for v in val if len(val) > 1 ] #I'm taking each slice from dic, not each group of slices
slices = sorted(slices, key=lambda item: item[1] - item[0], reverse=True) #longest to shortest
slices = sorted(slices, key=lambda item: item[0]) #imitial number small to big inside the longest to shortest

def subset_of(longest_slices, slise):
    return any(ls[0] <= slise[0] and slise[1] <= ls[1] for ls in longest_slices)

longest_slices = []
for slise in slices:
    if not subset_of(longest_slices, slise):
        longest_slices.append(slise)

readydic = defaultdict(list)
for sli in longest_slices:
    readydic[tuple(seq[sli[0]:sli[1]])].append(sli)
t = readydic.keys()

readydic = dict(sorted(((k, v) for k, v in readydic.items() if len(v) > 1), key=lambda x: len(x[0]), reverse=True))
print(readydic)
debug = 0