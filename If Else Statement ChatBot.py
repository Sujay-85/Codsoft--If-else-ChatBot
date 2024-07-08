# Simple chatbot using if-else statements
def chatbot_response(message):
    # Convert the message to lowercase to make it case insensitive
    message = message.lower ( )

    # Define some predefined patterns and responses
    if message in ['hi' , 'hello' , 'hey' , 'hola']:
        return "Hello there! How can I help you today?"
    elif 'weather' in message:
        return "The weather is nice today."
    elif 'chatgpt' in message:
        return ("I am ChatGPT, a conversational AI developed by OpenAI,\n"
                " based on the GPT-4 architecture. My primary function \n"
                "is to assist users by providing information, answering \n"
                "questions, and engaging in discussions on a wide range \n"
                "of topics.")

    elif 'dog' in message:
        return ("Dogs are domesticated mammals belonging to the species \n"
                "Canis lupus familiaris. They are known for their loyalty,\n "
                "companionship, and diverse roles in human society,\n "
                "including as pets, working animals, and service animals\n")

    elif 'bye' in message:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that. Could you please rephrase?"


# Main function to run the chatbot
def main():
    print ( "Welcome! Ask me something or just say hi." )

    while True:
        user_input = input ( "You: " )
        if user_input.lower ( ) == 'exit':
            print ( "Chatbot: Goodbye!" )
            break

        response = chatbot_response ( user_input )
        print ( "Chatbot:" , response )


if __name__ == "__main__":
    main ( )

