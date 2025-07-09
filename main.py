import speech_recognition as sr  #speech to text
import os    #say function connectivity between programme and os
from vosk import Model, KaldiRecognizer  #vosk model recognize
import pyaudio   #helps in speech reco in python
import webbrowser    #connection between the programme and webbrowser
import datetime    #time and date recognition
from openai import OpenAI
#using in basic maths and deepseek
client = OpenAI(api_key="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")    #for using a_i model in the programme
from openai import OpenAI, base_url
import random     #open ai
import datetime as dt    #whether api
import requests   #weather api
# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/talk', methods=['GET'])
# def talk():
#     # Here integrate speech recognition + OpenAI response logic
#     # For now, return a placeholder
#     return jsonify({"reply": "Hello! I am your AI assistant."})

# if __name__ == "__main__":
#     app.run(port=16000)

#Say HEY STEVEN to access AI

# #todo: Initialize the calendar (this will prompt OAuth2 on first run)
# calendar = GoogleCalendar('2327bcse23@uit.hpu.ac.in')  # Or leave blank to use default account
# It will store a token.pickle for future sessions after login.

model = Model(r'/Users/dhawaljoshi/Developer/PythonProject/english')  #path of the vosk model
recognizer = KaldiRecognizer(model, 16000)


#todo: import news and weather api's

# provides functions for interacting with the operating system
#
# chatStr = ""

# def chat(query):
#     global chatStr
#     print(chatStr)
#     chatStr += f"Dhawal: {query}\n Steve: "
#     response = client.completions.create(model = "deepseek/deepseek-r1:free",
#     prompt= chatStr)
#
#     say(response.choices[0].text)
#     chatStr += f"{response.choices[0].text}\n"
#     return response.choices[0].text
#
#     with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w", encoding="utf-8") as f:
#         f.write(text)
#


# def ai(prompt):
#
#     text = f"AI response for PROMPT: {content}\n ************************\n\n"
#     client = OpenAI(api_key="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",
#                     base_url="https://openrouter.ai/api/v1")
#
#     chat = client.chat.completions.create(
#         model="deepseek/deepseek-r1:free",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )
#
# # todo: Wrap this inside a try catch block
#
#     return chat.choices[0].message.content.strip()
#     if __name__ == "__main__":
#         while True:
#             user_input = input("you: ")
#             if user_input.lower() in ["quit", "exit", "bye"]:
#                 break
#
#                 chat = ai(user_input)
#                 ptint("chatbot: ", chat)


def say(text):       #text....          #shiv... start
    os.system(f"say {text}")


def takeCommand():     #taking command as speech or text   most important
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1.2    #kitne second ka gap leke reco karega
        audio = r.listen(source)

        try:
            query = r.recognize_vosk(audio, language="en-in")     #find better voice model if possible
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Can't recognize your voice... Sorry sir"

if __name__ == '__main__':     #firstly ye execute hogaa
    print('Steven Bot')
    say("hello, i am an A.I bot")
    os.system(f"open /Users/dhawaljoshi/Downloads/beep.mp3")
    #os module

