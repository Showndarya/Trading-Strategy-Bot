import openai
import config
import time

openai.api_key = config.openai_key
# client = OpenAI(api_key=config.openai_key)
durations = []
answers = []
prompts = []
lengths = []

def get_test_questions():
    with open('../test_questions.txt', 'r') as file:
        for line in file:
            line = line.split(' ', maxsplit=1)[1]
            prompts.append(line.strip())

def send_to_custom_model(user_input):
    response = openai.ChatCompletion.create(model='ft:gpt-3.5-turbo-0613:boston-university::8SrghL6F',
    messages=[{"role": "user", "content": user_input}])
    #print(response)
    return response.choices[0].message.content

def chatbot():
    print("Hello! Welcome, you can call me Tradot and I am here to help you with everything Trading!")

    print("Reading prompts...")
    get_test_questions()
    print("Prompts ready, Tradot chat starting")

    for prompt in prompts:
        start_time = time.time()
        response = send_to_custom_model(prompt)
        end_time = time.time()
        duration = end_time - start_time

        durations.append(duration)
        answers.append(response)
        lengths.append(len(response))

    print("Tradot chat done, processing data...")
    avg_duration = round(sum(durations)/len(durations), 2)
    avg_length = round(sum(lengths)/len(lengths), 2)
    print("Data processing done, writing results to file")
    
    with open('test_results/responses.txt', 'w') as response_file:
        for i, answer in enumerate(answers, start=1):
            response_file.write(f"{i}. {answer}\n\n")

    with open('test_results/response_times.txt', 'w') as response_time_file:
        for i, duration in enumerate(durations, start=1):
            response_time_file.write(f"{i}. {duration}\n")

        response_time_file.write(f"\nAverage response time: {avg_duration}")

    with open('test_results/response_lengths.txt', 'w') as response_lengths_file:
        for i, length in enumerate(lengths, start=1):
            response_lengths_file.write(f"{i}. {length}\n")

        response_lengths_file.write(f"\nAverage response length: {avg_length}")

if __name__ == "__main__":
    chatbot()