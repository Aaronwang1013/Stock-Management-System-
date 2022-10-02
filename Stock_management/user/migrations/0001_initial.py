# Generated by Django 4.1 on 2022-09-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='用戶名')),
                ('password', models.CharField(max_length=32, verbose_name='密碼')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
            ],
        ),
    ]
