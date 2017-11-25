from slistener import SListener
import settings as st
import time, tweepy, sys

## authentication
# username = ''  ## put a valid Twitter username here
# password = ''  ## put a valid Twitter password here
# auth = tweepy.auth.BasicAuthHandler(username, password)
# api = tweepy.API(auth)

auth = tweepy.OAuthHandler(st.CONSUMER_KEY, st.CONSUMER_SECRET)
auth.set_access_token(st.ACCESS_TOKEN, st.ACCESS_TOKEN_SECRET)
GTA=[-80.35,43.22,-78.75,44.09]
USA=[-124.848974, 24.396308,-66.885444, 49.384358]
NA=[-127.53,25.01,-61.08,56.32]


def main():
    tracks = ["StrangerThings","Stranger_Things"]
    twitter_stream = tweepy.Stream(auth, SListener())
    print("Streaming started...")
    try:
        #twitter_stream.filter(track=tracks, locations=GTA, async=True)  # does not accept two filters simultaneously
        twitter_stream.filter(locations=NA, async=True)
    except:
        print("error!")
        twitter_stream.disconnect()

if __name__ == '__main__':
    main()