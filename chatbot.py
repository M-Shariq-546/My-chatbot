import random

#Function to load data
def load_data():
    load_data = 'custome_responses.txt'
    loadX = load_data.lstrip()
    return loadX

# Function to train the model 
def train_data():
    train_data = 'custome_responses.txt'
    trainX = train_data.encode()
    return trainX

# Function to read greetings from 'greetings.txt'
def read_greetings():
    with open('greetings.txt', 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# Function to read custom responses from 'custom_responses.txt'
def read_custom_responses():
    with open('custom_responses.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        return dict(line.split(',', 1) for line in lines)

# Custom greetings and responses
greetings = read_greetings()
custom_responses = read_custom_responses()

# Function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()

    # Check for custom greetings
    for greeting in greetings:
        if greeting in user_input:
            return random.choice(greetings)

    # Check for custom responses
    for question, response in custom_responses.items():
        if question in user_input:
            return response

    # If no custom response, provide a default answer
    return "I'm sorry, I didn't quite understand. Can you please clarify?"

# Interact with the chatbot
print("ChatBot: Hi there! How can I assist you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye!")
        break

    response = get_response(user_input)
    print("ChatBot:", response)
