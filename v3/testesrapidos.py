import f_diretorios as f_d

diretorio = f_d.diretorio('ler', '.analise')
caminho = f_d.caminhos_arquivo(diretorio, '.analise')
pronto = f_d.le_arquivo(caminho[0], 'rb')
debug = pronto