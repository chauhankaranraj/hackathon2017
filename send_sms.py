from twilio.rest import Client

def sendSms():
	# Your Account SID from twilio.com/console (karan's account for now)
	account_sid = "AC1d4436e51683f91b73388902cc64de76"

	# Your Auth Token from twilio.com/console (karan's account for now)
	auth_token  = "c241eec721b4c78f03c2cafa186b44ef"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+14083142208",
	    from_="+12566702628",	# karan's number
	    body="THERE'S A FUCKING INTRUSION DAWG!!!")
