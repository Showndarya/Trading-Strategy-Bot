import random

def send_to_custom_model(user_input):
    # below is stub code. should be replaced with the model we create

    responses = [
        f"Hello, {user_input}!",
        f"Why did you say {user_input}?",
        f"I'm not sure about {user_input}.",
        f"Can you explain more about {user_input}?",
        f"{user_input} is interesting."
    ]
    return random.choice(responses)

def chatbot():
    print("Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = send_to_custom_model(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()