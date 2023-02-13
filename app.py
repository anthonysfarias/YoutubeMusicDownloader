from pytube import YouTube
import pandas as pd
import os

def baixarMusica(url, nome, grupo):
    url = url  # URL da música no YouTube
    nome_musica = nome  # Nome da música
    grupo = grupo  # Categoriza a musica em grupos

    # Cria um objeto YouTube a partir da URL
    yt = YouTube(url)

    # Seleciona a melhor resolução disponível
    melhor_resolucao = yt.streams.filter(
        progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Adiciona a extensão .mp4 ao novo nome
    nome_musica = f"{nome_musica}.mp4"

    # Verifica se a pasta existe // Se não existir, é criada
    if not os.path.exists(f"./music/{grupo}"):
        os.makedirs(f"./music/{grupo}")
    else:
        print(f"A pasta {grupo} já existe e não será criada.")

    # Baixa a música com o novo nome
    melhor_resolucao.download(filename=f"./music/{grupo}/{nome_musica}")

    print(f"A música foi baixada com sucesso como {nome_musica}!")


def lerExcel(data):
    baixarMusica(data.URL, data.Nome, data.Grupo)


# Le o dados da planilha excel
df = pd.read_excel("./doc/musicas.xlsx")

df.apply(lerExcel, axis=1)
