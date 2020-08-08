#twilio.rest api 
from twilio.rest import Client
import os
import secrets

#key data are stored as environment variables and obtained through os module
account_sid = os.getenv(TWIL_ACC_SID)
auth_token = os.getenv(TWIL_AUTH_TOKEN)

reciever = str(input('Please enter your number'))
#secrets is a module which produces crytographically safe numbers
otp = secrets.choice(range(0000,9999))
#otp is a 4 digit number
client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to = reciever,
    from_= os.getenv(TWIL_PHONE_NUMBER),
    body = f'The OTP is {otp} ' )


