#!/usr/bin/python2
# -*- coding:utf8 -*-

"""Create regression function and dump it to file
"""

import codecs
import json
import pickle
import sys

from sklearn import linear_model

import create_vectors


def get_regression_from_keywords(trainset, keywords):
    """Return regression
    """
    data = create_vectors.get_data(trainset, keywords, False)
    regression = linear_model.LinearRegression()
    regression.fit(data[0], data[1])
    return regression


def get_regression(trainset, keywords_file):
    """Return regression
    """
    with codecs.open(keywords_file, 'r', encoding='utf-8') as kfile:
        return get_regression_from_keywords(trainset, json.load(kfile))
    return False


if __name__ == '__main__':
    TRAINSET = create_vectors.load_text()
    KEYWORDS_FILE = sys.argv[1]
    REGR = get_regression(TRAINSET, KEYWORDS_FILE)
    if REGR:
        pickle.dump(REGR, open('regr_for_{}'.format(KEYWORDS_FILE), 'wb'))
