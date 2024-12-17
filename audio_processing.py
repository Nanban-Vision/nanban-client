import speech_recognition as sr
import os

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        speak("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        speak('Say that again please...')
        query = 'error'
    return query

def play_audio(audio):
    os.system(f"mpg321 {audio}")  

