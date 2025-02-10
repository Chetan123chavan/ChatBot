import streamlit as st
from chatbot import Chatbot

# Set up Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("💬 AI Chatbot")

# Initialize Chatbot
bot = Chatbot()

# File Upload
uploaded_file = st.file_uploader("📂 Upload a file (PDF, TXT, CSV)", type=["pdf", "txt", "csv"])
if uploaded_file:
    bot.process_file(uploaded_file)

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
user_input = st.chat_input("Ask me anything...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = bot.get_response(user_input)
    st.session_state.chat_history.append({"role": "bot", "content": response})
    st.experimental_rerun()
