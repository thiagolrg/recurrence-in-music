import f_diretorios as f_d
import f_analise as f_a

dimapamus = f_d.diretorio('ler','.mapamus')
listacaminhos = f_d.caminhos_arquivo(dimapamus, '.mapamus')
for caminho in listacaminhos:
    mapamus = f_d.le_mapamus(caminho)
    interdurloc = f_a.interdurunicos_loc(mapamus)

