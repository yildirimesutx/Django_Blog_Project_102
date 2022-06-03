from django.contrib import admin

from .models import NewPost, Comments
# Register your models here.
admin.site.register(NewPost)
admin.site.register(Comments)
