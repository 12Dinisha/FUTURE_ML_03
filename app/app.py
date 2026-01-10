import streamlit as st
import openai
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env from project root
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    st.error("❌ OpenAI API key not loaded")
    st.stop()

st.set_page_config(page_title="Customer Support Chatbot", layout="centered")

st.title("🤖 Customer Support Chatbot")
st.write("Ask me about orders, billing, refunds, or general support.")

if "messages" not in st.session_state:
    st.session_state.messages = []

def chatbot_reply(user_input):
    text = user_input.lower()

    if "refund" in text:
        return "Sure 🙂 Please share your order ID and reason for refund."
    elif "order" in text or "track" in text:
        return "📦 You can track your order from the 'My Orders' section."
    elif "billing" in text or "payment" in text:
        return "💳 For billing issues, please contact billing@company.com."
    elif "cancel" in text:
        return "❌ To cancel an order, go to Orders → Cancel Order."
    elif "hello" in text or "hi" in text:
        return "Hello! 👋 How can I help you today?"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = chatbot_reply(user_input)
    st.chat_message("assistant").write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
