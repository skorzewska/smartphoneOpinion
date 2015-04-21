from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from webpage.items import Website

import re
from scrapy.http import Request
from goose import Goose


class WebSpider(BaseSpider):
    name = "web_spider"
    allowed_domains = ["swimming.about.com"]

    start_urls = [
        "http://swimming.about.com/",
    ]

    rules = (Rule(SgmlLinkExtractor(), callback='parse', follow=True), )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select("//a/@href").extract()

        # We stored already crawled links in this list
        crawledLinks = []

        # Pattern to check proper link
        linkPattern = re.compile(
            """^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+
                ]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?
                \+=&%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&%@!\-\/\(\)]+))?$""")

        for link in links:
            if linkPattern.match(link) and not link in crawledLinks:
                crawledLinks.append(link)
                yield Request(link, self.parse)

        # Goose dziala lepiej, niz soup, do tego moze wyciagac img
        # moze wyciagac tekst, albo z url, albo z czystego html
        g = Goose()
        raw_html = response.body
        article = g.extract(raw_html=raw_html)
        text = article.cleaned_text
        if text.isspace() or not text:
            pass

        item = Website()
        item['text'] = text
        item['filename'] = '1.txt'
        yield item