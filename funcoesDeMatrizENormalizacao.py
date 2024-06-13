global funcaoNormalizadora, metadeDoVetor, coeficienteAngular, valorAbs

import numpy as np

def funcaoNormalizadora(vetorANormalizar):
    equacaoDeNormalizacao = (2*vetorANormalizar-((vetorANormalizar.max()+vetorANormalizar.min())))/(vetorANormalizar.max()-vetorANormalizar.min())
    return equacaoDeNormalizacao


def metadeDoVetor(vetorAlvo):
    return (len(vetorAlvo)//2)

def coeficienteAngular(abscissas, ordenadas):
    acharCoeficienteAngular = np.polyfit(abscissas, ordenadas, 1)[0]
    return float(acharCoeficienteAngular)
