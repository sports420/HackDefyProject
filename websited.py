from timeInfo import *
from playsound import *
from speech_recognition import *
from gtts import gTTS
from datetime import *
import pyttsx3
from subprocess import *
from webbrowser import *
from time import *

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

def getUserAudio():
   recognizeAudio = Recognizer()

   with Microphone() as source:
       userAudio = recognizeAudio.listen(source)
       userAudioText = ""

       try:
           userAudioText = recognizeAudio.recognize_google(userAudio)
       except Exception as e:
           speak("There was a problem in detecting your audio and printing it out to the console. Please try again.")

   return userAudioText

def getWebsiteInfo():
    speak("Which website would you like to open: ")
    speak("Please say 'open' and then the name of the website. For example, you can say open YouTube or open Amazon.")
    userChoice = getUserAudio()

    if userChoice.lower() == "open youtube":
        speak("What would you like to search up on YouTube?")
        userSearch = getUserAudio()
        openWebsite("YouTube", userSearch)
        speak("YouTube is open")
        sleep(7)

    elif userChoice.lower() == "open amazon":
        speak("What would you like to search up on Amazon?")
        userSearch = getUserAudio()
        openWebsite("Amazon", userSearch)
        speak("Amazon is open")
        sleep(7)

    elif userChoice.lower() == "open walmart":
        speak("What would you like to search up on Walmart?")
        userSearch = getUserAudio()
        openWebsite("Walmart", userSearch)
        speak("Walmart is open")
        sleep(7)

    elif userChoice.lower() == "open adidas":
        speak("What would you like to search up on Adidas?")
        userSearch = getUserAudio()
        openWebsite("Adidas", userSearch)
        speak("Adidas is open")
        sleep(7)

    elif userChoice.lower() == "open nike":
        speak("What would you like to search up on Nike?")
        userSearch = getUserAudio()
        openWebsite("Nike", userSearch)
        speak("Nike is open")
        sleep(7)

def openWebsite(website, search):
    finalSearch = ""
    if len(search.split()) > 1:
        for word in range(len(search.split()) - 1):
            finalSearch += search.split()[word]
            finalSearch += "+"
        finalSearch += search.split()[len(search.split()) - 1]
    else:
        finalSearch = search

    if website == "YouTube":
        url = "https://www.youtube.com/results?search_query=" + finalSearch
    elif website == "Amazon":
        url = "https://www.amazon.com/s?k=" + finalSearch + "&ref=nb_sb_noss"
    elif website == "Walmart":
        url = "https://www.walmart.com/search/?query=" + finalSearch
    elif website == "Adidas":
        url = "https://www.adidas.com/us/search?q=" + finalSearch
    elif website == "Nike":
        url = "https://www.nike.com/w?q=" + finalSearch

    open(url)
