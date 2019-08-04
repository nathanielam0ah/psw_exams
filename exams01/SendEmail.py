#!/usr/bin/env

import smtplib, ssl
import getpass
import config

# this method creates an smtp server and sends an email using the given parameters
def send_email(subject,message,mailto):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        password = getpass.getpass("PASSWORD: ")
        server.login(config.email_server, password) #sender login
        text="Subject: {}\n\n{}".format(subject,message)
        server.sendmail(config.email_client,mailto,text)
        server.quit()
        print(f"NOTIFICATION SENT TO {mailto}")
    except:
        print("FAILED TO SEND.")

send_email("TEST EMAIL", "HELLO $USER", config.email_client)