while True:   #iss statement ki vajah se loop is continued from here only

    print("listening...")
    query = takeCommand()   #input via microphone

    if "hi".lower() in query.lower():
        print("hi, how may i help you?")
        say("hi, how may i help you?")

    if "hello".lower() in query.lower():
        say("hello, how may i help you?")

    if "thank you".lower() in query.lower():
        say("my pleasure")

    if "thankyou".lower() in query.lower():
        say("my pleasure")

    if "name".lower() in query.lower():
        print("my name is Steven")
        say("my name is Steven")

    if "time" in query:
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        print(f" {hour}:{minute}")
        say(f" {hour}:{minute}")

    if "role".lower() in query.lower():
        say("our roles are:"
            "Backend: Dhawal and Praggyaat"
            "Frontend: Shivang and mritunjay"
            "Report and management: Rashi and Sunidhi")

    if "technology".lower() in query.lower():
        say("Backend: Django and flask"
            "Frontend: HTML, CSS, React Java-script")

    if "Google".lower() in query.lower():      #add more sites
        say("Opening google...")
        webbrowser.open("https://www.google.com")

    if "you tube".lower() in query.lower():
        say("Opening youtube...")
        webbrowser.open("https://www.youtube.com")

    if "college website".lower() in query.lower():
        say("opening UIT website...")
        webbrowser.open("https://www.hpuniv.ac.in/university-detail/home.php?uiit")

    if "wikipedia".lower() in query.lower():
        say("Opening wikipedia...")
        webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")

    if "camera" in query:        #working.. but optimize this
        say("Starting camera...")
        os.system(f"open /System/Applications/FaceTime.app")

    if "calculator" in query:
        os.system(f"open /System/Applications/Calculator.app")

    if "calculated" in query:
        os.system(f"open /System/Applications/Calculator.app")

    if "music".lower() in query.lower():       #still not working try
        # musicPath = "/Users/dhawaljoshi/Downloads/music.mp3"
        webbrowser.open(f"https://www.youtube.com/watch?v=T3CNMFjZdKU")  #used to access files through programme

    if "Introduce".lower() in query.lower():
        say("hi... i am an A.I bot.... as our project....members of group 12 are......"
            "roll number 49, Rashi Sharma....."
            "roll number 64, Sunidhi Sharma....."
            "roll number 61, Shivang Thakur......"
            "roll number 36, Mritunjay Sharma......"
            "roll number 45, Praggyaat Pathania......"
            "and roll number 23, Dhawal Joshi......"
            )

    if "Project".lower() in query.lower():
        say("HELLO, MY NAME IS STEVEN, I AM AN A.I DESKTOP ASSISTANT MADE BY GROUP-12 "
            "An AI Desktop Assistant is a smart software application designed to help users perform various tasks on their computer using voice commands. It uses artificial intelligence to understand natural language and respond appropriately, making interactions more intuitive and efficient. Typical functions of an AI desktop assistant include opening applications, searching the internet, providing weather updates and answering general knowledge questions. By integrating voice recognition, machine learning, and automation, it acts as a personal helper that simplifies daily tasks and enhances productivity on a desktop environment.")

    if "weather".lower() in query.lower():
        os.system(f"open /System/Applications/Weather.app")

    if "appreciate".lower() in query.lower():
        say("Thankyou everyone for listening my non-sense talk....."
            "mmai mam se aasha karta hun ki inn logo ki mehnat ko dekhte huye group-12 ko full marks diye jaaye")

        # time=strftime("%A, %B %d, %Y")
        # print(time)

    if "date".lower() in query.lower():
        print(datetime.date.today())
        say(str(datetime.date.today()))

    # if "ask".lower() in query.lower():
    #     ai(prompt=query)

    if "exit".lower() in query.lower():  #exits the code and stop its execution
        say("Goodbye")
        os.system(f"open /Users/dhawaljoshi/Downloads/beep2.mp3")
        os._exit()

        # weather api
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "ac4e49e5b74ca479803c8c98e5f80166"

    if "temperature".lower() in query.lower():
        say("what is your city")
        City = takeCommand()

        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "ac4e49e5b74ca479803c8c98e5f80166"
        CITY = ("Shimla")


        def kelvin_to_celsius_fahrenheit(kelvin):
            celsius = kelvin - 273.15
            fahrenheit = (9 / 5) * celsius + 32
            return celsius, fahrenheit


        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

        response = requests.get(url).json()

        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        print(f"Temperature in {CITY} {temp_celsius:.2f}degree celsius")
        say(f"Temperature in {CITY} {temp_celsius:.2f}degree celsius")

# A.I module using deepseek-chat api instead deepseek-R1 free
    if "Steven".lower() in query.lower():
        os.system(f"open /Users/dhawaljoshi/Downloads/AIbeep.wav")

        #start the loop from the print until the statement is proven false
        while True:
         print("ASK ANYTHING")
         question = takeCommand()     #input through voice command

         client = OpenAI(api_key="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",
                        base_url="https://openrouter.ai/api/v1")

         chat = client.chat.completions.create(    #output chat
            model="deepseek/deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": f"{question} short "
                }
            ]
         )

         print(chat.choices[0].message.content)  # only response is printed
         say(chat.choices[0].message.content)






#list of lists is not working to list multiple sites ib the same function or f-string
#say(query)    speaks the user output outloud
#say(query) command not working
#add cephai
#recognizer_google also not present using vosk speech recognizer
#use python version >3.11



