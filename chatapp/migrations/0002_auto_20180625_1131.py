# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': '\u0427\u0430\u0442', 'verbose_name_plural': '\u0427\u0430\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='chatuser',
            options={'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', 'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438'},
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_name',
            field=models.CharField(default=' ', max_length=30, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0447\u0430\u0442\u0430'),
            preserve_default=False,
        ),
    ]
