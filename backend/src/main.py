import pprint
from time import sleep
from requests.sessions import get_netrc_auth
import tweepy as tw
from dotenv import load_dotenv
import os 
from collections import Counter
from analysis import show_distribution_likes

# use test_data for dev when possible to limit API requests
from test_data import likes_by_user_test, following_names_test


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


def get_likes_by_user(me_name):
  # Get liked tweets
  liked_tweets = [item for item in tw.Cursor(api.favorites, name=me_name).items(20)]
  # Extract usernames
  liked_users  = [tweet.user for tweet in liked_tweets]
  # make counter dict
  likes_by_user = Counter([user.name for user in liked_users])
  return likes_by_user


def get_following(me_name):
  following = []
  print('getting users you are following (friends) ...')
  for user in tw.Cursor(api.friends, name=me_name).items():
    print(user.name)
    following.append(user)
    sleep(2)
  following_names = [user.name for user in following] # List of name strings
  return following_names


def get_least_liked_friends(following_names, likes_by_user):
  least_liked_friends = list(filter((lambda user: user not in likes_by_user.keys() or likes_by_user[user] < 2), following_names))
  return least_liked_friends


# likes_by_user = get_likes_by_user(me.name)
likes_by_user = likes_by_user_test

# following_names = get_following(me.name)
following_names = following_names_test

least_liked_friends = get_least_liked_friends(following_names, likes_by_user)

print(f"Users you might want to unfollow: \n{least_liked_friends}")







