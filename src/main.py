import tweepy as tw
from dotenv import load_dotenv
import os 


load_dotenv()

CONSUMER_KEY = os.environ.get("API_KEY")
CONSUMER_SECRET = os.environ.get("API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)


print(api.rate_limit_status())

me = api.me()

friends = api.friends(me.name)

latest_follow = friends[0]

# api.destroy_friendship(latest_follow.id)

print(latest_follow.id)
print(me.id)