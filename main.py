#!/usr/bin/python2
# -*- coding:utf8 -*-

"""System that rates (1-5) a review of a smartphone
"""

import create_vectors
import sys

from sklearn import linear_model


def get_regression():
    """Return regression
    """
    data = create_vectors.get_data()
    regression = linear_model.LinearRegression()
    regression.fit(data[0], data[1])
    return regression


def get_rating(text, regr):
    """Return rating of given text
    """
    vec = create_vectors.get_tfidf(text)
    return regr.predict(vec)


if __name__ == '__main__':
    OPINION = sys.argv[1]
    REGR = get_regression()
    print get_rating(OPINION, REGR)
