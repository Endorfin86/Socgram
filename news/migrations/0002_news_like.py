# Generated by Django 4.1.3 on 2022-12-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='like',
            field=models.ImageField(default=1, upload_to='', verbose_name='Лайки'),
            preserve_default=False,
        ),
    ]
