a = {'inte1': [('nome1',1,2),('nome2',1,2),('nome2',1,2)], 'inte2': [('nome',1,2),('nome',1,2),('nome',1,2)]}

def emmaisdeuma(dicio):
    musicas = set()
    for valores in a['inte1']:
        musicas.add(valores[0])
    if len(musicas) > 1:
        return ('inte1', valores)

teste = emmaisdeuma(a)

debug = teste

