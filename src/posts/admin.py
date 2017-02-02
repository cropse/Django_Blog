from django.contrib import admin
# from pagedown.widgets import AdminPagedownWidget
# from ckeditor.widgets import CKEditorWidget
# from django import forms
from django.db import models
# Register your models here.
# from .models import Post
from pagedown.widgets import AdminPagedownWidget

from django.utils.translation import ugettext_lazy as _
from zinnia.models.entry import Entry
from zinnia.admin.entry import EntryAdmin

# class PostModelAdmin(admin.ModelAdmin):
#     """docstring for PostModelAdmin"""
#     list_display = ['title', 'updated', 'timestamp']
#     list_display_links = ['updated']
#     list_filter = ['updated', 'timestamp']
#     list_editable = ['title']
#     search_fields = ['title', 'content']
#     # content = forms.CharField(widget=AdminPagedownWidget())
#     content = forms.CharField(widget=CKEditorWidget())
#     # formfield_overrides = {
#     #     models.TextField: {'widget': AdminPagedownWidget },
#     # }
#     class Meta:
#         model = Post


# admin.site.register(Post, PostModelAdmin)

class EntryGalleryAdmin(EntryAdmin):
  formfield_overrides = {
      models.TextField: {'widget': AdminPagedownWidget },
  }
  # In our case we put the gallery field
  # into the 'Content' fieldset
  fieldsets = (
    (_('Content'), {
      'fields': (('title', 'status'), 'lead', 'content',)}),
    # (_('Illustration'), {
    #   'fields': ('image', 'gallery'),
    #   'classes': ('collapse', 'collapse-closed')}),
    ) + \
    EntryAdmin.fieldsets[1:]

admin.site.register(Entry, EntryGalleryAdmin)