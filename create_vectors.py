#!/usr/bin/python2
# -*- coding: utf-8 -*-

import codecs
import math


def load_text():
    opinions = {}
    with codecs.open('opinie1', 'r', encoding='utf-8') as my_file:
        for line in my_file:
            pair = line.split(";", 2)
            key = pair[1]
            value = pair[0]
            opinions[key] = float(value)
    return opinions

def split_to_words(doc):
    return doc.split()

def freq(word, doc):
    return doc.count(word)
  
def word_count(doc):
    return len(doc)
 
def tf(word, doc):
    return (freq(word, doc) / float(word_count(doc)))
 
def num_docs_containing(word, list_of_docs):
    count = 0
    for document in list_of_docs:
        if freq(word, document) > 0:
            count += 1
    return 1 + count
 
def idf(word, list_of_docs):
    return math.log(len(list_of_docs) /
            float(num_docs_containing(word, list_of_docs)))
 
 
def tf_idf(word, doc, list_of_docs):
    return (tf(word, doc) * idf(word, list_of_docs))

def count_tfidf(dictionary):
    result = []
    for key in dictionary.keys():
        key = split_to_words(key)
        tf_idf_result = [tf_idf(word, key, dictionary.keys()) for word in key]
        result.append(tf_idf_result)
    return result

def choose_words(dictionary):
    result = set()
    for i, key in enumerate(dictionary.keys()):
        key = split_to_words(key)
        maximum = 0
        for word in key:
            tfidf = tf_idf(word, key, dictionary.keys())
            if tfidf > maximum:
                maximum = tfidf
                best_word = word
        result.add(word)
        print i
    return result

def count_vec_list(dictionary):
    result = []
    words = choose_words(dictionary)
    for key in dictionary.keys():
        vector = count_vec(key, dictionary, words)
        result.append(vector)
    return result

def count_vec(text, dictionary, words):
    text = split_to_words(text)
    vector = []
    for word in words:
        if word in text:
            tf_idf_result = tf_idf(word, text, dictionary.keys())
        else:
            tf_idf_result = 0.0
        vector.append(tf_idf_result)
    return vector

def get_data(dictionary):
    vectors = []
    stars =[]
    words = choose_words(dictionary)
    for key, value in dictionary.iteritems():
        vector = count_vec(key, dictionary, words)
        vectors.append(vector)
        stars.append(value)
        print value
    return [vectors, stars]

