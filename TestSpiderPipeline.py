# -*- coding: utf-8 -*-
import pymysql
from pymysql import connections
class TestSpiderPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect("localhost","root","root","douban_book", charset='utf8mb4')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql ="insert into book("
        placeHolder = ""
        selectKey = ""
        params=[]
        if 'url' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "URL"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['url'])
        if 'imgUrl' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "IMG_URL"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['imgUrl'])
        if 'author' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "AUTHOR"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['author'])
        if 'name' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "NAME"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['name'])
        if 'press' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "PRESS"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['press'])
        if 'score' in item and item['score'] != "":
            if selectKey != "":
                selectKey += ","
            selectKey += "SCORE"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['score'])
        if 'pageCount' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "PAGE_COUNT"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['pageCount'])
        if 'price' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "PRICE"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['price'])
        if 'isbn' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "ISBN"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['isbn'])
        if 'publishYear' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "PUBLISH_YEAR"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['publishYear'])
        if 'binding' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "BINDING"
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(item['binding'])
        if 'label' in item:
            if selectKey != "":
                selectKey += ","
            selectKey += "LABEL"
            label = ",".join(item['label'])
            if placeHolder != "":
                placeHolder += ","
            placeHolder += "%s"
            params.append(label)
        sql += selectKey + ") VALUES(" + placeHolder+")"
        # sql ="insert into book(URL,IMG_URL,AUTHOR,NAME,PRESS,SCORE,PAGE_COUNT,PRICE,ISBN,PUBLISH_YEAR,BINDING,LABEL) VALUES(%s,%s,%s,%s,%s,%s,%d,%s,%s,%s,%s,%s)"
        # label = ",".join(item['label'])
        self.cursor.execute(sql, params)
        # self.cursor.execute(sql,(item['url'],item['imgUrl'],item['author'],item['name'],item['press'],item['score'],item['pageCount'],item['price'],item['isbn'],item['publishYear'],item['binding'],label))
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()