def bangladesh_chatbot():
    print("Welcome to the Bangladesh Chatbot!")
    print("I can provide information on various aspects of Bangladesh.")
    print("Feel free to ask me questions. Type 'exit' to end the conversation.")

    while True:
        question = input("Ask me a question: ").lower()

        if question == "exit":
            print("Goodbye! Have a great day.")
            break
        elif "capital" in question:
            print("The capital of Bangladesh is Dhaka.")
        elif "population" in question:
            print("The population of Bangladesh is approximately 165 million.")
        elif "currency" in question:
            print("The currency of Bangladesh is the Bangladeshi Taka.")
        elif "national animal" in question:
            print("The national animal of Bangladesh is the Royal Bengal Tiger.")
        elif "national flower" in question:
            print("The national flower of Bangladesh is the Shapla (water lily).")
        elif "largest university" in question:
            print("The largest university in Bangladesh is Dhaka University.")
        elif "born" in question:
            print("Bangladesh was born on December 16, 1971.")
        elif "victory" in question:
            print("Bangladesh achieved victory on December 16, 1971.")
        elif "liberation war" in question:
            print("The Bangladesh Liberation War started on March 26, 1971, and lasted until December 16, 1971.")
        else:
            print("Sorry, I don't know the answer to that question. Feel free to ask something else.")

bangladesh_chatbot()
