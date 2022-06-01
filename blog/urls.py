
from django.urls import path
from .views import newpost_add

urlpatterns = [
    path('', newpost_add, name='add'),
 
]