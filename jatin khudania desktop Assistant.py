''' Name: Jatin khudania
 Project:Desktop Assistant '''
import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):


    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
          speak("good night")

    speak("I am jarvis sir. Please tell me how  I may I help you ")


def takeCommand():
    ''' it take the microphone input from the  user and return srting output''' 
    r = sr.Recognizer() #It help to reconize the voice 
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")  

    except Exception as e:
        #print(e)   
        print("say that again Please...") 
        return "None" #this none is simple none not the python none we not put a string
    return query

if __name__ == "__main__":
    wishMe()
    while True: #if in case we not repeat this code then we use if statment: (if 1: ) it's mean that we apply only one time to cade run.  
        query = takeCommand().lower() #this lower meaning if we use Google to google (then they not give the issue)thats why we use lower() camand. 

        # Logic for excuting task based on query
        if 'wikipedia' in query:
            speak('searching wkipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'you tube' in query:
            webbrowser.open("you tubee")
        elif 'open google' in query:
            webbrowser.open("google.com")   
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif 'open code' in query:
            codePath = "a\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

# Any function we ctreate like speak then we introduce the 'def' string to import in pyhton 
'''Now after this last statment. if you add new statement or string,function 
than use this file contaning code and procced ''' 
#Thanku           


        





        

    