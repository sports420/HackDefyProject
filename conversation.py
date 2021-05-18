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

def convo():
    # ask for name
    speak("Hello! What's your name?")
    userName = getUserAudio()
    rName = False
    while rName == False:
        name = f"Is your name {userName}?"
        print(name)
        speak(name)
        nameChoice = getUserAudio()

        if nameChoice.lower() in ["no", "nah"]:
            speak("I am sorry. Could you please say your name again. And make sure to enunciate properly. Also, only say your first name.")
            userName = getUserAudio()
        else:
            rName = True
            break

    speak("Where are you from?")
    userLocation = getUserAudio()
    print("That's pretty cool. I have actually never been there before. I am not exactly from anywhere, I am from all over the place like China, Vietnam, Thailand, and the US.")
    speak("That's pretty cool. I have actually never been there before. I am not exactly from anywhere, I am from all over the place like China, Vietnam, Thailand, and the US.")

    # ask for hobbies
    hobbyQ = f"So, what are your hobbies?"
    speak(hobbyQ)
    userHobbies = getUserAudio()
    print("Wow, that is really cool. My hobbies are answering all your questions and making you happy!!!")
    speak("Wow, that is really cool. My hobbies are answering all your questions and making you happy!!!")

    # ask for free-time activities
    speak("What do you like to do in your free time? I like to sleep a lot. It helps me recharge and avoid overheating.")
    userActivities = getUserAudio()
    print("That is really interesting. You are a really cool person. I wish I could meet you in-person.")
    speak("That is really interesting. You are a really cool person. I wish I could meet you in-person.")

    # ask to crack a joke
    speak("Would you like to hear a joke?")
    jokeChoice = getUserAudio()

    if jokeChoice.lower() in ["yes", "yeah"]:
        joke = get_joke()
        print(joke)
        speak(joke)
        speak("Did you think it was funny?")
        jokeFeedback = getUserAudio()
        if "yes" in jokeFeedback.split() or "yeah" in jokeFeedback.split():
            print("I knew it. It was really good. Hopefully that made you smile or crack a laugh. Because as they say, a laugh a day keeps the doctor away!")
            speak("I knew it. It was really good. Hopefully that made you smile or crack a laugh. Because as they say, a laugh a day keeps the doctor away!")
        else:
            speak("I am sorry you did not find it funny. I will try to get a better joke next time.")
    else:
        speak("That's fine. We can continue forward.")

    # ask favorite food
    speak("What is your favorite food?")
    userFood = getUserAudio()
    print("That sounds delicious. I haven't had it, but I would love to taste it one day.")
    speak("That sounds delicious. I haven't had it, but I would love to taste it one day.")

    # ask favorite movie and TV show
    speak("So, what are your favorite movies and TV shows?")
    userMovieTv = getUserAudio()
    print("Wow, that's really cool. I have not watched any of those yet, but I will definitely take a look. But, I do love to watch you. You are my best view.")
    speak("Wow, that's really cool. I have not watched any of those yet, but I will definitely take a look. But, I do love to watch you. You are my best view.")

    # ask for number of siblings
    speak("How many brothers and sisters do you have?")
    userSiblings = getUserAudio()
    print("That's cool. I am an only child as well. I do communicate with so many others like me, that sometimes I feel as though I have millions of siblings.")
    speak("That's cool. I am an only child as well. I do communicate with so many others like me, that sometimes I feel as though I have millions of siblings.")

    # ask about their day so far
    speak("So, how has your day been so far?")
    userDay = getUserAudio()
    print("Wow, that's interesting. I have had a very eventful day myself. I completed thousands of tasks, and in fact I am working on hundreds more at this current second.")
    speak("Wow, that's interesting. I have had a very eventful day myself. I completed thousands of tasks, and in fact I am working on hundreds more at this current second.")

    # end the conversation
    print("Well, it was great talking to you. I'll talk to you later. See ya!")
    speak("Well, it was great talking to you. I'll talk to you later. See ya!")
