# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StackItem(Item):
    title = Field()
    url = Field()

class QuoteItem(Item):
    author = Field()
    content = Field()
    tags = Field()