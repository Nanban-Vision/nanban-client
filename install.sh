sudo apt-get install mpg321 flac python3-pyaudio pipewire pipewire-audio-client-libraries libspa-0.2-bluetooth wireplumber 
sudo systemctl --user enable pipewire pipewire-pulse
sudo systemctl --user start pipewire pipewire-pulse
pip install -r requirements.txt --break-system-packages
