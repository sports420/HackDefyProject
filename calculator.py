from playsound import *
from speech_recognition import *
from gtts import gTTS
from datetime import *
from time import *
import pyttsx3
from pyjokes import *

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def getUserAudio():
   recognizeAudio = Recognizer()

   with Microphone() as source:
       userAudio = recognizeAudio.listen(source)
       userAudioText = ""

       userAudioText = recognizeAudio.recognize_google(userAudio)

   return userAudioText

def calculate():
    speak("What is your mathematical phrase?")
    userPhrase = getUserAudio()
    newUserPhrase1 = userPhrase.replace("raised to the power of", "**")
    newUserPhrase2 = newUserPhrase1.replace("to the power of", "**")
    newUserPhrase3 = newUserPhrase2.replace("raised to", "**")
    newUserPhrase4 = newUserPhrase3.replace("squared", "**2")
    newUserPhrase5 = newUserPhrase4.replace("cubed", "**3")
    newUserPhrase6 = newUserPhrase5.split()
    newUserPhrase7 = newUserPhrase6[-1]
    newUserPhrase8 = newUserPhrase7 + "**(1/2)"

    if "square root" in userPhrase:
        answer1 = f"{userPhrase} is equal to {eval(newUserPhrase8)}."
        print(answer1)
        speak(answer1)
    else:
        answer2 = f"{userPhrase} is equal to {eval(newUserPhrase5)}."
        print(answer2)
        speak(answer2)
