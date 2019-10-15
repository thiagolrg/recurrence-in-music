import f_diretorios as f_d
import f_analise as f_a
import os

dimapamus = f_d.diretorio('ler','.mapamus')
dianalise = f_d.diretorio('gravar', '.analise')+'\\'+'analise'
nomeanalise = input('nome do arquivo de analise: ')
caminhosmapamusler = f_d.caminhos_arquivo(dimapamus, '.mapamus')
os.makedirs(dianalise, exist_ok=True)

interdurunicoloc = {}
for caminho in caminhosmapamusler:
    nomemapamus = f_d.nome_arquivo(caminho, '.mapamus')
    mapamus = f_d.le_arquivo(caminho, 'rb')
    interdurunicoloc = f_a.interdurunicos_loc(interdurunicoloc, mapamus, nomemapamus)
    
    print(caminhosmapamusler.index(caminho)+1,' de ',len(caminhosmapamusler))

interdurunicoloc = f_a.filtro_maisde1musica(interdurunicoloc)
f_d.escreve_arquivo(dianalise, nomeanalise+'.analise', interdurunicoloc, 'wb')

with open(dianalise+'\\'+nomeanalise+'.txt', 'w') as f:
    linha = 0
    for items in interdurunicoloc.items():
        linha = linha + 1
        print(linha,'.   ',items,'\n',file=f)

