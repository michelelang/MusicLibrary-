# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 08:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_lib', '0003_artists'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Album',
            new_name='Albums',
        ),
    ]
