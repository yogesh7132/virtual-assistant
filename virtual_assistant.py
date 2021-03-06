import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
# print(voices[1].id
engine.setProperty("voices", voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am scoopy sir, Please tell me how can i help you")


def input():
    """
    This function takes microphone input from the user and return string output
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please ...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    password=open("pwd.txt","r").read()
    server.login("testscoop4321@gmail.com", password)
    server.sendmail("testscoop4321@gmail.com", to,content)
    server.close()

if __name__ == "__main__":
    greet()
    # input()

    while True:
        query = input().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = r'D:\Songs\Pendrive\Eng'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            code_path = r"C:\Users\yogesh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)

        elif "send email" in query:
            try:
                speak("What should i say?")
                content = input()
                to = "testscoop4321@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, not able to sent email at this moment")

        elif "goodbye" in query:
            speak("Goodbye sir, have a nice day")
            break