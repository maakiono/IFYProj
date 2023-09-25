import tweepy

class twitter():
    def __init__(self,dat) -> None:
        try:
            auth = tweepy.OAuthHandler(dat["consumer_key"], dat["consumer_secret"])
            auth.set_access_token(dat["access_token"], dat["access_token_secret"])
            api = tweepy.API(auth)
            news_keywords = dat["news_keywords"]
            print("Twitter API authentication Successfull, watching for data!")
        except Exception as x:
            print("Twitter Scraper failed to authenticate, stopping")
            print("Error:",x)
            return
        class StreamListener(tweepy.StreamListener):
            def on_status(self, status):
                print(f'New tweet from @{status.user.screen_name}: {status.text}')
        stream_listener = StreamListener()
        stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
        stream.filter(track=news_keywords)

