import streamlit as st
import json, random

# Load intents
with open('intents.json', 'r') as f:
    data = json.load(f)

def get_response(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm here for you. Tell me more about how you're feeling 💬"

# Streamlit UI
st.set_page_config(page_title="MindMate Chatbot", page_icon="🧠")
st.title("🧠 MindMate – Your Mental Health Chatbot")
st.write("Talk to MindMate whenever you feel low or need a boost 💙")

# Input field
user_input = st.text_input("You:", "")

if st.button("Send"):
    response = get_response(user_input)
    st.markdown(f"**MindMate:** {response}")
