import subprocess
import wolframalpha
import pyttsx3
import tkinter as ttk
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import ctypes
import times
import requests
import shutil
from twilio.rest import Client
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")

    speak("I am jeyaprakash's voice assistant")
    speak("Its jessie")

def username():
    speak("what should i call you sir")
    uname=takeCommand()
    speak(uname)
    colums=shutil.get_terminal_size().columns
    speak("How can i help you sir")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

website_urls = {
    'wikipedia':"https://www.wikipedia.org/",
    'youtube': "https://www.youtube.com/",
    'stackoverflow': "https://stackoverflow.com/",
    'facebook': "https://www.facebook.com/",
    'twitter': "https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D",
    'google': "https://www.google.com/",
    'opera': "https://www.opera.com/",
}
system_locs={}

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.echo()
    server.starttls()

    #enable low security in gmail
    server.login('your email id','your email password')
    server.sendmail('your email id',to,content)
    server.close()


while  True:
    query=takeCommand().lower()
    if "open" in query:
        to_open = query.split(" ")[1].lower()
        if to_open in website_urls:
            webbrowser.open_new(website_urls[to_open])
        if to_open in system_locs:
            subprocess.call(f"explorer {system_locs[to_open]}")

    if 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir,the is {strTime}")
    
    elif 'send Gmail' in query:
        try:
            speak("What should I say?")
            content=takeCommand()
            speak("Whom should i send?")
            to=input()
            sendEmail(to, content)
            speak("Email  has been sent!")
        except Exception as e:
            print(e)
            speak("I am not able to send this gmail")
    
    elif "search" in query or "play" in query:
        query = query.replace("search" , "")
        query = query.replace("play", "")
        webbrowser.open(query)
    
    elif "lock window" in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()
    
    elif "shutdown system"  in query:
        speak("Hold On a Sec! Your System is on its way to shut down")
        subprocess.call('shutdown /p /f')
    
    elif "empty recycle bin" in query:
        winshell.recycle_bin().empty(confirm = False,show_progress = False,sound=True)
        speak("Recycle Bin Cleaned")
    
    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop jessi from listening commands")
        a = int(takeCommand())
        time.sleep(a)
        print(a)
    
    elif "where is" in query:
        query = query.replace("where is", "")
        location = query 
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.com/maps/@11.4001643,79.706331,15z" + location + " ")
    
    elif "camera" in query or "take a photo" in query:
        subprocess.call("camera")
        ec.capture(0,"Jessie Camera","img.jpg")
    
    elif "restart" in query:
        subprocess.call(["shutdown","/r"])
    
    elif "log off" in query or "sign out" in query:
        speak("Make sure all the applications are closed before sign-out")
        subprocess.call(["shutdown", "/l"])
    
    elif "news" in query:
        speak("Here you go to times now")
        webbrowser.open("https://www.timesnownews.com/")

    elif 'how are you' in query:
        speak("I am fine,Thank you")
        speak("How are you,My Dear Friend?")
    
    elif 'fine' in query or 'good' in query:
        speak("It's good to know that your fine")
    
    
    elif "what is your name" in query or "what is your name" in query:
        speak("My friends call me jessie")
    
    elif "who made you" in query or "who created you" in query or "who is your creator" in query:
        speak("created by Jp")
    
    elif "joke" in query:
        speak(pyjokes.get_joke())
        
    elif "who i am" in query:
        speak("If you talk then definitely your human")
    
    elif "why you come to world" in query:
        speak("Thanks to Jp. further It's a secret")
    
    elif "is love" in query:
        speak("It's 7th sense that destroy all the other senses")
    
    elif "who are you" in query:
        speak("I am your virtual assistant, My name is jessi")
    
    elif "reason for you" in query:
        speak("I was created as a minor project by Jp")    
    
    elif "will you be my gf" in query or "will you be my bf" in query:
        speak("I'm not sure about, may be you should give me some time")
    
    elif "i love you" in query:
        speak("It's hard to understand")
    
    elif "exit" in query:
        speak("Thanks for giving me your time")
        exit()



     


    