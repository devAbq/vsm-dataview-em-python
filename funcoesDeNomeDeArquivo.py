global extrairPartesDoNome, extrair_angulo, nomeConcatenadoDaAmostra

def extrairPartesDoNome(nome_arquivo):
    partes = nome_arquivo.split('_')
    return partes

def extrair_angulo(nomeDoArquivoParticionado):
    angulo_str = extrairPartesDoNome(nomeDoArquivoParticionado)[-1].split('.')[0]
    return angulo_str

def nomeConcatenadoDaAmostra(nomeDoArquivoParticionado):
    nomeParticionado = extrairPartesDoNome(nomeDoArquivoParticionado)
    nomeConcatenado = f"{nomeParticionado[0]}_({nomeParticionado[1]}_{nomeParticionado[2]}){nomeParticionado[3]}{nomeParticionado[4]}"
    return nomeConcatenado