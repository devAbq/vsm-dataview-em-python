global funcaoNormalizadora, metadeDoVetor

def funcaoNormalizadora(vetorANormalizar):
    equacaoDeNormalizacao = (2*vetorANormalizar-((vetorANormalizar.max()+vetorANormalizar.min())))/(vetorANormalizar.max()-vetorANormalizar.min())
    return equacaoDeNormalizacao


def metadeDoVetor(vetorAlvo):
    return (len(vetorAlvo)//2)