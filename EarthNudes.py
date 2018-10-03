import praw

reddit = praw.Reddit(client_id = 'zpLjVh3uoEoWog',
                     client_secret = 'j0cyR5uUR6zvGIDmSxSyO6-T9Ao',
                     username = 'theSuppleLemur',
                     password = '7mmRem.mag',
                     user_agent = 'EarthNudesv1')

subreddit = reddit.subreddit('EarthPorn')

hot_pics = subreddit.hot(limit = 10)

for submission in hot_pics:
    if not submission.stickied:
        print(submission.title)
for comment in subreddit.comments(limit = 50):
    print(comment.author)

    

    
                      
