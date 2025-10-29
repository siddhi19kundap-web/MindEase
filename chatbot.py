import json
import random

# Load intents
with open('intents.json', 'r') as f:
    data = json.load(f)

def get_response(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm here for you. Tell me more about how you're feeling 💬"

# Chat loop
print("🧠 MindMate: Hello! I’m here to listen and support you. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("🧠 MindMate: Take care of yourself 💖")
        break
    print("🧠 MindMate:", get_response(user_input))
