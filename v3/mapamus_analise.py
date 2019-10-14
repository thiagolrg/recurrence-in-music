import f_diretorios as f_d
import f_analise as f_a
import os

dimapamus = f_d.diretorio('ler','.mapamus')
dianalise = f_d.diretorio('gravar', '.analise')+'\\'+'analise'
listacaminhos = f_d.caminhos_arquivo(dimapamus, '.mapamus')
os.makedirs(dianalise, exist_ok=True)
arquivoanalise = dianalise+'\\'+'interdur_loc em mais de uma musica.analise'

'''ajeitar o caos do moludo f_d, principalmente as funcoes de escrever e ler arquivos
definir um momento exato para declarar a existencia do arquivo de analise
e manter essa declaracao durente todo esse modulo'''

for caminho in listacaminhos:
    nomemus = f_d.nome_arquivo(caminho, '.mapamus')
    mapamus = f_d.le_mapamus(caminho, 'rb')

    interdurloc = f_a.interdurunicos_loc(mapamus, arquivoanalise)
    print(interdurloc+' com '+nomemus)

analise = f_d.le_mapamus(arquivoanalise, 'rb')
resultado = f_a.filtro_maisde1musica(analise)
