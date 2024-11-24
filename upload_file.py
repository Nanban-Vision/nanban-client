import requests

url_object_detection = 'http://127.0.0.1:8000/object-detection/'
url_voice_assistant = 'http://127.0.0.1:8000/voice-assistant/'

def upload_picture(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file, 'image/jpeg')}
        response = requests.post(url_object_detection, files=files)

    if response.status_code == 200:
        print("Object detection successful!")
        
        filename = "processed_audio.mp3" 

        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"Saved as {filename}")
        return filename
    else:
        print(f"Error in object detection: {response.status_code}, {response.text}")
        return None

def upload_audio(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file, 'audio/mpeg')}
        response = requests.post(url_voice_assistant, files=files)

    if response.status_code == 200:
        print("Voice processing successful!")
        
        filename = "processed_audio.mp3" 

        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"Saved as {filename}")
        return filename
    else:
        print(f"Error in voice assistant: {response.status_code}, {response.text}")
        return None

