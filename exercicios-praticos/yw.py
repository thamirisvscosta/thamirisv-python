from pytube import YouTube
import moviepy.editor as mp
import os

# Insira o link do vídeo que você deseja baixar
link = "https://www.youtube.com/watch?v=EtJvPRRNCjI"

# Cria uma instância do objeto YouTube
yt = YouTube(link)

# Obtém a stream de áudio com a melhor qualidade
audio_stream = yt.streams.filter(only_audio=True).first()

# Baixa o arquivo de áudio em formato mp4
audio_file = audio_stream.download()

# Converte o arquivo de áudio mp4 para mp3
audio_clip = mp.AudioFileClip(audio_file)
audio_clip.write_audiofile(audio_file.replace(".mp4", ".mp3"))

# Remove o arquivo de áudio mp4
audio_clip.close()
os.remove(audio_file)
