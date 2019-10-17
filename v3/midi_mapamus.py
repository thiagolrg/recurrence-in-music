import os
import diretorios as di
import limpa_extrai as le
import mapa_bpm as mb
import mapa_complocdur as mcld
import mapa_mus as mm

#1 diretórios
dimidi = di.diretorio('ler','.mid')
caminhosmidiler = di.caminhos_arquivo(dimidi, '.mid')
dimapamus = di.diretorio('gravar', '.mapamus')+'\\'+'mapamus'
os.makedirs(dimapamus, exist_ok=True)

for caminho in caminhosmidiler:
    #2 limpa extrai
    nome = di.nome_arquivo(caminho,'.mid')
    entrada = le.midi_csv(caminho)
    entradalimpa = le.limpa(entrada)
    tom, modo, ppq, compassos, tempos, notas = le.extrai(entradalimpa)

    #3 mapabpm
    mapabpm = mb.mapa_bpm(tempos,compassos)

    #4 mapacomplocdur
    mapacomplocdur = mcld.mapa_complocdur(compassos,ppq)

    #5 mapamus
    mapamus = mm.mapa_mus(notas, mapacomplocdur, mapabpm, ppq)
    mapamus.setdefault('nome', nome)
    mapamus.setdefault('tom', tom)
    mapamus.setdefault('modo', modo)
    
    #6 salva o resultado
    di.escreve_arquivo(dimapamus, nome+'.mapamus', mapamus,'xb')
    print((caminhosmidiler.index(caminho)+1),' de ',len(caminhosmidiler))