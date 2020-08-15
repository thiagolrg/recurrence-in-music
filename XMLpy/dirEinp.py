import os
import pickle

def diretorio_ler(extensoes):
    di=input(f'diretorio para ler {extensoes}:')
    if os.path.exists(di) == False:
        print('diretorio nao existe')
        return diretorio_ler(extensoes)
    else:
        #r=root, d=directoriesinroot, f=filesinroot
        for r, d, f in os.walk(di):
            for file in f:
                for extensao in extensoes:
                    if extensao in file:
                        return di
        else:
            print(f'nao existem {extensoes} no diretorio')
            return diretorio_ler(extensoes)         


def cria_pasta(diretorio):
    os.makedirs(diretorio, exist_ok=True)
    return None

#retorna uma lista com o caminho de todos os arquivos do diretorio com a extensao
def caminhos_extensoes(diretorio, extensoes):
    caminhos = []
    #r=root, d=directoriesinroot, f=filesinroot
    for r, d, f in os.walk(diretorio):
        for file in f:
            for extensao in extensoes:
                if extensao in file:
                    caminhos.append(os.path.join(r, file))
    return caminhos

def caminho_nome(caminho, extensoes):
    for linha in caminho.split('\\'):
        for extensao in extensoes:
            if extensao in linha:
                return linha.replace(extensao,'')

def xml_sem_dict(di, extensoes, diD, extensaoP):
    nomesdict = []
    caminhosxmlsemdict = []
    caminhosxml = caminhos_extensoes(di, extensoes)
    caminhosdict = caminhos_extensoes(diD, extensaoP)
    for caminho in caminhosdict:
        nomesdict.append(caminho_nome(caminho, extensaoP))
    for caminho in caminhosxml:
        if caminho_nome(caminho, extensoes) not in nomesdict:
            caminhosxmlsemdict.append(caminho)
    return caminhosxmlsemdict

def entrada_xml(caminho):
    with open(caminho) as f:
        xml = []
        for l in f.read().splitlines():
            xml.append(l.strip())
    return xml

def entrada_mxl(caminho, nome):
    import zipfile
    xml = []
    with zipfile.ZipFile(caminho) as z:
        with z.open(nome+'.mxl') as arq:
            for l in arq.read().splitlines():
                xml.append(l.decode().strip())
    return xml

def le_pickle(caminho):
   with open(caminho, 'rb') as f:
      arquivo = pickle.loads(f.read())
   return arquivo

def escreve_pickle(diretorio, arquivo ,nome, trunca=False):
    if trunca == False:
        modo = 'xb'
    elif trunca == True:
        modo = 'wb'
    with open(diretorio+'\\'+nome+'.p', modo) as f:
        pickle.dump(arquivo, f)
    return None

def escreve_txt(diretorio, arquivo, nome):
    with open(diretorio+'\\'+nome+'.txt', 'a') as f:
        linha = 0
        for item in arquivo.items():
            linha = linha + 1
            print(linha,'.   ',item,'\n',file=f)
    return None

#inputs gerais do usuario
def inp(texto, opcoes):
    def printtexto(texto):
        if isinstance(texto, list):
            for i in texto:
                printtexto(i)
        elif isinstance(texto, dict):
            for item in texto.items():
                print(item)
        else:
            print(texto)
    printtexto(texto)
    print()
    for o in range(len(opcoes)):
        print(f'{o+1}. {opcoes[o]}')
    ip = input('escolha uma opcao: ')
    if ip.isdigit() and int(ip) <= len(opcoes):
        print()
        return opcoes[int(ip)-1]
    else:
        print(f'{ip} não é uma ooção\n')
        return inp(texto, opcoes)

#usado nos inputs de quantidade
def quantidade_():
    q = input('que ocorrem pelo menos _ vezes: ')
    try:
        return int(q)
    except ValueError:
        print('deve ser inteiro')
        return quantidade_()