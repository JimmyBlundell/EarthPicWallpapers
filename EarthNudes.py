import praw
import urllib.request

reddit = praw.Reddit(client_id = 'zpLjVh3uoEoWog',
                     client_secret = 'j0cyR5uUR6zvGIDmSxSyO6-T9Ao',
                     username = 'theSuppleLemur',
                     password = '7mmRem.mag',
                     user_agent = 'EarthNudesv1')

subreddit = reddit.subreddit('EarthPorn')

todays_pic = subreddit.hot(limit = 1)

print(todays_pic.url)

response = urllib.request.urlopen('https://i.redd.it/ycnocy3ijeq11.jpg')

print(response)








 
    
                      
