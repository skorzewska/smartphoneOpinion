#!/usr/bin/python2
# -*- coding:utf8 -*-

"""System that rates (1-5) a review of a smartphone
"""

import argparse
import codecs
import json
import pickle
import stemmer

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


def main(use_tfidf, opinion_text):
    """Print rating of given text
    """
    opinion = " ".join(stemmer.stem(
        create_vectors.split_to_words(opinion_text.decode('utf-8'))))
    trainset = create_vectors.load_text()
    if use_tfidf:
        keywords_file = 'tfidf_keywords'
    else:
        keywords_file = 'keywords'
    regression_file = 'regr_for_{}'.format(keywords_file)
    with codecs.open(keywords_file, 'r', encoding='utf-8') as kfile:
        keywords = json.load(kfile)
        regr = get_regression_from_file(regression_file)
        rating = get_rating(opinion, regr, trainset, keywords, use_tfidf)
        if rating < 0.0:
            rating = 0.0
        elif rating > 5.0:
            rating = 5.0
        print '{:.2f}'.format(rating)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description='Print rating of a given text')
    PARSER.add_argument(
        '-t', '--use_tfidf', action='store_true', help='Use TFIDF')
    PARSER.add_argument('opinion', help='Opinion text')
    ARGS = PARSER.parse_args()
    main(ARGS.use_tfidf, ARGS.opinion)
