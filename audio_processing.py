import speech_recognition as sr

recorded_audio_filename = os.path.join(current_directory, "recorded_audio.wav")  
processed_audio_filename = os.path.join(current_directory, "processed_audio.mp3")

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

def play_audio():
    os.system(f"mpg321 {processed_audio_filename}")  

