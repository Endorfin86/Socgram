# Generated by Django 4.1.3 on 2022-12-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='like',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
    ]
