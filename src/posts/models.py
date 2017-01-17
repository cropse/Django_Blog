from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=user_directory_path,
            null=True, blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'id':self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]
