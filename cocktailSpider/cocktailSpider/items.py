# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CocktailItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    ingredients = scrapy.Field()
    ing_amount = scrapy.Field()
    preparation = scrapy.Field()
