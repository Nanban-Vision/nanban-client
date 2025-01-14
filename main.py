from camera_processing import *
from audio_processing import *
from pulse import *
import threading
import time
import subprocess
from gpiozero import Button
import warnings
import pulsectl
import requests

API_BASE_URL = "https://admittedly-wired-halibut.ngrok-free.app"  

warnings.simplefilter('ignore')
button1 = Button(2)
button2 = Button(4)

volume_control = VolumeControl(button2)
volume_control.start()

while True:
    if button1.is_pressed:
        image_path = capture_surroundings()
        with open(image_path, 'rb') as image_file:
            files = {'file': (image_path, image_file, 'image/jpeg')}
            response = requests.post(f"{API_BASE_URL}/object-detection/", files=files)

        if response.status_code != 422:
            audio_file_path = "audio.mp3"
            with open(audio_file_path, "wb") as audio_file:
                audio_file.write(response.content)

            play_audio(audio_file_path)  
    else:
        query = take_command()

        payload = {"query": query}  
        headers = {"Content-Type": "application/json"}  
        response = requests.post(f"{API_BASE_URL}/voice-assistant/", json=payload, headers=headers)  

        audio_file_path = "audio.mp3"
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)

        play_audio(audio_file_path)  

volume_control.stop()
volume_control.join()
