from statistics import mode
from django.db import models

# Create your models here.

from django.db import models


#QFII外資 Qualified Foreign Institutional Investors
#SI投信 Securities Investment 
#Dealer 自營商 
class Institute(models.Model):
    Stock_code = models.CharField("股票名稱" , max_length = 50 , default='')
    Stock_name = models.CharField("股票代號" , max_length = 50 , default='')
    QFII_status = models.DecimalField("外資買賣超(不含外資自營商)" , max_digits=10 , decimal_places=3 ,default=0.00)
    # QFII_SELL = models.DecimalField("外資賣出股數(不含外資自營商)" , max_digits=10 , decimal_places=3 , default=0.00)
    SI_status = models.DecimalField("投信買賣超" , max_digits=10 , decimal_places=3 , default=0.00)
    Dealer_status = models.DecimalField("自營商買賣超" , max_digits=10 , decimal_places=3 , default=0.00)
    Total = models.DecimalField("三大法人買賣超",max_digits=15 , decimal_places=3 , default=0.00)
