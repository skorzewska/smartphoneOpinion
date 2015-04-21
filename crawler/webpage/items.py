from scrapy.item import Item, Field


class Website(Item):

    text = Field()
    filename = Field()