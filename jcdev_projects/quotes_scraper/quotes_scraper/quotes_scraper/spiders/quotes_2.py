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
    name = 'new_q'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    #if os.path.exists('quotes_2.csv'):
    #    os.remove("quotes_2.csv")

    custom_settings = {
        "FEEDS":{"quotes_2.csv":{"format":"csv"}}
    }

    def parse(self, response):
        title = response.xpath('//h1/a/text() ').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        
        for i in range(len(quotes)):
            yield {
                'title': title,
                'quote' : quotes[i],
                'ten_tags': ten_tags[i]
            }
        
        next_page_button_link = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)



        
