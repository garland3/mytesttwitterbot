
# # read tweets from a user
# user = "@AnthonyPGarland"
# # get the tweets
# twitter = Twython(api_key, apk_secret, oauth_version=2)
# ACCESS_TOKEN = twitter.obtain_access_token()
# twitter = Twython(api_key, access_token=ACCESS_TOKEN)
# tweets = twitter.get_user_timeline(screen_name=user, count=200)
# for tweet in tweets:
#     print(tweet['text'])

# Import the necessary libraries
# import tweepy

# # Enter your Twitter API keys and tokens here
# consumer_key = "YOUR_CONSUMER_KEY"
# consumer_secret = "YOUR_CONSUMER_SECRET"
# access_token = "YOUR_ACCESS_TOKEN"
# access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# # Authenticate with the Twitter API using your keys and tokens
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# # Set up a listener that will respond to mentions of your bot's account
# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         if "@YOUR_BOT_USERNAME" in status.text:
#             api.update_status(
#                 "Thank you for mentioning me! Here is a pre-written response.",
#                 in_reply_to_status_id=status.id)

# # Create a stream object and start listening for mentions of your bot's account
# my_stream_listener = MyStreamListener()
# stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)
# stream.filter(track=["@YOUR_BOT_USERNAME"])