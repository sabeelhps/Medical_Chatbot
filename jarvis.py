import speech_recognition as sr
import pyttsx3 


engine=pyttsx3.init()
rate = engine.getProperty('rate')   
# print (rate)                       
engine.setProperty('rate',160)     
voices = engine.getProperty('voices')  
# print(len(voices))
engine.setProperty('voice', voices[17].id)

def takeVoiceCommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        # r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        query=r.recognize_google(audio,language="en-in")
        print("You : {}".format(query))
    
    except Exception as e:

        # print(e)

        # speak("Please say that again")
        
        return "None"

    return query


def speak(query):
    engine.say(query)
    engine.runAndWait()
    engine.stop()


    


