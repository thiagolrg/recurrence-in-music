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
    parametrosanalise.append(
    ('posicoes_contidas', f_f.filtroposicoes_contidas(parametrosanalise,'retirar vazios'))  
    )
    parametrosanalise.append(
    ('posicoes_amontoadas', f_f.filtroposicoes_amontoadas(parametrosanalise, 'marcar segundo'))
    )
    return parametrosanalise

def analise2(caracteristicas):
    parametrosanalise = []
    parametrosanalise.append(
    ('segmentacao', f_s.segmentacao(caracteristicas, {'segmentosPar': [('intDia','p1p2'),('duracao','p1p2')], 'posicoesPar': [('Ncompasso','p1'),('Pcompasso','p1')]}))
    )
    parametrosanalise.append(
    ('posicoes_quantidade', f_f.filtroposicoes_quantidade(parametrosanalise,2))
    )
    parametrosanalise.append(
    ('posicoes_contidas', f_f.filtroposicoes_contidas(parametrosanalise,'retirar vazios'))  
    )
    parametrosanalise.append(
    ('posicoes_amontoadas', f_f.filtroposicoes_amontoadas(parametrosanalise, 'retirar vazios'))
    )
    return parametrosanalise