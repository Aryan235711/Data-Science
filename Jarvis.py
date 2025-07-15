import os
import random

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning master")

    elif 12 <= hour < 18:
        speak("Good Afternoon master")

    else:
        speak("Good Evening master")

    print("I am a super intellect program named \"String\".")
    speak("I am a super intellect program named \"string\".")
    speak("Ask me anything.")

def takeCommand():
    """It takes microphone input from the user and returns string output"""
    try:

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
            r.dynamic_energy_threshold = None

            try:
                audio = r.listen(source, timeout=10)  # Set timeout to avoid infinite waiting
                print("Recognizing....")
                query1 = r.recognize_google(audio, language="en-in" or 'hi-in')
                print(f"Master said -{query1}")
                return query1

            except sr.RequestError:
                speak("Speech recognition service is unavailable.")
                exit()

            except sr.UnknownValueError:
                speak("Could not understand the audio")
                return 'None'


            except sr.WaitTimeoutError:
                speak("Timed out!!")
                str1 = "Timed out!!"
                return str1

            except KeyboardInterrupt:
                speak("Program stopped by the human itself.")

    except KeyboardInterrupt:
        speak("Program stopped by the human itself.")


if __name__ == '__main__':

    wishMe()

    while True:

        query = takeCommand().lower()

        #Logic for executing tasks based on query
        try:
            if 'wikipedia' in query:
                speak("Searching Wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                print(results)
                speak(f"According to wikipedia-{results}")
                speak("Anything else I can help you with. Feel free to ask.")

            elif 'open youtube' in query or 'youtube kholo' in query:
                webbrowser.open('youtube.com')
                speak("Anything else I can help you with. Feel free to ask.")


            elif 'open google' in query or 'google kholo' in query:
                webbrowser.open('google.com')
                speak("Anything else I can help you with. Feel free to ask.")


            elif 'open stackoverflow' in query or 'stackoverflow kholo' in query:
                webbrowser.open('stackoverflow.com')
                speak("Anything else I can help you with. Feel free to ask.")


            elif 'play music' in query or 'music chalao' in query:
                path_song = "C:\\Users\\pc\\Downloads\\Music"
                songs = os.listdir(path_song)
                os.startfile(os.path.join(path_song, songs[ random.randint(0,1)]))

            elif 'today\'s date' in query or'date is today' in query or 'date of today' in query or 'aaj ki tarik' in query:
                str_date = datetime.date.today().strftime('Today\'s date is %b %d, 20%y') #should be changed if the century changes
                speak(str_date)
                print(str_date)
                speak("Anything else I can help you with. Feel free to ask.")


            elif 'thank you' in query or 'thanks' in query or 'dhanyvad' in query or 'shukriya' in query:
                speak("Glad to help you!! Tell me anything you want to know about and i will help you find it. Have a good day.")
                exit()

            elif 'timed out!!' in query:
                speak('Since you haven\'t said anything. Going into rest mode on the count of 5!!')
                speak("If you still want to use me, speak within the counting period and i will listen to you.")


                for i in range(5, 0, -1):

                    speak(str(i)), print(i,end=" ")

                    r = sr.Recognizer()

                    if i == 1:
                        exit()

                    with sr.Microphone() as source:
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source, duration=1)
                        r.dynamic_energy_threshold = None

                        try:
                            audio = r.listen(source, timeout=10)  # Set timeout to avoid infinite waiting
                            print("Recognizing....")
                            query1 = r.recognize_google(audio, language="en-in")

                        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
                            query1 = None

                    if query1 is not None and query1.strip():
                        speak("Oh! You actually stopped me. Well since you are so persistent..I will help you this time.")
                        break

                    else:
                        continue


                continue

            elif query == 'none':
                speak("Speak again.")
                continue

            else:
                speak("Feature not available yet!! Might be added in the future.")
                speak("Try asking something else.")
                continue

        except wikipedia.PageError or wikipedia.DisambiguationError:
            speak("Sorry. Couldn't find what you are looking for!!")

        except KeyboardInterrupt:
            speak("Program stopped by the human itself.")



