import codecs


def load_text():
    opinions = {}
    with codecs.open('opinie1', 'r', encoding='utf-8') as my_file:
        for line in my_file:
            if ";" not in line:
                print line
            else:
                pair = line.split(";", 2)
                key = pair[1]
                value = pair[0]
                if key in opinions:
                    print key
                opinions[key] = float(value)
        return opinions


def get_data():
    """TODO
    """
    return [[[1.5, 2.5], [2.5, 1.5]], [2.0, 4.0]]


def get_tfidf(text):
    """TODO
    """
    return [2.0, 2.0]
