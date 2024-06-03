global funcaoNormalizadora

def funcaoNormalizadora(vetorANormalizar):
    equacaoDeNormalizacao = (2*vetorANormalizar-((vetorANormalizar.max()+vetorANormalizar.min())))/(vetorANormalizar.max()-vetorANormalizar.min())
    return equacaoDeNormalizacao
