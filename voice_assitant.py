#Importing Modules

import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
#import python-vlc
import urllib
import urllib2
import json
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
import wikipedia
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from time import strftime
#import contractions
#import inflect
#import re, string, unicodedata
from applications import launch_application
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('punkt')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 

def my_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:

        print('Sorry Couldnot Understand Please Try Again')
        command = myCommand();
    return command

def response(audio):
    print(audio)
    for line in audio.splitlines():
              os.system("say"+audio)
              

def remove_stopwords(text):

  word_tokens = word_tokenize(text) 
  filtered_sentence = ' '.join(w for w in word_tokens if not w in stop_words )
  return filtered_sentence

def lemmatization_text(text):
  
  word_tokens = word_tokenize(text) 
  filtered_sentence=(' '.join([lemmatizer.lemmatize(word) for word in word_tokens]))
  return filtered_sentence

def stemming_text(text):
  
  word_tokens = word_tokenize(text) 
  filtered_sentence=(' '.join([stemmer.stem(word) for word in word_tokens]))
  return filtered_sentence

def assistant(command):
    command=remove_stopwords(command)
    command=lemmatization_text(command)
    command=stemming_text(command)
    print (command)

   


    #Email Section
    if 'send mail' in command:
        email_provider=raw_input("Who's is the email Provider?")
        response('Who is the recipient?')
        #recipient = myCommand()
        recipient=raw_input(str("Recipient:"))
        if recipient:
            #response('What should I say to him?')
            #content = myCommand()
            #recipient=recipient_name+'@gmail.com'
            content='hey'
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
        
    

#while(True):
#    assistant(my_command())

assistant("Hey Killer open facebook.com for me")
