import f_diretorios as f_d

diretorio = f_d.diretorio('ler', '.analise')
caminho = f_d.caminhos_arquivo(diretorio, '.analise')
nome = f_d.nome_arquivo(caminho[0], '.analise')
pronto = f_d.le_arquivo(caminho[0], 'rb')

with open(diretorio+'\\'+nome+'.txt', 'w') as f:
    linha = 0
    for items in pronto.items():
        linha = linha + 1
        print(linha,'.   ',items,'\n',file=f)