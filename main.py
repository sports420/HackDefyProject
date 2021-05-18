from timeInfo import *
from playsound import *
from speech_recognition import *
from gtts import gTTS
from datetime import *
from time import *
import pyttsx3
from pyjokes import *
from webbrowser import *
from weather import getWeather
from stocks import stockAlert
from websites import speak, getWebsiteInfo
from timeInfo import getDateAndTime
from note import createNote
from joke import getJoke
from conversation import convo
from calculator import calculate

noteCommands = ["make a note", "create a note", "write a note"]
jokeCommands = ["tell me a joke", "say a joke", "make me laugh", "say something funny"]
weatherCommands = ["what is the weather", "what is the temperature", "how is it outside"]

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty('voice', 'english+f2')
    engine.say(text)
    engine.runAndWait()

def getCommands():
    print("\t\t\t\t````````````````````")
    print("\t\t\t\t` CURRENT COMMANDS `")
    print("\t\t\t\t````````````````````")

    print("\t\t\t1. Make/Open/Create a note")

    print("\n\t\t\t2. Open a website")
    print("\t\t\t\tOpen YouTube")
    print("\t\t\t\tOpen Amazon")
    print("\t\t\t\tOpen Walmart")
    print("\t\t\t\tOpen Nike")
    print("\t\t\t\tOpen Adidas")

    print("\n\t\t\t3.What is the time and date")
    print("\t\t\t\tWhat is the time")
    print("\t\t\t\tWhat is the date")

    print("\n\t\t\t4. What is the weather")

    print("\n\t\t\t5. Get me a stock price")

    print("\n\t\t\t6. Let's have a conversation")

    print("\n\t\t\t7. I have a math equation")

    print("\n\t\t\t8. Quit the program")

def getUserAudio():
   recognizeAudio = Recognizer()

   with Microphone() as source:
       userAudio = recognizeAudio.listen(source)
       userAudioText = ""

       try:
           userAudioText = recognizeAudio.recognize_google(userAudio)
       except Exception as e:
           speak("There was a problem in detecting your audio. Please try again.")

   return userAudioText

for i in range(50):
    print()

speak("Hello, and welcome to the best voice assistant you have ever used and you will ever need. To get a list of what I can do, simply say 'What can you do?' To exit the program, please say 'quit' or 'exit'")

while True:
    speak("What is your command?")
    userSpeech = getUserAudio()

    userWords = userSpeech.lower().split()

    if "exit" in userSpeech.lower() or "quit" in userSpeech.lower():
        print("Thank you for using me. Have a great rest of your day!!!")
        speak("Thank you for using me. Have a great rest of your day!!!")
        break

    elif "do" in userSpeech.lower() or "can you" in userSpeech.lower():
        speak("Some of the things I can do are create notes, open websites, get the weather, get stock prices, and more. Printed to the console are the commands I can currently take.")
        getCommands()
        sleep(8)
        needTime = True
        while needTime == True:
            speak("Do you need more time to view the commands?")
            userTimeChoice = getUserAudio()
            if userTimeChoice.lower() in ["yes", "yeah", "yea"]:
                speak("I will give you 10 more seconds")
                sleep(10)
            else:
                needTime = False
                break


    elif userSpeech.lower() in noteCommands:
        speak("What would you like me to write down?")
        noteText = getUserAudio()
        speak("What would you like to name your new note?")
        noteTitle = getUserAudio()
        createNote(str(noteText), str(noteTitle))
        speak("I have noted that down!")
        sleep(12)

    elif userSpeech.lower() in noteCommands or "joke" in userSpeech.lower().split():
        speak("Would you like a neutral joke, a tongue-twister, or any type of joke?")
        category = getUserAudio()
        joke = getJoke(category.lower())
        print(joke)
        speak(joke)
        sleep(20)

    elif userSpeech.lower() in weatherCommands or "weather" in userSpeech.lower() or "temperature" in userSpeech.lower():
        print("What city's weather would you like?")
        speak("What city's weather would you like?")
        weatherCity = getUserAudio()
        print("What is the acronym of the state which the city is in?")
        speak("What is the acronym of the state which the city is in?")
        weatherState = getUserAudio()
        weather = getWeather(weatherCity, weatherState)
        speak(weather)
        sleep(20)

    elif "stock" in userSpeech.lower() or "price" in userSpeech.lower():
        speak("What is the symbol of your stock?")
        stockSymb = getUserAudio()

        stock = stockAlert(stockSymb, "Apple")
        speak(stock)
        sleep(20)

    elif "open" in userSpeech.lower() and "website" in userSpeech.lower():
        getWebsiteInfo()
        sleep(20)

    elif "date" in userSpeech.lower() or "time" in userSpeech.lower():
        dateAndTime = getDateAndTime()

        if "date" in userSpeech.lower() and "time" in userSpeech.lower():
            date = "Today's date is " + dateAndTime[0]
            time = "The current time is " + dateAndTime[1]

            print(date)
            speak(date)

            print(time)
            speak(time)

            sleep(20)

        elif "date" in userSpeech.lower():
            date = "Today's date is " + dateAndTime[0]
            print(date)
            speak(date)

            sleep(20)

        else:
            time = "The current time is " + dateAndTime[1]

            print(time)
            speak(time)

            sleep(20)

    elif "conversation" in userSpeech.lower().split() or "talk" in userSpeech.lower().split():
        convo()
        sleep(15)

    elif "math" in userSpeech.lower() or "equation" :
        calculate()
        sleep(5)

    for i in range(5):
        print()

print("Process finished")
