import os
import pandas as pd
from caminhosDosDiretorios import diretorioDeDadosDesteDispositivo as dirDados #de caminhosDosDiretorios, importamos a variavel string diretorioDeDadosDesteDispositivo que guarda o caminho do diretorio de dados deste dispositivo. -ABQ

# Create the directories if they don't exist
os.makedirs(dirDados+'dadosCrusMenos12', exist_ok=True)

#encaminhar os diretorios de dados brutos e processados -ABQ
dirDadosCrus = (dirDados+'dadosCrus/')
dirDadosMenos12 = (dirDados+'dadosCrusMenos12/')

#lista todos os arquivos do diretorio de dados brutos -ABQ
arquivosCrus = [arquivo for arquivo in os.listdir(dirDadosCrus) if arquivo.endswith('.txt')]

#processa cada arquivo -ABQ
for arquivoCru in arquivosCrus:
    #lê os dados do arquivo bruto pulando as 12 primeiras linhas -ABQ
    dados = pd.read_csv(os.path.join(dirDadosCrus, arquivoCru), skiprows=12, header=None, delim_whitespace=True)

    #novo caminho do arquivo processado -ABQ
    novoCaminhoDoArquivo = os.path.join(dirDadosMenos12, arquivoCru)

    #salva o arquivo processado no diretório dadosMenos12 -ABQ
    dados.to_csv(novoCaminhoDoArquivo, index=False, header=False, sep=' ')