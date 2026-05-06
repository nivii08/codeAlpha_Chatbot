def greet():
    print("\n--- Python Chatbot ---")
    print("Type 'bye' to exit.\n")
def get_response(user_input):
    if "internship" in user_input:
        return (
            "An internship is a valuable opportunity to gain practical experience, "
            "develop technical skills, and understand real-world work environments. "
            "It also helps in building your resume and improving career prospects."
        )
    if "bye" in user_input:
        return "Goodbye. Have a good day."
    responses = {
        "hello": "Hello. How can I assist you?",
        "hi": "Hi. How can I help you?",
        "how are you": "I am functioning normally. How can I assist you today?",
        "your name": "I am a simple Python-based chatbot.",
        "what can you do": "I can respond to basic queries and assist with simple conversations.",
        "thank you": "You're welcome.",
        "thanks": "You're welcome.",
        "college": "I hope your academic work is going well.",
        "project": "Working on projects is a great way to improve your skills."
    }
    for key in responses:
        if key in user_input:
            return responses[key]

    return "I'm sorry, I didn't understand that. Please try again."
def main():
    greet()

    while True:
        user_input = input("You: ").strip().lower()

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        response = get_response(user_input)
        print("Bot:", response)

        if "bye" in user_input:
            break


if __name__ == "__main__":
    main()