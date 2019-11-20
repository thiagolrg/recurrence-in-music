import segmentacao as f_s
import filtrosord as f_f

def analise1(caracteristicas):
    parametrosanalise = []
    parametrosanalise.append(
    ('segmentacao', f_s.segmentacao(caracteristicas, {'segmentosPar': [('intDia','p1p2'),('duracao','p1p2')], 'posicoesPar': [('Ncompasso','p1'),('Pcompasso','p1')]}))
    )
    parametrosanalise.append(
    ('posicoes_quantidade', f_f.filtroposicoes_quantidade(parametrosanalise,2))
    )
    return parametrosanalise