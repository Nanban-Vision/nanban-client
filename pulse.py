from gpiozero import Button
import pulsectl

class VolumeControl:
    def __init__(self, button_pin):
        self.pulse = pulsectl.Pulse('volume-control')
        self.button = Button(button_pin)

        self.button.when_pressed = self.button_pressed
        self.button.when_released = self.button_released

    def set_volume(self, volume):
        sinks = self.pulse.sink_list()
        for sink in sinks:
            self.pulse.volume_set_all_chans(sink, volume)

    def button_pressed(self):
        self.set_volume(1.0)  

    def button_released(self):
        self.set_volume(0.0)  

    def run(self):
        try:
            while True:
                pass  


