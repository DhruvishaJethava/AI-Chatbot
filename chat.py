def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("🤖 Chatbot: Goodbye!")
            break

        elif "hello" in user or "hi" in user:
            print("🤖 Chatbot: Hi there!")

        elif "how are you" in user:
            print("🤖 Chatbot: I'm just code, but I'm doing great!")

        elif "your name" in user:
            print("🤖 Chatbot: I'm a Python chatbot.")

        else:
            print("🤖 Chatbot: Sorry, I don't understand.")

chatbot()