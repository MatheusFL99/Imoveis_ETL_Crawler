import scrapy
import json
from scrapy.crawler import CrawlerProcess
import pymongo
from config import MONGODB_URI


def write_results_file(imoveis):
    imoveis_ordenados = sorted(imoveis, key=lambda d: d['title'])
    jsonstring = json.dumps(imoveis_ordenados)
    jsonfile = open('imoveis.json', 'w', encoding='utf8')
    jsonfile.write(jsonstring)
    jsonfile.close()


def connectDB(connString):
    try:
        client = pymongo.MongoClient(connString)
        db = client.spider
        collection = db.imoveis

        with open('imoveis.json') as file:
            file_data = json.load(file)

        if isinstance(file_data, list):
            collection.insert_many(file_data)
        else:
            collection.insert_one(file_data)

        print('Sucesso!')
    except:
        print('Fail!')


def Url_vivareal():

    base_url = 'https://www.vivareal.com.br/venda/sp/campinas/casa_residencial/?pagina='
    urls = list()
    for l in range(1, 277):
        urls.append(base_url + str(l))
    return urls


class SpiderVivaReal(scrapy.Spider):
    name = 'vivarealSpider'
    start_urls = Url_vivareal()
    imoveis = list()

    def parse(self, response):
        print('PARSER COMEÇA AQUI!')
        for container in response.css('article.property-card__container.js-property-card'):
            title = container.css(
                'span.property-card__title.js-cardLink.js-card-title::text').get()
            infos = container.css(
                'li.property-card__detail-item.property-card__detail-area span::text').get()
            price = container.css(
                '.property-card__price.js-property-card-prices.js-property-card__price-small p::text').get()
            address = container.css(
                'span.property-card__address::text').get()

            self.imoveis.append(
                {'title': title.strip(), 'infos': infos, 'price': price.strip(), 'address': address})
            yield {'title': title.strip(), 'infos': infos, 'price': price.strip(), 'address': address}

    def close(self, reason):
        write_results_file(self.imoveis)


def Url_lopes():

    base_url = 'https://www.lopes.com.br/busca/venda/br/sp/campinas/tipo/casa/pagina/'
    urls = list()
    for l in range(1, 20):
        urls.append(base_url + str(l) +
                    '?placeId=ChIJJWNL5x3GyJQRKsJ4IWo65Rc&tipo=HOUSE')
    return urls


class SpiderLopes(scrapy.Spider):
    name = 'lopesSpider'
    start_urls = Url_lopes()
    imoveis = list()

    def parse(self, response):
        for container in response.css('article.card__textbox.ng-star-inserted'):
            title = container.css(
                'p.card__location::text').get()
            infos = container.css(
                'span.attributes__info::text').get()
            price = container.css(
                'h4.card__price.ng-star-inserted::text').get()
            address = container.css(
                'p.card__location::text').get()

            self.imoveis.append(
                {'title': title.strip(), 'infos': infos, 'price': price.strip(), 'address': address})
            yield {'title': title.strip(), 'infos': infos, 'price': price.strip(), 'address': address}

    def close(self, reason):
        write_results_file(self.imoveis)


def Url_dlange():

    base_url = 'https://www.dlange.com.br/imoveis/a-venda/casa/campinas?pagina='
    urls = list()
    for l in range(1, 84):
        urls.append(base_url + str(l))
    return urls


class Spiderdlange(scrapy.Spider):
    name = 'lopesSpider'
    start_urls = Url_dlange()
    imoveis = list()

    def parse(self, response):
        for container in response.css('.card-with-buttons__footer'):
            title = container.css(
                'h3::text').get()
            infos = container.css(
                'li::text').getall()
            price = container.css(
                'p.card-with-buttons__value::text').get()
            address = container.css(
                'h3::text').get()

            self.imoveis.append(
                {'title': title.strip(), 'infos': infos, 'price': price.strip(), 'address': address})
            yield {'title': title.strip(), 'infos': infos, 'price': price.strip(), 'address': address}

    def close(self, reason):
        write_results_file(self.imoveis)


process = CrawlerProcess()
process.crawl(SpiderVivaReal)
process.crawl(SpiderLopes)
process.crawl(Spiderdlange)
process.start()

connectDB(MONGODB_URI)
