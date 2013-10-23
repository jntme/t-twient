import tweepy

auth = tweepy.OAuthHandler("vXdj3J4I1lMxOr2L48EKuA", "jLNqbs2hDPwLBdqVJJKdbncEvXkaqEuS477kT1kKU")
try:
	redirect_url = auth.get_authorization_url()
	print redirect_url
except tweepy.TweepError:
	print "Error! Failed to get request token." 

verifier = raw_input('Verifier:')
try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print "Error! Failed to get access token."


print auth.access_token.key
print auth.access_token.secret

api = tweepy.API(auth)

while True:
	should_go_on = raw_input("tweet?")
	should_go_on = should_go_on.lower()
	if should_go_on == "y":
		api.update_status("this is a tweepy status :) #tweepy")
	else:
		break