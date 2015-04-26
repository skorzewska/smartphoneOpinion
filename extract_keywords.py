#!/usr/bin/python2
# -*- coding:utf8 -*-

"""Extracts words that mean 'good' or 'bad' from trainset
"""

import codecs
import json

import create_vectors


GOOD_THRESHOLD = 4.5
BAD_THRESHOLD = 3.0

KEYWORDS_FILE = 'keywords'


def extract_good_and_bad_keywords(trainset):
    """Extract good and bad keywords from trainset into two lists
    """
    good_keywords = []
    bad_keywords = []
    goods = []
    bads = []
    alls = []
    words = set()

    for opinion, stars in trainset.iteritems():
        opinion_contents = opinion.split()
        if stars > GOOD_THRESHOLD:
            goods.extend(opinion_contents)
        elif stars < BAD_THRESHOLD:
            bads.extend(opinion_contents)
        alls.extend(opinion_contents)
        words.update(opinion_contents)

    good_sthres = float(len(goods)) / (len(goods) + len(bads))
    bad_sthres = float(len(bads)) / (len(goods) + len(bads))

    for i, word in enumerate(words):
        all_count = float(alls.count(word))
        if all_count > 1:
            if goods.count(word)/all_count > good_sthres:
                good_keywords.append(word)
            if bads.count(word)/all_count > bad_sthres:
                bad_keywords.append(word)
        create_vectors.update_progress((i + 1) * 100 / len(words))
    print

    return (good_keywords, bad_keywords)


def extract_all_keywords(trainset):
    """Extracts good and bad keywords from trainset into one list
    """
    keywords = extract_good_and_bad_keywords(trainset)
    return keywords[0] + keywords[1]


if __name__ == '__main__':
    TRAINSET = create_vectors.load_text()
    KEYWORDS = extract_all_keywords(TRAINSET)
    with codecs.open(KEYWORDS_FILE, 'w', encoding='utf-8') as kfile:
        json.dump(KEYWORDS, kfile)
