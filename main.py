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

API_BASE_URL = "http://0.0.0.0:8000"  

warnings.simplefilter('ignore')
button1 = Button(2)
button2 = Button(3)

volume_control = VolumeControl(button2)
volume_control.run()

while True:
    if button1.is_pressed:
        image_path = capture_surroundings()
        with open(image_path, 'rb') as image_file:
            files = {'file': (image_path, image_file, 'image/jpeg')}
            response = requests.post(f"{API_BASE_URL}/object-detection/", files=files)
        play_audio(response.content)  
    else:
        query = take_command()
        response = requests.post(f"{API_BASE_URL}/voice-assistant/", json={"query": query})
        play_audio(response.content)  

volume_control.stop()
volume_control.join()

