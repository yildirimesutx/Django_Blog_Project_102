
from django.urls import path
from .views import newpost_add, post_list, post_detail, post_update,post_delete

urlpatterns = [
    path('add', newpost_add, name='add'),
    path('', post_list, name='list'),
    path('detail/<int:id>', post_detail, name='detail'),
    path('update/<int:id>', post_update, name='update'),
    path('delete/<int:id>', post_delete, name='delete'),
    
]