
from django.urls import path
from .views import newpost_add, post_list

urlpatterns = [
    path('add', newpost_add, name='add'),
    path('', post_list, name='list'),
]