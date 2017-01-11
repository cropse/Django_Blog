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
    url(r'^detail/$', post_detail),
    url(r'^list/$', post_list),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]
