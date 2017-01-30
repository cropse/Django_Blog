from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget
from ckeditor.widgets import CKEditorWidget

from ckeditor_uploader.fields import RichTextUploadingField

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    # content = RichTextUploadingField()
    # publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]