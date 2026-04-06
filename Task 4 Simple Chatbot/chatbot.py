def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        
        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        
        elif "your name" in user_input:
            print("Chatbot: I am a simple chatbot created in Python.")

        
        elif "weather" in user_input:
            print("Chatbot: I can't check live weather yet, but it's always a good idea to carry an umbrella!")

        
        elif "study" in user_input or "exam" in user_input:
            print("Chatbot: Stay consistent and practice daily. You’ll do great!")

        
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: Current time is {current_time}")

        
        else:
            print("Chatbot: Sorry, I don't understand that. Can you ask something else?")


chatbot()
