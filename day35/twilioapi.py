from twilio.rest import Client
import os
account_sid = 'AC91d68a7586b73e0b2dad10287c34d8ad'
auth_token = os.environ.get("T_API_KEY")

def text_weather(will_rain: bool):
    client = Client(account_sid, auth_token)
    if will_rain:
        text = "Bring your rain jacket today 🌧️!"
    else:
        text = "No rain today ☀"
    message = client.messages \
                    .create(
                         body=text,
                         from_='+18595358396',
                         to='+13522267999'
                     )

    print(message.status)