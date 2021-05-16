from typing import Set
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. please tell how may i help you")
def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print("Recognizing.....") 
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('siddharthjha20k@gmail.com', 'no-paasword')
    server.sendmail('krshalini1704@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
     wishme()
     while True:
         query = takeCommand().lower()

        #  logic for executing tasks based on query
         if 'wikipedia' in query:
            speak("searching wikipedia....")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("according to wikipedia")
            speak(results)
            
         elif 'open youtube' in query:
          webbrowser.open_new("youtube.com")

         elif 'open google' in query:
          webbrowser.open_new("google.com")

         elif 'open stackoverflow' in query:
          webbrowser.open_new("stackoverflow.com")
         
         elif 'play music' in query:
             music_dir = 'C:\\musics\\favouritesongs'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[1 ]))


         elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        
         elif 'open code' in query:
            codepath = "C:\\Users\\91620\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


         elif 'open steam' in query:
            codepath2 = "C:\Program Files (x86)\Steam\steam.exe"
            os.startfile(codepath2)
        
         elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = 'krshalini1704@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry siddarth iam not able to send the email")




        
            


     
         
        
        
        

        
