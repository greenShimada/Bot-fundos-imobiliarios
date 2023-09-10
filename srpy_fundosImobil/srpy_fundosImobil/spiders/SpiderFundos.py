import scrapy
import requests

class FundosSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://investidor10.com.br/fiis/']

    def parse(self, response):
        links = response.xpath('//section[@class="section-sectors"]//div[@class="actions fii"]//a/@href')
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_each
            )


    def parse_each(self, response):
        response.xpath('//div[@class="value"]').getall()
        pass

