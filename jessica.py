import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import pyjokes
import wikipedia
import simple-webbrowser
import os
import cv2
import random
from requests import get
import sys
import wolframalpha
import json
from urllib.request import urlopen
import requests
from datetime import datetime
from playsound import playsound



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
        print('Good Morning!')

    elif hour >= 12 and hour <= 18:
        speak('Good Afternoon!')
        print('Good Afternoon!')

    else:
        speak('Good Evening!')
        print('Good Evening!')

    speak("I am Jessica Sir. Please tell me how may I help you")
    print("I am Jessica Sir. Please tell me how may I help you")



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:

        speak("sir, do you have any other work. ")
        return "None"
    return query



app = wolframalpha.Client("8VQ2PL-ULG26Y2KPT")



if _name_ == "_main_":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("Opening notepad")
            print('OPENING NOTEPAD.')

        #not working
        elif 'open valorant' in query:
            vpath = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(vpath)
            speak("Opening valorant")
            print('Opening valorant')

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                speak("Opening camera")
                print('Opening camera')

                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'play music' in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("playing music")
            print('playing music.')

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP address is {ip}")


        elif 'temperature' in query:
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)

        elif 'calculate' in query:
            print("what should i calculate?")
            speak("what should i calculate?")
            gh = takeCommand().lower()
            res = app.query(gh)
            print(next(res.results).text)
            speak(next(res.results).text)




        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'open google' in query:
            speak("Sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening google")


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that", "")
            remeberMsg = remeberMsg.replace("jarvis", "")
            speak("You Told me to remind you that :" + remeberMsg)
            remeber = open('data.txt', 'w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt', 'r')
            speak('You Tell Me That' + remeber.read())

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening facebook")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")
            speak("opening amazon")

        elif 'open gmail' in query:
            webbrowser.open("accounts.google.com")
            speak("opening gmail")

        elif 'create a file' in query:
            folder = query.replace('create a file', '')
            filename = input(speak('enter file name to be created '))

            if os.path.exists(filename):
                print("This file already exists ")
                speak("This file already exists ")
            else:
                f = None
                try:
                    f = open(filename, 'w')
                except Exception as e:
                    print('issue --> ', e)
                else:
                    print("your file is created")
                    speak("your file is created")
                finally:
                    if f is not None:
                        f.close()


        elif 'delete a file' in query:
            folder = query.replace('delete a file', '')
            filename = input(speak('enter filename to be deleted '))
            if os.path.exists(filename):
                os.remove(filename)
                print('Your file is deleted')
                speak('Your file is deleted')

            else:
                print('Such file does not exist')
                speak('Such file does not exist')



        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            speak('sorry, I have a headache')


        elif 'are you single ?' in query:
            speak('I am in a relationship with wifi')
            print('I am in a relationship with wifi')
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes)


        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day. ")
            print("Thanks for using me sir, have a good day. ")
            sys.exit()


        else:
            speak('Please say the command again.'