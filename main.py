from logging import debug
import speech_recognition as sr
from flask import Flask, render_template, render_template_string, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/start_recording")
def start():
    input=sr.Recognizer()
    print("yes")
    with sr.Microphone() as source:
        print("Listening...")
        input.adjust_for_ambient_noise(source=source)
        audio=input.listen(source,timeout=2)
        print("Recognising...")
        data=""
        try:
            data1=input.recognize_google(audio, language='bn-BD')
            data=data1.lower()
            print("This is what you said:\t",data)
            if 'value error' in data:
                print("this is how you should solve!!")
            else:
                print("try keywords!!")
        except sr.UnknownValueError:
            print("sorry")
    print("ok")
    return render_template("results.html", data=data)

 
    

if __name__=="__main__":
    app.run(debug=True)