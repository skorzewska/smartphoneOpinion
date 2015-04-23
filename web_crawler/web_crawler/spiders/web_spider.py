from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re
from scrapy.http import Request
from BeautifulSoup import BeautifulSoup
import codecs

class WebSpider(BaseSpider):
    name = "web_spider"

    start_urls = [
        "http://www.ceneo.pl/32065633#tab=reviews",
        "http://www.ceneo.pl/32065633/opinie-2",
        "http://www.ceneo.pl/32065633/opinie-3",
        "http://www.ceneo.pl/32065633/opinie-4",
        "http://www.ceneo.pl/32065633/opinie-5",
        "http://www.ceneo.pl/32065633/opinie-6",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select("//a/@href").extract()
        ratings = hxs.select("//dl[@class='product-review-score']/dd/text()").extract()
        reviews = hxs.select("//div/p[@class='product-review-body']/text()").extract()

        ratings = [rating.strip('\r\n\t ') for rating in ratings]    
        ratings = filter(None, ratings)

        with codecs.open("opinie", 'a', encoding='utf8') as my_file:
            len_reviews = 0
            for item in range(len(ratings)):
            # for rating in ratings:
                if len(reviews[item]) > 50:
                    my_file.write(ratings[item])
                    my_file.write(";")
                    my_file.write(reviews[item])
                    my_file.write(";;;;\n")
                    len_reviews += 1

            print "==============================================="
            print "MAMY JUZ TYLE RECENZJI: "
            print len_reviews
            print "\n=============================================="

