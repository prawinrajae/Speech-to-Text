#pip install speechrecognition
#brew install portaudio
#pip install pyaudio

import speech_recognition as SRG
import time
import textblob
list = []
store = SRG.Recognizer()
with SRG.Microphone() as s:
    print("Speak....")
    
    audio_input = store.record(s, duration=5)
    print("Recording time:",time.strftime("%I:%M:%S"))
    
    try:
        text_output = store.recognize_google(audio_input)
        print("Text converted from audio:\n")
        print(text_output)
        #list.append(text_output)
        print("Finished")
        
        print("Execution time :", time.strftime("%I:%M:%S"))
        
    except:
        print("Couldn't process the audio input")
        
from textblob import TextBlob
print("Score",TextBlob(text_output).sentiment.polarity)
if TextBlob(text_output).sentiment.polarity > 0.5:
    print("Positive")
else:
    print("Negative")
