# BOT FUNDOS IMOBILIÁRIOS

Esse código tem como função extrair dados do endereço www.investidor10.com.br/fiis e seus dependentes afim de auxiliar a escolha de investimentos.

## Ambiente virtual
Para rodar esse código é necessário um ambiente virtual com as seguintes bibliotecas instaladas:
- Requests
- Scrapy
- Unidecode
- Pandas (no momento não implementado)

## Como rodar
Com o ambiente virtual ativado, navegue até a pasta "spiders" e digite:
`scrapy runspider SpiderFundos.py -o output.json`
Um json com o resultado vai ser gerado, e posteriormente tratado.
