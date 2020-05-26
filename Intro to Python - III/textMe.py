# -*- coding: utf-8 -*-
"""
textMe application for send yourself a text with a message.
"""

from twilio.rest import Client

def textme(msg):
    account = "<your account>"
    token = "<your token>"
    client = Client(account, token)
    
    message = client.messages.create(
    to="<your phone number>", 
    from_="<trial phone number>",
    body=msg)

    print(message.sid)
