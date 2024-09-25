import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import pyautogui
import os
import pyaudio


name= "Jarvis"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')   #get the voices in the system
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)  # Selecting the voices in the two voices

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good Evening")  
    speak("I am Jarvis assistent of you, how i can help you!")
    
def takecommand():
    # It take the microphone input and converted into the text
    read=sr.Recognizer()
    global flag1
    with sr.Microphone() as source:
        if flag1==False :
            print("Listening......!")
        read.pause_threshold=0.5
        audio=read.listen(source)
    try:
        if flag1==False :
            print("recognizing...!")
        queury=read.recognize_google(audio,language='en-in')
        print(f"user said {queury}\n")
    except Exception as e:
        # print(e)
        print("say again plaese  i can't listen")
        return "None"
    return queury

def datesay():
    dateQuery=""
    date= datetime.datetime.now().strftime("%d")
    todaysmounth=datetime.datetime.now().strftime("%B")
    year=datetime.datetime.now().strftime("%Y")
    dateQuery=f"Today's day is {date}{ todaysmounth}{year}"
    speak(dateQuery)

def currentTime():
    hour = datetime.datetime.now().strftime("%H")
    hour=int(hour)-12
    minutes = datetime.datetime.now().strftime("%M")
    speak(f"Current time is {hour}hours and{minutes} minutes")
 
WakeUp=1
flag1=True
google=1
youtube=False

while(True):
    queury=takecommand().lower()
    if(flag1):
        wish()
        flag1=False
    if("wake up" in queury):
        WakeUp=1
    if(WakeUp==0):
        continue
    if("wikipedia" in queury):            #information includeed in wikipedia
        queury=queury.replace("wikipedia","")
        result=wikipedia.summary(queury,sentences=2)
        speak(f"According to the wikipedia {result}")
        
    elif all(keyword in queury for keyword in ["quit"]):       # Quite the programme
        speak("OK Sir")
        break
    
    elif ("open" in queury or "start" in queury) and "youtube" in queury: # You tube open
        speak("Youtube will be start..!")
        webbrowser.open("https://www.youtube.com")
        youtube=True
        google=0
        
    elif all(keyword in queury for keyword in ["close", "youtube"]):  #close the youtube
        speak("Youtube will be close..!")
        pyautogui.hotkey('ctrl', 'w') 
        
    elif youtube and queury!="none"and "search" in queury:
        queury=queury.replace("search","")
        webbrowser.open( f"https://www.youtube.com/results?search_query={queury}")
        google=0
        
    elif all(keyword in queury for keyword in ["today's", "date"]):  # Todays date
        datesay()
        
    elif all(keyword in queury for keyword in ["current", "time"]):  # Current Time 
        currentTime()
        
    elif "thank you" in queury:
        speak("Welcome sir its my work!")
        
    elif "sleep" in queury:
        speak("Ok sir if want a help call the wake up")
        WakeUp=0
        
#----------------------------------------google-----------------------------------   
    elif ("open" in queury or "start" in queury) and "google" in queury:
        webbrowser.open( "https://www.google.com")
        speak("what i can search ?")
        google=1
        youtube=False
        
    elif google==1 and queury!="none"and "search" in queury:
        queury=queury.replace("search","")
        pyautogui.hotkey('ctrl', 'w')
        webbrowser.open( f"https://www.google.com/search?q={queury}")
        
    elif all(keyword in queury for keyword in ["close", "google"]):  # close Google
        speak("Google will be closed..!")
        subprocess.run(["taskkill", "/f", "/im", "chrome.exe"])
        google=0
        youtube=False
        
    elif all(keyword in queury for keyword in ["close", "tab"]):
        pyautogui.hotkey('ctrl', 'w')
        google=0
        
    elif "add today's task" in queury:
        from taskManager import TaskManager
        tk=TaskManager()
        tk.addTask(queury)
        speak("Your task is added")
# -------------------------------------------- File Working---------------------
    elif ("filemanager" in queury or "this pc" in queury) and "open" in queury:
        if("filemanager" in queury):
            queury.replace("filemanager","")
        else:
            queury.replace("this pc","")
        os.systemfile("C:\Windows\System32")
    
    
        
        
    
        
 
    
