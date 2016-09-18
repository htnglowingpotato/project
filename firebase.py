import tweepy, requests, json, datetime

auth = tweepy.OAuthHandler("HGpIzfstBHMSLgGGVI43LVMGC", "sCoIuJx4UxFdiBFCMUdA8V6qPgnJk1Y6P6E03pu6kWf5mqAPK8")
auth.set_access_token("320874505-DnA2A0GUUJhOMdF0xyqT3mOlLfchxht8pwL13I58", "sqvSDjLXcs4uB3urlMDIx7KGi5XigSJIlnZe3iwuR9RzU")

api = tweepy.API(auth)

urlAndroid = 'https://hackthenorth-b9b85.firebaseio.com/android.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme'
urliPhone = 'https://hackthenorth-b9b85.firebaseio.com/iphone.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme'
urliPad = 'https://hackthenorth-b9b85.firebaseio.com/ipad.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme'
urlWeb = 'https://hackthenorth-b9b85.firebaseio.com/web.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme'
urlOther = 'https://hackthenorth-b9b85.firebaseio.com/other.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme'
for x in range(1, 100000000):
    public_tweets = api.user_timeline("realdonaldtrump",page=x)

    for tweet in public_tweets:
        if tweet.created_at <= datetime.datetime(2016, 8, 1):
            break
        txt = tweet.text
        txt = ''.join(i for i in txt if ord(i)<128)

        data = {"message":txt,"retweets":str(tweet.retweet_count), "source": tweet.source, "date": str(tweet.created_at)}

        parsed = json.dumps(data)

        if tweet.source == "Twitter for iPhone":
            response = requests.post(urliPhone, data=parsed)
        elif tweet.source == "Twitter for Android":
            response = requests.post(urlAndroid, data=parsed)
        elif tweet.source == "Twitter Web Client":
            response = requests.post(urlWeb, data=parsed)
        elif tweet.source == "Twitter for iPad":
            response = requests.post(urliPad, data=parsed)
        else:
            response = requests.post(urlOther, data=parsed)
        print response.text
    else:
        continue
    break
