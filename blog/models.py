
from django.db import models

from django.contrib.auth.models import User
from django.db.models.enums import Choices

# Create your models here.


category_choices = [
   ('Frontend', 'Frontend'),
   ('Backend', 'Backend'),
   ('FullStack', 'FullStack')
]


class NewPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category =  models.CharField(max_length=20, choices=category_choices,  blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment = models.TextField(max_length=100)
    create = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(NewPost, on_delete=models.CASCADE,null=True, blank=True)
