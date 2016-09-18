from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import math
import os
import random
import zipfile
import itertools
import string

import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf


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
#Combine positive words and negative words
dataset = pos_words + bs_words
#Remove other characters
dataset2 = [clean_sentence(x) for x in dataset]
#Remove whitespace
dataset2 = [x.split() for x in dataset2]
#Flatten list of lists
merged = list(itertools.chain.from_iterable(dataset2))
#Lowercase for all strings
merged = [x.lower() for x in merged]
