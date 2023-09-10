import scrapy
import requests

class FundosSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://investidor10.com.br/fiis/']

    def parse(self, response):
        links = response.xpath('//section[@class="section-sectors"]//div[@class="actions fii"]//a/@href').getall()
        for link in links:
            yield scrapy.Request(
                link,
                callback=self.parse_each
            )


    def parse_each(self, response):
        cot_dy_val =  response.xpath('//div[@class="_card-body"]/div/span/text()').getall()
        pvp_liq =  response.xpath('//div[@class="_card-body"]/span/text()').getall()
        tipo_de_fundo = response.xpath('//div[@class="cell"]/div[@class="desc"]/span[text()="\nTIPO DE FUNDO\n"]/following::div/span/text()').get()
        arq = open("arq.txt", "a")
        arq.writelines(cot_dy_val)
        arq.writelines (pvp_liq)
        arq.writelines (tipo_de_fundo)
        pass

