import segmentacao as f_s

def analise1(caracteristicas):
    parametros = []
    parametros.append(
    ('segmentacao', f_s.segmentacao(caracteristicas, {'segmentosPar': [('intDia','p1p2'),('duracao','p1p2')], 'posicoesPar': [('Ncompasso','p1'),('Pcompasso','p1')]}))
    )
    return parametros