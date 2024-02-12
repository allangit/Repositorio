from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class Hotel(Item):

    nombre=Field()
    precio=Field()
    descripcion=Field()

class Hotel_Scraping(CrawlSpider):

    name='hoteles'

    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
      
    }

    allowed_domains = ['tripadvisor.com']
    start_urls=['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']
    download_delay = 3

    #definir una regla que me permita ir a los links especificos donde se encuentra la informacion

    rules=(

        Rule(

            LinkExtractor(

                    allow=r'/Hotel_Review-'

            ),follow=True,callback='parse_hoteles'),
    )

    def parse_hoteles(self,response):

        sel=Selector(response)
        item=ItemLoader(Hotel(),sel)
        item.add_xpath('nombre','//h1[@id="HEADING"]/text()')
        item.add_xpath('precio','//div[@class="biGQs _P fiohW uuBRH"]/div[@class="aLfMd"]/text()')
        #item.add_xpath('descripcion','//div[@class="_T FKffI TPznB Ci ajMTa Ps Z BB"]/div[@class="fIrGe _T"]/text()')
  

        yield item.load_item()











