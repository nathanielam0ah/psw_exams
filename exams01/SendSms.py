#!/usr/bin/env python3

import nexmo
from config import nexmo_key, nexmo_key_secret

def send_sms():
    client = nexmo.Client(key=nexmo_key, secret=nexmo_key_secret)

    client.send_message({
        'from': 'CAR WASH',
        'to': testCustomer.phone_number,
        'text': 'Hello Customer, we are done washing your car.',
    })
