import speech_recognition as siri
import pyttsx3
import pywhatkit

listener = siri.Recognizer()
engine = pyttsx3.init()
#voice = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)
#engine.say("Hello World")
#engine.runAndWait()

def speak(response):
    engine.say(response)
    engine.runAndWait()

try:
    with siri.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        #command = command.lower()
        #if 'alexa' in command:
            #speak(command)
        speak(command)
        if 'play' in command:
            song = command.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
except:
    pass
