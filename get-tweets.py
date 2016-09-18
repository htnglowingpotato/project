import tweepy, requests, json

auth = tweepy.OAuthHandler("HGpIzfstBHMSLgGGVI43LVMGC", "sCoIuJx4UxFdiBFCMUdA8V6qPgnJk1Y6P6E03pu6kWf5mqAPK8")
auth.set_access_token("320874505-DnA2A0GUUJhOMdF0xyqT3mOlLfchxht8pwL13I58", "sqvSDjLXcs4uB3urlMDIx7KGi5XigSJIlnZe3iwuR9RzU")

api = tweepy.API(auth)

url = 'https://hackthenorth-b9b85.firebaseio.com/toptweets.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme'
topTweets = []
minRetweetCount = 10000000000000000000000
minTweet = {}
for x in range(40, 41):
    public_tweets = api.user_timeline("realdonaldtrump",page=x)
            print tweet.text + "," + str(tweet.retweet_count)

            txt = tweet.text
            txt = ''.join(i for i in txt if ord(i)<128)

            data = {"message":txt,"retweets":str(tweet.retweet_count)}
            # print data

            parsed = json.dumps(data)

            response = requests.post(url, data=parsed)
            print response.text
