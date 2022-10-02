# import logging
# logging.basicConfig(filename="/home/aaron/Desktop/Stock-Management-System-/temp/temp.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')



# logger = logging.getLogger("test")
# logger.setLevel(logging.INFO)
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")
# logger.critical("Internet is down")
import pandas as pd
import numpy as np
from datetime import date
import requests
from io import StringIO

def get_ins_info():
        
        today = date.today()
        # today = today.strftime("%Y%m%d")
        today = '20220907' # (if test this function after 12pm, will fail cause the web doesn't have data yet)
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
        
        return df
