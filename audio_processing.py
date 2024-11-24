import speech_recognition as sr

current_directory = os.path.dirname(os.path.abspath(__file__))
recorded_audio_filename = os.path.join(current_directory, "recorded_audio.wav")  
processed_audio_filename = os.path.join(current_directory, "processed_audio.mp3")

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    with open(recorded_audio_filename, "wb") as f:
        f.write(audio.get_wav_data())

    print(f"Audio saved as {recorded_audio_filename}")
    return recorded_audio_filename

def play_audio():
    os.system(f"mpg321 {processed_audio_filename}")  

