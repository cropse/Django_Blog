from django.contrib import admin
# from pagedown.widgets import AdminPagedownWidget
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.db import models
# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    """docstring for PostModelAdmin"""
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp']
    list_editable = ['title']
    search_fields = ['title', 'content']
    # content = forms.CharField(widget=AdminPagedownWidget())
    content = forms.CharField(widget=CKEditorWidget())
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminPagedownWidget },
    # }
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
