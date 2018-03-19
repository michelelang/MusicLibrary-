from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name="index"),

    # /music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

    # /music/library/
    url(r'^library/$', views.library, name="library"),
]
