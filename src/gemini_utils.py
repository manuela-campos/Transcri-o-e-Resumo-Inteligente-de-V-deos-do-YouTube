import os
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# 1. Extrai o ID do vídeo a partir da URL
def extract_video_id(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    elif query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query).get('v', [None])[0]
    return None

# 2. Obtém a transcrição do vídeo (se disponível)
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'pt-BR', 'en'])
        full_text = " ".join([item['text'] for item in transcript])
        return full_text
    except Exception as e:
        print(f"Erro ao obter transcrição: {e}")
        return None

# 3. Configura a API do Gemini (só carrega a chave por enquanto)
def configure_gemini():
    return os.getenv("GEMINI_API_KEY")

# 4. Gera um resumo a partir do texto usando Gemini (exemplo fictício — substitua pela API real)
def generate_summary(transcript_text):
    api_key = configure_gemini()
    if not api_key:
        raise ValueError("GEMINI_API_KEY não está configurada.")
    
    # Aqui você integraria com a API real do Gemini. Exemplo fictício:
    summary = f"[Resumo simulado] Texto tem {len(transcript_text)} caracteres."
    return summary
