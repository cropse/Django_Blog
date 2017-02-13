"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from pages.views import soundcloud, about_me
from gallery.views import gallery

blog_urls = ([
    # url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    # url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    # url(r'^blog/random/', include('zinnia.urls.random')),
    # url(r'^blog/authors/', include('zinnia.urls.authors')),
    # url(r'^blog/categories/', include('zinnia.urls.categories')),
    # url(r'^blog/comments/', include('zinnia.urls.comments')),
    # url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    # url(r'^blog/', include('zinnia.urls.shortlink')),
    # url(r'^blog/', include('zinnia.urls.quick_entry'))
], 'zinnia')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^weblog/', include(blog_urls)),
    # url(r'^weblog/', include('zinnia.urls')),
    url(r'^filer/', include('filer.urls')),
    # url(r'^comments/', include('django_comments.urls')),
    url(r'^soundcloud/$', soundcloud, name="soundcloud"),
    url(r'^$', about_me, name="about_me"),
    url(r'^gallery/(?P<folder_id>\d*)$', gallery, name="gallery"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
