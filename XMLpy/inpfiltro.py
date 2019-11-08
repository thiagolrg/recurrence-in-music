listaC = ['a','b','c','d']
listaT = ['a','b','c','d']
listaFT = ['a','b','c','d']

listachave = []
listavalor = []
for valor in listaC:
    cv = input(valor,'chave ou valor?', ['chave','valor','proximo'])
    t = input(valor,['como extrair?',listaT])

    

def inp(texto, opcoes):
    print(f'{texto}\n')
    for o in opcoes:
        print(o)
    ip = input('escolha uma opcao: ')
    if ip in opcoes:
        return ip
    else:
        print(f'{ip} não é uma ooção')
        return inp(texto, opcoes)

def chavevalor_VT(listaC, listaT):
    chaveV = inp('qual chave extrair:', listaC)
    chaveT = inp('como extrair chave:', listaT)
    return (chaveV, chaveT)

def denovo(lista, listaC, listaT):
    lista.append(chavevalor_VT(listaC,listaT))
    outra = inp('outra chave?', ['s','n'])
    if outra == 's':
        return denovo(lista,listaC,listaT)
    else:
        return lista




