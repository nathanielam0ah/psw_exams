#!/usr/bin/env python3

import nexmo

client = nexmo.Client(key='e9f66586', secret='M0RJEF25MU6zGFqH')

client.send_message({
    'from': 'THE CAR WASH',
    'to': '233554351607',
    'text': 'Hello Customer, we are done washing your car.',
})
