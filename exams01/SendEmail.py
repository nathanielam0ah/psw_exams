#!/usr/bin/env python3

import smtplib, ssl
import config

def send_email(subject,message,mailto):             # this method creates an smtp server and sends an email using the given parameters
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.email_server, config.email_server_pass) #sender login
        text="Subject: {}\n\n{}".format(subject,message)
        server.sendmail(config.email_client,mailto,text)
        server.quit()
        print(f"EMAIL NOTIFICATION SENT TO {mailto}")
    except:
        print("COULD NOT SEND EMAIL.")
        input("press any key to continue: ")
