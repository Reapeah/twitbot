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

while True:
    now = datetime.datetime.now()
    my_date = date.today()
    calendar.day_name[my_date.weekday()]
    if now.hour == 0 and now.minute == 0:        
        word="Today is " + str(calendar.day_name[my_date.weekday()]) +" which means it's " + str(calendar.day_name[my_date.weekday()]) + ' #' + str(calendar.day_name[my_date.weekday()])            
        api.update_status(word)    
        time.sleep(120)






