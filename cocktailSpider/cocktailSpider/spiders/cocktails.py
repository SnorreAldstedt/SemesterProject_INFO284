from scrapy.spiders import CrawlSpider
from cocktailSpider.items import CocktailItem
import scrapy
from cocktailSpider.cocktails_selenium import get_cocktails

# Specify which site you get your urls from.
# cocktails_selenium.py has to be customized if site is changed.
site = 'https://www.makemycocktail.com/sitemap.xml'

class drinkSpider(CrawlSpider):
    name = "cocktails"
    allowed_domains = ['www.makemycocktail.com']

    def start_requests(self):
        urls = get_cocktails(site)
        print(len(urls))
        return [scrapy.Request(url=url, callback=self.parse_items) for url in urls]


    def parse_items(self, response):
        cocktail = CocktailItem()
        cocktail['url'] = response.url
        cocktail['title'] = response.xpath('(//h1)[2]/text()').extract_first()
        cocktail['ingredients'] = response.xpath("(//*/table[@class='w3-table w3-striped w3-bordered']/tbody)[1]/tr/td[2]/text()").getall()
        cocktail['ing_amount'] = response.xpath("(//*/table[@class='w3-table w3-striped w3-bordered']/tbody)[1]/tr/td[4]/text()").getall()
        cocktail['preparation'] = response.xpath("(//*/table[@class='w3-table w3-striped w3-bordered']/tbody)[4]/tr/td/ol/li/text()").getall()
        yield cocktail

