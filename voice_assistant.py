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
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from time import strftime
sys.path.append('Applications/')
from applications import launch_application
sys.path.append('Automated Office/Templates/Word/')
from speak import say
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('punkt')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 

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

def assistant(command):
    command=remove_stopwords(command)
    command=command.lower()
    print (command)

    #Email Section
    if 'send mail' in command:
        #email_provider=input("Who's is the email Provider?")
        say('Which Networks Email do you use')
        email_provider=my_command()
        say('To which address should i send the mail')
        #recipient = my_command()
        recipient=input(str("Recipient:"))
        if recipient:
            #response('What should I say to him?')
            #content = my_command()
            #recipient=recipient_name+'@gmail.com'
            say("What's the matter?")
            #content=input("Body of Email:")
            content=my_command()
            if email_provider=='gmail':
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                login_email_id='sanathsingavarapu265@gmail.com'
                login_email_password='sanath99'
            elif email_provider =='outlook':
                mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                login_email_id=''
                login_email_password=''
            elif email_provider=='yahoo':
                mail=smtplib.SMTP('smtp.mail.yahoo.com',587)
                login_email_id=''
                login_email_password=''
            else:
                print("Sorry I didn't get you")
            mail.ehlo()
            mail.starttls()
            mail.login(login_email_id, login_email_password)
            mail.sendmail(login_email_id, recipient, content)
            mail.close()
            response('Email has been sent successfuly. You can check your inbox.')
        else:
            response('I don\'t know what you mean!')



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
        if recognize_type=="image" or recognize_type=="photo":
            pass
        elif recognize_type=="video":
            pass
            
        

    #Launch System Application
    elif 'launch' in command:
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            response("Launching Application")
            appname = reg_ex.group(1)
            launch_application(appname)
            response('I have launched the desired application')
    

    #Open Website        
    elif 'open' or 'open website'  in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            response('The website you have requested has been opened for you .')
        else:
            pass

   
    

while(True):
    assistant(my_command())

