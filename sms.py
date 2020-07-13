from twilio.rest import Client


account_sid = 'AC796faed55aeb13717cd3d6f724db6793'
auth_token = '5351db30bf9910061ee9f6b671a5404f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13344234326',
                     to='+995568661939'
                 )

print(message.sid)