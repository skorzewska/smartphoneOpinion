#!/usr/bin/python2
# -*- coding:utf8 -*-

"""System that rates (1-5) a review of a smartphone
"""

import codecs
import json
import stemmer
import sys

from sklearn import linear_model

import create_vectors


def get_regression(trainset, keywords):
    """Return regression
    """
    data = create_vectors.get_data(trainset, keywords)
    regression = linear_model.LinearRegression()
    regression.fit(data[0], data[1])
    return regression


def get_rating(text, regression, trainset, keywords, use_tfidf):
    """Return rating of given text
    """
    vec = create_vectors.count_vec(text, trainset, keywords, use_tfidf)
    return regression.predict(vec)


if __name__ == '__main__':
    OPINION = sys.argv[2].decode('utf-8')
    OPINION = create_vectors.split_to_words(OPINION)
    OPINION = stemmer.stem(OPINION)
    OPINION = " ".join(OPINION)
    print 'Loading trainset...'
    TRAINSET = create_vectors.load_text()
    print 'Choosing keywords...'
    KEYWORDS_FILE = sys.argv[1]
    with codecs.open(KEYWORDS_FILE, 'r', encoding='utf-8') as kfile:
        KEYWORDS = json.load(kfile)
        print 'Calculating regression function...'
        REGR = get_regression(TRAINSET, KEYWORDS)
        print 'Predicting rating...'
        print get_rating(OPINION, REGR, TRAINSET, KEYWORDS, False)
