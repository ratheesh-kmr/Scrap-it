import scrapy
from ..items import ScrapItItem

class Scr1Spider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # Create an instance of ScrapItItem
            items = ScrapItItem()
            
            # Extract data
            items["text"] = quote.css('span.text::text').get()
            items["author"] = quote.css('span small.author::text').get()
            items["tags"] = quote.css('div.tags a.tag::text').getall()

            # Yield the item
            yield items
