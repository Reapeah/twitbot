import tweepy
from datetime import date
import calendar
import time
import datetime

now = datetime.datetime.now()

my_date = date.today()
calendar.day_name[my_date.weekday()]



ckey ='aDnftecvhJVUmMcOkNEtWUhPu'
csecret = 's7dSrZ75TfkTb1JIcelQeSb3vGETWqXdWvjm17yzZWuoR77l5X'
akey ='369656146-WKyNfoPVEE0w1VTlu5VFQnFzUaNa880HkFfbk57D'
asecret = 'kng4JBJLATTVGkUpWZ8KG6YJicLUNwpbxNrW09nBx7iLW'

auth =  tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api = tweepy.API(auth)

while True:
    if now.hour == 0 and now.minute == 0:
        word="Today is " + str(calendar.day_name[my_date.weekday()]) +" which means it's " + str(calendar.day_name[my_date.weekday()])
        api.update_status(word )
        time.sleep(120)
#api.update_status('Hello World')
