import pickle
import dirEinp as f_d
from collections import defaultdict



dire = r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\testepickle'

direarqs = f_d.caminhos_extensoes(diretorio, ['.p'])
if direarqs == []:
    dicio = defaultdict(list)
    with open(diretorio+'1.p', 'wb') as f:
        pickle.dumb(dicio, f)
    direarqs = f_d.caminhos_extensoes(diretorio, ['.p'])

for direarq in direarqs:
    with open(direarq,'rb') as f:
        dicio = pickle.load(f)
    
    if chave in dicio.keys():
        dicio[chave].append(valor)
        break

with open(direarq[-1],'rb') as f:
    dicio = pickle.load(f)
dicio[chave].append(valor)

if len(dicio) == tamarq:
    dicio = defaultdict(list)
    with open(f'diretorio+{len(direarqs)+1}.p', 'wb') as f:
        pickle.dumb(dicio, f)
    direarqs = f_d.caminhos_extensoes(diretorio, ['.p'])

with open(diretorio+'1.p', 'wb') as f:
    pickle.dumb(dicio, f)
    direarqs = f_d.caminhos_extensoes(diretorio, ['.p'])

    


