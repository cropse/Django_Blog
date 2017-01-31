from django.contrib import admin

from .models import Gallery, Picture
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    """docstring for GalleryAdmin"""
    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)

class PictureAdmin(admin.ModelAdmin):
    """docstring for PictureAdmin"""
    class Meta:
        model = Picture

admin.site.register(Picture, PictureAdmin)