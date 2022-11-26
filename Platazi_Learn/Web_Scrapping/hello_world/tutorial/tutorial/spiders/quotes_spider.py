import scrapy

class quotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        with open('resultados.html', 'w', encoding='utf8') as f:
            f.write(response.text)
            