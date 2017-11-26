from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACf8fd2767468529f2fd503b069b23f2a9"
# Your Auth Token from twilio.com/console
auth_token  = "7b6417472ebba0813525aa345ed907af"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+14807477215",    # to number
    from_="+14803866268", # my twilio number
    body="A new user registered on your website!")

print message.sid
