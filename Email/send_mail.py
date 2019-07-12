import sys
sys.path.append('../')
from speak import say
def mail():
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
            say('Email has been sent successfuly. You can check your inbox.')
    else:
            says('I don\'t know what you mean!')

