import pprint
import tweepy as tw
from dotenv import load_dotenv
import os 
from collections import Counter
from analysis import show_distribution_likes

# use test_data for dev when possible to limit API requests
from test_data import likes_by_user 


load_dotenv()
pp = pprint.PrettyPrinter(indent=4)


CONSUMER_KEY = os.environ.get("API_KEY")
CONSUMER_SECRET = os.environ.get("API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)

me = api.me()

# Get liked tweets    (: Tweet)
# liked_tweets = [item for item in tw.Cursor(api.favorites, name=me.name).items(1000)]

# Extract usernames
# liked_accounts  = [tweet.user for tweet in liked_tweets]

# Count combine with above - nested comprehension?
# likes_by_user = Counter([user.name for user in liked_accounts])

# Get list of users whose tweets you've liked
liked_users = likes_by_user.keys()

# Get friends
following = [user for user in tw.Cursor(api.friends, name=me.name).items()] # list of friends
following_names = [user.name for user in following] # List of name strings

print(following_names, end="   ")
print(len(following_names))

# Working but following_names not full because of pagination
least_liked_friends = [user for user in following_names 
                       if user not in likes_by_user.keys()
                       or likes_by_user[user] < 2]


print(least_liked_friends)

def manage_friends_insomeway():
  pass