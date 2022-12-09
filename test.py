# import twitter
# from twython import Twython
# ALSO trying https://www.dynaconf.com/
# pip install dynaconf

# %% [markdown]
from config import settings
import tweepy

print(settings.mycoolsetting)
print(settings.myint)
# My markdown
# %%
# # Consumer keys and access tokens, used for OAuth
consumer_secret = settings. apk_secret
consumer_key =  settings.api_key
# %%
client = tweepy.Client(bearer_token= settings.bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token= settings.access_token,
                       access_token_secret= settings.access_token_secret)
# %%
response = client.get_user(username=settings.username)
userid = response.data.id
# show user id
print(f"User ID: {userid}")
# %%
tweets = client.get_users_tweets(userid, max_results=10)
for t in tweets.data:
    print(t.text)
# %%
