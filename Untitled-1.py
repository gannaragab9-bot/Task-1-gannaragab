def rule_based_chatbot():
    print("=========================================")
    print("Welcome")
    print("Ai chatbot started")
    print("Type 'exit' or 'quit' to end the chat")
    print("=========================================\n")
    
    while True:
        
        raw_input = input('You: ')
        clean_input = raw_input.lower().strip() 
        
        if clean_input == 'exit' or clean_input == 'quit':
            print("Chatbot: Goodbye! System chat closed.")
            break
            
        elif clean_input in ['hello', 'hi', 'hey', 'hello ']:
            print("Chatbot: Hello! How can I help you?")
            
        elif clean_input == 'what is your name':
            print("Chatbot: I am a Rule-based AI chatbot.")
                  
        elif clean_input == 'how are you':
            print("Chatbot: I am a deterministic logic engine, Operating at 100% efficiency. Thanks for asking!")
            
        elif clean_input in ['what is your purpose', 'purpose']:
            print("Chatbot: I act as a Rule-based guardrail to ensure precision and safety in communication.")
            
        else:
            print("Chatbot: I'm sorry, I don't understand, Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    rule_based_chatbot()