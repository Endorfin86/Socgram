# Generated by Django 4.1.5 on 2023-01-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0002_delete_chatmessages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('sender', models.CharField(max_length=100, verbose_name='Отправитель')),
                ('friend', models.CharField(max_length=100, verbose_name='Получатель')),
                ('status', models.BooleanField(default=False, verbose_name='Статус сообщения')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
    ]
