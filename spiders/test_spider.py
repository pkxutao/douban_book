import scrapy
# from bs4 import BeautifulSoup
from test_spider.items import TestSpiderItem
import re

class DmozSpider(scrapy.spiders.Spider):
    itemCount = 0
    name = "dbbook"
    allowed_domains = ["douban.com"]
    start_urls = []
    start_urls.append("https://book.douban.com/subject/27609047/")
    print(start_urls)

    def parse(self, response):
        book = TestSpiderItem()
        imgUrl = response.xpath("//div[@id='mainpic']/a[@class='nbg']/@href").extract_first()
        name = response.xpath("//span[@property='v:itemreviewed']/text()").extract_first()
        score = response.xpath("//strong[@property='v:average']/text()").extract_first().strip()
        label = response.xpath("//a[@class='  tag']/text()").extract()
        book['url'] = response.url
        book['label'] = label
        book['score'] = score
        book['imgUrl'] = imgUrl
        book['name'] = name
        infos = response.xpath("//div[@id='info']")
        curType = ""  # 当前获取的类型
        # print(infos.xpath("./*"))
        # print(infos.xpath("./text()"))
        if "作者" in infos.extract_first():
            author = infos.xpath(".//a/text()").extract_first().strip()
            book['author'] = self.getFormatStr(author)
        # print("作者：", infos.xpath(".//a/text()").extract_first().strip())
        for info in infos.xpath("./*|./text()"):
            name = info.xpath("text()").extract_first()
            if name is not None:
                curType = ""
            # if "作者:" == name or "作者" == name:
            #     curType = "author"
            #     continue
            if "出版社:" == name:
                curType = "press"
                continue
            elif "出版年:" == name:
                curType = "publishYear"
                continue
            elif "页数:" == name:
                curType = "pageCount"
                continue
            elif "定价:" == name:
                curType = "price"
                continue
            elif "ISBN:" == name:
                curType = "isbn"
                continue
            elif "装帧:" == name:
                curType = "binding"
                continue

            span = info.extract()
            span = span.strip()  # 去掉空格
            span = span.replace("\n", "")  # 去掉换行符
            span = span.replace("<br>", "")  # 去掉换行符
            if len(span) != 0:
                # if curType == "author":
                    # book['author'] = self.getFormatStr(info.xpath("text()").extract_first())  # 作者名字特殊一点
                if curType == "press":
                    book['press'] = span
                elif curType == "publishYear":
                    book['publishYear'] = span
                elif curType == "pageCount":
                    book['pageCount'] = int(re.sub("\D", "", span))  #todo 这里限制只获取数字 去掉冒号 单位
                elif curType == "price":
                    book['price'] =  float(re.findall(r"\d+\.?\d*",span)[0])
                elif curType == "isbn":
                    book['isbn'] = span
                elif curType == "binding":
                    book['binding'] = span
        yield book
        # 添加其他书到url列表
        similarUrls = response.xpath("//div[@id='db-rec-section']/div[@class='content clearfix']/dl/dt/a/@href").extract()
        for url in similarUrls:
            if self.itemCount < 10:
                # self.itemCount += 1
                yield scrapy.Request(url)

    def getFormatStr(self, params):
        params = params.strip()#去掉空格
        params = params.replace(" ", "")
        params = params.replace("\n" , "")#去掉换行符
        return params
