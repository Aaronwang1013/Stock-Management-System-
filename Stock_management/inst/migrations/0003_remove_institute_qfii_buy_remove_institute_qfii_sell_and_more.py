# Generated by Django 4.1 on 2022-09-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0002_institute_dealer_status_institute_si_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='QFII_BUY',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='QFII_SELL',
        ),
        migrations.AddField(
            model_name='institute',
            name='QFII_status',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='外資買賣超(不含外資自營商)'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='Dealer_status',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='自營商買賣超'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='SI_status',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='投信買賣超'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='Total',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=15, verbose_name='三大法人買賣超'),
        ),
    ]
