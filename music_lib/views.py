# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render

from .models import Songs
from .models import Albums
from .models import Library

def index(request):
    all_albums = Albums.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music_lib/index.html', context)


def detail(request, album_id):

    try:
        album = Albums.objects.get(id=album_id)
        song = Songs.objects.all()
        context = {
            'song': song,
        }
    except Albums.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music_lib/details.html', {'album': album}, context)

def library(request):
    all_library = Library.objects.all()
    context = {
        'all_library': all_library,
    }
    return render(request, 'music_lib/library.html', context)
