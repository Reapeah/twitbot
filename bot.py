import tweepy

ckey ='aDnftecvhJVUmMcOkNEtWUhPu'
csecret = 's7dSrZ75TfkTb1JIcelQeSb3vGETWqXdWvjm17yzZWuoR77l5X'
akey ='369656146-WKyNfoPVEE0w1VTlu5VFQnFzUaNa880HkFfbk57D'
asecret = 'kng4JBJLATTVGkUpWZ8KG6YJicLUNwpbxNrW09nBx7iLW'

auth =  tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api = tweepy.API(auth)
c=1
while True:
    word='Hello' + str(c)
    api.update_status(word )
    c+=1

#api.update_status('Hello World')
