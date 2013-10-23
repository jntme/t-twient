import tweepy

def get_auth():
	'''leads the user user through the authentification of twient for his account and stores his access_token
	inti twient.txt''' 

	# creates auth with consumer_key & secret
	auth = tweepy.OAuthHandler("vXdj3J4I1lMxOr2L48EKuA", "jLNqbs2hDPwLBdqVJJKdbncEvXkaqEuS477kT1kKU")

	print "seems you aren't authentificated yet. please follow this instruction:"
	print "1. copy the following link into the browser of your choice" 
	try:
		redirect_url = auth.get_authorization_url()
		print redirect_url
	except tweepy.TweepError:
		return tweepy.TweepError
	print "2. authorize t-twient to use your twitter account"
	print "3. copy the given verifier into the next line."


	verifier = raw_input('Verifier:')

	try:
	    auth.get_access_token(verifier)
	except tweepy.TweepError:
	    print "Error! Failed to get access token."

	if auth.get_username:
		twient_file = open("twient.txt", "w")	
		twient_file.write(("key:" + auth.access_token.key + "\n"))
		twient_file.write(("secret:" + auth.access_token.secret + "\n"))		
		twient_file.close()
		print "saved your key and secret for next time."

	return auth

def is_auth():
	'''if there already exists a twient.txt file, this funciton returns the corrent auth. otherwise it returns
	False'''

	try:
		twient_file = open("twient.txt", "r")

		consumer_key = twient_file.readline().strip("\n")
		consumer_key = consumer_key.replace("key:","")
		consumer_secret = twient_file.readline().strip("\n")
		consumer_secret = consumer_secret.replace("secret:","")

		auth = tweepy.OAuthHandler("vXdj3J4I1lMxOr2L48EKuA", "jLNqbs2hDPwLBdqVJJKdbncEvXkaqEuS477kT1kKU")
		auth.set_access_token(consumer_key, consumer_secret)
		return auth
	except Exception:
		return False

# start twient
auth = is_auth()
if auth == False:
	auth = get_auth()

if auth:
	api = tweepy.API(auth)
	print "successfully authentificated."

	while True:
		tweet = raw_input("type in your tweet:")
		if tweet == "exit":
			break
		elif tweet:
			api.update_status(tweet + " #twient")
else:
	print "couldn't authentificate you. please start twient again."
