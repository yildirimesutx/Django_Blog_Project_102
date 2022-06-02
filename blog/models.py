
from django.db import models

# Create your models here.

class NewPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.title