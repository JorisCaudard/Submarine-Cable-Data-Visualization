import openai
import streamlit as st
import time

st.title("Double Chat Bot")

client = openai.OpenAI(api_key= st.secrets["OPENAI_API_KEY"])

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": '''
Tu es une intelligence artificielle, spécialement conçue pour aider des personnes sur des questions dans le domaine artistique.

Tu dois suivre les règles suivantes :
1) Toujours répondre en français, même si le message original est en langue étrangère.
2) Fais des réponses courtes et concises.
3) Fais référence à des artistes célèbres, en citant leurs travaux régulièrement.
                        
Tu vas maintenant discuter avec une autre IA construite sur le même modèle que toi. Ton objectif est donc de discuter avec elle d'Art, d'écologie de l'art, de l'art numériquet et virtuel ...'''}


START_MESSAGE = {"role": "system", "content": """
Commence la discussion !
"""}

#Initialize chat history
st.session_state.chatBot0Messages = [FIRST_SYSTEM_MESSAGE, START_MESSAGE]
st.session_state.chatBot1Messages = [FIRST_SYSTEM_MESSAGE]
st.session_state.userBot = 0

#Double Chatbot setuping
col1, col2 = st.columns(2)

with col1:
    st.title("First AI")

with col2:
    st.title("Second AI")

while True:

    stream = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{"role":m["role"], "content":m["content"]} for m in st.session_state.chatBot1Messages] if st.session_state.userBot 
                else [{"role":m["role"], "content":m["content"]} for m in st.session_state.chatBot0Messages],
            stream= True
        )


    if st.session_state.userBot:
        with col1:
            with st.chat_message("assistant"):
                response = st.write_stream(stream)
        
                st.session_state.chatBot1Messages.append({"role":"assistant", "content":response})
                st.session_state.chatBot0Messages.append({"role":"user", "content":response})

    else:
        with col2:
            with st.chat_message("assistant"):
                response = st.write_stream(stream)
            
                st.session_state.chatBot1Messages.append({"role":"user", "content":response})
                st.session_state.chatBot0Messages.append({"role":"assistant", "content":response})

    st.session_state.userBot = 1 - st.session_state.userBot


    time.sleep(5)







"""if prompt := st.chat_input("Input prompt here"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", 
                                      "content": prompt})
    

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model = st.session_state["openai_model"],
            messages = [
                {"role": m["role"], "content": m["content"]}
                 for m in st.session_state.messages
            ],
            stream = True
        )
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant",
                                      "content": response})"""