import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import webbrowser
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning bhai!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon bhaiii!")
    else:
        speak("Good Evening bhhai!")
        

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query 



if __name__ == "__main__":
    wishMe()
    speak("myself jarvis how may i help you")
    while True:
       query= takeCommand().lower()
       if "wikipedia" in query:
           speak("searching wikipedia")
           query=query.replace("wikipedia"," ")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           speak(results)
       elif "open youtube" in query:
           webbrowser.open("youtube.com")
       elif "the time" in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is{strTime}")
       elif "google" in query:
           webbrowser.open("google.com")
       else:
           speak("i didn't get you")
           break
 