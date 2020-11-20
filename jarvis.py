import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir !")
        speak("Good Morning Sir !")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir !")
        speak("Good Afternoon Sir !")   

    else:
        print("Good Evening Sir !") 
        speak("Good Evening Sir !")  

    speak("I am Jarvis, Your Assistent. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        
        quit=['quit','thank you','stop']
        str=['wikipedia','who']
        for ch in quit:
            if ch in query:
                print("Quitting.... please wait...")
                speak("Quitting, please wait...")
                os.exit()
        for ch in str:
                if ch in query:
                    print('Searching Wikipedia.....')
                    speak('Searching Wikipedia.....')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)


        if 'what can' in query:
            print('I can search everything from Wikipedia')
            speak('I can search everything from Wikipedia')
            print('I can open some websites like as:\n\t\tgoogle.com,\tfacebook.com,\tyoutube.com,\tstackoverflow.com,\tsarkariresult.com')
            speak('I can open some websites,like as google.com, facebook.com, youtube.com, stackoverflow.com,sarkari result.com')
            print('I can play music')
            speak('I can play music')
            print('I can tell you the current time')
            speak('I can tell you the current time')
            print('I can open some applications like as\n \t\t\t vs code,\t google chrome,\teclipse ide,\tedit plus')
            speak('I can open some applications installed on this system like as vs code, google chrome,eclipse ide,edit plus')

        elif 'open youtube' in query:
            print("Opening.... youtube")
            speak("Opening youtube")
            webbrowser.open("youtube.com")
            os.exit()

        elif 'open google' in query:
            print("Opening.... Google")
            speak("Opening Google")
            webbrowser.open("google.com")
            os.exit()

        elif 'open stackoverflow' in query:
            print("Opening.... stackoverflow")
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com") 
            os.exit()

        elif 'open facebook' in query:
            print("Opening.... facebook")
            speak("Opening facebook")
            webbrowser.open("facebook.com")   
            os.exit()

        elif 'open sarkari' in query:
            print("Opening..... sarkariresult.com")
            speak("Opening sarkariresult.com")
            webbrowser.open("sarkariresult.com") 
            os.exit()

        elif 'play music'  in query:
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            print("Playing songs, please wait.....")
            speak("Playing songs")
            #print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            Path = "C:\\Users\\hp\\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("Opening.... VS Code")
            speak("Opening VSCode")
            os.startfile(Path) 
            os.exit()

        elif 'open chrome' in query:
            Path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            print("Opening.... Google Chrome")
            speak(" Opening Google Chrome")
            os.startfile(Path) 
            os.exit()

        elif 'open eclipse' in query:
            Path = "C:\\Users\\hp\\eclipse\\java-2018-09\\eclipse\\eclipse.exe"
            print("Opening... Eclipse ide")
            speak("Opening Eclipse ide")
            os.startfile(Path) 
            os.exit()

        elif 'open editplus' in query:
            Path = "C:\\Program Files\\EditPlus\\editplus.exe"
            print("Opening... Edit Plus")
            speak("Opening Edit Plus")
            os.startfile(Path)  
            os.exit()

        else:
          print("Sorry I can't tell you about this, please ask me something else")
          speak("Sorry I can't tell you about this, please ask me something else")   
