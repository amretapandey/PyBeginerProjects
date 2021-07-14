##############################
# Simple Speech Recognition  #
##############################
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something')
    audio = r.listen(source, timeout=2)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Try Again...")
