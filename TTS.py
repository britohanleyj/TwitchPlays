import pyttsx3 # GitHUb -> https://github.com/nateshmbhat/pyttsx3
import random


def Rand_Speak(msg):   #random voice says message
    engine = pyttsx3.init()
    voices= engine.getProperty('voices')
    int = random.randint(0,len(engine.getProperty('voices')))
    engine.setProperty('voice', voices[int].id)
    engine.say(msg) 
    engine.runAndWait()
    engine.stop 

## !DEPENDENT ON YOUR SYSTEM! ##
# def David(msg):        #Voice david will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Zira(msg):         #Voice Zira will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[11].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Hazel(msg):        #Voice Hazel will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[9].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Mark(msg):         #Voice Mark will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[8].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Ravi(msg):         #Voice Ravi will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[7].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Heera(msg):        #Voice Heera will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[6].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Sean(msg):         #Voice Sean will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[5].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Susan(msg):        #Voice Susan will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[4].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def George(msg):       #Voice George will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[3].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Richard(msg):      #Voice Richard will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[2].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def Linda(msg):        #Voice Linda will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


# def James(msg):        #Voice James will speak
#     engine = pyttsx3.init()
#     voices= engine.getProperty('voices')
#     engine.setProperty('voice', voices[10].id)
#     engine.say(msg) 
#     engine.runAndWait()
#     engine.stop 


