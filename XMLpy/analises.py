from collections import defaultdict
import dirEinp as f_d

def segdur_sodotamanho(caminhosdict, janela):
    aDicio = defaultdict(list)
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        for parte in musD:
            for voz, caracteristicas in musD[parte].items():
                if 'intDia' in caracteristicas:
                    p1 = 0
                    while p1 + janela <= len(caracteristicas['intDia']):
                        p2 = p1 + janela
                        aDicio[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]))].append((nome, parte, voz, (p1, p2), (caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1]),(caracteristicas['Ncompasso'][p2], caracteristicas['Pcompasso'][p2])))
                        p1 += 1
    aDicio = sorted([(k, v) for k, v in aDicio.items() if len(v) > 1], key=lambda x: (len(x[0][0]), len(x[1])), reverse=True)
    return aDicio

def encontrartamanho(caminhosdict, j=1):
    if len(segdur_sodotamanho(caminhosdict, j)) == 0:
        print('tamanho ', j-1)
        return j -1
    else:
        return encontrartamanho(caminhosdict, j=j+1)

def subset_of(longest_slices, slise):
    for item in longest_slices:
        for ls in item[1]:
            if slise[3][0] >= ls[3][0] and slise[3][1] <= ls[3][1] and slise[0:3] == ls[0:3]:
                return True
    return False

def part_of(longest_slices, slise):
    for item in longest_slices:
        for ls in item[1]:
            if slise[3][0] > ls[3][0] and slise[3][0] <= ls[3][1] and slise[3][1] > ls[3][1] and slise[0:3] == ls[0:3]:
                return True
    return False


def segdur_todosatetamanho(caminhosdict, tamanho):
    aDicio = defaultdict(list)
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        nome = musD.pop('nome')
        print(f'analisando {nome}, ',caminhosdict.index(caminho)+1,' de ', len(caminhosdict))
    
        for parte in musD:
            for voz, caracteristicas in musD[parte].items():
                if 'intDia' in caracteristicas:
                    p1 = 0
                    while p1 < len(caracteristicas['intDia']):
                        p2 = p1+1
                        while p2-p1 <= tamanho and p2 <= len(caracteristicas['intDia']):
                            aDicio[(tuple(caracteristicas['intDia'][p1:p2]),tuple(caracteristicas['duracao'][p1:p2]))].append((nome, parte, voz, (p1, p2),(caracteristicas['Ncompasso'][p1], caracteristicas['Pcompasso'][p1]), (caracteristicas['Ncompasso'][p2-1], caracteristicas['Pcompasso'][p2-1])))
                            p2 += 1
                        p1 += 1
    return sorted([(k, v) for k, v in aDicio.items() if len(v) > 1], key=lambda x: (len(x[0][0]), len(x[1])), reverse=True)

'''
    semconteamont = []
    for seg, pos in aDicio:
        posp = []
        for loc in pos:
            if not subset_of(semconteamont, loc) and not part_of(semconteamont, loc):
                posp.append(loc)
        if len(posp) > 1:
            semconteamont.append((seg,posp))
    print(len(aDicio))
    return {x:y for x,y in semconteamont}

def tamanho_seg(caminhosdict, n=1, t1=0):
    print(n)
    t2 = len(segdur2(caminhosdict))
    if t2 == t1:
        print(n-1)
        return n-1
    else:
        tamanho_seg(caminhosdict, n=n+1, t1=t2)
'''

'''
contidos = True
partes = True
Segmentos = caracteristicas e p1 p1p2 p2m1 p1p2set p2m1set
posicoes = caractetisticas localizacao p1 p1p2 p2m1 p1p2set p2m1set
filtrosset = caractetisticas p1f p1p2f p2m1f

(segmento1,sgmento2): [{car1: set(), car2: set()}, [nome, parte, voz, (p1,p2),{}]]
'''