# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_lib', '0008_auto_20180319_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='song_year',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]