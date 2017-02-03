from django import forms
from django.contrib import admin
from django.db import models
# from ckeditor.widgets import CKEditorWidget
from pagedown.widgets import AdminPagedownWidget
from .models import Introduce


# class IntroduceAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=AdminPagedownWidget())
#     class Meta:
#         model = Introduce

@admin.register(Introduce)
class IntroduceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    # form = IntroduceAdminForm

# admin.site.register(Introduce, IntroduceAdmin)