import random

# Define a dictionary of ChatGPT-related questions and their answers
chatgpt_faqs = {
    "what is chatgpt?": "ChatGPT is a language model developed by OpenAI that is designed for natural language conversation. It can answer questions, generate text, and have interactive discussions with users.",
    "how does chatgpt work?": "ChatGPT is powered by a deep learning model called GPT (Generative Pre-trained Transformer). It's trained on a large corpus of text from the internet and uses that knowledge to generate human-like text based on input.",
    "what can i do with chatgpt?": "You can use ChatGPT for a variety of tasks, such as answering questions, generating text, creating content, providing recommendations, and much more.",
    "is chatgpt free to use?": "OpenAI offers both free and paid access to ChatGPT. There may be usage limitations on the free tier, and you can check OpenAI's pricing for more details.",
    "what is prompt engineering?": "Prompt engineering is the process of designing specific instructions or questions to obtain desired responses from a language model like ChatGPT. It involves crafting prompts to be clear and effective in conveying your intent.",
    # Add more FAQs as needed...
}

# Define some sample rules for the chatbot
rules = {
    "hello": ["Hello!, How can I help you today?" ],
    "how are you": ["I'm just a computer program, so I don't have feelings, but thanks for asking! How can I assist you?", "I'm here to help. What can I do for you?"],
    "bye": ["Goodbye!,Have a great day!"],
    "help": ["You can ask me questions or say hello. If you want to exit, just type 'bye'."],
}

def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()
    
    if user_input_lower in chatgpt_faqs:
        return chatgpt_faqs[user_input_lower]
    elif user_input_lower in rules:
        return random.choice(rules[user_input_lower])
    else:
        return "I'm not sure I understand. Can you please rephrase your question or greeting?"

# Additional rules for the chatbot
rules.update({
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"],
    "favorite color": ["I don't have a favorite color, but I think chatbots look great in all colors!", "My favorite color is the one you like the most!"],
    "weather": ["I don't have real-time weather information, but you can check your favorite weather website for the latest updates."],
    "recommend a book": ["Have you tried reading 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams? It's a classic!"],
    "coding tips": ["Remember to comment your code for better readability and maintainability.", "Always test your code thoroughly to catch bugs early."],
    "movie recommendation": ["If you're into sci-fi, I recommend watching 'Blade Runner 2049'. It's visually stunning!"],
    "favorite programming language": ["I'm not biased, but I think all programming languages are unique and have their strengths!"],
    "time": ["I don't have real-time clock functionality, but you can check the time on your device."],
    "tell me about yourself": ["I'm just a computer program designed to chat with users and provide information. How can I assist you today?"],
    "what's new": ["I don't have real-time updates, but you can check the latest news on your preferred news website."],
    "sing a song": ["I'm afraid I don't have a singing voice, but I can help you with information or answer questions!"],
    "technology trends": ["Artificial intelligence, blockchain, and augmented reality are some exciting technology trends to watch."],
    "math problem": ["Sure, I can help with math problems. What specific problem are you working on?"],
    "fun fact": ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"],
    "favorite game": ["I don't play games, but I can certainly help you find information or answer questions about your favorite games!"],
    "coding challenges": ["If you're looking for coding challenges, websites like LeetCode and HackerRank offer a variety of problems to solve."],
    "tell me a story": ["Once upon a time in the digital realm, there was a chatbot named ChatGPT, always ready to assist and engage in conversations."]
})

# Enhanced chatbot response function
def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()
    
    if user_input_lower in chatgpt_faqs:
        return chatgpt_faqs[user_input_lower]
    elif user_input_lower in rules:
        return random.choice(rules[user_input_lower])
    else:
        return "I'm not sure I understand. Can you please rephrase your question or greeting?"

# Main chat loop
print("Jarvis: Hi! I'm your friendly chatbot named Jarvis. You can start a conversation with me or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Jarvis: Goodbye!,Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Jarvis:", response)
