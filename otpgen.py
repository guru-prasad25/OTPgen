#twilio.rest api 
from twilio.rest import Client
import os
import secrets
#hello2 is the file in which the variables are stored
import hello2

account_sid = hello2.TWIL_AUTH_SID
auth_token = hello2.TWIL_AUTH_TOKEN

reciever = str(input('Please enter your number'))
#secrets is a module which produces crytographically safe numbers
otp = secrets.choice(range(0000,9999))
#otp is a 4 digit number
client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to = reciever,
    from_= hello2.TWIL_PHONE_NUMBER,
    body = f'The OTP is {otp} ' )
