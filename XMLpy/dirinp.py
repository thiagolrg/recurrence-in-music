def diretorio_ler(extensao):
    di=input('diretorio para ler '+extensao+': ')
    import os
    if os.path.exists(di) == False:
        print('diretorio nao existe')
        return diretorio_ler(extensao)
    else:
        # r=root, d=directories, f=folder
        for r, d, f in os.walk(di):
            for file in f:
                if extensao in file:
                    break
            else:
                continue
            break
        else:
            print('nao existem '+extensao+' no diretorio')
            return diretorio_ler(extensao)         
    return di

def cria_pasta(diretorio):
    import os
    os.makedirs(diretorio, exist_ok=True)
    return None

#retorna uma lista com o caminho de todos os arquivos do diretorio com a extensao
def caminhos_extensao(diretorio, extensao):
    import os
    caminhos = []
    # r=root, d=directories, f=folder
    for r, d, f in os.walk(diretorio):
        for file in f:
            if extensao in file:
                caminhos.append(os.path.join(r, file))
    return caminhos

def caminho_nome(caminho, extensao):
    for linha in caminho.split('\\'):
        if extensao in linha:
            return linha.replace(extensao,'')

def xml_sem_dict(caminhosxml,caminhosdict):
    nomesdict = []
    caminhosxmlsemdict = []
    for caminho in caminhosdict:
        nomesdict.append(caminho_nome(caminho, '.p'))
    for caminho in caminhosxml:
        if caminho_nome(caminho, '.xml') not in nomesdict:
            caminhosxmlsemdict.append(caminho)
    return caminhosxmlsemdict

def entrada_xml(caminho):
    with open(caminho) as f:
        arquivo = []
        for l in f.readlines():
            arquivo.append(l.strip().replace('\n', ''))
    return arquivo

def escreve_pickle(diretorio, arquivo ,nome):
   import pickle
   with open(diretorio+'\\'+nome+'.p', 'xb') as f:
      pickle.dump(arquivo, f)
   return None

def le_pickle(caminho):
   import pickle
   with open(caminho, 'rb') as f:
      arquivo = pickle.loads(f.read())
   return arquivo



        