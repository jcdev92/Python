import scrapy

xpath_links = '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href'
xpath_title = '//h1[@class="documentFirstHeading"]/text()'
xpath_paragraph = '//div[@class="field-item even"]//p[not(@class)]/text()'

class spiderCia(scrapy.Spider):
    name = 'cia'
    start_urls = ['https://www.cia.gov/readingroom/historical-collections']

    custom_settings={
        'FEEDS':{
            'cia.json':{
                'format': 'json',
                'encoding': 'utf-8',
                'indent': 4,
            }
        },
    }

    def parse(self, response):
        links_declassiefied = response.xpath(xpath_links).getall()
        for link in links_declassiefied:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url':response.urljoin(link)})
    
    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath(xpath_title).get()
        body = response.xpath(xpath_paragraph).getall()

        yield {
            'url' : link,
            'title': title,
            'body' : body
        }

