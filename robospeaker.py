import pyttsx3
def robospeak():
    engine = pyttsx3.init()
    while True:
        text=input("what do you want to say") 
        if text.lower()=="exit":
            print("Good bye")
            engine.say("Good bye")
            engine.runAndWait()
            break
        engine.say(text)
        engine.runAndWait()
if __name__=="__main__":
    robospeak()
