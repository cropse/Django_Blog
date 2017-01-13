from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_create,
    post_detail,
    post_list,
    post_update,
    post_delete,
    )

urlpatterns = [
    # url(r'^$', views.post_detail ),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^$', post_list, name='list'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]
