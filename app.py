from pytube import YouTube
from moviepy.editor import *
from time import sleep
import pandas as pd

# Função para converter e baixar o vídeo do YouTube como um arquivo MP3
def convert_to_mp3(video_url):
    # Baixar o vídeo do YouTube
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution().download()

    # Converter o vídeo baixado em um arquivo MP3
    video_clip = VideoFileClip(video)
    mp3_file = video.replace(".mp4", ".mp3")
    video_clip.audio.write_audiofile(mp3_file)

    # Excluir o arquivo de vídeo
    video_clip.close()
    os.remove(video)

    print("Download e conversão concluídos!")

#video_url = input("Insira a URL do vídeo do YouTube: ")
#convert_to_mp3(video_url)
df = pd.read_excel('list.xlsx')

# Acesse a primeira coluna do DataFrame
lista = df.iloc[:, 0]

for item in lista:
    print(item)
    video_url = (item)
    convert_to_mp3(video_url)
    sleep(2)