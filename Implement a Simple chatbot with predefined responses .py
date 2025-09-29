#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def chatbot(): 
    print("Bot: Hi! I am a Simple Chatbot. Type 'bye' to exit.") 
    responses = { 
        'hi': 'Hello','hello': 'Hi there!', 
        'how are you?': 'I am doing great, hope you are fine.', 
        'what is your name?': 'I am Chatbot 2.0', 
        'bye': 'Goodbye! Have a nice day.' } 
 
    while True: 
        userinput = input("You: ").lower().strip() 
        if userinput == 'bye': 
            print(f"Bot: {responses['bye']}") 
            break 
        response = responses.get(userinput, "Sorry, I don't understand that.") 
        print(f"Bot: {response}") 
 
chatbot() 


# In[ ]:




