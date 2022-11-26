import scrapy
import os

# Business Title
## '//h2[@class="qrShPb kno-ecr-pt PZPZlf q8U8x PPT5v hNKfZe"]/span/text()'

# Direction
## PATH 1  -----  '//*[@id="akp_tsuid10"]//div[2]/div/div/span[2]/text()'
## PATH 2  -----  '//*[@id="akp_tsuid10"]//div[3]/div/div[2]/div/div/span[2]/text()'

# Phone Number 
## response.xpath('//a[@data-dtype="d3ph"]//span/text()').get()

# Website URL 
## response.xpath('//a[@class="ab_button CL9Uqc"]/@href').get()

class contactsSpider(scrapy.Spider):
    name = 'contacts_scraper'
    allowed_domains = ["www.yellowpages.com"]
    start_urls = ['https://www.yellowpages.com/search?search_terms=75219+hospital&geo_location_terms=Dallas%2C+TX']

#    if os.path.exists('contacts.csc'):
#        os.remove("contacts.csc")

    def parse(self, response):
        
        name = response.xpath('//a[@class="business-name"]/span/text()').getall()
        direction = response.xpath('//div[@class="street-address"]/text()').getall()
        zone = response.xpath('//div[@class="locality"]/text()').getall()
        number = response.xpath('//div[@class="phones phone primary"]/text()').getall()
        website = response.xpath('//div/div[@class="links"]/a/@href').getall()
        
        for i in range(len(name)):
            yield {
            'organitation': name[i],
            'direction': direction[i],
            'zone': zone[i],
            'number': number[i],
            'website': website[i],
        }

        next_page_button_link = response.xpath('//div[2]/div[4]/ul/li[3]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)       
