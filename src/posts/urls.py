from django.conf.urls import url
from django.contrib import admin

from zinnia.views.search import EntrySearch

from .views import (
    post_create,
    post_detail,
    post_list,
    post_update,
    post_delete,
    CustomTemplateEntrySearch,
    )

urlpatterns = [
    # url(r'^$', views.post_detail ),
    # url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^$', post_list, name='list'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'^123/$', CustomTemplateEntrySearch),
        # url(r'^$', EntrySearch.as_view(
        # template_name='custom/base.html'),
        # name='entry_search'),
]
