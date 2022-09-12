#!/usr/bin/env python

##download acount information from each bank (here I use Cathay)

#import required module

import pandas as pd
import numpy as np
from datetime import date
import requests
from io import StringIO
import schedule
import time

import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html




class Record:
    def __init__(self) -> None:
        # self.today = date.today()
        pass
    #獲取法人當日買賣超資訊
    @staticmethod
    def get_ins_info():
        
        today = date.today()
        today = today.strftime("%Y%m%d")
        # today = '20220907' # (if test this function after 12pm, will fail cause the web doesn't have data yet)
        try:
            r = requests.get('http://www.tse.com.tw/fund/T86?response=csv&date='+today+'&selectType=ALLBUT0999')
            df = pd.read_csv(StringIO(r.text) , header = 1).dropna(how='all' ,axis =1 ).dropna(how='any')
            #移除原先表格中會有的多餘符號
        except:
            return None
        ##轉為適當格式
        df = df.astype(str).apply(lambda s: s.str.replace('"' , ''))
        df['股票名稱'] = df['證券代號'].str.replace('=' , '').str.replace('"' , '')
        df = df.drop(['證券代號'] , axis=1)
        df = df.set_index(['股票名稱'])
        return df
    
    def inputDB():
        pass

schedule.every().day.at('15:30').do(Record.get_ins_info)


          
if __name__ == '__main__':
    # df = Record().get_ins_info()
    # print(df)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
