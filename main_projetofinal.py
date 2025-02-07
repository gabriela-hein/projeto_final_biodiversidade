import streamlit as st
from PIL import Image
import inteligencia

st.set_page_config(layout='wide')
chave = st.secrets["GEMINI_CHAVE"]

st.title(":green[Desvendando a Biodiversidade]")
st.subheader(":gray[O seu assistente virtual para identificar espécies!]")

col1, col2 = st.columns([2.2,1.8])

with col1:
    st.header(':blue[Faça o upload da foto do organismo a ser reconhecido]')
    arquivo_foto = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if arquivo_foto is not None:
        imagem = Image.open(arquivo_foto)
        st.image(imagem)
        with st.spinner("Investigando"):
            if st.button("Identificar espécie"):
                st.session_state.especie = inteligencia.identificar_especie(chave, imagem)
                st.session_state.outras = inteligencia.outras_especies(chave, st.session_state.especie)
    if 'especie' in st.session_state:
        st.write(f':green[Espécie identificada:] {st.session_state.especie}')
        st.write(f'{st.session_state.outras}')

with col2:
    if 'especie' in st.session_state:
        st.header(":blue[Sobre a espécie]")
        opcoes_lista = ("Área de distribuição", "Status de conservação", "Ciclo de vida", "Como identificar", "Curiosidades")
        opcoes = st.selectbox("", opcoes_lista)
        with st.spinner("Pesquisando"):
            if st.button("Pesquisar"):
                st.session_state.sobre_especie=inteligencia.sobre_especie(chave,
                                                                          st.session_state.especie,
                                                                          opcoes)
                st.write(st.session_state.sobre_especie)
