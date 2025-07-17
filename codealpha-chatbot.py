def respond(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I don't understand, but I'm learning!"

# --- Main Chat Loop ---
print("🤖 Chatbot ready! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower():
        break
