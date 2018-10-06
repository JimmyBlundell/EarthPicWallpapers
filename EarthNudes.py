import praw

reddit = praw.Reddit(client_id = '---',
                     client_secret = '---',
                     username = '---',
                     password = '---',
                     user_agent = '---')

subreddit = reddit.subreddit('EarthPorn')

hot_pics = subreddit.hot(limit = 1)

for submission in hot_pics:
    if not submission.stickied:
        print(submission.title)

 
    
                      
