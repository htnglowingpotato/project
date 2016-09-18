import random
from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import movie_reviews

# Thank you http://stackoverflow.com/questions/14663428/python-cleaning-words-in-a-sentence
#Cleaning Sentence
def remove_unw2anted(str):
    str = ''.join([c for c in str if c in 'ABCDEFGHIJKLNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890\''])
    return str

def clean_sentence(s):
    lst = [word for word in s.split()]

    lst_cleaned = []
    for items in lst:
        lst_cleaned.append(remove_unw2anted(items))
    return ' '.join(lst_cleaned)

try:
    bswords = open("rt-polaritybs.txt", "r")
    poswords = open("rt-polaritypos.txt", "r")
    # print ("files successfully opened")
except IOError:
    print ("error, could not open file")

#Establish poswords and bswords as lists
pos_words = []
bs_words = []

#Strip each line of text
pos_words = [line.strip() for line in poswords]
bs_words = [line.strip() for line in bswords]
cleanpos = [clean_sentence(x) for x in pos_words]
cleanbs = [clean_sentence(x) for x in bs_words]
# print (cleanbs)
# setting up while loops
i = 0
pos = []
bs = []
while i<len(cleanpos):
    pos.append("pos")
    i+=1
pos_tweets = list(zip(cleanpos, pos))
# print (newpos)
i = 0
while i<len(cleanbs):
    bs.append("neg")
    i+=1
neg_tweets = list(zip(cleanbs, bs))

train = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    train.append((words_filtered, sentiment))

test = [
(['feel', 'happy', 'this', 'morning'], 'pos'),
(['larry', 'friend'], 'pos'),
(['not', 'like', 'that', 'man'], 'neg'),
(['house', 'not', 'great'], 'neg'),
(['your', 'song', 'annoying'], 'neg')]

cl = NaiveBayesClassifier(train)

reviews = [(list(movie_reviews.words(fileid)), category)
  for category in movie_reviews.categories()
  for fileid in movie_reviews.fileids(category)]
new_train, new_test = reviews[0:100], reviews[101:200]
cl.update(new_train)
accuracy = cl.accuracy(test + new_test)
# print(cl.classify("Their burgers are amazing"))
# print(cl.classify("But the hangover was horrible. My boss was not happy."))
# print(cl.classify("There is a guy who has got nothing going, a waste!"))
# print(cl.accuracy(test))

def posorneg(tweet):
    return cl.classify(tweet)
