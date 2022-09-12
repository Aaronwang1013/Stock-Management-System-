# Generated by Django 4.1 on 2022-09-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stock_code', models.CharField(default='', max_length=50, verbose_name='stock code')),
                ('Stock_name', models.CharField(default='', max_length=50, verbose_name='stock name')),
                ('QFII_BUY', models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='QFII BUY')),
                ('QFII_SELL', models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='QFII SELL')),
            ],
        ),
    ]