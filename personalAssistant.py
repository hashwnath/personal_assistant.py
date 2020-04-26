import speech_recognition as sr
import datetime
import webbrowser
import time
import pyttsx3
import requests
from bs4 import BeautifulSoup
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
# def num_maker(wlst):
#     num2words1 = {1: 'one', 2: 'two', 3: 'Three', 4: 'Four', 5: 'Five', \
#             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
#             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
#             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}  
#     intlst = list(num2words1.keys())
#     worlist = list(num2words1.values())        
#     slst = []
#     for i in wlst:
#         if i in worlist:
#             m = intlst[worlist.index(i)]
#             slst.append(m)
#     return slst[0],slst[1]        
# def calc(a,b,voice_data):
#     if 'add' or 'sum' in voice_data:
#         re = a+b
#         speak('the result of addition of'+str(a)+'and'+str(b)+'is'+str(re))
#     if 'subract' or 'difference' in voice_data:
#         re = a-b
#         speak('the result of subraction of'+str(a)+'and'+str(b)+'is'+str(re))
#     if 'product' or 'multiply' in voice_data:
#         re = a*b
#         speak('the result of multiplication of'+str(a)+'and'+str(b)+'is'+str(re))
#     if 'div' in voice_data:
#         re = a/b
#         speak('the result of division of'+str(a)+'and'+str(b)+'is'+str(re))            
def carona(voice_data):
    if 'active' in voice_data:
        x = 'blue'
    elif 'deaths' in voice_data:
        x = 'red'
    elif 'recovery'in voice_data:
        x = 'green'
    elif 'migrated' in voice_data:
        x = 'orange'    


    mhaw = requests.get('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(mhaw.content, 'html.parser')
    status = soup.select('.bg-'+x)
    actstr = str(status[0])
    # print(actstr)
    splv2 = actstr.split('strong>')
    # print(splv2)
    sth = splv2[1]
    num = sth[:-2]
    print(num)
    speak('The number in India is '+str(num))    




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
    if 'about you' in voice_data:
        speak('Hi, I am alexa made by Hashwanth Sutharapu in Hyderabad this program is made from basic python and speech recognition modules.It is a great previalge to s[eak to you.')
    if 'your master' in voice_data:
        url = 'https://www.google.com/search?q=sutharapu+hashwanth&sxsrf=ALeKk000JAmlSqUKgn5sBdoDuipW_Cnj8w:1587899960903&tbm=isch&source=iu&ictx=1&fir=MElM2qOdXKyCoM%253A%252CU0MEFcq0kZINcM%252C_&vet=1&usg=AI4_-kR2xCe37mitjkNRJEtR0uyPyG9Wxw&sa=X&ved=2ahUKEwjp2u6o_IXpAhVMxDgGHd40CuQQ9QEwBHoECAkQBQ#imgrc=MElM2qOdXKyCoM:'    
        webbrowser.get().open(url) 
        speak('I was made by Sutharapu Hashwanth,Here is the image of my master, Hashwanth.')
        speak('would you like to look at his linkedin profile')
        agr = record_audio()
        if 'yes' in agr:
            url = 'https://www.linkedin.com/in/sutharapuhashwanth/?originalSubdomain=in'    
            webbrowser.get().open(url)
            speak('Here is the the linked profile of my master, Hashwanth,would you like to look at his other social media accounts like Youtube, github, blogspot.')
            agrall = record_audio()
            if 'yes' in agrall:
                url = 'https://www.youtube.com/channel/UClRRIYpM3G90naVrJxrVC0w?view_as=subscriber'    
                webbrowser.get().open(url)
                speak('Here is the Youtube channel of my master, please have a look at the danger video,Guess who is that, its my master,Do not try this at home')
                url = 'https://github.com/hashwnath'    
                webbrowser.get().open(url)
                speak('And here comes the Github account of my master,check out the netflix clone and the personal_assistant is none other than me.')
                url = 'https://hashwanth531.blogspot.com/'    
                webbrowser.get().open(url)
                speak('This is the blogspot of hashwanth, he put all the cool stuff over there')
    # if 'add' or 'sum' or 'diffrence' or 'subract' or 'product' or 'multiply' or 'div' in voice_data:
    #     wlst = voice_data.split()
    #     a,b = num_maker(wlst)
    #     calc(a,b,voice_data)
    if 'virus' in voice_data:
        carona(voice_data)            
    

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

    

    

  
