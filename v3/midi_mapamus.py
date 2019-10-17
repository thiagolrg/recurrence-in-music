import f_limpaextrai as f_l 
import f2_mapa as f2_m
import f2_segmenta as f2_s
import f_diretorios as f_d
import os

dimidi = f_d.diretorio('ler','.mid')
caminhosmidiler = f_d.caminhos_arquivo(dimidi, '.mid')

dimapamus = f_d.diretorio('gravar', '.mapamus')+'\\'+'mapamus'
os.makedirs(dimapamus, exist_ok=True)

for caminho in caminhosmidiler:
    entrada = f_l.entrada_midi(caminho)
    entradalimpa = f_l.limpeza(entrada)
    nome = f_d.nome_arquivo(caminho,'.mid')
    tom, modo, ppq, compassos, tempos, notas = f_l.limpa_extrai(entradalimpa)

    mapabpm = f2_m.mapa_bpm(tempos,compassos)
    mapacomploc = f2_m .mapa_comploc(compassos,ppq)
    mapamus = f2_s.mapa_mus(nome, tom, modo, notas, mapacomploc, mapabpm, ppq)

    f_d.escreve_arquivo(dimapamus, nome+'.mapamus', mapamus,'xb')
    print((caminhosmidiler.index(caminho)+1),' de ',len(caminhosmidiler))