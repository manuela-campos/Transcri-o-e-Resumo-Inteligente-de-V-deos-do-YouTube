from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

# Exemplo de vídeo com transcrição pública (TED Talk)
video_url = 'https://www.youtube.com/watch?v=5MgBikgcWnY'

def get_video_title(video_url):
    """Extrai o título de um vídeo do YouTube."""
    try:
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Erro ao obter o título do vídeo: {e}")
        return None

def extract_video_id(url):
    """Extrai o ID do vídeo da URL do YouTube."""
    try:
        yt = YouTube(url)
        return yt.video_id
    except Exception as e:
        print(f"Erro ao extrair o ID do vídeo: {e}")
        return None

def get_transcript(video_id):
    """Obtém a transcrição do vídeo, se disponível publicamente."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'pt-BR', 'en'])
        text = ' '.join([entry['text'] for entry in transcript])
        return text
    except TranscriptsDisabled:
        print("❌ Transcrições estão desativadas para este vídeo.")
    except NoTranscriptFound:
        print("❌ Nenhuma transcrição disponível para este vídeo.")
    except VideoUnavailable:
        print("❌ O vídeo não está disponível.")
    except Exception as e:
        print(f"⚠️ Erro inesperado ao obter transcrição: {e}")
    return None

# Uso das funções
title = get_video_title(video_url)
print(f"Título do vídeo: {title}")

video_id = extract_video_id(video_url)
print(f"ID do vídeo: {video_id}")

transcript = get_transcript(video_id)
if transcript:
    print(f"\n📝 Transcrição:\n{transcript[:500]}...")  # mostra os primeiros 500 caracteres
else:
    print("⚠️ Nenhuma transcrição foi encontrada.")
