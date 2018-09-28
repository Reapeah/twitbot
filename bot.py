import tweepy
import os
from datetime import date
import calendar
import time
import datetime

now = datetime.datetime.now()

my_date = date.today()
calendar.day_name[my_date.weekday()]



ckey = os.getenv('CKEY')
csecret = os.getenv('CSECRET')
akey = os.getenv('AKEY')
asecret = os.getenv('ASECRET')

auth =  tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api = tweepy.API(auth)

while True:
    print('9')
#api.update_status('Hello World')
