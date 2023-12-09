from openai import OpenAI
import config

client = OpenAI(api_key="")

def send_to_custom_model(user_input):
    response = client.chat.completions.create(model='ft:gpt-3.5-turbo-0613:boston-university::8Ttg35Ro',
    messages=[{"role": "user", "content": user_input}])
    
    print(response)

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