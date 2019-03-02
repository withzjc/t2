import requests
from lxml import etree
import os

class Spider(object):
    def start_request(self):
        response = requests.get("https://www.qidian.com/all")
        html = etree.HTML(response.content)
        Bigtit_list = html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        Bigsrc_list = html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        for Bigtit, Bigsrc in zip(Bigtit_list,Bigsrc_list):
            if os.path.exists(Bigtit) ==False:
                os.mkdir(Bigtit)
    def file_data(self,Bigsrc,Bigtit):
        response = requests.get("http:"+Bigsrc)
        html = etree.HTML(response.content.decode())
        Littit_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        Litsrc_list = html.xpath('//ul')

spider = Spider()
spider.start_request()