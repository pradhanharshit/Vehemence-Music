import speech_recognition as sr
import pyttsx3
import pyaudio as py
import pywhatkit

def assistant():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)        #using google api to send audio and google will send the text
            command=command.lower()
            if 'alexa' in command:
                print(command)
                if 'play' in command:
                    pywhatkit.playonyt(command)
                print(command)
    except:
        pass    

if __name__ == assistant():
    assistant()
    
    
