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