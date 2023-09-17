import scrapy
import requests


class FundosSpider(scrapy.Spider):

    name = 'example'
    start_urls = ['https://investidor10.com.br/fiis/']

    def parse(self, response):
        paginas = response.xpath('//section[@class="section-sectors"]//div[@class="section-sectors-pagination"]//li[@class="pagination-item"]//a/@href').getall()
        for pagina in paginas:
            yield scrapy.Request(
                pagina,
                callback=self.parse_each
            )

    def parse_each(self, response):
        links = response.xpath('//section[@class="section-sectors"]//div[@class="actions fii"]//a/@href').getall()

        for link in links:
            yield scrapy.Request(
                link,
                callback=self.parse_each_fundo
            )

    def parse_each_fundo(self, response):

        from unidecode import unidecode

        nome = response.css("h1::text").get()
        cotacao =  response.xpath('//div[@class="_card-body"]/div/span/text()').get()
        pvp =  response.xpath('//div[@class="_card-body"]/span/text()').get()
        div = response.xpath('//div[@class="_card dy"]//div[@class="_card-body"]/div/span/text()').get()
        tipo_de_fundo = response.xpath('//div[@class="cell"]/div[@class="desc"]/span[text()="\nTIPO DE FUNDO\n"]/following::div/span/text()').get()
        todos_imoveis = response.xpath('//section[@class="section-sectors"]//div[@class="container"]//div[@id="properties-section"]//div[@id="container-properties"]//div//h3')
        vacancia = response.xpath('//div[@class="cell"]/div[@class="desc"]/span[text()="\nVACÂNCIA\n"]/following::div/span/text()').get()
        segmento = response.xpath('//div[@class="cell"]/div[@class="desc"]/span[text()="\nSEGMENTO\n"]/following::div/span/text()').get()

        yield {
            'nome': nome,
            'cotacao: ': cotacao,
            'dividend yield': div,
            'pvp_liquidez': pvp,
            'tipo_de_fundo': unidecode(tipo_de_fundo),
            'qntd imoveis': len(todos_imoveis),
            'vacancia': vacancia,
            'segmento': unidecode(segmento)
        }

        pass

