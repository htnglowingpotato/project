# Thanks https://github.com/abromberg/sentiment_analysis_python/blob/master/sentiment_analysis.py

import re, math, collections, itertools, os
import nltk
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

# Check if NLTK is installed
# print('The nltk version is {}.'.format(nltk.__version__))
# NLTK test
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print tokens

#Feature Selection is variable / attribute selection
#It is the automatic selection of attributes in your data (such as columns in tabular data) that are most relevant to the predictive modeling problem you are working on.
#Source: http://machinelearningmastery.com/an-introduction-to-feature-selection/


# this function takes a feature selection mechanism and returns its performance in a variety of metrics
# def evaluate_features(feature_select):
# posFeatures = []
# negFeatures = []
# with open("text_files/negativewords.txt", "r") as posWords:
#     print "opened"
#     for i in posWords:
#         pos_words = [feature_select(posWords), "pos"]
#         posFeatures.append(pos_words)
# with open ("text_files/positivewords.txt", "r"):
#     for i in negWords:
#         neg_words = [feature_select(negWords), "neg"]
#         negFeatures.append(neg_words)

# evaluate_features(feature_select)

#     	#selects 3/4 of the features to be used for training and 1/4 to be used for testing
# 	posCutoff = int(math.floor(len(posFeatures)*3/4))
# 	negCutoff = int(math.floor(len(negFeatures)*3/4))
# 	trainFeatures = posFeatures[:posCutoff] + negFeatures[:negCutoff]
# 	testFeatures = posFeatures[posCutoff:] + negFeatures[negCutoff:]
#
# 	#trains a Naive Bayes Classifier
# 	classifier = NaiveBayesClassifier.train(trainFeatures)
#
# 	#initiates referenceSets and testSets
# 	referenceSets = collections.defaultdict(set)
# 	testSets = collections.defaultdict(set)
#
# 	#puts correctly labeled sentences in referenceSets and the predictively labeled version in testsets
# 	for i, (features, label) in enumerate(testFeatures):
# 		referenceSets[label].add(i)
# 		predicted = classifier.classify(features)
# 		testSets[predicted].add(i)
#
# 	#prints metrics to show how well the feature selection did
# 	print 'train on %d instances, test on %d instances' % (len(trainFeatures), len(testFeatures))
# 	print 'accuracy:', nltk.classify.util.accuracy(classifier, testFeatures)
# 	print 'pos precision:', nltk.metrics.precision(referenceSets['pos'], testSets['pos'])
# 	print 'pos recall:', nltk.metrics.recall(referenceSets['pos'], testSets['pos'])
# 	print 'neg precision:', nltk.metrics.precision(referenceSets['neg'], testSets['neg'])
# 	print 'neg recall:', nltk.metrics.recall(referenceSets['neg'], testSets['neg'])
# 	classifier.show_most_informative_features(10)

# try:
#     myfile= open("text_files/negativewords.txt", "r")
#     print "file successfully opened"
# except IOError:
#     print "error, could not open file"
