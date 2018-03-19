# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Albums(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=300)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Songs(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=500)

    def __str__(self):
        return self.song_title

class Library(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    song_list = models.ForeignKey(Songs, on_delete=models.CASCADE)
    song_year = models.IntegerField(max_length=4, default=0)


    def __str__(self):
        return self.artist + ' - ' + str(self.album) + ' - ' + str(self.song_list) + ' - ' + str(self.song_year)
