# Generated by Django 4.1 on 2022-09-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='Dealer_status',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='自營商買賣超股數'),
        ),
        migrations.AddField(
            model_name='institute',
            name='SI_status',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='投信買賣超股數'),
        ),
        migrations.AddField(
            model_name='institute',
            name='Total',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=15, verbose_name='三大法人買賣超股數'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='QFII_BUY',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='外資買進股數(不含外資自營商)'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='QFII_SELL',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='外資賣出股數(不含外資自營商)'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='Stock_code',
            field=models.CharField(default='', max_length=50, verbose_name='股票名稱'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='Stock_name',
            field=models.CharField(default='', max_length=50, verbose_name='股票代號'),
        ),
    ]
