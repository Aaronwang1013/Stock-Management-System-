#!usr/bin/env python

#An API to det daily Buy and Sell of three institutional investors
from fileinput import filename
import requests
from urllib import parse
import re

class BS:
    def __init__(self):
        """
        定義常用變量
        外資:"http://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZGK_D.djhtm"
        自營商:"http://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZGK_DB.djhtm"
        投信:"http://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZGK_DD.djhtm"
        """
        self.url = 'http://fubon-ebrokerdj.fbs.com.tw/Z/ZG/{}.djhtm'
        self.headers = {'UserAgent': 'rawUa: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

        
    def get_BS(self , url):
        html = requests.get(url = url , headers = self.headers).content.decode('big5','replace')
        return html
    def get_date(self , html):
        date_regex = '<div class="t11">(.*?)</td></tr>'
        date_pattern = re.compile(date_regex , re.S)
        date = date_pattern.findall(html)
        return date
    def get_stock(self , html):
        stock_regex = 
    def save_data(self , filename , html):
        pass
    def run(self):
        """
        啟動程式
        """
        inv = input("請輸入券商種類(外資:ZGK_D,自營商:ZGK_DB,投信:ZGK_DD):")
        params = parse.quote(inv)
        url = self.url.format(params)
        html = self.get_BS(url = url)
        date = self.get_date(html =html)
        print(date)

if __name__ == "__main__":
    bs = BS()
    bs.run()