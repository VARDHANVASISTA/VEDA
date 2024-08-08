import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5') # 'sapi5' is the microsoft's speech API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)# voices[0].id is for male voice which is of person named DAVID and voices[1].id is for female voice which is of a person named ZIRA

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    speak("...VEDA activated...")
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("VEDA at your service sir...")
    speak("Please tell me, how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # pause_threshold >> seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("Verifying your command sir...")
        print("You said: ", query, "\n")
    except Exception as e:
        print(e)
        speak("Say that again please sir...")
        print("Say that again please sir...")
        return "None"
    return query

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    'For this function to work, you must enable "Less Secure Apps" for the account that you will use below.'
    server.login("your-mail-id@gmail.com", "enter your password")
    server.sendmail("your-mail-id@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    greetMe()
    while True:
        cmd = takeCommand()
        speak("Verifying your command sir...")
        vc = "You said: " + cmd
        speak(vc)
        cmd = cmd.lower()
        if "wikipedia" in cmd:
            speak("Searching Wikipedia...")
            cmd = cmd.replace("wikipedia", "")
            output = wikipedia.summary(cmd, sentences = 2) # sentences = 2 tells to get a two line summary, this can be altered to get desired number of lines as summary
            speak("Here is a two line summary for your search on wikipedia...")
            speak_output = "According to wikipedia, " + output
            print(speak_output)
            speak(speak_output)
        elif "time now" in cmd:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The current time is...{t}")
            speak(f"The current time is...{t}")
        elif "open youtube" in cmd:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")
        elif "open google" in cmd:
            speak("Opening google...")
            webbrowser.open("googlr.com")
        elif "open github" in cmd:
            speak("Opening github...")
            webbrowser.open("github.com")
        elif "open linkedin" in cmd:
            speak("Opening linkedin...")
            webbrowser.open("linkedin.com")
        elif "open leetcode" in cmd:
            speak("Opening leetcode...")
            webbrowser.open("leetcode.com")
        elif "open stackoverflow" in cmd:
            speak("Opening stackoverflow...")
            webbrowser.open("stackoverflow.com")
        elif "play music" in cmd:
            dp = "E:\\SONGS\\VoiAsFol"
            songs = os.listdir(dp)
            print(songs)
            speak("Playing music...")
            random_song = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(dp, songs[random_song]))
        elif "open vs code" in cmd:
            path = "E:\\Microsoft VS Code\\Code.exe"
            speak("Opening VS Code...")
            os.startfile(path)
        elif "send mail to" in cmd:
            d = {
                'vardhan': 'vardhanvasistanche2002@gmail.com',
                'appa': 'mnvasuki69@gmail.com'
            }
            s = cmd.split(" ")
            print(s, s[-1])
            if s[-1] not in d:
                speak("Sir the user you mentioned does not exist in your library...")
                speak(f"would you like me to add {s[-1]} to your dictionary and then proceed sir?")
                speak("sir, please reply with 'yes' or 'no' only")
                reply = takeCommand().lower()
                if reply == "yes":
                    speak("Sir, please type the email id of " + s[-1])
                    eid = input("Email id >> ")
                    d[s[-1]] = eid
                    try:
                        speak("What is the content of the email sir?")
                        content = takeCommand()
                        to = s[-1]
                        sendMail(to, content)
                        speak("Mail sent successfully sir...")
                    except Exception as e:
                        print(e)
                        speak("Sorry sir, the mail was not sent due to technical error...")
                elif reply == "no":
                    speak(f"OK Sir, I will not proceed to write mail to {s[-1]}") 
            else:
                try:
                    speak("What is the content of the email sir?")
                    content = takeCommand()
                    to = s[-1]
                    sendMail(to, content)
                    speak("Mail sent successfully sir...")
                except Exception as e:
                    print(e)
                    speak("Sorry sir, the mail was not sent due to technical error...")
        elif "quit" in cmd:
            speak("Goodbye sir...")
            speak("VEDA signing off..")
            exit()
