from time import sleep
import tweepy as tw
from dotenv import load_dotenv
import os 


load_dotenv()

CONSUMER_KEY = os.environ.get("API_KEY")
CONSUMER_SECRET = os.environ.get("API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# print(CONSUMER_KEY)
# print(CONSUMER_SECRET)
# print(ACCESS_TOKEN)
# print(ACCESS_TOKEN_SECRET)

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)
friends = api.friends("oli_c_g")

print(friends[0].name)
latest_follow = friends[0]

api.destroy_friendship(latest_follow.id)

friendships = api.lookup_friendships([latest_follow.id, friends[7].id])

print(friendships, file=open("friendships.txt", "w"))