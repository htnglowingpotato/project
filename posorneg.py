from textblob.classifiers import NaiveBayesClassifier

#sees if files can be opened
try:
    bswords = open("rt-polaritybs.txt", "r")
    poswords = open("rt-polaritypos.txt", "r")
    negwords2 = open("negativewords.txt", "r")
    poswords2 = open("positivewords.txt", "r")
    # print ("files successfully opened")
except IOError:
    print ("error, could not open file")

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

#Establish poswords and bswords as lists
pos_words = []
bs_words = []

#Strip each line of text
# our own classified trump data
pos_words = [line.strip() for line in poswords]
bs_words = [line.strip() for line in bswords]
#clean each sentence of extra characters
cleanpos = [clean_sentence(x) for x in pos_words]
cleanbs = [clean_sentence(x) for x in bs_words]
# print (cleanbs)

# create tuples with ("tweet", "pos")
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

#split up tweet into individual strings attached to tag (pos/neg)
train = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    train.append((words_filtered, sentiment))

#small test sample
#thanks http://stevenloria.com/how-to-build-a-text-classification-system-with-python-and-textblob/
test = [
(['feel', 'happy', 'this', 'morning'], 'pos'),
(['larry', 'friend'], 'pos'),
(['not', 'like', 'that', 'man'], 'neg'),
(['house', 'not', 'great'], 'neg'),
(['your', 'song', 'annoying'], 'neg')]

#our basic classification system
cl = NaiveBayesClassifier(train)

# Comment out if too slow, uses a lot of data

# movie reviews data
poswords2 = [x.strip(".\n") for x in poswords2]
poswords2 = [clean_sentence(x) for x in poswords2]
poswords20 = [x.split(",") for x in poswords2]

poswords3 = []
i=0
while i<len(poswords20):
    poswords3.append("pos")
    i+=1
posadjectives = list(zip(poswords2, poswords3))
#change second number to make the dataset bigger and more accurate
posadj = posadjectives[1:250]

negwords2 = [x.strip(".\n") for x in negwords2]
negwords2 = [clean_sentence(x) for x in negwords2]
negwords20 = [x.split(",") for x in negwords2]

negwords3 = []
i=0
while i<len(negwords20):
    negwords3.append("neg")
    i+=1
negadjectives = list(zip(negwords2, negwords3))
#change second number to make the dataset bigger and more accurate
negadj = negadjectives[1:250]

train2 = []
for (words, sentiment) in posadj + negadj:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    train2.append((words_filtered, sentiment))
# print(train2)

cl.update(train2)

print(cl.accuracy(test))

def posorneg(tweet):
    return cl.classify(tweet)

# print(posorneg("Their burgers are amazing"))
# print(posorneg("There is a guy who has got nothing going, a waste!"))
# print(posorneg("But the hangover was horrible. My boss was not happy."))
# print(posorneg("Great poll Florida - thank you! #ImWithYou #AmericaFirst"))
