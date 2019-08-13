import tweepy

# fill your details
API_KEY="*******************************"
API_SECRET="******************************"
ACCESS_TOKEN="***************************************"
ACCESS_TOKEN_SECRET="*********************************"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of your account printed
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status(status='Updating using OAuth authentication via Tweepy!')
