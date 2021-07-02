import pprint
import tweepy as tw
from dotenv import load_dotenv
import os 
from collections import Counter

from test_data import likes_by_user 



#--------
#--------




load_dotenv()

CONSUMER_KEY = os.environ.get("API_KEY")
CONSUMER_SECRET = os.environ.get("API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)

#-----------
#-----------


me = api.me()
friends = api.friends(me.name)
latest_follow = friends[0]

# Get liked tweets    (: Tweet)
# liked_tweets = [item for item in tw.Cursor(api.favorites, name=me.name).items(1000)]

# Extract usernames
# liked_accounts  = [tweet.user for tweet in liked_tweets]

# Count combine with above - nested comprehension?
# likes_by_user = Counter([user.name for user in liked_accounts])

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(likes_by_user)

# print(likes_by_user)

print(len(likes_by_user))