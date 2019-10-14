import f_diretorios as f_d
import f_analise as f_a
import os

dimapamus = f_d.diretorio('ler','.mapamus')
dianalise = f_d.diretorio('gravar', '.analise')+'\\'+'analise'
listacaminhos = f_d.caminhos_arquivo(dimapamus, '.mapamus')
os.makedirs(dianalise, exist_ok=True)
arquivoanalise = 'interdur_loc em mais de uma musica'

for caminho in listacaminhos:
    nomemus = f_d.nome_arquivo(caminho, '.mapamus')
    mapamus = f_d.le_mapamus(caminho, 'rb')

    interdurloc = f_a.interdurunicos_loc(mapamus, dianalise, nomemus , arquivoanalise)
    print(interdurloc+' com '+nomemus)

analise = f_d.le_mapamus(dianalise+'\\'+arquivoanalise+'.analise', 'rb')
resultado = f_a.filtro_maisde1musica(analise)
