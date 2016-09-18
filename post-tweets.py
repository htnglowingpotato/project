import tweepy, requests, json
from textblob.classifiers import NaiveBayesClassifier
from posorneg import posorneg

auth = tweepy.OAuthHandler("HGpIzfstBHMSLgGGVI43LVMGC", "sCoIuJx4UxFdiBFCMUdA8V6qPgnJk1Y6P6E03pu6kWf5mqAPK8")
auth.set_access_token("320874505-DnA2A0GUUJhOMdF0xyqT3mOlLfchxht8pwL13I58", "sqvSDjLXcs4uB3urlMDIx7KGi5XigSJIlnZe3iwuR9RzU")

api = tweepy.API(auth)

url = 'https://hackthenorth-b9b85.firebaseio.com/negtweets.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme'

for x in range(1, 2):
    public_tweets = api.user_timeline("realdonaldtrump",page=x)
    for tweet in public_tweets:
        # print tweet.text + "," + str(tweet.retweet_count)

        txt = tweet.text
        txt = ''.join(i for i in txt if ord(i)<128)

        print posorneg(txt)
        if posorneg(txt) == "neg":
            data = {"message":txt,"retweets":str(tweet.retweet_count),"classification":posorneg(txt)}
            print data

            parsed = json.dumps(data)

            response = requests.post(url, data=parsed)
            # print response.text
