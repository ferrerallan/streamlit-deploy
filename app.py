import streamlit as st
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

st.title("Minha App Streamlit com Chatbot")

# Tenta pegar a API key do .env ou dos secrets do Streamlit
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")

if api_key:
    client = OpenAI(api_key=api_key)
    
    st.header("🤖 Chatbot")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        try:
            with st.chat_message("assistant"):
                with st.spinner("Pensando..."):
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=st.session_state.messages,
                        max_tokens=150
                    )
                    assistant_response = response.choices[0].message.content
                    st.markdown(assistant_response)
            
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        except Exception as e:
            st.error(f"Erro: {str(e)}")
else:
    st.error("⚠️ API Key da OpenAI não encontrada. Configure a variável OPENAI_API_KEY.")