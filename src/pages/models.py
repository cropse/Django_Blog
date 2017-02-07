from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
import markdown

# Create your models here.
class Introduce(models.Model):
    """docstring for Introduce"""
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="introduce",
            null=True, blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(null=True, default=0)
    width_field = models.IntegerField(null=True, default=0)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("about_me")

    def get_markdown(self):
        content = self.content
        # adding model image to markdown named "image"
        content += "[image]: " + self.image.url
        markdown_text = markdown.markdown(content, ['markdown.extensions.extra'])
        return markdown_text