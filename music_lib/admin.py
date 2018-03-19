# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Albums
from .models import Songs
from .models import Library

admin.site.register(Albums)
admin.site.register(Songs)
admin.site.register(Library)