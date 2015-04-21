from scrapy.exceptions import DropItem

import os.path


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    def process_item(self, item, spider):
        num = 1
        while os.path.isfile(str(num) + '.txt'):
            num += 1
        with open(str(num) + '.txt', 'w') as myFile:
            myFile.write(item['text'].encode('utf-8'))
        #return item

        with open(str(num) + '.txt', 'r') as readFile:
            readFile.seek(0)
            first_char = readFile.read(1)
            if not first_char:
                os.remove(str(num) + '.txt')
