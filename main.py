import speech_recognition as sr

def take_queries():
    input=sr.Recognizer()
    print("yes")
    with sr.Microphone() as source:
        print("Listening...")
        input.adjust_for_ambient_noise(source=source)
        
        audio=input.listen(source,timeout=2)
        print("Recognising...")
        data=""
        try:
            data1=input.recognize_google(audio)
            data=data1.lower()
            print("This is what you said:\t",data)
            if 'value error' in data:
                print("this is how you should solve!!")
            else:
                print("try keywords!!")
        except sr.UnknownValueError:
            print("sorry")
    print("ok")

if __name__=="__main__":
    take_queries()