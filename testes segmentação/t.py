import pickle
from collections import defaultdict
caminho = r'C:\Users\Thiago.DESKTOP-13409IC\Documents\TesteChordVoiceLayer\k5 principais voice1\Dicts\K5.p'
with open(caminho, 'rb') as f:
    arquivo = pickle.loads(f.read())
seqE = arquivo['P1'][1]['intDia']
#seqE = [9,9,1,2,3,4,5,6,0,1,2,8,1,2,3,4,5,6,9,1,2,3,8,0,1,2,1,2,3,9]
#seqE = [8,0,1,2]

len_seqE = len(seqE)

n = 0
d = defaultdict(list)
for i in range(len_seqE):
    for j in range(i + 1, len_seqE+1):
        d[tuple(seqE[i:j])].append((i, j))
        n +=1
print(n)


size = int(len(seqE)/2) #inteiro para arredondar para baixo caso len seja impar
n=0
while size > 1:
    p1 = 0
    p2 = p1+size
    while p1+size*2 <= len_seqE:
        comparar = seqE[p1:p1+size]
        p2 = p1+size
        while p2+size <= len_seqE:
            n +=1
            comparando = seqE[p2:p2+size]
            if comparar == comparando:
                print(comparar,comparando, n)
            p2 += 1
        p1 += 1
    size -= 1

print(n)