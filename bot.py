import pyttsx3
import datetime
import wikipedia
import pyaudio
#below library is to give command
import speech_recognition as sr
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#it has two voices male and female
# print(voices)
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am a bot. Please tell how i can help you")

'''It takes microphone input from user and returns string
output'''


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        #seconds of non speaking audio before a phase is
        #considered complete if i take above gap it does
        #not complete
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    #if not able to recognize will go inside there
    except Exception as e:
        print(e)

        print("Say that again please")
        #if a problem return none string
        return "None"

    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail.com','pwd')
    server.sendmail('yourmail', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Bro, the time is {strTime}")

        elif 'email to ritik' in query:
            try:
                speak('what should i say')
                content = takeCommand()
                to = "hritikgaur44@gmail.com"
                sendEmail(to, content)
                speak("Email is end")

            except Exception as e:
                print(e)
                speak("sorry sir. Not able to send email")


    #Logic for executing tasks based on query
