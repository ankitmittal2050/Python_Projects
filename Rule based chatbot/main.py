# Rule based Chatbot
import datetime as d
import time as t
name=input("Swagat hai! Enter your name: ")
presenthour=d.datetime.now().hour
if 5<=presenthour<=11:
    print("Good Morning! ",name)
elif 12<=presenthour<=17:
    print("Good Afternoon! ",name)
elif 18<=presenthour<=21:
    print("Good Evening! ",name)
else:
    print("Good Night! ",name)

print(f"Namaste! Welcome {name} to Your ChatBot Krishna")
print("You can ask me basic questions, Type Bye to exit")


# Chatbot Memory Creation [dictionary of response]
responses={
    'hello': 'Hi, Welcome! How can i help you?',
    'How are you': 'I am very fine. Thank You',
    'who are you': 'I am smart AI chatbot',
    'motivate me': 'Keep going. Every bug of your project makes you a better developer',
    'happy': 'Great to hear that',
    'what are functions': 'A function in Python is a named, reusable block of code that performs a specific task, takes optional inputs (parameters), and can return a value as an output'
}

#Method define
def getresponse(userquestion):
    userquestion=userquestion.lower()
    for i in responses:
        if i in userquestion:
            return responses[i]
    return "I have no idea! I am still learning"

#Take user input
while True:
    userinput=input("Please ask your question: ")
    if "bye" in userinput.lower():
        break
    else:
        reply=getresponse(userinput)
        print("Bot answer: ",reply)
   