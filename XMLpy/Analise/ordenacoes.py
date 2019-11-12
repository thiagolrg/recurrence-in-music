def sort_tamKquanV(entrada):
    pronto = {}
    for chave, valor in sorted(entrada.items(), key=lambda item: (len(item[0][0]), len(item[1])), reverse=True):
        pronto.setdefault(chave, valor[1:])
    return pronto