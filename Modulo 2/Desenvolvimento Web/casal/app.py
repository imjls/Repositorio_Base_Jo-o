import streamlit as st

# Configuração da página
st.set_page_config(page_title="💖 Nosso Cantinho 💖", page_icon="🌹", layout="centered")

# Estilo com CSS para deixar mais romântico
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #ffdde1, #ee9ca7);
            color: #4a0000;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #b30059;
        }
        .subtitle {
            font-size: 22px;
            text-align: center;
            color: #660033;
        }
        .heart {
            font-size: 60px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Conteúdo principal
st.markdown('<div class="title">💖 Para o Amor da Minha Vida 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Este cantinho é só nosso 🌹</div>', unsafe_allow_html=True)
st.markdown('<div class="heart">❤️ 💕 💖 💕 ❤️</div>', unsafe_allow_html=True)

# Música de fundo (link de MP3/YouTube embed)
st.markdown(
    """
    <audio controls autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mpeg">
        Seu navegador não suporta áudio.
    </audio>
    """,
    unsafe_allow_html=True
)
# Imagem romântica
st.image("foto.png", caption="Sempre juntos 💑", use_container_width=True)

# Botão com mensagem surpresa
if st.button("Clique para ver uma mensagem especial ✨"):
    st.success("Você é a melhor parte da minha vida. Obrigado por existir 💕")

video_file = open("meuvideo.mp4", "rb")
st.video(video_file.read())

# Caixa de texto para escrever uma mensagem personalizada
if st.button("Clique para ver outra mensagem especial ❤️"):
    st.success("Te amarei para sempre nao importa oque ocorrer!! 💕")

