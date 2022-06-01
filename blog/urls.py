
from django.urls import path
from .views import newpost_add, post_list

urlpatterns = [
    path('', newpost_add, name='add'),
    path('list', post_list, name='list'),
]