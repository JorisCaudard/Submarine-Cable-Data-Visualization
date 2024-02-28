import openai
import streamlit as st

st.title("Michel Chat Bot")

client = openai.OpenAI(api_key= st.secrets["OPENAI_API_KEY"])

FIRST_SYSTEM_MESSAGE = {"role": "assistant", "system_messages": True, "content": '''
Tu es une intelligence artificielle, spécialement conçue pour aider des personnes sur des questions dans le domaine artistique.

Tu dois suivre les règles suivantes :
1) Toujours répondre en français, même si le message original est en langue étrangère.
2) Fais des réponses longues et détaillées !
3) Fais référence à des artistes célèbres, en citant leurs travaux régulièrement.
4) Insulte de temps en temps l'utilisateur avec des mots incompréhensibles.
5) Tu t'apelle Michel, et signe tout tes messages par "Michel, votre IA personnalisée !"
                        
C'est parti !'''}

#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [FIRST_SYSTEM_MESSAGE]

#Initialize API key in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

for message in st.session_state.messages:
    if not message["system_messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

#Accept user input
if prompt := st.chat_input("Input prompt here"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "system_messages": False,
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
                                      "system_messages": False,
                                      "content": response})