#!/usr/bin/env python3

import nexmo
from config import nexmo_key, nexmo_key_secret

def send_sms(message, smsto):
    try:
        client = nexmo.Client(key=nexmo_key, secret=nexmo_key_secret)

        client.send_message({
            'from': 'CAR WASH',
            'to': smsto,
            'text': message,
        })
        print("SMS NOTIFICATION SENT")
    except:
        print("COULD NOT SEND SMS")
