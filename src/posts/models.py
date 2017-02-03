from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.utils import timezone
from markdown2 import markdown
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from unidecode import unidecode

from django.db import models
# from zinnia.models import Entry
from zinnia.models_bases.entry import AbstractEntry

from django.contrib import admin


class MyEntry(AbstractEntry):

    def active(self):
        return self.advanced_search("ed")
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'slug':self.slug})

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return markdown_text

    def __str__(self):
        return 'EntryGallery %s' % self.title

    class Meta(AbstractEntry.Meta):
        abstract = True


# class PostManager(models.Manager):
#     def active(self, *args, **kwargs):
#         # Post.object.all() = super(PostManager, self).all()
#         return super().filter(draft=False).filter(publish__lte=timezone.now())

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

# class Post(models.Model):
#     """Post model"""
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     title = models.CharField(max_length=120)
#     slug = models.SlugField(unique=True, blank=False)
#     image = models.ImageField(upload_to=user_directory_path,
#             null=True, blank=True,
#             width_field="width_field",
#             height_field="height_field")
#     height_field = models.IntegerField(null=True, default=0)
#     width_field = models.IntegerField(null=True, default=0)
#     content = RichTextUploadingField()
#     draft = models.BooleanField(default=False)
#     publish = models.DateField(auto_now=False, auto_now_add=False)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

#     objects = PostManager()

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("posts:detail", kwargs={'slug':self.slug})

#     class Meta:
#         ordering = ["-timestamp", "-updated"]

#     def get_markdown(self):
#         content = self.content
#         markdown_text = markdown(content)
#         return markdown_text


# def create_slug(instance, new_slug=None):
#     slug = slugify(unidecode(instance.title))# fix unicode null in slugify
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "{0}-{1}".format(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)



# pre_save.connect(pre_save_post_receiver, sender=Post)