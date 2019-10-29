import diretorios as f_d
import analises as f_a
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

    interdurunicoloc = f_a.interdurunicos_intmus_loc(interdurunicoloc, mapamus, nomemapamus)
    #interdurunicoloc = f_a.interdurunicos_loc(interdurunicoloc, mapamus, nomemapamus)

interdurunicoloc = f_a.filtro_maisde1musica(interdurunicoloc)
interdurunicoloc = f_a.sort_tamSIquanLOC(interdurunicoloc)

interdurunicoloc_ni = f_a.nested_identificados(interdurunicoloc)
f_d.escreve_arquivo(dianalise, nomeanalise+', nested marcados.analise', interdurunicoloc, 'wb')
f_d.escreve_txt(dianalise, nomeanalise+', nested marcados.txt', interdurunicoloc)

interdurunicoloc_fn = f_a.filtro_nested(interdurunicoloc)
f_d.escreve_arquivo(dianalise, nomeanalise+', filtro nested.analise', interdurunicoloc, 'wb')
f_d.escreve_txt(dianalise, nomeanalise+', filtro nested.txt', interdurunicoloc)

interdurunicoloc_limpo = f_a.limpa_posicoes(interdurunicoloc_fn)
f_d.escreve_arquivo(dianalise, nomeanalise+', filtro nested sem posicoes.analise', interdurunicoloc, 'wb')
f_d.escreve_txt(dianalise, nomeanalise+', filtro nested sem posicoes.txt', interdurunicoloc)


'''
    analise = f_a.interdurunicos_maisoumenos_loc(interdurunicoloc, mapamus, nomemapamus)
    interdurunicoloc = f_a.interdurunicos_loc(interdurunicoloc, mapamus, nomemapamus)
    print(caminhosmapamusler.index(caminho)+1,' de ',len(caminhosmapamusler))

interdurunicoloc = f_a.filtro_maisde1musica(interdurunicoloc)
interdurunicoloc = f_a.sort_tamSIquanLOC(interdurunicoloc)

f_d.escreve_arquivo(dianalise, nomeanalise+', filtro mais de uma musica.analise', interdurunicoloc, 'wb')
f_d.escreve_txt(dianalise, nomeanalise+', filtro mais de uma musica.txt', interdurunicoloc)
'''