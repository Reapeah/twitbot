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
print(now.hour,now.minute)

curr_hour = 0
curr_min = 50

while True:
    if now.minute == curr_min:        
        word="The current time is " + now.hour + ":" + now.minute
        curr_min += 10
        if curr_min >= 60:
            curr_min = 0
        api.update_status(word)    
        time.sleep(120)
#api.update_status('Hello World')
