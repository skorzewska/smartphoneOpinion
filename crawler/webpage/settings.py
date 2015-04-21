# Scrapy settings for project

SPIDER_MODULES = ['webpage.spiders']
NEWSPIDER_MODULE = 'webpage.spiders'
DEFAULT_ITEM_CLASS = 'webpage.items.Website'

ITEM_PIPELINES = ['webpage.pipelines.FilterWordsPipeline']