import requests, json, random
url = 'https://hackthenorth-b9b85.firebaseio.com/negtweets.json?auth=k8oUcZFSAcbBZpHcQkyTPeepFj8ckSG4zQcp1tme&print=pretty'
response = requests.get(url)
json.loads(response.text)[random.choice(list(json.loads(response.text).keys()))]['message']
