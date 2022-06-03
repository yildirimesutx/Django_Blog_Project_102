
from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class NewPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment = models.TextField(max_length=100)
    create = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(NewPost, on_delete=models.CASCADE,null=True, blank=True)
