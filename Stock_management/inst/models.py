from django.db import models

# Create your models here.

from django.db import models


#QFII外資 Qualified Foreign Institutional Investors
#SI投信 Securities Investment 
#Dealer 自營商 
class Institute(models.Model):
    Stock_code = models.CharField("stock code" , max_length = 50 , default='')
    Stock_name = models.CharField("stock name" , max_length = 50 , default='')
    QFII_BUY = models.DecimalField("QFII BUY" , max_digits=10 , decimal_places=3 ,default=0.00)
    QFII_SELL = models.DecimalField("QFII SELL" , max_digits=10 , decimal_places=3 , default=0.00)

