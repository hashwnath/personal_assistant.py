import speech_recognition as sr
import datetime
import webbrowser
import time
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# this is speak funcy=tion
def speak(text):

    engine.say(text)
    engine.runAndWait()
r = sr.Recognizer()
def record_audio(ask = False):
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        speak('say something')
        print('listening...')
        audio = r.listen(source,phrase_time_limit=5)
    
    
    try:
        print('recognizing...')
        voice_data = r.recognize_google(audio)
        # speak(voice_data)
    except sr.UnknownValueError:
        speak('sorry, I did not get that')
    except sr.RequestError:
        speak('Sorry my speech service is down') 
    return voice_data       
def respond():
    if 'what is your name' in voice_data:
        speak('My name is Alexa')
    if 'what time is it' in voice_data:
        speak(datetime.datetime.now())
    # if 'search' in voice_data:
    #     search = record_audio('What do you want to search')
    #     url= 'https://google.com/search?q='+search
    #     webbrowser.get().open(url)
    #     speak('Here is what I found for '+search)
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url= 'https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        speak('Here is The location of '+location)  
    # if 'open netflix' in voice_data:
    #     url = 'https://www.netflix.com/in/'
    #     webbrowser.get().open(url)
    if 'open' in voice_data:
        nd = voice_data.split()
        ws = nd[1]
        url = 'http://www.'+ws+'.com'
        webbrowser.get().open(url)
    if 'search' in voice_data:
        nd = voice_data.split()
        search = nd[1]
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)    
    if 'play' in voice_data:
        nd = voice_data.split()
        audio = nd[1]
        url = 'https://www.youtube.com/results?search_query='+audio
        webbrowser.get().open(url) 
        speak('please select the video you like...')


    if 'exit' in voice_data:
        exit()      
speak('Initializing alexa')

for i in range(12345):
    
    voice_data = record_audio()
    respond()
    speak('Any more help?')
    res = record_audio()
    if 'yes' in res:
        
        continue
       
    else:
        speak('Closing Alexa have a great day')
        exit()

    

    

  
