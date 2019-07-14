#Importing Modules

import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
#from pyowm import OWM
#import youtube_dl
#import python-vlc
#import urllib
#import urllib2
#import json
#from bs4 import BeautifulSoup as soup
#from urllib2 import urlopen
#import wikipedia
import aiml
from autocorrect import spell
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from time import strftime
sys.path.append('Email/')
from send_mail import mail
sys.path.append('Applications/')
from applications import launch_application
sys.path.append('Automated Office/Templates/Word/')
from speak import say
sys.path.append('Face Recognition/')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('punkt')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
BRAIN_FILE="aiml_pretrained_model.dump"

k = aiml.Kernel()
k.loadBrain(BRAIN_FILE)

say("Hey Dude, This is Killer.Your Personal Assistant")
def my_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:

        print('Sorry Couldnot Understand Please Try Again')
        command = my_command();
    return command

def response(audio):
    print(audio)
    say(audio)
              

def remove_stopwords(text):

  word_tokens = word_tokenize(text) 
  filtered_sentence = ' '.join(w for w in word_tokens if not w in stop_words )
  return filtered_sentence
print("This is Killer, Your Personal Assistant")
def assistant(command):
    #initial_command=command
    #command=remove_stopwords(command)
    command=command.lower()
    #print (command)

    #Email Section
    if 'send mail' in command:
        send_mail()
   
    #Automated Office
    elif 'automated office' in command:
        
        say("Select Either Word or PowerPoint")
        #app_type=input("Which Application:")
        app_type=my_command()
        app_type=app_type.lower()
        print ('Here:'+app_type)
        if app_type=="word" or app_type=="microsoft word":
            
            say("Build your Own or Use Existing Ones")
            #option=input("Build or Use Templates:")
            option=my_command()
            print (option)
            option=option.lower()
            if 'build' in option:
                pass
            elif 'template' or 'templates' in option:
                say("Select any one template")
                print("Template Types \n 1.Letter 2.Resume")
                #template_option=input("Template Type:")
                template_option=my_command()
                print('Here'+template_option)
                template_option=template_option.lower()
                if template_option=="letter":
                    from letter_template import letter
                    letter()
                elif template_option=="cv" or template_option=="resume":
                    from cv_template import cv
                    cv()
                
            
    #Recognizer
    
    elif 'recognizer' in command:
        #recognize_type=input("Recognizer Type:")
        say("Choose Either Image or Live Stream")
        #recognize_type=my_command()
        recognize_type=input("Type:")
        if recognize_type=="image" or recognize_type=="photo":
            from image import recognize_image
            recognize_image()
        
        elif recognize_type=="video":
            from video import recognize_video
            recognize_video()

    

    #Launch System Application
    elif 'launch' in command:
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            response("Launching Application")
            appname = reg_ex.group(1)
            launch_application(appname)
            response('I have launched the desired application')
              
    elif 'open' in command:
        website = re.search('open (.*)', command).group(1)
        webbrowser.open(website)
        response('I have launched the desired application')
    
    elif(command):  
        #print("Here")
        #query = input("User > ")
        query = [spell(w) for w in (command.split())]
        question = " ".join(query)
        reply = k.respond(question)
        question=question.lower()
        if reply:
            print("Killer > ", reply)
            say(reply)
                    
        else:
            print("Killer > :) ", )

    elif command=='quit':
        quit()

   

while(True):
    command=input("User > ")
    assistant(command)

#assistant('hey dude ')

