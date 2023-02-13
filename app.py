import pandas as pd
from pytube import YouTube
from pathlib import Path

def download_music(url, name, group):
    """
    Baixa música a partir da URL do YouTube e salva com o nome e grupo especificados.
    """
    youtube = YouTube(url)
    best_resolution = youtube.streams.filter(
        progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    music_path = Path("./music") / group / f"{name}.mp4"
    music_path.parent.mkdir(parents=True, exist_ok=True)
    best_resolution.download(filename=str(music_path))
    print(f"A música foi baixada com sucesso como {name}.mp4 em {group}")

def read_excel(data):
    """
    Lê dados do arquivo excel e chama a função de download de música para cada linha.
    """
    try:
        download_music(data.URL, data.Nome, data.Grupo)
    except Exception as e:
        print(f"Erro ao baixar música {data.Nome}: {e}")

def main():
    try:
        music_data = pd.read_excel("./doc/musicas.xlsx")
        music_data.apply(read_excel, axis=1)
    except FileNotFoundError as e:
        print(f"Erro ao ler arquivo excel: {e}")
main()