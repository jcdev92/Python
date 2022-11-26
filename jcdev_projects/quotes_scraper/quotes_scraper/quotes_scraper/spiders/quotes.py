import scrapy
import os
# Title
## h1/a/text() 

# Citas 
## //span[@class="text" and @itemprop="text"]/text()

# Top Ten Tags
## //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()

# Next Page Button 
## '//li[@class="next"]/a/@href'

class quotesSpider(scrapy.Spider):
    
    name = 'quotes'

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    if os.path.exists('quotes.json'):
         os.remove("quotes.json")
    

    custom_settings = {
        "FEEDS": {"quotes.json" : {"format":"json"}},
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2024,
        'MEMUSAGE_NOTIFY_MAIL': ['jcdeveloper92@gmail.com'],
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT' : 'JCDEV',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
            author = kwargs['author']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        author.extend(response.xpath('//small/text()').getall())
        next_page_button_link = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_quotes, cb_kwargs={'quotes': quotes, 'author': author})
        else: 
            yield {
                'quotes' : quotes,
                'author' : author
            }
    

    def parse(self, response):
        title = response.xpath('//h1/a/text() ').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        author = response.xpath('//small/text()').getall()
        top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield {
            'title': title,
            'top_tags': top_tags
        }

        next_page_button_link = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_quotes, cb_kwargs={'quotes': quotes, 'author': author})       
