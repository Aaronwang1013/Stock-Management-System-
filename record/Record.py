#!/usr/bin/env python

##download acount information from each bank (here I use Cathay)

#import required module

import pandas as pd
import numpy as np
from datetime import date
import requests
from io import StringIO

import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash import html



class CredictCard:
    def __init__(self) -> None:
        pass
    #獲取法人當日買賣超資訊
    def get_ins_info():
        today = date.today()
        date = today.strftime("%Y%m%d")
        r = requests.get('http://www.tse.com.tw/fund/T86?response=csv&date='+date+'&selectType=ALLBUT0999')
        df = pd.read_csv(StringIO(r.text) , header = 1).dropna(how='all' ,axis =1 ).dropna(how='any')
