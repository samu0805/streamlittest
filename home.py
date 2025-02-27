import streamlit as st
from gpt_wraper import gpt_wraper_message

# Titulo de la aplicacion
st.title("GPT Wrapper")

# Linea divisora
st.divider()

# Subtitulo
st.subheader("Interactua con LLMs")

# Imagen 
#st.image("bee.jpg")

prompt = st.text_input("Escribe tu mensaje")

if st.button("Enviar"):
    gpt_wrapper_message(prompt)
    st.success("Respuesta generada")
else:
    st.warning("Envia tu mensaje")
