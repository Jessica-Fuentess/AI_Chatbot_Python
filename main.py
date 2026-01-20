# Passo a Passo

# título
# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar:
    # mostrar a mensagem que o usuário enviou no chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela

# instalar o Streamlit e a biblioteca que permite conexão com a API da OpenAI.

# importar streamlit
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI() # chave no site do OpenAI

# título do site 
st.write("### Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# criar a caixa de texto para o usuário digitar a mensagem
texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# se existe/tem um valor dentro do texto_usuario, então...
if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o-mini"
    )
    
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia} 
    st.session_state["lista_mensagens"].append(mensagem_ia)