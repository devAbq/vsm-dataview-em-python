global extrairPartesDoNome, extrair_angulo, nomeConcatenadoDaAmostra

def extrairPartesDoNome(nome_arquivo):
    partes = nome_arquivo.split('_')
    return partes


# Função para extrair o ângulo do nome do arquivo. Para aplicação da função é necessário que os arquivos .txt estejam nomeados seguindo o exemplo:Ta_CoFeB_Ag_x15_00.txt (ou Ta_CoFeB_Ag_x_05_000.txt, podendo ser ajustado -ABQ). Ou seja, com os últimos dígitos referenciando o ângulo de cada medida -CLEIZA
def extrair_angulo(nomeDoArquivoParticionado):
    angulo_str = extrairPartesDoNome(nomeDoArquivoParticionado)[-1].split('.')[0]
    return int(angulo_str)

def nomeConcatenadoDaAmostra(nomeDoArquivoParticionado):
    nomeParticionado = extrairPartesDoNome(nomeDoArquivoParticionado)
    nomeConcatenado = f"{nomeParticionado[0]}_({nomeParticionado[1]}_{nomeParticionado[2]}){nomeParticionado[3]}{nomeParticionado[4]}"
    return nomeConcatenado