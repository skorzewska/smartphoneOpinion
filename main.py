#!/usr/bin/python2
# -*- coding:utf8 -*-

"""System that rates (1-5) a review of a smartphone
"""

import codecs
import json
import pickle
import stemmer
import sys

from sklearn import linear_model

import create_vectors


def get_regression_from_file(regr_file):
    """Deserialize regression from file
    """
    return pickle.load(open(regr_file, 'rb'))


def get_rating(text, regression, trainset, keywords, use_tfidf):
    """Return rating of given text
    """
    vec = create_vectors.count_vec(text, trainset, keywords, use_tfidf)
    return regression.predict(vec)


if __name__ == '__main__':
    OPINION = " ".join(stemmer.stem(
        create_vectors.split_to_words(sys.argv[2].decode('utf-8'))))
    TRAINSET = create_vectors.load_text()
    KEYWORDS_FILE = sys.argv[1]
    REGRESSION_FILE = 'regr_for_{}'.format(KEYWORDS_FILE)
    with codecs.open(KEYWORDS_FILE, 'r', encoding='utf-8') as kfile:
        KEYWORDS = json.load(kfile)
        REGR = get_regression_from_file(REGRESSION_FILE)
        print get_rating(OPINION, REGR, TRAINSET, KEYWORDS, False)
