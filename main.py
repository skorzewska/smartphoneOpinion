#!/usr/bin/python2
# -*- coding:utf8 -*-

"""System that rates (1-5) a review of a smartphone
"""

import create_vectors
import sys

from sklearn import linear_model


def get_regression(trainset, keywords):
    """Return regression
    """
    data = create_vectors.get_data(trainset, keywords)
    regression = linear_model.LinearRegression()
    regression.fit(data[0], data[1])
    return regression


def get_rating(text, regression, trainset, keywords):
    """Return rating of given text
    """
    vec = create_vectors.count_vec(text, trainset, keywords)
    return regression.predict(vec)


if __name__ == '__main__':
    OPINION = sys.argv[1]
    print 'Loading trainset...'
    TRAINSET = create_vectors.load_text()
    print 'Choosing keywords...'
    KEYWORDS = create_vectors.choose_words(TRAINSET)
    print 'Calculating regression function...'
    REGR = get_regression(TRAINSET, KEYWORDS)
    print 'Predicting rating...'
    print get_rating(OPINION, REGR, TRAINSET, KEYWORDS)
