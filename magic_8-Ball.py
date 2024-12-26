import random

answers = [
    "It is certain",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "Most likely",
    "Outlook good",
    "Reply hazy, try again",
    "Ask again later",
    "Cannot predict now",
    "Don't count on it",
    "My reply is no",
    "Very doubtful"
]

print("Welcome to the Magic 8 Ball!")

while True:
    question = input("\nAsk me a question (or 'quit' to exit): ")
    if question.lower() == 'quit':
        print("Goodbye!")
        break
    
    print("\nMagic 8 Ball says:", random.choice(answers))