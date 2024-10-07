import pyttsx3 as pt
import speech_recognition as sr
import subprocess
from app_spotify_auto import play_song_in_spotify
import os

# setting up the voice engine 
engine = pt.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command(prompt="Listening..."):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(prompt)
        while True:
            try:
                audio = r.listen(source)
                user_input = r.recognize_google(audio).lower()
                print(f"User said: {user_input}")
                return user_input
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Could you repeat?")
                speak("Sorry, I didn't catch that. Could you repeat?")
            except sr.RequestError:
                print("Sorry, there's a problem with the speech service.")
                speak("Sorry, there's a problem with the speech service.")
                return None  

def handle_wikipedia():
    speak("What do you need to know about, sir")
    query = listen_command("Listening for Wikipedia search query...").lower()
    if query:
        speak(f"Searching Wikipedia for {query}.")
        subprocess.run(['python', 'sel_wiki.py', query]) # run the wikipedia script

def handle_youtube():
    speak("Which video would you like to play, sir")
    video_query = listen_command("Listening for YouTube video...").lower()
    if video_query:
        subprocess.run(['python', 'sel_yt.py', video_query]) # run the youtube script

# NOTE- spotify should be installed from the microsoft store
def handle_spotify():
    speak("Which song would you like to play, sir")
    song_query = listen_command("Listening for song name...").lower()
    if song_query:
        play_song_in_spotify(song_query) # run the spotify script

def main():
    # Initial greeting
    speak("Hi, my name is Orpheus. It's a nice day, sir. How are you?")
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 5000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            print('User:', text)
            if "how are you" in text or "what about you" in text:
                speak("I am an engine dummy, me no feelings!") # trying to be funny 
            else:
                speak("How can I assist you?")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return
        except sr.RequestError:
            speak("Sorry, there's a problem with the speech service.")
            return
    
    while True:
        command = listen_command()

        if command:
            if "wikipedia" in command or "search" in command or "info" in command:
                handle_wikipedia()
            elif "youtube" in command or "video" in command:
                handle_youtube()
            elif "music" in command or "spotify" in command or "song" in command:
                handle_spotify()
            else:
                speak("I'm not sure how to handle that request. Please try again.")
        else:
            speak("Exiting the program due to an error.")
            break

if __name__ == "__main__":
    main()
import pyttsx3 as pt
import speech_recognition as sr
import subprocess
from app_spotify_auto import play_song_in_spotify
import os

# setting up the voice engine 
engine = pt.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command(prompt="Listening..."):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(prompt)
        while True:
            try:
                audio = r.listen(source)
                user_input = r.recognize_google(audio).lower()
                print(f"User said: {user_input}")
                return user_input
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Could you repeat?")
                speak("Sorry, I didn't catch that. Could you repeat?")
            except sr.RequestError:
                print("Sorry, there's a problem with the speech service.")
                speak("Sorry, there's a problem with the speech service.")
                return None  

def handle_wikipedia():
    speak("What do you need to know about, sir")
    query = listen_command("Listening for Wikipedia search query...").lower()
    if query:
        speak(f"Searching Wikipedia for {query}.")
        subprocess.run(['python', 'sel_wiki.py', query]) # run the wikipedia script

def handle_youtube():
    speak("Which video would you like to play, sir")
    video_query = listen_command("Listening for YouTube video...").lower()
    if video_query:
        subprocess.run(['python', 'sel_yt.py', video_query]) # run the youtube script

# NOTE- spotify should be installed from the microsoft store
def handle_spotify():
    speak("Which song would you like to play, sir")
    song_query = listen_command("Listening for song name...").lower()
    if song_query:
        play_song_in_spotify(song_query) # run the spotify script

def main():
    # Initial greeting
    speak("Hi, my name is Orpheus. It's a nice day, sir. How are you?")
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 5000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            print('User:', text)
            if "how are you" in text or "what about you" in text:
                speak("I am an engine dummy, me no feelings!") # trying to be funny 
            else:
                speak("How can I assist you?")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return
        except sr.RequestError:
            speak("Sorry, there's a problem with the speech service.")
            return
    
    while True:
        command = listen_command()

        if command:
            if "wikipedia" in command or "search" in command or "info" in command:
                handle_wikipedia()
            elif "youtube" in command or "video" in command:
                handle_youtube()
            elif "music" in command or "spotify" in command or "song" in command:
                handle_spotify()
            else:
                speak("I'm not sure how to handle that request. Please try again.")
        else:
            speak("Exiting the program due to an error.")
            break

if __name__ == "__main__":
    main()
