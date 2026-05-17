def college_chatbot():
    print("Welcome to College Chatbot!")
    print("You can ask about: 'about', 'fees', 'departments', or type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "about":
            print("Bot: Our college was established in 1990 and offers quality education in engineering and science.")
        elif user_input == "fees":
            print("Bot: The average annual fee is around 80,000 INR depending on the course.")
        elif user_input == "departments":
            print("Bot: We have Computer Science, Mechanical, Civil, Electronics, and IT departments.")
        elif user_input == "exit":
            print("Bot: Thank you for visiting. Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand. Please ask about 'about', 'fees', or 'departments'.")

# Run chatbot
college_chatbot()
