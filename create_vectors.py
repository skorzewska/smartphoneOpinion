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