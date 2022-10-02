#!/usr/bin/python3

##download acount information from each bank (here I use Cathay)

#import required module

import pandas as pd
import numpy as np
from datetime import date
import requests
from io import StringIO
# import schedule
import time

import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html

# Mysql
from sqlalchemy import create_engine

#log file

import os
##Directory path
path = os.path.abspath(os.path.abspath(os.path.join(os.getcwd(), "../..")))

import logging
logging.basicConfig(filename= os.path.join(path,'log',"database.log"),
                    format='%(asctime)s %(message)s',
                    filemode='w')
        
logger = logging.getLogger("record_database")
logger.setLevel(logging.INFO)
#self.logger.setLevel(logging.DEBUG)




class Record:
    def __init__(self) -> None:
        # self.today = date.today()
        # self.logger = logger.getLogger()
        pass
    #獲取法人當日買賣超資訊

    @staticmethod
    def get_ins_info():
        
        today = date.today()
        # today = today.strftime("%Y%m%d")
        today = '20220928' # (if test this function after 12pm, will fail cause the web doesn't have data yet)
        try:
            r = requests.get('http://www.tse.com.tw/fund/T86?response=csv&date='+today+'&selectType=ALLBUT0999')
            df = pd.read_csv(StringIO(r.text) , header = 1).dropna(how='all' ,axis =1 ).dropna(how='any')
            #移除原先表格中會有的多餘符號
        except:
            return None
        ##轉為適當格式
        df = df.astype(str).apply(lambda s: s.str.replace('"' , ''))
        df['證券代號'] = df['證券代號'].str.replace('=' , '').str.replace('"' , '')
        # df = df.drop(['證券代號'] , axis=1)
        # df = df.set_index(['股票名稱'])
        ## remain specific columns
        df = df[["證券代號" , "證券名稱" , "外陸資買賣超股數(不含外資自營商)" , "投信買賣超股數" ,"自營商買賣超股數" , "三大法人買賣超股數"]]
        df.set_axis(['股票代號','股票名稱','外資買賣超(不含外資自營商)','投信買賣超','自營商買賣超','三大法人買賣超'] , axis =1 , inplace=True)
        df.to_csv("data.csv")
        return df
    

    
    def inputDB(self , table):
        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="aaron",
                               pw="goxgox147",
                               db="Stock_management"))
        today = date.today()
        table.to_sql('institute_status_%s'%today, con = engine, if_exists = 'append', chunksize = 1000)
        #Create log file
        logger.info("%s , successfully save into database"%today)


          
if __name__ == '__main__':
#     # print(Record().get_ins_info())
    try:
            R = Record()
            table= R.get_ins_info()
            R.inputDB(table)
    except Exception as e:
            print(e)
    
