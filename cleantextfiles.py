import collections
import nltk
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.probability import FreqDist, ELEProbDist
from nltk.classify.util import apply_features,accuracy
#
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
    pos.append("positive")
    i+=1
pos_tweets = list(zip(cleanpos, pos))
# print (newpos)
i = 0
while i<len(cleanbs):
    bs.append("negative")
    i+=1
neg_tweets = list(zip(cleanbs, bs))

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

test_tweets = [
(['feel', 'happy', 'this', 'morning'], 'positive'),
(['larry', 'friend'], 'positive'),
(['not', 'like', 'that', 'man'], 'negative'),
(['house', 'not', 'great'], 'negative'),
(['your', 'song', 'annoying'], 'negative')]

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

word_features = get_word_features(get_words_in_tweets(tweets))
print (word_features)

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# training_set = nltk.classify.apply_features(extract_features, tweets)
#
# def classifier(training_set):
#     return nltk.NaiveBayesClassifier.train(training_set)
#
# def train(labeled_featuresets, estimator=ELEProbDist):
#     # Create the P(label) distribution
#     label_probdist = estimator(label_freqdist)
#     ...
#     # Create the P(fval|label, fname) distribution
#     feature_probdist = {}
#     ...
#     return NaiveBayesClassifier(label_probdist, feature_probdist)
#
# def classify(tweet):
#     print classifier(classify(extract_features(tweet.split()))
