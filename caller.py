from twilio.rest import Client


account_sid = 'AC7c77128736c4172d264e9e3244d4f418'
auth_token = '781cbbec3695333b33a96e80157e42e9'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+254719489574',
                        from_='+12029529279'
                    )

print(call.sid)
