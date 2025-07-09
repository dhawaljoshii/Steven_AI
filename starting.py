import sys
import speech_recognition as sr  #speech to text
import os    #say function connectivity between programme and os
from vosk import Model, KaldiRecognizer  #vosk model recognize
import pyaudio   #helps in speech reco in python
import subprocess

model = Model(r'/Users/dhawaljoshi/Developer/PythonProject/english')  #path of the vosk model
recognizer = KaldiRecognizer(model, 16000)

def say(text):       #text.... speech
    os.system(f"say {text}")

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1.0
        audio = r.listen(source)
        try:
            query = r.recognize_vosk(audio, language="en-in")  # find better voice model if possible
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Can't recognize your voice... Sorry sir"


if __name__ == '__main__':
    print('SAY WAKE UP TO ACTIVATE STEVEN')

while True:   #iss statement ki vajah se loop is continued from here only

    query = take()

    if "wake".lower() in query.lower():
        os.system(f"open /Users/dhawaljoshi/Developer/PythonProject/AI_G-12/.venv/main.py")
        subprocess.run(["python", "/Users/dhawaljoshi/Developer/PythonProject/AI_G-12/.venv/main.py"])
        break




