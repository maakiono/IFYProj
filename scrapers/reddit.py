import praw

class reddit():
    # def __init__(self,client_id,client_secret,username,password,user_agent,subreddits) -> None:
    def __init__(self,dat:dict) -> None:
        try: 
            reddit = praw.Reddit(
                client_id=str(dat["client_id"]),
                client_secret=str(dat["client_secret"]),
                username=str(dat["username"]),
                password=str(dat["password"]),   
                user_agent=str(dat["user_agent"])
            )
            subreddits = dat["subreddits"]
            print("Twitter API authentication Successfull, watching for data!")
        except KeyError as x:
            print("Required keys not provided, Failed to load Reddit Scraper")
            return x
        except Exception as x:
            print("Twitter Scraper failed to authenticate, stopping")
            print("Error:", x )
            return x
    
        subredditstream = {subreddit_name: reddit.subreddit(subreddit_name).stream.submissions() for subreddit_name in subreddits}

        while True:
            for subreddit, stream in subredditstream.items():
                try:
                    post = next(stream)
                    print(f'New post in /r/{subreddit}: {post.title}')
                except StopIteration:
                    print("Stopping Stream.")
                    pass
