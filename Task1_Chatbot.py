print("Hello! I'm a simple chatbot.")
while True:
    user_input = input("You: ").lower()

    if "hello" in user_input:
        print("Bot: Hi there!")
    elif "how are you" in user_input:
        print("Bot: I'm doing great, thanks for asking!")
    elif "who made you" in user_input:
        print("Bot: I was created by Nigar Fathima as part of a CodSoft internship project!")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
