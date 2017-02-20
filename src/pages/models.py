from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
import markdown

from django.utils.text import slugify
from unidecode import unidecode
from zinnia.models import Entry
from django.db.models.signals import pre_save

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
        markdown_text = markdown.markdown(content, ['markdown.extensions.extra', 'markdown_checklist.extension','markdown.extensions.nl2br'])
        return markdown_text

def create_slug(instance, new_slug=None):
    slug = slugify(unidecode(instance.title))# fix unicode null in slugify
    if new_slug is not None:
        slug = new_slug
    qs = Entry.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "{0}-{1}".format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Entry)
