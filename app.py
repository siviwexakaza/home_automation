from gtts import gTTS
import speech_recognition as sr
import playsound
import os
import webbrowser
import random

def instruct(cmd):

    if 'hello' or 'hi' in cmd:
        speak('Hey there, you good?')
    
    if 'search' in cmd:
        
        search = listen('What would you like me to search for?')
        google = 'https://google.com/search?q='+ search
        webbrowser.get().open(google)
        speak('Here is what I found for '+search)





def speak(txt):
    gtts = gTTS(text=txt, lang='en')
    rndm = random.randint(1,10000000)
    mp3 = 'audio-'+str(rndm)+'.mp3'
    gtts.save(mp3)
    print(txt)
    playsound.playsound(mp3)
    #playsound.playsound('beep.mp3')
    os.remove(mp3)

def listen(txt = False):
    

    with sr.Microphone() as mic:

        r = sr.Recognizer()
        cmd=''

        if txt:
            speak(txt)

        r.pause_threshold =1
        r.adjust_for_ambient_noise(mic, duration=1)
        audio = r.listen(mic)

    try:
        cmd = r.recognize_google(audio)

    except sr.UnknownValueError:
        speak('Boss, I did not get that')
        instruct(listen())

    return cmd

speak('Hey boss, I am at your service')

while True:
    instruct(listen())