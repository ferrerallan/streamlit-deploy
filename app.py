import streamlit as st

st.title("Minha Primeira App Streamlit")
st.write("Olá, mundo!")

nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Olá, {nome}!")