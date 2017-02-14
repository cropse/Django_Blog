from django import forms
# from .models import Post
from zinnia.models import Entry
from pagedown.widgets import PagedownWidget
from zinnia.admin.widgets import TagAutoComplete
from zinnia.admin.widgets import MiniTextarea
from django.utils.translation import ugettext_lazy as _


# from ckeditor_uploader.fields import RichTextUploadingField

# class PostForm(forms.ModelForm):
#     # content = forms.CharField(widget=CKEditorWidget())
#     # content = RichTextUploadingField()
#     # publish = forms.DateField(widget=forms.SelectDateWidget)
#     class Meta:
#         model = Post
#         fields = [
#             "title",
#             "content",
#             "image",
#             "draft",
#             "publish",
#         ]

class EntryForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget())
    # publish = forms.DateField(widget=forms.SelectDateWidget)
    tags = forms.CharField(widget=TagAutoComplete())
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Entry
        fields = forms.ALL_FIELDS
        widgets = {
            'tags': TagAutoComplete,
            'lead': MiniTextarea,
            'excerpt': MiniTextarea,
            'image_caption': MiniTextarea,
        }
        fields = [
            "title",
            "content",
            "image",
            "status",
            "tags"
        ]
