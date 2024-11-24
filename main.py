def main():
    
from main_mode import *
from voice_assistant import *
from pulse import *
import threading
import time
import subprocess
from gpiozero import Button
import warnings 
import pulsectl

warnings.simplefilter('ignore')
button1 = Button(2)
button2 = Button(3)

volume_control = VolumeControl(button2)
volume_control.run()  

while True:
    if button1.is_pressed:
        image = capture_surroundings()
        processed_audio = upload_picture(image)
        play_audio(processed_audio)
    else:
        audio = record_audio()
        processed_audio = upload_audio(audio)
        play_audio(processed_audio)

volume_control.stop()
volume_control.join()

