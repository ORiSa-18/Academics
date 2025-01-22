#Q1. WRITE A PROGRAM TO FIND OUT THE FREQUENCIES OF DISTINCT WORDS, GIVEN A SENTENCE USING N-GRAMS.

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

def n_grams(text,n):
    words = word_tokenize(text)
    nGrams = ngrams(words, n)
    return list(nGrams)

text = "I love Python"

n=2

bigrams = n_grams(text, n)

hmap = Counter(bigrams)

for pair in hmap:
    print(pair," ",hmap[pair])

#Additional Exercise: Q1. WRITE A PROGRAM TO FIND OUT THE FREQUENCIES OF DISTINCT WORDS, GIVEN A SENTENCE USING N-GRAMS.

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

def n_grams(text,n):
    words = word_tokenize(text)
    nGrams = ngrams(words, n)
    return list(nGrams)

text = "I love Python"

n=2

bigrams = n_grams(text, n)

hmap = Counter(bigrams)
total = len(bigrams)

for pair in hmap:
    print("P[",pair,"]=",hmap[pair]/total)

#Additional Exercise: Q2.Write a program to generate n-grams in reverse order (e.g., starting from the end of the sentence).

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

def n_grams(text,n):
    words = word_tokenize(text)
    nGrams = ngrams(words, n)
    return list(nGrams)

text = "I love Python"

n=2

bigrams = n_grams(text, n)
bigrams = bigrams[::-1]

for gram in bigrams:
    print(gram[::-1])
