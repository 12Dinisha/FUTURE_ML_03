import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Customer Support Chatbot", layout="centered")

st.title("🤖 Customer Support Chatbot")
st.write("Ask me about orders, billing, refunds, or general support.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response["choices"][0]["message"]["content"]
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

