lista = [x for x in range(10)]



def tamanhoslista(caminhosdict):
    TintDia = []
    for caminho in caminhosdict:
        musD = f_d.le_pickle(caminho)
        for parte in musD:
                for voz, caracteristicas in musD[parte].items():
                    if 'intDia' in caracteristicas:
                        TintDia.append(len(caracteristicas['intDia']))
    return TintDia

def segmentacao(lista, janela=0):
    seg = []
    lenlista = len(lista)
    if janela == 0:
	    janela = len(lista)
    p1 = 0
    while p1 < lenlista:
        p2 = p1+1
        while p2-p1 <= janela and p2 <= lenlista:
            seg.append(lista[p1:p2])
            p2 += 1
        p1 += 1
    return seg

def complexidade_segmentacao(lista, janela=0):
    if janela == 0:
        janela = len(lista)
    return int(((len(lista)-(janela-1))*janela)+(((janela-1)*janela)/2))

n = 0
for lista in TindDia:
    n = complexidade_segmentacao(lista, janela=133)+n

debug = 0