import streamlit as st
import gemini_utils
from googletrans import Translator

# Configura a página
st.set_page_config(page_title="🎙️ Transcrição + Tradução YouTube", layout="centered")

# Estilo visual - Tema Escuro Personalizado
st.markdown("""
    <style>
    html, body {
        background-color: #1e1e2f;
    }
    .title {
        font-size: 40px;
        color: #f1c40f;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #bdc3c7;
        margin-bottom: 30px;
    }
    .section {
        background-color: #2c3e50;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.3);
        margin-top: 30px;
    }
    .text-box {
        background-color: #34495e;
        padding: 25px;
        border-radius: 15px;
        text-align: justify;
        line-height: 1.7;
        font-size: 16px;
        color: #ecf0f1;
        white-space: pre-wrap;
        word-wrap: break-word;
        margin-bottom: 30px;
    }
    .stTextInput > div > div > input {
        background-color: #1e1e2f;
        color: #ecf0f1;
        border: 2px solid #f1c40f;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton > button {
        background: linear-gradient(to right, #f39c12, #e67e22);
        color: white;
        border-radius: 10px;
        padding: 10px 25px;
        font-size: 16px;
        margin-top: 20px;
        transition: background 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(to right, #e67e22, #d35400);
    }
    .footer {
        text-align: center;
        margin-top: 60px;
        color: #7f8c8d;
        font-size: 14px;
    }
    .social-icons a {
        color: #f1c40f;
        text-decoration: none;
        margin: 0 10px;
        font-size: 18px;
    }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Título e subtítulo
st.markdown('<div class="title">🖥️ Transcrição + Tradução de Vídeos</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Cole a URL de um vídeo do YouTube e veja a mágica acontecer ✨</div>', unsafe_allow_html=True)

# Função para formatar texto
def format_text_as_stanzas(text, stanza_length=3):
    sentences = text.split('. ')
    stanzas = [sentences[i:i + stanza_length] for i in range(0, len(sentences), stanza_length)]
    formatted = '\n\n'.join(['. '.join(stanza).strip() + '.' for stanza in stanzas if stanza])
    return formatted

# Função de tradução
def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text

# App principal
def main():
    with st.container():
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📼 Passo 1: Cole o Link do Vídeo 🎥")

        video_url = st.text_input("🔗 Exemplo: https://www.youtube.com/watch?v=abcd1234")

        if video_url:
            try:
                video_id = gemini_utils.extract_video_id(video_url)
                transcript = gemini_utils.get_transcript(video_id)

                if transcript:
                    st.markdown("### 📝 Transcrição Original")
                    formatted = format_text_as_stanzas(transcript)
                    st.markdown(f'<div class="text-box">{formatted}</div>', unsafe_allow_html=True)

                    if st.button("🌐 Traduzir para Inglês 🇺🇸"):
                        translated = translate_to_english(transcript)
                        formatted_translated = format_text_as_stanzas(translated)
                        st.markdown("### 🇺🇸 Tradução para Inglês")
                        st.markdown(f'<div class="text-box">{formatted_translated}</div>', unsafe_allow_html=True)
                else:
                    st.error("❌ Não foi possível obter a transcrição.")
            except Exception as e:
                st.error(f"⚠️ Ocorreu um erro: {e}")

        st.markdown('</div>', unsafe_allow_html=True)

    # Rodapé estilizado com ícones de redes sociais
    st.markdown("""
        <div class="footer">
            Desenvolvido com ❤️ por Você | Conecte-se:
            <div class="social-icons">
                <a href="https://github.com" target="_blank">🐱 GitHub</a>
                <a href="https://linkedin.com" target="_blank">💼 LinkedIn</a>
                <a href="https://twitter.com" target="_blank">🐦 Twitter</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
